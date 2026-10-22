"""Notebook 800 PRE-FLIGHT A: technical inventories only; no program scoring.

Run from project root:
    python scripts/phase8_800_preflight_audit.py

Requires previously executed Notebook 111 local audit files and frozen Phase 4
artifacts. Does not change manifests, raw payloads, registries or any frozen
upstream result. Program weights are checked for identity, not applied.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd

from pancancer_epigenetics.utils.paths import Paths, project_relative_path


BASE = Paths.metadata
OUT = BASE
SOURCE_FILES = {
    "file_index": BASE / "111_cptac3_file_index.csv",
    "candidate_primary": BASE / "111_cptac3_provisional_primary_tumor_files.csv",
    "ambiguity_by_lineage": BASE / "111_cptac3_ambiguity_by_lineage.csv",
    "ambiguous_sample_candidates": BASE / "111_cptac3_ambiguous_sample_candidates.csv",
}
SUMMARY_PATH = BASE / "111_cptac3_acquisition_audit_summary.json"
GENE_UNIVERSE_ID = "phase4.400.cross_system_shared_gene_universe"
WEIGHTS_ID = "phase4.401.consensus_transcriptomic_gene_weights"
TCGA_MAPPING_ID = "phase2.203.final_sample_mapping"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(2**20), b""):
            digest.update(block)
    return digest.hexdigest()


def check_columns(frame: pd.DataFrame, required: set[str], name: str) -> None:
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"{name} missing columns: {sorted(missing)}")


def strset(frame: pd.DataFrame, column: str) -> set[str]:
    return set(frame[column].dropna().astype(str))


def unique_join(values: pd.Series) -> str:
    return "|".join(sorted({str(value) for value in values.dropna()}))


def record_path(path: Path) -> str:
    return project_relative_path(path)


def main() -> None:
    if not SUMMARY_PATH.is_file():
        raise FileNotFoundError(f"First execute Notebook 111: {SUMMARY_PATH}")
    with SUMMARY_PATH.open(encoding="utf-8") as handle:
        summary = json.load(handle)
    if summary.get("cohort_frozen") is not False:
        raise ValueError("Unexpected Notebook 111 cohort-freeze status")
    if summary.get("phase8_validation_performed") is not False:
        raise ValueError("Unexpected Notebook 111 validation status")
    if summary.get("n_files_by_modality") != {"rnaseq": 2968, "methylation": 2610}:
        raise ValueError("Unexpected Notebook 111 source universe")

    inputs = {}
    for name, path in SOURCE_FILES.items():
        if not path.is_file():
            raise FileNotFoundError(f"Missing Notebook 111 audit artifact: {path}")
        current_sha = sha256(path)
        expected_sha = summary["audit_artifacts"][name]["sha256"]
        if current_sha != expected_sha:
            raise ValueError(f"Notebook 111 artifact fingerprint mismatch: {name}")
        inputs[name] = {
            "path": record_path(path),
            "sha256": current_sha,
        }
    inputs["111_summary"] = {
        "path": record_path(SUMMARY_PATH),
        "sha256": sha256(SUMMARY_PATH),
    }

    index = pd.read_csv(SOURCE_FILES["file_index"], dtype="string")
    primary = pd.read_csv(SOURCE_FILES["candidate_primary"], dtype="string")
    ambiguity = pd.read_csv(SOURCE_FILES["ambiguity_by_lineage"], dtype="string")
    candidates = pd.read_csv(SOURCE_FILES["ambiguous_sample_candidates"], dtype="string")
    required = {
        "modality", "file_id", "filename", "case_uuid", "aliquot_uuid",
        "sample_uuid", "mapping_status", "sample_type", "primary_site",
        "disease_type", "platform", "case_submitter_id",
    }
    check_columns(index, required, "111 file_index")
    check_columns(primary, required, "111 provisional primary")
    check_columns(ambiguity, {"modality", "primary_site", "disease_type",
                              "platform"}, "111 ambiguity by lineage")
    check_columns(candidates, {"modality", "file_id", "candidate_sample_uuid"},
                  "111 ambiguous sample candidates")
    if index.duplicated(["modality", "file_id"]).any():
        raise ValueError("Duplicate file in authoritative 111 index")
    if primary.duplicated(["modality", "file_id"]).any():
        raise ValueError("Duplicate primary file in 111 inventory")
    expected_primary = index[
        index["mapping_status"].eq("unique_aliquot_sample")
        & index["sample_type"].eq("Primary Tumor")
    ][["modality", "file_id"]]
    if set(map(tuple, expected_primary.to_numpy())) != set(
        map(tuple, primary[["modality", "file_id"]].to_numpy())
    ):
        raise ValueError("Primary subset inconsistent with 111 technical flag")
    if len(index) != 5578 or len(primary) != 3181 or len(candidates) != 1402:
        raise ValueError("Unexpected 111 local audit inventory dimensions")

    stratum_keys = ["modality", "primary_site", "disease_type", "platform"]
    index["unresolved_sample_ancestry"] = index["mapping_status"].eq(
        "ambiguous_sample_ancestry"
    ).astype("int64")
    index["provisional_primary"] = (
        index["mapping_status"].eq("unique_aliquot_sample")
        & index["sample_type"].eq("Primary Tumor")
    ).astype("int64")
    stratum = (
        index.groupby(stratum_keys, dropna=False)
        .agg(
            all_files=("file_id", "nunique"),
            all_case_uuids=("case_uuid", "nunique"),
            all_aliquot_uuids=("aliquot_uuid", "nunique"),
            all_resolved_sample_uuids=("sample_uuid", "nunique"),
            ambiguous_files=("unresolved_sample_ancestry", "sum"),
            primary_files=("provisional_primary", "sum"),
        )
        .reset_index()
    )
    eligible = (
        primary.groupby(stratum_keys, dropna=False)
        .agg(primary_case_uuids=("case_uuid", "nunique"),
             primary_sample_uuids=("sample_uuid", "nunique"),
             primary_aliquot_uuids=("aliquot_uuid", "nunique"))
        .reset_index()
    )
    stratum = stratum.merge(
        eligible, on=stratum_keys, how="left", validate="one_to_one"
    )
    for column in ["primary_case_uuids", "primary_sample_uuids",
                   "primary_aliquot_uuids"]:
        stratum[column] = stratum[column].fillna(0).astype("int64")
    stratum["ambiguous_file_fraction"] = (
        stratum["ambiguous_files"] / stratum["all_files"]
    )
    stratum = stratum.sort_values(
        ["modality", "primary_case_uuids", "primary_site", "disease_type"],
        ascending=[True, False, True, True], kind="stable"
    ).reset_index(drop=True)

    case_rows = (
        primary.groupby(["modality", "case_uuid"], dropna=False)
        .agg(
            n_files=("file_id", "nunique"),
            n_samples=("sample_uuid", "nunique"),
            n_aliquots=("aliquot_uuid", "nunique"),
            primary_site_values=("primary_site", unique_join),
            disease_type_values=("disease_type", unique_join),
            file_uuids=("file_id", unique_join),
            sample_uuids=("sample_uuid", unique_join),
        )
        .reset_index()
        .sort_values(["modality", "case_uuid"], kind="stable")
    )
    if case_rows["case_uuid"].isna().any():
        raise ValueError("Candidate primary case UUID missing")
    case_rows["requires_selection_review"] = (
        case_rows["n_files"].gt(1) | case_rows["n_samples"].gt(1)
        | case_rows["n_aliquots"].gt(1)
    )
    case_rows["selected_file_uuid"] = pd.NA
    case_rows["selection_state"] = "NOT_FROZEN"

    rna = primary[primary["modality"].eq("rnaseq")]
    meth = primary[primary["modality"].eq("methylation")]
    exact_overlap = {
        name: len(strset(rna, col) & strset(meth, col))
        for name, col in (
            ("case_uuids", "case_uuid"),
            ("sample_uuids", "sample_uuid"),
            ("aliquot_uuids", "aliquot_uuid"),
        )
    }

    with Paths.artifact_registry.open(encoding="utf-8") as handle:
        registry = json.load(handle)["artifacts"]
    frozen_frames = {}
    for key in (GENE_UNIVERSE_ID, WEIGHTS_ID, TCGA_MAPPING_ID):
        spec = registry[key]
        if spec["status"] != "frozen":
            raise ValueError(f"Not frozen: {key}")
        path = Paths.root / spec["path"]
        if not path.is_file() or sha256(path) != spec["sha256"]:
            raise ValueError(f"Missing/modified frozen artifact: {key}")
        frozen_frames[key] = pd.read_csv(path, dtype="string")
        inputs[key] = {"path": spec["path"], "sha256": spec["sha256"]}

    universe = frozen_frames[GENE_UNIVERSE_ID]
    weights = frozen_frames[WEIGHTS_ID]
    check_columns(universe, {"gene_symbol", "tumor_gene_id"},
                  "frozen gene universe")
    check_columns(weights, {"consensus_program_id", "gene_symbol",
                            "consensus_weight"}, "frozen gene weights")
    if len(universe) != 2389 or not universe["gene_symbol"].is_unique:
        raise ValueError("Unexpected frozen gene universe")
    if len(weights) != 7167 or weights.duplicated(
        ["consensus_program_id", "gene_symbol"]
    ).any():
        raise ValueError("Invalid frozen weight identity")
    if set(weights["consensus_program_id"]) != {
        "CONSENSUS_TX_01", "CONSENSUS_TX_02", "CONSENSUS_TX_03"
    }:
        raise ValueError("Unexpected frozen consensus program IDs")
    for program, frame in weights.groupby("consensus_program_id"):
        if strset(frame, "gene_symbol") != strset(universe, "gene_symbol"):
            raise ValueError(f"Frozen gene-set mismatch: {program}")
        if pd.to_numeric(frame["consensus_weight"], errors="coerce").isna().any():
            raise ValueError(f"Invalid frozen weights: {program}")

    tcga = frozen_frames[TCGA_MAPPING_ID]
    check_columns(tcga, {"case_submitter_id", "rna_case_uuid"},
                  "frozen TCGA mapping")
    exact_tcga_overlap = {
        "case_uuid_rna": len(strset(rna, "case_uuid")
                             & strset(tcga, "rna_case_uuid")),
        "case_submitter_id": len(strset(rna, "case_submitter_id")
                                 & strset(tcga, "case_submitter_id")),
    }
    # This is only a lexical ID comparison. It cannot certify donor independence.
    independence_state = "UNRESOLVED_DONOR_INDEPENDENCE"

    # A single deterministic *technical pilot* checks one external file's gene
    # ID format. It is not a representative cohort, a coverage gate, or a score.
    pilot = {
        "status": "NOT_ASSESSED",
        "reason": "No candidate RNA-seq payload inspected",
    }
    pilot_rows = []
    candidate = rna.sort_values("file_id", kind="stable").iloc[0]
    pilot_path = (Paths.root / "data" / "raw" / "cptac3"
                  / "rnaseq_star_counts" / str(candidate["file_id"])
                  / str(candidate["filename"]))
    if pilot_path.is_file():
        try:
            genes = pd.read_csv(
                pilot_path, sep="\t", comment="#", usecols=["gene_id"],
                dtype="string"
            )["gene_id"]
            provider_ids = set(genes.dropna().astype(str))
            provider_without_version = {
                item.split(".", 1)[0] for item in provider_ids
            }
            for item in universe.itertuples(index=False):
                source_id = str(item.tumor_gene_id)
                exact = source_id in provider_ids
                versionless = source_id.split(".", 1)[0] in provider_without_version
                pilot_rows.append({
                    "pilot_file_uuid": str(candidate["file_id"]),
                    "frozen_gene_symbol": str(item.gene_symbol),
                    "frozen_tumor_gene_id": source_id,
                    "exact_id_match": exact,
                    "version_insensitive_match_diagnostic": versionless,
                    "not_a_final_mapping_rule": True,
                })
            pilot = {
                "status": "PILOT_ONLY_NOT_COHORT_COVERAGE",
                "file_uuid": str(candidate["file_id"]),
                "n_exact_id_matches": sum(v["exact_id_match"] for v in pilot_rows),
                "n_version_insensitive_diagnostic_matches": sum(
                    v["version_insensitive_match_diagnostic"]
                    for v in pilot_rows
                ),
                "frozen_gene_universe_n": len(universe),
                "source_path": record_path(pilot_path),
                "warning": "No version-stripping rescue or primary coverage gate",
            }
        except (OSError, ValueError, KeyError) as exc:
            pilot = {
                "status": "PILOT_PARSE_FAILED",
                "file_uuid": str(candidate["file_id"]),
                "reason": str(exc),
            }
    else:
        pilot["reason"] = "Deterministic pilot payload absent: " + str(
            pilot_path
        )

    OUT.mkdir(parents=True, exist_ok=True)
    paths = {
        "lineage_inventory": OUT / "800_preflight_a_candidate_lineage_inventory.csv",
        "case_multiplicity": OUT / "800_preflight_a_case_multiplicity.csv",
        "gene_compatibility_pilot": OUT
        / "800_preflight_a_gene_compatibility_pilot.csv",
        "readiness": OUT / "800_preflight_a_readiness.json",
    }
    stratum.to_csv(paths["lineage_inventory"], index=False)
    case_rows.to_csv(paths["case_multiplicity"], index=False)
    pd.DataFrame(pilot_rows, columns=[
        "pilot_file_uuid", "frozen_gene_symbol", "frozen_tumor_gene_id",
        "exact_id_match", "version_insensitive_match_diagnostic",
        "not_a_final_mapping_rule",
    ]).to_csv(paths["gene_compatibility_pilot"], index=False)

    result = {
        "scope": "PHASE8_800_PREFLIGHT_A_ONLY_NO_PROGRAM_SCORING",
        "cohort_frozen": False,
        "replication_results_inspected": False,
        "inputs": inputs,
        "observed_local_counts": {
            "source_files": len(index),
            "provisional_primary_files": len(primary),
            "provisional_primary_cases_rnaseq": int(rna["case_uuid"].nunique()),
            "provisional_primary_cases_methylation": int(
                meth["case_uuid"].nunique()
            ),
            "case_rows_requiring_selection_review": int(
                case_rows["requires_selection_review"].sum()
            ),
            "primary_exact_cross_modality_overlap": exact_overlap,
            "lexical_overlap_with_tcga": exact_tcga_overlap,
        },
        "feature_mapping_pilot": pilot,
        "readiness": {
            "source_and_111_derivative_identity": "PASS",
            "frozen_phase4_input_identity": "PASS",
            "provisional_primary_inventory": "PASS_NOT_FROZEN",
            "one_per_case_selection_rule": "BLOCKED_PENDING_POLICY",
            "external_donor_independence": independence_state,
            "full_external_feature_compatibility": "NOT_ASSESSED",
            "transcriptomic_replication_contract": "NOT_FROZEN",
            "biological_replication_authorized": False,
        },
        "outputs": {
            k: {"path": record_path(p), "sha256": sha256(p)}
            for k, p in paths.items() if k != "readiness"
        },
    }
    with paths["readiness"].open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(json.dumps({
        "counts": result["observed_local_counts"],
        "feature_mapping_pilot": pilot,
        "readiness": result["readiness"],
        "readiness_file": record_path(paths["readiness"]),
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
