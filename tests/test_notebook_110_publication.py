import json
from pathlib import Path
from types import SimpleNamespace

import h5py
import numpy as np
import pandas as pd
import pytest

from pancancer_epigenetics.utils import artifact_registry
from pancancer_epigenetics.utils.file_checks import calculate_sha256

NOTEBOOK = (
    Path(__file__).resolve().parents[1]
    / "notebooks/phase1_data_acquisition_and_auditing"
    / "110_lincs_cmap_acquisition_and_audit.ipynb"
)
CELLS = json.loads(NOTEBOOK.read_text(encoding="utf-8"))["cells"]
CATALOG = "phase4.401.consensus_transcriptomic_program_catalog"
WEIGHTS = "phase4.401.consensus_transcriptomic_gene_weights"
PREFIX = "phase1.110."
CATALOG_DEPENDENCY = {"type": "artifact", "artifact_id": CATALOG}


def run_cells(env, *numbers):
    for number in numbers:
        source = "".join(CELLS[number - 1]["source"])
        exec(compile(source, f"{NOTEBOOK.name}:cell {number}", "exec"), env)


class NotebookFiles:
    def __init__(self, root, monkeypatch):
        self.root = root
        self.paths = SimpleNamespace(
            root=root,
            lincs=root / "data/raw/lincs",
            consensus_programs=root / "data/processed/consensus_programs",
            perturbational=root / "data/interim/perturbational",
            artifact_registry=root / "config/artifact_registry.json",
            raw_data_registry=root / "config/raw_data_registry.json",
        )
        for directory in (
            self.paths.lincs,
            self.paths.consensus_programs,
            self.paths.perturbational,
            self.paths.artifact_registry.parent,
        ):
            directory.mkdir(parents=True)
        self.env = {}
        run_cells(self.env, 2)
        self.env["Paths"] = self.paths
        monkeypatch.setattr(artifact_registry, "Paths", self.paths)
        run_cells(self.env, 3)
        raw_paths = [
            path for name, path in self.env.items() if name.startswith("LINCS_")
        ]
        for path in raw_paths:
            path.write_text(path.name, encoding="utf-8")
        self.geneinfo = self.env["LINCS_GENEINFO_PATH"]
        self.set_feature_spaces(["landmark", "best inferred", "inferred"])
        gctx = self.env["LINCS_LEVEL5_TRT_CP_PATH"]
        with h5py.File(gctx, "w") as handle:
            handle.create_dataset("0/META/ROW/id", data=[b"17", b"4", b"8"])
        self.raw_paths = raw_paths
        self.files = {}
        self.registry = {"schema_version": 1, "artifacts": {}}

    def set_feature_spaces(self, feature_spaces):
        pd.DataFrame(
            {
                "gene_symbol": ["G1", "G2", "G3"],
                "gene_id": [8, 4, 17],
                "feature_space": feature_spaces,
            }
        ).to_csv(self.geneinfo, sep="\t", index=False)

    def write_raw_registry(self):
        raw = {
            "lincs": {
                "provenance_mode": "file_managed",
                "canonical_dir": self.paths.lincs.relative_to(self.root).as_posix(),
                "files": {
                    path.name: {
                        "role": path.name,
                        "status": "acquired_and_used",
                        "size_bytes": path.stat().st_size,
                        "sha256": calculate_sha256(path),
                    }
                    for path in self.raw_paths
                },
            }
        }
        self.paths.raw_data_registry.write_text(json.dumps(raw), encoding="utf-8")

    def add(self, artifact_id, path, frame, inputs=()):
        phase4 = artifact_id.startswith("phase4.")
        if path.suffix == ".parquet":
            frame.to_parquet(path, index=False)
        else:
            frame.to_csv(path, index=False)
        self.files[artifact_id] = path
        self.registry["artifacts"][artifact_id] = {
            "path": path.relative_to(self.root).as_posix(),
            "phase": 4 if phase4 else 1,
            "status": "frozen",
            "artifact_role": "data",
            "producer": {
                "type": "notebook",
                "path": (
                    "notebooks/phase4_consensus_programs/"
                    "401_consensus_program_construction.ipynb"
                    if phase4
                    else NOTEBOOK.relative_to(NOTEBOOK.parents[2]).as_posix()
                ),
            },
            "shape": list(frame.shape),
            "size_bytes": path.stat().st_size,
            "sha256": calculate_sha256(path),
            "inputs": list(inputs),
        }

    def inputs(self, ids, weights=None):
        catalog = pd.DataFrame(
            {
                "consensus_program_id": ids,
                "tumor_rna_axis": [f"tumor-{key}" for key in ids],
                "cell_line_program": [f"cell-{key}" for key in ids],
                "orientation_multiplier": [-1 if key == "Z" else 1 for key in ids],
            }
        )
        if weights is None:
            weights = catalog.iloc[::-1].merge(
                pd.DataFrame(
                    {
                        "gene_symbol": ["G4", "G3", "G2", "G1"],
                        "tumor_loading": [1.0, 2.0, 3.0, 4.0],
                        "cell_line_loading": [2.0, 3.0, 4.0, 5.0],
                        "consensus_weight": [4.0, -1.0, -3.0, 2.0],
                    }
                ),
                how="cross",
            )
        self.add(CATALOG, self.paths.consensus_programs / "catalog.csv", catalog)
        self.add(WEIGHTS, self.paths.consensus_programs / "weights.csv", weights)
        self.save_registry()
        return weights

    def save_registry(self):
        self.paths.artifact_registry.write_text(
            json.dumps(self.registry), encoding="utf-8"
        )

    def audit(self):
        self.write_raw_registry()
        run_cells(self.env, 4, 16, 17, 18, 19, 20, 21, 22, 23, 72, 73)

    def prepare_publication(self):
        run_cells(self.env, 74, 75, 76, 77, 78)
        for artifact_id in (*self.env["RETAINED_IDS"], *self.env["program_candidates"]):
            name = artifact_id.removeprefix(PREFIX)
            suffix = ".parquet" if name == "primary_signature_handoff" else ".csv"
            frame = (
                self.env["verified_lincs_inventory"]
                if name == "raw_input_inventory"
                else pd.DataFrame({"historical": [name]})
            )
            inputs = (
                [{"type": "artifact", "artifact_id": WEIGHTS}]
                if artifact_id in self.env["program_candidates"]
                else []
            )
            self.add(
                artifact_id, self.paths.perturbational / (name + suffix), frame, inputs
            )
        self.save_registry()

    def snapshot(self):
        return {
            path: path.read_bytes()
            for path in (
                self.paths.raw_data_registry,
                self.paths.artifact_registry,
                *self.files.values(),
            )
        }


