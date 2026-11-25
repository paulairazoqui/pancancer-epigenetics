import json
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import pytest

from pancancer_epigenetics.utils import artifact_registry
from pancancer_epigenetics.utils.file_checks import calculate_sha256

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = {
    "450": "notebooks/phase4b_secondary_molecular_characterization/450_secondary_genomic_context_characterization.ipynb",
    "602": "notebooks/phase6_pharmacogenomic_contexts/602_shap_attribution_and_stability_analysis.ipynb",
}


@pytest.mark.parametrize("number", ["450", "602"])
@pytest.mark.parametrize("corrupt", [False, True])
def test_notebook_closure_publishes_complete_verified_outputs(
    tmp_path, monkeypatch, number, corrupt
):
    notebook_path = NOTEBOOKS[number]
    notebook = json.loads((ROOT / notebook_path).read_text(encoding="utf-8"))
    source = "".join(notebook["cells"][-1]["source"])
    registry = artifact_registry.load_artifact_registry()
    entries = {
        key: value
        for key, value in registry["artifacts"].items()
        if value["producer"].get("path") == notebook_path
    }
    assert len(entries) == {"450": 1, "602": 7}[number]
    registry_path = tmp_path / "registry.json"
    registry_path.write_text(json.dumps(registry), encoding="utf-8")
    original = registry_path.read_bytes()
    real_refresh = artifact_registry.refresh_notebook_artifacts
    real_load = artifact_registry.load_artifact_registry
    calls = []

    def refresh(producer, outputs, *, require_unchanged):
        calls.append((producer, outputs, require_unchanged))
        return real_refresh(
            producer,
            outputs,
            registry_path=registry_path,
            root=tmp_path,
            require_unchanged=require_unchanged,
        )

    monkeypatch.setattr(artifact_registry, "refresh_notebook_artifacts", refresh)
    monkeypatch.setattr(
        artifact_registry,
        "load_artifact_registry",
        lambda path=registry_path: real_load(path),
    )
    env = {"pd": pd, "json": json, "Paths": SimpleNamespace(root=tmp_path)}
    frame = pd.DataFrame({"value": [1, 2], "label": ["a", "b"]})
    paths = {}
    for artifact_id, entry in entries.items():
        name = artifact_id.rsplit(".", 1)[-1]
        path = tmp_path / entry["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        paths[name] = path
        if path.suffix == ".parquet":
            frame.to_parquet(path, index=False)
        elif path.suffix == ".csv":
            frame.to_csv(path, index=False)
        else:
            path.write_text(json.dumps({"outputs": "verified"}), encoding="utf-8")

    if number == "450":
        env.update(
            PRIMARY_ASSOCIATIONS_OUTPUT_PATH=paths["primary_gene_program_associations"],
            reloaded_primary_associations=frame.copy(),
            final_gene_program_summary=frame.copy(),
        )
        if corrupt:
            paths["primary_gene_program_associations"].write_text(
                "value,label\n99,a\n2,b\n", encoding="utf-8"
            )
    else:
        env.update(
            output_paths={k: v for k, v in paths.items() if k != "analysis_metadata"},
            metadata_path=paths["analysis_metadata"],
            analysis_metadata={"outputs": "verified"},
        )
        for name in env["output_paths"]:
            env[name + "_output"] = frame.copy()
        if corrupt:
            paths["repeat_program_attribution"].write_text(
                "value,label\n99,a\n2,b\n", encoding="utf-8"
            )

    if corrupt:
        with pytest.raises(AssertionError):
            exec(compile(source, notebook_path, "exec"), env)
        assert not calls
        assert registry_path.read_bytes() == original
        return

    exec(compile(source, notebook_path, "exec"), env)
    assert len(calls) == 1
    producer, verified, require_unchanged = calls[0]
    assert producer == notebook_path
    assert not require_unchanged
    assert set(verified) == set(paths.values())
    updated = real_load(registry_path)["artifacts"]
    for artifact_id, entry in entries.items():
        path = tmp_path / entry["path"]
        assert updated[artifact_id]["sha256"] == calculate_sha256(path)
        assert updated[artifact_id]["size_bytes"] == path.stat().st_size
        assert updated[artifact_id]["shape"] == (
            None if path.suffix == ".json" else [2, 2]
        )
        assert {
            k: v
            for k, v in updated[artifact_id].items()
            if k not in {"shape", "size_bytes", "sha256"}
        } == {
            k: v for k, v in entry.items() if k not in {"shape", "size_bytes", "sha256"}
        }
