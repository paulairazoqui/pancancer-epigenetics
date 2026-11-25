import ast
import csv
import json
from functools import partial
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest

from pancancer_epigenetics import analysis_parameters
from pancancer_epigenetics.utils import artifact_registry

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks/phase5_functional_vulnerabilities"
PROGRAM_IDS = ["P2", "P1"]


def notebook_cells(number):
    notebook = next(NOTEBOOKS.glob(f"{number}_*.ipynb"))
    document = json.loads(notebook.read_bytes())
    return notebook.relative_to(ROOT).as_posix(), [
        "".join(cell["source"]) for cell in document["cells"]
    ]


def run_cells(cells, indices, env):
    for index in indices:
        exec(compile(cells[index], f"cell {index}", "exec"), env)


def registry_entry(path, producer, role="data"):
    return {
        "path": path,
        "phase": 5,
        "status": "frozen",
        "artifact_role": role,
        "producer": {"type": "notebook", "path": producer},
        "shape": None,
        "size_bytes": 0,
        "sha256": "0" * 64,
        "inputs": [],
    }


@pytest.fixture
def catalog(tmp_path, monkeypatch):
    path = tmp_path / "catalog.csv"
    path.write_text(
        "consensus_program_id,tumor_rna_axis,cell_line_program,orientation_multiplier\n"
        "P2,T2,C2,1\nP1,T1,C1,-1\n",
        encoding="utf-8",
    )
    registry_path = tmp_path / "catalog_registry.json"
    registry_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "artifacts": {
                    "phase4.401.consensus_transcriptomic_program_catalog": registry_entry(
                        "catalog.csv", "notebooks/401.ipynb"
                    )
                },
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        analysis_parameters,
        "load_consensus_programs",
        partial(
            analysis_parameters.load_consensus_programs,
            registry_path=registry_path,
            root=tmp_path,
        ),
    )


@pytest.fixture
def input_layers(monkeypatch):
    scores = pd.DataFrame(
        {"P1": [1.5, 2.5, 3.5], "ModelID": ["M2", "M1", "M3"], "P2": [9.0, 1.0, -2.0]},
        index=[7, 2, 11],
    )
    cohort = pd.DataFrame(
        {"ModelID": ["M1", "M3", "M2"], "OncotreeLineage": ["L1", "L3", "L2"]}
    )
    frozen = cohort.iloc[:2].copy()
    files = {
        "scores": scores,
        "crispr": pd.DataFrame(
            {"Unnamed: 0": ["M4", "M1", "M2"], "G (7)": [41.0, 11.0, 21.0]}
        ),
        "cohort": cohort,
        "rnai": pd.DataFrame(
            {"M3": [-3.0, -2.0], "M1": [-1.0, -2.0]}, index=["G7", "G8"]
        ),
        "frozen": frozen,
        "model_coverage": frozen.assign(source_pattern=["s1", "s2"]),
        "gene_coverage": pd.DataFrame(
            {
                "gene_label": ["G8", "G7"],
                "is_composite": [True, False],
                "observed_models": [2, 2],
            }
        ),
    }
    monkeypatch.setattr(pd, "read_csv", lambda key: files[key].copy())
    monkeypatch.setattr(pd, "read_parquet", lambda key: files[key].copy())
    env = {
        "consensus_cellline_scores_path": "scores",
        "crispr_gene_effect_path": "crispr",
        "cell_line_cohort_path": "cohort",
        "CONSENSUS_CELLLINE_SCORES_PATH": "scores",
        "RNAI_DEPENDENCY_HANDOFF_PATH": "rnai",
        "RNAI_FROZEN_COHORT_PATH": "frozen",
        "RNAI_MODEL_COVERAGE_PATH": "model_coverage",
        "RNAI_GENE_COVERAGE_PATH": "gene_coverage",
    }
    return files, env