@pytest.fixture
def files(tmp_path, monkeypatch):
    return NotebookFiles(tmp_path, monkeypatch)


@pytest.mark.parametrize("ids", [("Z",), ("Z", "A"), ("Z", "M", "A")])
def test_catalog_order_signed_weights_and_provider_index(files, ids):
    files.inputs(list(ids))
    files.audit()
    env = files.env
    assert tuple(env["representation_fidelity"]["consensus_program_id"]) == ids
    bing = env["phase7_bing_gene_handoff"]
    assert tuple(bing["consensus_program_id"].drop_duplicates()) == ids
    assert list(bing["consensus_weight"]) == [2.0, -3.0] * len(ids)
    assert list(bing["gene_id"]) == [8, 4] * len(ids)
    assert list(bing["gctx_gene_index"]) == [2, 1] * len(ids)
    assert bing.iloc[0]["orientation_multiplier"] == -1
    fidelity = env["representation_fidelity"].iloc[0]
    assert fidelity["bing_l1_fraction"] == pytest.approx(5 / 10)
    assert fidelity["bing_l2_sq_fraction"] == pytest.approx(13 / 30)
    assert fidelity["bing_cosine_fidelity"] == pytest.approx(np.sqrt(13 / 30))
    assert fidelity["bing_negative_l1_fraction"] == pytest.approx(3 / 4)
    assert fidelity["landmark_negative_l1_fraction"] == 0
    assert fidelity["landmark_minimum_signed_arm_l1_fraction"] == 0


@pytest.mark.parametrize(
    ("problem", "diagnostic"),
    [
        ("missing", "Missing: .*A"),
        ("unexpected", "Unexpected: .*B"),
        ("duplicate", "Duplicate consensus program-gene"),
        ("orientation", "Catalog metadata disagree"),
        ("axis", "Catalog metadata disagree"),
        ("source", "Catalog metadata disagree"),
        ("identifier", "Missing or invalid consensus identifier"),
        ("support", "Unequal Phase 4 gene support"),
        ("nonfinite", "Consensus weights must be finite"),
        ("zero_mass", "Invalid full-program weight mass"),
        ("overflow", "Invalid full-program weight mass"),
    ],
)
def test_invalid_weights(files, problem, diagnostic):
    ids = ["Z", "A"]
    weights = files.inputs(ids)
    if problem == "missing":
        weights = weights.loc[weights["consensus_program_id"].ne("A")]
    elif problem == "unexpected":
        weights = pd.concat(
            [weights, weights.iloc[[0]].assign(consensus_program_id="B")]
        )
    elif problem == "duplicate":
        weights = pd.concat([weights, weights.iloc[[0]]])
    elif problem == "orientation":
        weights.loc[0, "orientation_multiplier"] *= -1
    elif problem == "axis":
        weights.loc[0, "tumor_rna_axis"] = "wrong-axis"
    elif problem == "source":
        weights.loc[0, "cell_line_program"] = "wrong-source"
    elif problem == "identifier":
        weights.loc[0, "gene_symbol"] = ""
    elif problem == "support":
        weights.loc[0, "gene_symbol"] = "other"
    elif problem == "nonfinite":
        weights.loc[0, "consensus_weight"] = np.inf
    elif problem == "zero_mass":
        weights["consensus_weight"] = 0
    elif problem == "overflow":
        weights["consensus_weight"] = 1e200
    files.inputs(ids, weights)
    with pytest.raises(ValueError, match=diagnostic):
        files.audit()


