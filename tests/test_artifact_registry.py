import json
from pathlib import Path

import pytest

from pancancer_epigenetics.utils.artifact_registry import (
    load_artifact_registry,
    refresh_notebook_artifacts,
    register_artifacts,
    resolve_artifact_path,
    validate_artifact_registry,
)
from pancancer_epigenetics.utils.file_checks import calculate_sha256


def _artifact(path: str = "data/interim/example.csv", inputs: list | None = None) -> dict:
    return {
        "path": path,
        "phase": 2,
        "status": "frozen",
        "artifact_role": "data",
        "producer": {"type": "notebook", "path": "notebooks/example.ipynb"},
        "shape": [1, 1],
        "size_bytes": 1,
        "sha256": "a" * 64,
        "inputs": inputs or [{"type": "raw_registry", "ref": "/raw/resource"}],
    }


def _registry() -> tuple[dict, dict]:
    return {"schema_version": 1, "artifacts": {"a": _artifact()}}, {"raw": {"resource": {}}}


def test_valid_registry() -> None:
    registry, raw = _registry()
    assert validate_artifact_registry(registry, raw) == registry


@pytest.mark.parametrize("field, value, message", [
    ("path", "/absolute.csv", "repository-relative"),
    ("path", "C:/Users/example/artifact.csv", "repository-relative"),
    ("sha256", "a" * 63, "sha256"),
    ("size_bytes", -1, "size_bytes"),
    ("producer", {"type": "script"}, "producer"),
])
def test_invalid_artifact_fields_are_rejected(field: str, value: object, message: str) -> None:
    registry, raw = _registry()
    registry["artifacts"]["a"][field] = value
    with pytest.raises(ValueError, match=message):
        validate_artifact_registry(registry, raw)


def test_duplicate_path_rejected() -> None:
    registry, raw = _registry()
    registry["artifacts"]["b"] = _artifact()
    with pytest.raises(ValueError, match="duplicate artifact path"):
        validate_artifact_registry(registry, raw)


def test_missing_artifact_and_raw_references_rejected() -> None:
    registry, raw = _registry()
    registry["artifacts"]["a"]["inputs"] = [{"type": "artifact", "artifact_id": "missing"}]
    with pytest.raises(ValueError, match="does not exist"):
        validate_artifact_registry(registry, raw)
    registry["artifacts"]["a"]["inputs"] = [{"type": "raw_registry", "ref": "/missing/resource"}]
    with pytest.raises(ValueError, match="does not resolve"):
        validate_artifact_registry(registry, raw)


def test_duplicate_direct_input_rejected() -> None:
    registry, raw = _registry()
    registry["artifacts"]["a"]["inputs"] = [
        {"type": "raw_registry", "ref": "/raw/resource"},
        {"type": "raw_registry", "ref": "/raw/resource"},
    ]
    with pytest.raises(ValueError, match="duplicate direct input"):
        validate_artifact_registry(registry, raw)


@pytest.mark.parametrize("coarse_ref", ["/tcga", "/depmap", "/gdsc", "/epifactors", "/msigdb"])
def test_top_level_raw_registry_references_are_rejected(coarse_ref: str) -> None:
    registry, raw = _registry()
    raw[coarse_ref[1:]] = {}
    registry["artifacts"]["a"]["inputs"] = [{"type": "raw_registry", "ref": coarse_ref}]
    with pytest.raises(ValueError, match="cohort, resource, or file"):
        validate_artifact_registry(registry, raw)


def test_self_dependency_and_cycle_rejected() -> None:
    registry, raw = _registry()
    registry["artifacts"]["a"]["inputs"] = [{"type": "artifact", "artifact_id": "a"}]
    with pytest.raises(ValueError, match="itself"):
        validate_artifact_registry(registry, raw)
    registry, raw = _registry()
    registry["artifacts"]["b"] = _artifact("data/processed/b.csv", [{"type": "artifact", "artifact_id": "a"}])
    registry["artifacts"]["a"]["inputs"] = [{"type": "artifact", "artifact_id": "b"}]
    with pytest.raises(ValueError, match="cycle"):
        validate_artifact_registry(registry, raw)


def test_resolution_is_deterministic(tmp_path: Path) -> None:
    registry, _ = _registry()
    assert resolve_artifact_path(registry, "a", tmp_path) == (tmp_path / "data/interim/example.csv").resolve()


