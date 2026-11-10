"""TCGA-only feasibility audit for Phase 8 matched negative controls.

This is deliberately an exploratory methodological audit, not a CPTAC-3
replication analysis.  CPTAC-3 annotations are used only to retain genes with
technical identifier availability; no CPTAC-3 expression or outcome is read.

The script tests the two calipers already displayed in Notebook 800 (0.10 and
0.14), derives unconditional balance bounds, and reproduces the one existing
uncalipered minimum-distance pilot in TCGA-STAD.  It does not search across
calipers, objective weights, or optimisation algorithms.
"""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import linear_sum_assignment
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
from scipy.spatial import cKDTree
from scipy.spatial.distance import cdist


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "audits" / "phase8" / "tables"
CALIPERS = (0.10, 0.14)
PILOT_LINEAGE = "TCGA-STAD"
PROGRAM_IDS = ("CONSENSUS_TX_01", "CONSENSUS_TX_02", "CONSENSUS_TX_03")
FEATURES = ("mean_logcpm", "sd_logcpm", "prevalence_logcpm_gt0")


def smd_bounds(target: np.ndarray, alternative: np.ndarray, weights: np.ndarray) -> tuple[float, float]:
    """Bounds on a weighted alternative mean with distinct selected genes.

    Rearrangement gives the extrema after allowing any target--alternative
    pairing.  Therefore these are *optimistic* bounds: failing them proves
    impossibility for that single SMD, while passing does not prove feasibility
    once pairwise matching and the other features are imposed.
    """
    order_w = np.sort(weights)
    denominator = weights.sum()
    alt_sorted = np.sort(alternative)
    return (
        # The rearrangement inequality pairs the largest weights with the
        # smallest selected values to attain the lower weighted mean.
        float(np.dot(order_w[::-1], alt_sorted[: len(weights)]) / denominator),
        float(np.dot(order_w, alt_sorted[-len(weights) :]) / denominator),
    )


def calculate_features(values: np.ndarray, gene_ids: np.ndarray) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "gene_id": gene_ids,
            "mean_logcpm": values.mean(axis=1),
            "sd_logcpm": values.std(axis=1, ddof=1),
            "prevalence_logcpm_gt0": (values > 0).mean(axis=1),
        }
    )


def write_csv(frame: pd.DataFrame, name: str, suffix: str = "") -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    stem, extension = name.rsplit(".", 1)
    frame.to_csv(OUT / f"{stem}{suffix}.{extension}", index=False)