@pytest.mark.parametrize("artifact_id", [CATALOG, WEIGHTS])
@pytest.mark.parametrize(
    ("problem", "diagnostic"),
    [
        ("hash", "sha256_mismatch"),
        ("size", "size_mismatch"),
        ("shape", "Declared dimensions"),
        ("producer", "Unexpected producer"),
        ("path", "Unexpected registered path"),
    ],
)
def test_reject_inconsistent_registered_inputs(files, artifact_id, problem, diagnostic):
    files.inputs(["Z"])
    path = files.files[artifact_id]
    entry = files.registry["artifacts"][artifact_id]
    if problem == "hash":
        path.write_bytes(path.read_bytes().replace(b"tumor-Z", b"tumor-B"))
    elif problem == "size":
        with path.open("ab") as handle:
            handle.write(b"\n")
    elif problem == "shape":
        entry["shape"][0] += 1
    elif problem == "producer":
        entry["producer"]["path"] = "notebooks/wrong.ipynb"
    elif problem == "path":
        entry["path"] = f"data/interim/{path.name}"
    files.save_registry()
    with pytest.raises(ValueError, match=diagnostic):
        files.audit()


def test_undefined_full_arm_differs_from_zero_mapped_retention(files):
    weights = files.inputs(["Z"])
    weights["consensus_weight"] = weights["consensus_weight"].abs()
    files.inputs(["Z"], weights)
    files.audit()
    fidelity = files.env["representation_fidelity"].iloc[0]
    assert np.isnan(fidelity["landmark_negative_l1_fraction"])
    assert np.isnan(fidelity["landmark_minimum_signed_arm_l1_fraction"])
    assert fidelity["landmark_positive_l1_fraction"] > 0
    files.prepare_publication()
    frame = files.env["representation_fidelity"]
    staged = files.root / "fidelity.csv"
    frame.to_csv(staged, index=False)
    assert files.env["verify_candidate_csv"](staged, frame) == frame.shape


def test_ambiguous_lincs_symbol_blocks_handoff(files):
    files.inputs(["Z", "A"])
    genes = pd.read_csv(files.geneinfo, sep="\t")
    genes.loc[1, "gene_symbol"] = "G1"
    genes.to_csv(files.geneinfo, sep="\t", index=False)
    with pytest.raises(
        ValueError, match="Ambiguous exact LINCS gene-symbol mapping.*G1"
    ):
        files.audit()


@pytest.mark.parametrize(
    ("spaces", "artifact_id"),
    [
        (["inferred"] * 3, "bing_gene_handoff"),
        (["best inferred", "best inferred", "inferred"], "landmark_gene_handoff"),
    ],
)
def test_empty_representation_remains_in_audit_but_blocks_publication(
    files, spaces, artifact_id
):
    files.inputs(["Z", "A"])
    files.set_feature_spaces(spaces)
    files.audit()
    files.prepare_publication()
    before = files.snapshot()
    assert list(files.env["representation_fidelity"]["consensus_program_id"]) == [
        "Z",
        "A",
    ]
    assert files.env["program_candidates"][PREFIX + artifact_id].empty
    with pytest.raises(ValueError, match=f"Non-evaluable .*{artifact_id} for Z"):
        files.env["publish_program_handoffs"](files.env["program_candidates"])
    assert files.snapshot() == before


def test_prospective_declarations_change_only_three_dependencies(files):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    before = files.snapshot()
    entries = files.registry["artifacts"]
    proposed = files.env["propose_catalog_dependencies"](entries)
    assert proposed.keys() == files.env["program_candidates"].keys()
    for key, entry in proposed.items():
        assert entry == {
            **entries[key],
            "inputs": [*entries[key]["inputs"], CATALOG_DEPENDENCY],
        }
        assert CATALOG_DEPENDENCY not in entries[key]["inputs"]
    assert files.snapshot() == before


