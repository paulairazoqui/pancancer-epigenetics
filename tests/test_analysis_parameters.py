import json
from pathlib import Path

import pytest
import pandas as pd

from pancancer_epigenetics.analysis_parameters import (
    attribution_column,
    load_consensus_programs,
    load_model_ids,
    score_column,
    align_program_columns,
)

CATALOG = "phase4.401.consensus_transcriptomic_program_catalog"
COHORT = "phase3.302.integrated_modeling_cohort"
HEADER = (
    "consensus_program_id,tumor_rna_axis,cell_line_program,orientation_multiplier\n"
)


@pytest.fixture
def artifacts(tmp_path):
    def entry(path):
        return {
            "path": path,
            "phase": 4,
            "status": "frozen",
            "artifact_role": "data",
            "producer": {"type": "notebook", "path": "notebooks/example.ipynb"},
            "shape": None,
            "size_bytes": 0,
            "sha256": "a" * 64,
            "inputs": [],
        }

    registry = tmp_path / "registry.json"
    registry.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "artifacts": {
                    CATALOG: entry("catalog.csv"),
                    COHORT: entry("cohort.csv"),
                },
            }
        ),
        encoding="utf-8",
    )
    return tmp_path, registry


def write_catalog(root, ids):
    (root / "catalog.csv").write_text(
        HEADER
        + "".join(f"{pid},axis{i},source{i},{(-1)**i}\n" for i, pid in enumerate(ids)),
        encoding="utf-8",
    )


@pytest.mark.parametrize("ids", [["B"], ["B", "A"], ["D", "C", "B", "A"]])
def test_catalog_order_and_orientation(artifacts, ids):
    root, registry = artifacts
    write_catalog(root, ids)
    programs = load_consensus_programs(root=root, registry_path=registry)
    assert [p.program_id for p in programs] == ids
    assert programs[0].tumor_rna_axis == "axis0"
    assert programs[0].orientation_multiplier == 1


@pytest.mark.parametrize("ids", [[], ["A", "A"], ["A", ""], [" A"]])
def test_invalid_catalog_ids(artifacts, ids):
    root, registry = artifacts
    write_catalog(root, ids)
    with pytest.raises(ValueError, match="identifier"):
        load_consensus_programs(root=root, registry_path=registry)


def test_invalid_catalog_schema_and_orientation(artifacts):
    root, registry = artifacts
    (root / "catalog.csv").write_text("wrong\nA\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Missing required columns"):
        load_consensus_programs(root=root, registry_path=registry)
    (root / "catalog.csv").write_text(HEADER + "A,axis,source,0\n", encoding="utf-8")
    with pytest.raises(ValueError, match="orientation multiplier"):
        load_consensus_programs(root=root, registry_path=registry)


def test_columns_and_validation():
    assert score_column("B") == "B"
    assert attribution_column("B") == "phi_B"
    for columns in (
        ["ModelID", "B"],
        ["ModelID", "B", "A", "C"],
        ["ModelID", "B", "B", "A"],
    ):
        with pytest.raises(ValueError):
            align_program_columns(
                pd.DataFrame(columns=columns), ["B", "A"], metadata_columns=["ModelID"]
            )
    with pytest.raises(ValueError, match="duplicate"):
        align_program_columns(pd.DataFrame(columns=["A"]), ["A", "A"])
    with pytest.raises(ValueError, match="overlap"):
        align_program_columns(
            pd.DataFrame(columns=["A"]), ["A"], metadata_columns=["A"]
        )
    with pytest.raises(ValueError, match="missing=.*ModelID"):
        align_program_columns(
            pd.DataFrame(columns=["A"]), ["A"], metadata_columns=["ModelID"]
        )
    with pytest.raises(ValueError, match="duplicate"):
        align_program_columns(
            pd.DataFrame(columns=["A", "ModelID"]),
            ["A"],
            metadata_columns=["ModelID", "ModelID"],
        )


@pytest.mark.parametrize("attribution", [False, True])
def test_align_program_columns(attribution):
    prefix = "phi_" if attribution else ""
    frame = pd.DataFrame(
        {
            f"{prefix}A": [1, 2],
            "lineage": ["x", "y"],
            f"{prefix}B": [3, 4],
            "ModelID": ["m1", "m2"],
        },
        index=[7, 9],
    )
    original = frame.copy(deep=True)
    aligned = align_program_columns(
        frame,
        ["B", "A"],
        metadata_columns=["ModelID", "lineage"],
        attribution=attribution,
    )
    expected = pd.DataFrame(
        {
            "ModelID": ["m1", "m2"],
            "lineage": ["x", "y"],
            f"{prefix}B": [3, 4],
            f"{prefix}A": [1, 2],
        },
        index=[7, 9],
    )
    pd.testing.assert_frame_equal(aligned, expected)
    pd.testing.assert_frame_equal(frame, original)
    aligned.iloc[0, 0] = "changed"
    pd.testing.assert_frame_equal(frame, original)


def test_cohort_and_no_writes(artifacts):
    root, registry = artifacts
    write_catalog(root, ["B", "A"])
    cohort = root / "cohort.csv"
    cohort.write_text("ModelID,other\nM2,x\nM1,y\n", encoding="utf-8")
    before = {p.name: p.read_bytes() for p in root.iterdir()}
    assert load_model_ids(root=root, registry_path=registry) == ("M2", "M1")
    assert (
        len(load_model_ids(root=root, registry_path=registry, artifact_id=COHORT)) == 2
    )
    load_consensus_programs(root=root, registry_path=registry)
    assert {p.name: p.read_bytes() for p in root.iterdir()} == before
    cohort.write_text("ModelID\nM1\nM1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate"):
        load_model_ids(root=root, registry_path=registry)


def test_missing_inputs(artifacts):
    root, registry = artifacts
    with pytest.raises(FileNotFoundError, match="Required artifact"):
        load_consensus_programs(root=root, registry_path=registry)
    with pytest.raises(FileNotFoundError):
        load_model_ids(root=root, registry_path=root / "absent.json")
    with pytest.raises((KeyError, ValueError), match="missing"):
        load_model_ids(root=root, registry_path=registry, artifact_id="missing")


def test_import_does_not_read_configuration():
    import subprocess
    import sys

    code = """
import builtins
from pathlib import Path

def reject(*args, **kwargs):
    raise AssertionError('unexpected filesystem read during import')

builtins.open = reject
Path.open = reject
Path.read_text = reject
import pancancer_epigenetics.analysis_parameters
"""
    subprocess.run([sys.executable, "-c", code], check=True)