def test_batch_registration_refreshes_frozen_identities_and_guards_declarations(tmp_path):
    path = tmp_path / "artifact_registry.json"
    path.write_text('{"schema_version": 1, "artifacts": {}}', encoding="utf-8")
    inputs = [{"type": "raw_registry", "ref": "/depmap/files/CRISPRGeneEffect.csv"}]
    entry = _artifact(inputs=inputs)
    register_artifacts({"a": entry}, registry_path=path)
    original = path.read_bytes()

    register_artifacts({"a": entry}, registry_path=path)
    assert path.read_bytes() == original

    refreshed = {**entry, "shape": [2, 1], "size_bytes": 2, "sha256": "b" * 64}
    assert register_artifacts({"a": refreshed}, registry_path=path)["artifacts"] == {
        "a": refreshed
    }
    original = path.read_bytes()

    replacement = {**refreshed, "path": "data/interim/replacement.csv"}
    new_entry = _artifact("data/interim/new.csv", inputs=inputs)
    with pytest.raises(ValueError, match="Artifact declaration changed"):
        register_artifacts({"b": new_entry, "a": replacement}, registry_path=path)
    assert path.read_bytes() == original

    invalid_entry = {**new_entry, "inputs": [{"type": "artifact", "artifact_id": "missing"}]}
    with pytest.raises(ValueError, match="does not exist"):
        register_artifacts(
            {"a": refreshed, "b": invalid_entry}, registry_path=path
        )
    assert path.read_bytes() == original

    saved = register_artifacts(
        {"a": replacement, "b": new_entry},
        allow_declaration_change=True,
        registry_path=path,
    )
    assert json.loads(path.read_text(encoding="utf-8")) == saved
    assert saved["artifacts"] == {"a": replacement, "b": new_entry}


def test_refresh_updates_only_declared_output_identities(tmp_path):
    path = tmp_path / "artifact_registry.json"
    path.write_text('{"schema_version": 1, "artifacts": {}}', encoding="utf-8")
    inputs = [{"type": "raw_registry", "ref": "/depmap/files/CRISPRGeneEffect.csv"}]
    entry = _artifact(inputs=inputs)
    unrelated = {
        **_artifact("data/interim/other.csv", inputs=inputs),
        "producer": {"type": "notebook", "path": "notebooks/other.ipynb"},
    }
    register_artifacts({"a": entry, "b": unrelated}, registry_path=path)
    output = tmp_path / entry["path"]
    output.parent.mkdir(parents=True)
    output.write_bytes(b"gene\nA\nB\n")

    original = path.read_bytes()
    with pytest.raises(ValueError, match="Verified outputs differ"):
        refresh_notebook_artifacts(
            "notebooks/example.ipynb", {}, registry_path=path, root=tmp_path
        )
    assert path.read_bytes() == original

    count = refresh_notebook_artifacts(
        "notebooks/example.ipynb", {output: (2, 1)}, registry_path=path, root=tmp_path
    )
    assert count == 1
    assert load_artifact_registry(path)["artifacts"] == {
        "a": {
            **entry,
            "shape": [2, 1],
            "size_bytes": output.stat().st_size,
            "sha256": calculate_sha256(output),
        },
        "b": unrelated,
    }


def test_real_registry_structure_and_frozen_outputs() -> None:
    registry = load_artifact_registry()
    assert registry["schema_version"] == 1
    assert all(not item["path"].startswith("data/raw/") for item in registry["artifacts"].values())
    assert all(
        input_item.get("ref") not in {"/tcga", "/depmap", "/gdsc", "/epifactors", "/msigdb"}
        for item in registry["artifacts"].values()
        for input_item in item["inputs"]
        if input_item["type"] == "raw_registry"
    )
    for artifact_id in (
        "phase4.400.cross_system_shared_gene_universe",
        "phase4.401.consensus_transcriptomic_program_catalog",
        "phase4.402.cross_lineage_robustness_summary",
        "phase4.403.epigenetic_regulator_enrichment_summary",
        "phase4.404.program_annotation_enrichment",
        "phase4b.450.primary_gene_program_associations",
        "phase5.500.crispr_model_cohort",
        "phase5.500.crispr_gene_coverage",
        "phase5.500.crispr_primary_associations",
        "phase5.500.crispr_primary_significant_evidence",
        "phase5.500.crispr_within_lineage_associations",
        "phase5.500.crispr_putative_vulnerability_associations",
        "phase5.500.crispr_analysis_metadata",
    ):
        assert artifact_id in registry["artifacts"]