def test_nonempty_zero_norm_representation_blocks_publication(files):
    ids = ["Z", "A"]
    weights = files.inputs(ids)
    weights.loc[weights["gene_symbol"].eq("G1"), "consensus_weight"] = 0
    files.inputs(ids, weights)
    files.audit()
    files.prepare_publication()
    assert len(files.env["phase7_landmark_gene_handoff"]) == len(ids)
    before = files.snapshot()
    with pytest.raises(ValueError, match="Non-evaluable .*landmark_gene_handoff"):
        files.env["publish_program_handoffs"](files.env["program_candidates"])
    assert files.snapshot() == before


def test_complete_publication_preserves_retained_identities(files):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    before = files.snapshot()
    run_cells(files.env, 79)
    assert files.snapshot() == before

    files.env["AUTHORIZE_PROGRAM_REBUILD"] = True
    run_cells(files.env, 79)
    entries = artifact_registry.load_artifact_registry(files.paths.artifact_registry)
    published = files.env["published_entries"]
    assert len(published) == 7
    assert not artifact_registry.verify_artifact_identity(
        {"artifacts": published}, root=files.root
    )
    assert (
        files.paths.raw_data_registry.read_bytes()
        == before[files.paths.raw_data_registry]
    )
    for key in files.env["RETAINED_IDS"]:
        assert published[key] == files.registry["artifacts"][key]
        assert files.files[key].read_bytes() == before[files.files[key]]
    for key, candidate in files.env["program_candidates"].items():
        assert CATALOG_DEPENDENCY in published[key]["inputs"]
        assert published[key]["shape"] == list(candidate.shape)
        assert published[key] == entries["artifacts"][key]
        assert files.files[key].read_bytes() != before[files.files[key]]


def test_reject_changed_or_missing_retained_artifact(files):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    path = files.files[PREFIX + "primary_perturbagen_coverage"]
    path.write_bytes(b"x" + path.read_bytes()[1:])
    for issue in ("sha256_mismatch", "missing"):
        before = files.snapshot() if path.exists() else None
        registry = files.paths.artifact_registry.read_bytes()
        with pytest.raises(ValueError, match=f"primary_perturbagen_coverage.*{issue}"):
            files.env["publish_program_handoffs"](files.env["program_candidates"])
        assert files.paths.artifact_registry.read_bytes() == registry
        if before:
            assert files.snapshot() == before
            path.unlink()


def test_registered_raw_identity_mismatch_blocks_source_reads(files):
    files.write_raw_registry()
    files.geneinfo.write_bytes(b"x" + files.geneinfo.read_bytes()[1:])
    with pytest.raises(ValueError, match="Registered LINCS source identity differs"):
        run_cells(files.env, 4)


def test_raw_source_change_during_audit_blocks_publication(files):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    files.geneinfo.write_bytes(files.geneinfo.read_bytes() + b"\n")
    before = files.snapshot()
    with pytest.raises(
        ValueError, match="Registered LINCS source changed during the audit"
    ):
        files.env["publish_program_handoffs"](files.env["program_candidates"])
    assert files.snapshot() == before


def test_reject_invalid_in_memory_candidate(files):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    before = files.snapshot()
    candidates = files.env["program_candidates"].copy()
    key = PREFIX + "bing_gene_handoff"
    candidates[key] = candidates[key].assign(consensus_weight=1.0)
    with pytest.raises(AssertionError, match="consensus_weight"):
        files.env["publish_program_handoffs"](candidates)
    assert files.snapshot() == before


def test_reject_failed_staged_roundtrip(files, monkeypatch):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    before = files.snapshot()
    to_csv = pd.DataFrame.to_csv

    def corrupt_bing_index(frame, path, **kwargs):
        if path.name == "bing_gene_handoff.csv":
            frame = frame.assign(gctx_gene_index=99)
        return to_csv(frame, path, **kwargs)

    monkeypatch.setattr(pd.DataFrame, "to_csv", corrupt_bing_index)
    with pytest.raises(AssertionError, match="gctx_gene_index"):
        files.env["publish_program_handoffs"](files.env["program_candidates"])
    assert files.snapshot() == before


def test_declaration_failure_rolls_back_published_files(files):
    files.inputs(["Z", "A"])
    files.audit()
    files.prepare_publication()
    before = files.snapshot()

    def fail_declaration(*args, **kwargs):
        raise RuntimeError("Synthetic declaration failure")

    files.env["register_artifacts"] = fail_declaration
    with pytest.raises(RuntimeError, match="Synthetic declaration failure"):
        files.env["publish_program_handoffs"](files.env["program_candidates"])
    assert files.snapshot() == before
