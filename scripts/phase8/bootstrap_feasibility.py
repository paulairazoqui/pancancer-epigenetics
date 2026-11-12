"""Bounded Phase 8 feasibility check for tumour-level bootstrap inference.

This temporary utility is deliberately limited to frozen TCGA expression,
contractual CPTAC-3 sample sizes, and synthetic data.  It must never open a
CPTAC-3 expression matrix or report an external-concordance result.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time
from pathlib import Path

import h5py
import numpy as np
import pandas as pd

PROGRAMS = ("CONSENSUS_TX_01", "CONSENSUS_TX_02", "CONSENSUS_TX_03")
CONTRACT = {
    "HNSC": (520, 36), "LUAD": (512, 178), "LUSC": (500, 89),
    "PAAD": (178, 88), "SKCM": (103, 138), "STAD": (412, 142),
    "UCEC": (543, 56),
}
ARTIFACTS = {
    "expression": "phase2.205.rna_program_discovery_expression",
    "gene_metadata": "phase2.205.rna_program_discovery_gene_metadata",
    "sample_metadata": "phase2.205.rna_program_discovery_sample_metadata",
    "shared_genes": "phase4.400.cross_system_shared_gene_universe",
    "weights": "phase4.401.consensus_transcriptomic_gene_weights",
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def registered_paths(root: Path) -> tuple[dict[str, Path], dict[str, str]]:
    registry = json.loads((root / "config/artifact_registry.json").read_text())["artifacts"]
    paths, hashes = {}, {}
    for label, artifact_id in ARTIFACTS.items():
        path = root / registry[artifact_id]["path"]
        observed = digest(path)
        if observed != registry[artifact_id]["sha256"]:
            raise ValueError(f"SHA-256 mismatch: {artifact_id}")
        paths[label], hashes[artifact_id] = path, observed
    return paths, hashes


def load_frozen_tcga(paths: dict[str, Path]) -> tuple[np.ndarray, pd.DataFrame, dict[str, tuple[np.ndarray, np.ndarray]]]:
    shared = pd.read_csv(paths["shared_genes"])
    genes = shared["gene_symbol"].tolist()
    if len(genes) != 2389 or len(set(genes)) != 2389:
        raise ValueError("Frozen shared universe is not exactly 2,389 unique ordered genes.")
    metadata = pd.read_csv(paths["gene_metadata"])
    selected = metadata.loc[metadata["gene_name"].isin(genes), ["gene_name"]]
    # The HDF5 expression rows use the metadata frame's zero-based row order;
    # `matrix_row_index` is a provenance field, not this HDF5 coordinate.
    lookup = pd.Series(selected.index.to_numpy(), index=selected["gene_name"])
    if lookup.index.duplicated().any() or not set(genes).issubset(lookup.index):
        raise ValueError("Frozen gene identity cannot be mapped one-to-one to TCGA rows.")
    rows = lookup.loc[genes].to_numpy(int)
    samples = pd.read_csv(paths["sample_metadata"]).sort_values("final_sample_column_index").reset_index(drop=True)
    if not np.array_equal(samples["final_sample_column_index"].to_numpy(), np.arange(len(samples))):
        raise ValueError("Sample metadata do not match consecutive expression columns.")
    if samples["sample_submitter_id"].duplicated().any() or samples["case_submitter_id"].duplicated().any():
        raise ValueError("Frozen TCGA analysis samples are not one independent sample per case.")
    order = np.argsort(rows)
    restore = np.argsort(order)
    with h5py.File(paths["expression"], "r") as handle:
        if handle["logcpm"].shape[1] != len(samples):
            raise ValueError("Expression-column count differs from sample metadata.")
        expression = handle["logcpm"][rows[order], :][restore, :]
    if not np.isfinite(expression).all():
        raise ValueError("Frozen TCGA expression contains non-finite values in the shared universe.")
    frame = pd.read_csv(paths["weights"])
    triangle = np.triu_indices(len(genes), k=1)
    weights = {}
    for program in PROGRAMS:
        vector = frame.loc[frame["consensus_program_id"].eq(program)].set_index("gene_symbol").loc[genes, "consensus_weight"].to_numpy(float)
        if len(vector) != 2389 or not np.isfinite(vector).all():
            raise ValueError(f"Invalid aligned weights: {program}")
        edge_weight = np.abs(vector[triangle[0]] * vector[triangle[1]])
        if not np.isfinite(edge_weight).all() or edge_weight.sum() <= 0:
            raise ValueError(f"Degenerate edge weights: {program}")
        weights[program] = (edge_weight, np.sign(vector[triangle[0]] * vector[triangle[1]]))
    return expression, samples, weights


def correlations(sample_by_gene: np.ndarray) -> np.ndarray:
    centered = sample_by_gene - sample_by_gene.mean(axis=0, keepdims=True)
    norm = np.sqrt(np.einsum("ij,ij->j", centered, centered))
    if np.any(~np.isfinite(norm)):
        raise ValueError("nonfinite_gene_variance")
    if np.any(norm <= np.finfo(float).eps):
        raise ValueError("zero_gene_variance")
    corr = (centered / norm).T @ (centered / norm)
    if not np.isfinite(corr).all():
        raise ValueError("nonfinite_correlation")
    return corr


def weighted_median(values: np.ndarray, weights: np.ndarray) -> float:
    order = np.argsort(values)
    cumulative = np.cumsum(weights[order])
    return float(values[order][np.searchsorted(cumulative, weights.sum() / 2, side="left")])


def statistics(tcga_corr: np.ndarray, cptac_corr: np.ndarray, weights: np.ndarray, signs: np.ndarray, triangle: tuple[np.ndarray, np.ndarray]) -> dict[str, float]:
    first, second = tcga_corr[triangle], cptac_corr[triangle]
    total = weights.sum()
    a, b = np.dot(weights, first) / total, np.dot(weights, second) / total
    da, db = first - a, second - b
    denom = np.sqrt(np.dot(weights, da * da) * np.dot(weights, db * db))
    if not np.isfinite(denom) or denom <= np.finfo(float).eps:
        raise ValueError("degenerate_weighted_pearson_denominator")
    return {
        "T": float(np.dot(weights, da * db) / denom),
        "Delta_M": float(np.dot(weights, np.abs(second) - np.abs(first)) / total),
        "signed_mean_tcga": float(np.dot(weights, signs * first) / total),
        "signed_median_tcga": weighted_median(signs * first, weights),
        "signed_mean_cptac": float(np.dot(weights, signs * second) / total),
        "signed_median_cptac": weighted_median(signs * second, weights),
    }


def bootstrap_pair(tcga: np.ndarray, cptac: np.ndarray, weights: dict[str, tuple[np.ndarray, np.ndarray]], replicates: int, rng: np.random.Generator) -> tuple[list[dict[str, object]], dict[str, int]]:
    """One shared pair of resample indices per replicate, across all programs."""
    triangle = np.triu_indices(tcga.shape[1], k=1)
    rows, failures = [], {}
    for replicate in range(replicates):
        try:
            tcga_index = rng.integers(len(tcga), size=len(tcga))
            cptac_index = rng.integers(len(cptac), size=len(cptac))
            a = correlations(tcga[tcga_index])
            b = correlations(cptac[cptac_index])
            for program, (edge_weight, signs) in weights.items():
                for statistic, value in statistics(a, b, edge_weight, signs, triangle).items():
                    rows.append({"replicate": replicate, "program": program, "statistic": statistic, "value": value,
                                 "unique_tcga": len(np.unique(tcga_index)), "unique_cptac": len(np.unique(cptac_index))})
        except ValueError as error:
            failures[str(error)] = failures.get(str(error), 0) + 1
    return rows, failures


def synthetic_precision(rng: np.random.Generator, budgets: tuple[int, ...]) -> pd.DataFrame:
    """Known finite Gaussian setting; no parameter is learned from external data."""
    p, n_a, n_b = 80, 103, 36
    loadings = np.r_[np.repeat(0.45, p // 2), np.repeat(-0.45, p // 2)]
    covariance = np.outer(loadings, loadings) + np.diag(1 - loadings**2)
    weights = {program: (np.ones(p * (p - 1) // 2), np.ones(p * (p - 1) // 2)) for program in PROGRAMS}
    # A common data set and common ordered draws isolate finite-B variation from
    # ordinary sample-to-sample variation when comparing bootstrap budgets.
    tcga = rng.multivariate_normal(np.zeros(p), covariance, size=n_a)
    cptac = rng.multivariate_normal(np.zeros(p), covariance, size=n_b)
    draws, failures = bootstrap_pair(tcga, cptac, weights, max(budgets), rng)
    values = pd.DataFrame(draws).query("program == @PROGRAMS[0] and statistic == 'T'")["value"].to_numpy()
    records = []
    for budget in budgets:
        retained = values[:budget]
        probe = pd.DataFrame(draws).query("program == @PROGRAMS[0] and statistic == 'T'").iloc[:budget]
        records.append({"replicates": budget, "valid": len(retained), "failure_rate": sum(failures.values()) / max(budgets),
                        "T_p2_5": np.quantile(retained, .025), "T_p97_5": np.quantile(retained, .975),
                        "T_width": np.quantile(retained, .975) - np.quantile(retained, .025),
                        "min_unique_tcga": int(probe["unique_tcga"].min()), "min_unique_cptac": int(probe["unique_cptac"].min())})
    return pd.DataFrame(records)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20261112)
    parser.add_argument("--benchmark-replicates", type=int, default=3)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    paths, hashes = registered_paths(args.data_root)
    expression, samples, weights = load_frozen_tcga(paths)
    counts = samples.groupby("project_id")["case_submitter_id"].nunique()
    feasibility = []
    for lineage, (n_tcga, n_cptac) in CONTRACT.items():
        observed = int(counts.get(f"TCGA-{lineage}", 0))
        if observed != n_tcga:
            raise ValueError(f"Contract mismatch for {lineage}: {observed} TCGA cases, expected {n_tcga}.")
        feasibility.append({"lineage": lineage, "n_tcga": n_tcga, "n_cptac_contract": n_cptac,
                            "technical_feasibility": "candidate; requires preflight on both frozen matrices",
                            "smallest_cohort": min(n_tcga, n_cptac)})
    pd.DataFrame(feasibility).to_csv(args.output_dir / "lineage_feasibility.csv", index=False)
    # Bounded TCGA-only benchmark: one correlation matrix is shared by three programs.
    benchmark = []
    for n in (36, 56, 103):
        chosen = np.flatnonzero(samples["project_id"].eq("TCGA-HNSC"))
        start = time.perf_counter()
        for _ in range(args.benchmark_replicates):
            corr = correlations(expression[:, rng.choice(chosen, size=n, replace=True)].T)
        correlation_seconds = (time.perf_counter() - start) / args.benchmark_replicates
        triangle = np.triu_indices(corr.shape[0], 1)
        start = time.perf_counter()
        for edge_weight, signs in weights.values():
            _ = statistics(corr, corr, edge_weight, signs, triangle)
        statistic_seconds = time.perf_counter() - start
        benchmark.append({"n": n, "replicates": args.benchmark_replicates, "seconds_per_correlation": correlation_seconds,
                          "seconds_for_all_3_program_statistics_per_cohort": statistic_seconds,
                          "correlation_matrix_mib": corr.nbytes / 1024**2})
    pd.DataFrame(benchmark).to_csv(args.output_dir / "tcga_benchmark.csv", index=False)
    synthetic_precision(rng, (200, 500, 1000)).to_csv(args.output_dir / "synthetic_percentile_stability.csv", index=False)
    (args.output_dir / "metadata.json").write_text(json.dumps({"seed": args.seed, "artifact_sha256": hashes,
        "external_expression_opened": False, "python_platform": platform.platform(), "contract": CONTRACT}, indent=2))


if __name__ == "__main__":
    main()