@pytest.mark.parametrize("number", [500, 501])
@pytest.mark.parametrize(
    ("columns", "message"),
    [
        (["P1", "ModelID"], "missing=.*P2"),
        (["P1", "P2"], "missing=.*ModelID"),
        (["P1", "ModelID", "P2", "CONSENSUS_TX_OLD"], "unexpected=.*CONSENSUS_TX_OLD"),
        (["P1", "ModelID", "P2", "P2"], "duplicate"),
        (["P1", "ModelID", "P2", "ModelID"], "duplicate"),
    ],
)
def test_full_score_schema(catalog, input_layers, number, columns, message):
    files, env = input_layers
    files["scores"] = files["scores"].assign(CONSENSUS_TX_OLD=0)[columns]
    with pytest.raises(ValueError, match=message):
        run_cells(notebook_cells(number)[1], [1, 3], env)


def test_crispr_intersection_and_alignment(catalog, input_layers):
    files, env = input_layers
    _, cells = notebook_cells(500)
    run_cells(cells, [1, 3, 5, 6, 7, 17], env)
    expected_scores = (
        files["scores"].set_index("ModelID").loc[["M2", "M1"], PROGRAM_IDS]
    )
    pd.testing.assert_frame_equal(env["shared_consensus_scores"], expected_scores)
    assert env["consensus_cellline_scores"].index.tolist() == [7, 2, 11]
    assert env["shared_model_ids"] == {"M1", "M2"}
    assert env["shared_crispr_gene_effect"]["G (7)"].tolist() == [21.0, 11.0]
    assert env["shared_consensus_analysis"]["OncotreeLineage"].tolist() == ["L2", "L1"]


def test_crispr_rejects_302_mismatch_outside_platform(catalog, input_layers):
    files, env = input_layers
    files["scores"].loc[11, "ModelID"] = "M5"
    with pytest.raises(ValueError, match="missing=.*M3.*unexpected=.*M5"):
        run_cells(notebook_cells(500)[1], [1, 3, 5, 6], env)


def test_rnai_frozen_cohort_and_alignment(catalog, input_layers):
    files, env = input_layers
    run_cells(notebook_cells(501)[1], [1, 3, 4, 5, 6, 7, 9, 10], env)
    scores = env["consensus_cellline_scores"]
    pd.testing.assert_frame_equal(scores, files["scores"][["ModelID", *PROGRAM_IDS]])
    models = env["rnai_analysis_models"]
    assert models.columns.tolist() == [
        "OncotreeLineage",
        "source_pattern",
        *PROGRAM_IDS,
    ]
    assert models.index.tolist() == ["M3", "M1"]
    assert models["OncotreeLineage"].tolist() == ["L3", "L1"]
    assert models["source_pattern"].tolist() == ["s2", "s1"]
    assert models["P2"].tolist() == [-2.0, 1.0]
    pd.testing.assert_frame_equal(
        env["primary_rnai_dependency"], files["rnai"].loc[["G7"]]
    )
    assert env["PRIMARY_COVERAGE_FRACTION"] == 0.75
    assert env["SENSITIVITY_COVERAGE_FRACTION"] == 0.90


@pytest.mark.parametrize(
    ("layer", "old", "message"),
    [
        ("model_coverage", "M1", "model coverage ModelIDs differ"),
        ("rnai", "M1", "dependency handoff ModelIDs differ"),
        ("scores", "M1", "RNAi models are missing"),
        ("gene_coverage", "G7", "gene coverage and dependency handoff labels differ"),
    ],
)
def test_rnai_detects_incompatible_handoffs(catalog, input_layers, layer, old, message):
    files, env = input_layers
    files[layer] = files[layer].rename(columns={old: "unknown"}).replace(old, "unknown")
    with pytest.raises(ValueError, match=message):
        run_cells(notebook_cells(501)[1], [1, 3, 4, 5, 6], env)