def consolidate_lineage_outputs() -> None:
    """Replace per-lineage transient outputs with four review-sized tables."""
    suffixes = ("hnsc", "luad", "lusc", "paad", "skcm", "stad", "ucec")
    sources = {
        "negative_control_strict_caliper_feasibility.csv": "negative_control_strict_caliper_feasibility",
        "negative_control_caliper_010_availability.csv": "negative_control_caliper_010_availability",
        "negative_control_unconditional_balance_bounds.csv": "negative_control_unconditional_balance_bounds",
        "negative_control_uncalipered_assignment.csv": "negative_control_stad_uncalipered_pilot",
    }
    for destination, stem in sources.items():
        source_paths = [OUT / f"{stem}_{suffix}.csv" for suffix in suffixes]
        frames = [pd.read_csv(path) for path in source_paths]
        frame = pd.concat(frames, ignore_index=True).sort_values("tcga_lineage")
        frame.to_csv(OUT / destination, index=False)
        for path in source_paths:
            path.unlink()

    provenance = json.loads((OUT / "negative_control_feasibility_provenance_stad.json").read_text(encoding="utf-8"))
    provenance["lineages"] = [f"TCGA-{suffix.upper()}" for suffix in suffixes]
    provenance["output_layout"] = "consolidated_lineage_tables"
    (OUT / "negative_control_feasibility_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    for suffix in suffixes:
        (OUT / f"negative_control_feasibility_provenance_{suffix}.json").unlink()


def main(
    run_pilot: bool,
    extend_uncalipered: bool,
    selected_lineage: str | None,
    bounds_only: bool,
) -> None:
    gene_meta = pd.read_csv(ROOT / "data/interim/expression/tcga_primary_tumor_rnaseq_program_discovery_filtered_gene_metadata.csv")
    sample_meta = pd.read_csv(ROOT / "data/interim/expression/tcga_primary_tumor_rnaseq_program_discovery_sample_metadata.csv")
    shared = pd.read_csv(ROOT / "data/processed/consensus_programs/400_cross_system_shared_gene_universe.csv")
    weights = pd.read_csv(ROOT / "data/processed/consensus_programs/401_consensus_transcriptomic_gene_weights.csv")
    cptac_genes = pd.read_csv(ROOT / "data/interim/expression/800_cptac3_protein_coding_gene_metadata.csv")

    gene_ids = gene_meta["gene_id"].str.replace(r"\.\d+$", "", regex=True).to_numpy()
    frozen_ids = shared["tumor_gene_id"].str.replace(r"\.\d+$", "", regex=True).to_numpy()
    frozen_set = set(frozen_ids)
    cptac_set = set(cptac_genes["ensembl_gene_id"].dropna())
    available = set(gene_ids) & cptac_set
    alternatives_set = available - frozen_set
    if len(frozen_set) != 2389 or len(alternatives_set) != 15734:
        raise ValueError("Unexpected frozen or alternative universe size")

    id_by_symbol = shared.set_index("gene_symbol")["tumor_gene_id"].str.replace(r"\.\d+$", "", regex=True)
    weight_by_id = weights.assign(gene_id=weights["gene_symbol"].map(id_by_symbol)).pivot(
        index="gene_id", columns="consensus_program_id", values="consensus_weight"
    ).reindex(columns=PROGRAM_IDS)
    if weight_by_id.isna().any().any() or set(weight_by_id.index) != frozen_set:
        raise ValueError("Frozen weights cannot be aligned to frozen TCGA IDs")

    # The lineages are externally specified in Notebook 800, not discovered
    # from any expression outcome.
    lineages = ("TCGA-HNSC", "TCGA-LUAD", "TCGA-LUSC", "TCGA-PAAD", "TCGA-SKCM", "TCGA-STAD", "TCGA-UCEC")
    if selected_lineage is not None:
        if selected_lineage not in lineages:
            raise ValueError(f"Unknown audit lineage: {selected_lineage}")
        lineages = (selected_lineage,)
    strict_rows: list[dict] = []
    availability_rows: list[dict] = []
    bound_rows: list[dict] = []
    pilot_rows: list[dict] = []
    h5_path = ROOT / "data/interim/expression/tcga_primary_tumor_rnaseq_program_discovery_tmm_logcpm.h5"

    with h5py.File(h5_path, "r") as h5:
        expression = h5["logcpm"]
        for lineage in lineages:
            cols = np.flatnonzero(sample_meta["project_id"].eq(lineage).to_numpy())
            values = expression[:, cols]
            frame = calculate_features(values, gene_ids)
            ranks = frame.loc[:, FEATURES].rank(method="average", pct=True).to_numpy()
            frozen_mask = frame["gene_id"].isin(frozen_set).to_numpy()
            alternative_mask = frame["gene_id"].isin(alternatives_set).to_numpy()
            target_ranks, alt_ranks = ranks[frozen_mask], ranks[alternative_mask]
            target_features = frame.loc[frozen_mask, FEATURES].to_numpy()
            alt_features = frame.loc[alternative_mask, FEATURES].to_numpy()
            target_ids = frame.loc[frozen_mask, "gene_id"].to_numpy()
            profile_weights = {"unweighted": np.ones(target_ids.size)}
            aligned_weights = weight_by_id.reindex(target_ids)
            for program in PROGRAM_IDS:
                profile_weights[program] = aligned_weights[program].abs().to_numpy()

            if not bounds_only:
                tree = cKDTree(alt_ranks)
                for caliper in CALIPERS:
                    lists = tree.query_ball_point(target_ranks, r=caliper, p=np.inf)
                    lengths = np.fromiter((len(x) for x in lists), dtype=np.int64, count=len(lists))
                    graph = csr_matrix((np.ones(lengths.sum(), dtype=np.int8), np.concatenate(lists), np.r_[0, np.cumsum(lengths)]), shape=(len(lists), alt_ranks.shape[0]))
                    assignment = maximum_bipartite_matching(graph, perm_type="column")
                    strict_rows.append({"tcga_lineage": lineage, "caliper": caliper, "matched_genes": int((assignment >= 0).sum()), "unmatched_genes": int((assignment < 0).sum()), "complete_matching": bool((assignment >= 0).all())})
                    if caliper == CALIPERS[0]:
                        availability_rows.append({"tcga_lineage": lineage, "targets_without_candidate": int((lengths == 0).sum()), "minimum_candidates": int(lengths.min()), "median_candidates": float(np.median(lengths)), "p90_candidates": float(np.percentile(lengths, 90))})

            reference_sd = frame.loc[:, FEATURES].std(ddof=1).to_numpy()
            for profile, profile_weight in profile_weights.items():
                for feature_ix, feature in enumerate(FEATURES):
                    target_mean = float(np.average(target_features[:, feature_ix], weights=profile_weight))
                    lower, upper = smd_bounds(target_features[:, feature_ix], alt_features[:, feature_ix], profile_weight)
                    # Minimum possible absolute SMD for any distinct alternative set.
                    lower_abs = max(0.0, target_mean - upper, lower - target_mean) / reference_sd[feature_ix]
                    bound_rows.append({"tcga_lineage": lineage, "weighting": profile, "feature": feature, "target_mean": target_mean, "alternative_mean_lower_bound": lower, "alternative_mean_upper_bound": upper, "absolute_smd_lower_bound": lower_abs, "smd_threshold": 0.10, "single_feature_balance_impossible": lower_abs > 0.10})

            if not bounds_only and run_pilot and (lineage == PILOT_LINEAGE or extend_uncalipered):
                cost = cdist(target_ranks, alt_ranks, metric="euclidean")
                target_ix, alt_ix = linear_sum_assignment(cost)
                gaps = np.abs(target_ranks[target_ix] - alt_ranks[alt_ix])
                matched_target = target_features[target_ix]
                matched_alt = alt_features[alt_ix]
                for profile, profile_weight in profile_weights.items():
                    weights_here = profile_weight[target_ix]
                    for feature_ix, feature in enumerate(FEATURES):
                        smd = (np.average(matched_target[:, feature_ix], weights=weights_here) - np.average(matched_alt[:, feature_ix], weights=weights_here)) / reference_sd[feature_ix]
                        pilot_rows.append({"tcga_lineage": lineage, "strategy": "uncalipered_minimum_euclidean_distance", "weighting": profile, "feature": feature, "smd": smd, "absolute_smd": abs(smd), "passes_smd_0_10": abs(smd) <= 0.10, "matched_genes": len(target_ix), "unique_alternatives": len(np.unique(alt_ix)), "pairs_max_gap_gt_0_10": int((gaps.max(axis=1) > 0.10).sum()), "pairs_max_gap_gt_0_14": int((gaps.max(axis=1) > 0.14).sum()), "maximum_rank_gap": float(gaps.max())})
                del cost

    suffix = f"_{selected_lineage.removeprefix('TCGA-').lower()}" if selected_lineage else ""
    if strict_rows:
        write_csv(pd.DataFrame(strict_rows), "negative_control_strict_caliper_feasibility.csv", suffix)
    if availability_rows:
        write_csv(pd.DataFrame(availability_rows), "negative_control_caliper_010_availability.csv", suffix)
    write_csv(pd.DataFrame(bound_rows), "negative_control_unconditional_balance_bounds.csv", suffix)
    if pilot_rows:
        write_csv(pd.DataFrame(pilot_rows), "negative_control_stad_uncalipered_pilot.csv", suffix)
    provenance = {"analysis": "exploratory_tcga_only_negative_control_feasibility", "calipers": CALIPERS, "pilot_lineage": PILOT_LINEAGE if run_pilot else None, "seed": None, "python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__, "scipy": scipy.__version__, "h5py": importlib.metadata.version("h5py"), "cptac3_expression_read": False, "tcga_cptac3_coexpression_calculated": False}
    (OUT / f"negative_control_feasibility_provenance{suffix}.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-uncalipered-stad-pilot", action="store_true")
    parser.add_argument("--extend-uncalipered-all", action="store_true", help="Run the unchanged full assignment after the STAD pilot.")
    parser.add_argument("--bounds-only", action="store_true", help="Regenerate only analytical balance bounds; skip matching and assignment.")
    parser.add_argument("--consolidate-lineage-outputs", action="store_true", help="Create consolidated review tables from existing lineage outputs.")
    parser.add_argument("--lineage", choices=("TCGA-HNSC", "TCGA-LUAD", "TCGA-LUSC", "TCGA-PAAD", "TCGA-SKCM", "TCGA-STAD", "TCGA-UCEC"))
    args = parser.parse_args()
    if args.consolidate_lineage_outputs:
        consolidate_lineage_outputs()
        raise SystemExit(0)
    main(
        run_pilot=not args.skip_uncalipered_stad_pilot,
        extend_uncalipered=args.extend_uncalipered_all,
        selected_lineage=args.lineage,
        bounds_only=args.bounds_only,
    )