@pytest.mark.parametrize(
    ("crispr", "rnai", "sensitivity", "message"),
    [
        (["P1", "P2", "P2"], ["P2", "P1"], ["P1"], None),
        (["P1", "P2"], ["P2", "P1"], [], None),
        (["old1", "old2"], ["old1", "old2"], [], "CRISPR primary.*unexpected"),
        (["P1", "P2"], ["P1"], [], "RNAi primary.*missing"),
        (["P1", "P2"], ["P1", "P2", None], [], "RNAi primary.*missing identifiers=1"),
        (["P1", "P2"], ["P2", "P1"], ["old1"], "RNAi 90% coverage.*unexpected"),
    ],
)
def test_integrated_program_universe(catalog, crispr, rnai, sensitivity, message):
    env = {
        name: pd.DataFrame({"consensus_program_id": ids})
        for name, ids in {
            "crispr_primary_associations": crispr,
            "rnai_primary_associations": rnai,
            "crispr_within_lineage": [],
            "rnai_within_lineage": ["P2"],
            "rnai_source_adjusted": ["P1"],
            "rnai_coverage90": sensitivity,
        }.items()
    }
    env.update(crispr_model_cohort=[], rnai_model_cohort=[])
    _, cells = notebook_cells(502)
    if message:
        with pytest.raises(ValueError, match=message):
            run_cells(cells, [1, 4], env)
        return
    run_cells(cells, [1, 4], env)
    assert env["FROZEN_CONSENSUS_PROGRAM_IDS"] == PROGRAM_IDS
    env["integrated_primary_map"] = pd.DataFrame(
        {
            "consensus_program_id": ["P1", "P2", "P1"],
            "cross_platform_evidence_category": ["crispr_supported_only"] * 3,
        }
    )
    run_cells(cells, [25], env)
    summary = env["cross_platform_evidence_summary"]
    assert summary["consensus_program_id"].tolist() == PROGRAM_IDS
    assert summary["n_hypotheses"].tolist() == [1, 2]


PUBLICATION = {
    500: ([58, 59], [67, 68, 69], 70, "crispr_analysis_metadata", 7),
    501: ([47], [58], 59, "rnai_analysis_metadata", 9),
    502: ([57], [60], 61, "integrated_vulnerability_metadata", 5),
}


@pytest.mark.parametrize(
    ("number", "corruption"),
    [
        *[
            (n, mode)
            for n in PUBLICATION
            for mode in ("none", "value", "identity", "schema", "metadata")
        ],
        (502, "parquet_value"),
        (502, "parquet_key"),
    ],
)
def test_publication_closure(tmp_path, monkeypatch, number, corruption):
    notebook_path, cells = notebook_cells(number)
    path_cells, write_cells, closure_cell, metadata_var, count = PUBLICATION[number]
    declarations = json.loads((ROOT / "config/artifact_registry.json").read_bytes())[
        "artifacts"
    ]
    declared_paths = {
        entry["path"]: entry["artifact_role"]
        for entry in declarations.values()
        if entry["producer"].get("path") == notebook_path
    }
    assert len(declared_paths) == count
    env = {
        "Paths": SimpleNamespace(
            dependencies=tmp_path / "data/interim/dependencies",
            functional_vulnerabilities=tmp_path
            / "data/processed/functional_vulnerabilities",
        ),
        "pd": pd,
        "np": np,
        "json": json,
        "display": lambda obj: None,
        "project_relative_path": lambda path: path.relative_to(tmp_path).as_posix(),
        metadata_var: {"program_ids": PROGRAM_IDS, "analysis": {"n_tests": 2}},
    }
    run_cells(cells, path_cells, env)
    frame = pd.DataFrame(
        {
            "consensus_program_id": ["P2", "P1"],
            "cross_platform_entrez_id": pd.array([2**53 + 1, 18], dtype="Int64"),
            "annotation": pd.Categorical(["NA", "symbol, with\nnewline"]),
            "p_value": [1e-200, np.nan],
            "supported": pd.array([True, pd.NA], dtype="boolean"),
        },
        index=[7, 2],
    )
    outputs = {}
    for index in write_cells:
        for node in ast.walk(ast.parse(cells[index])):
            if not isinstance(node, ast.Call) or not isinstance(
                node.func, ast.Attribute
            ):
                continue
            if node.func.attr in {"to_csv", "to_parquet"}:
                path = env[node.args[0].id]
                table = frame
                if node.func.value.id.endswith(
                    ("evidence_artifact", "significant_output")
                ):
                    table = frame.iloc[:0]
                env[node.func.value.id] = table
                outputs[path] = table
            elif node.func.attr == "open":
                outputs[env[node.func.value.id]] = None

    assert {
        env["project_relative_path"](path) for path in outputs
    } == declared_paths.keys()
    assert cells[closure_cell].count("refresh_notebook_artifacts(") == 1

    for path in outputs:
        path.parent.mkdir(parents=True, exist_ok=True)
    run_cells(cells, write_cells, env)

    registry_path = tmp_path / "registry.json"
    old_registry = {
        "schema_version": 1,
        "artifacts": {
            f"synthetic.{i}": registry_entry(path, notebook_path, role)
            for i, (path, role) in enumerate(declared_paths.items())
        },
    }
    registry_path.write_text(json.dumps(old_registry), encoding="utf-8")
    old_bytes = registry_path.read_bytes()
    real_refresh = artifact_registry.refresh_notebook_artifacts
    real_load = artifact_registry.load_artifact_registry
    refresh_calls = []

    def refresh(path, verified_outputs, *, require_unchanged):
        refresh_calls.append(path)
        assert path == notebook_path
        assert not require_unchanged
        assert verified_outputs == {
            file: table.shape if table is not None else None
            for file, table in outputs.items()
        }
        return real_refresh(
            path,
            verified_outputs,
            registry_path=registry_path,
            root=tmp_path,
            require_unchanged=require_unchanged,
        )

    monkeypatch.setattr(artifact_registry, "refresh_notebook_artifacts", refresh)

    def load(path=registry_path):
        assert path == registry_path
        return real_load(path)

    monkeypatch.setattr(artifact_registry, "load_artifact_registry", load)

    csv_path = next(path for path in outputs if path.suffix == ".csv")
    with csv_path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.reader(handle))
    if corruption == "value":
        rows[1][3] = "0.0"
    elif corruption == "identity":
        rows[1], rows[2] = rows[2], rows[1]
    elif corruption == "schema":
        rows[0][0] = "old_program_id"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle, quoting=csv.QUOTE_ALL).writerows(rows)

    if corruption == "metadata":
        metadata_path = next(path for path in outputs if path.suffix == ".json")
        metadata_path.write_text('{"program_ids":["old"]}', encoding="utf-8")
    if corruption.startswith("parquet"):
        parquet_path = next(path for path in outputs if path.suffix == ".parquet")
        changed = frame.copy()
        if corruption == "parquet_value":
            changed.loc[7, "p_value"] = 0.0
        else:
            changed.iloc[1, :2] = changed.iloc[0, :2]
        changed.to_parquet(parquet_path, index=False)

    if corruption != "none":
        with pytest.raises((ValueError, AssertionError)):
            run_cells(cells, [closure_cell], env)
        assert not refresh_calls
        assert registry_path.read_bytes() == old_bytes
        return

    run_cells(cells, [closure_cell], env)
    assert refresh_calls == [notebook_path]
    updated = real_load(registry_path)
    assert artifact_registry.verify_artifact_identity(updated, root=tmp_path) == []
    mutable_fields = {"shape", "size_bytes", "sha256"}
    for artifact_id, before in old_registry["artifacts"].items():
        after = updated["artifacts"][artifact_id]
        assert {k: v for k, v in after.items() if k not in mutable_fields} == {
            k: v for k, v in before.items() if k not in mutable_fields
        }
        table = outputs[tmp_path / before["path"]]
        assert after["shape"] == (None if table is None else list(table.shape))
