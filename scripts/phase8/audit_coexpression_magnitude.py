"""Phase 8 audit of sample-size bias in weighted coexpression magnitude.

The utility is intentionally restricted to simulations and frozen TCGA data.
It never accepts, discovers, or opens CPTAC-3 expression data.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from pathlib import Path

import h5py
import numpy as np
import pandas as pd
from scipy.special import gamma

PROGRAMS = ("CONSENSUS_TX_01", "CONSENSUS_TX_02", "CONSENSUS_TX_03")
N_REPLICATES = 800
N_SUBSAMPLES = 32
N_TCGA_PARTITIONS = 16
SEED = 20261111
ARTIFACTS = {
    "expression": "phase2.205.rna_program_discovery_expression",
    "gene_metadata": "phase2.205.rna_program_discovery_gene_metadata",
    "sample_metadata": "phase2.205.rna_program_discovery_sample_metadata",
    "shared_genes": "phase4.400.cross_system_shared_gene_universe",
    "weights": "phase4.401.consensus_transcriptomic_gene_weights",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_artifacts(data_root: Path) -> tuple[dict[str, Path], dict[str, str]]:
    registry = json.loads((data_root / "config/artifact_registry.json").read_text())[
        "artifacts"
    ]
    paths: dict[str, Path] = {}
    hashes: dict[str, str] = {}
    for label, artifact_id in ARTIFACTS.items():
        artifact = registry[artifact_id]
        path = data_root / artifact["path"]
        observed = sha256(path)
        if observed != artifact["sha256"]:
            raise ValueError(f"SHA-256 mismatch for {artifact_id}.")
        paths[label] = path
        hashes[artifact_id] = observed
    return paths, hashes


def upper_triangle_mean_abs(
    values: np.ndarray, triangle: tuple[np.ndarray, np.ndarray], weights: np.ndarray
) -> float:
    centered = values - values.mean(axis=0, keepdims=True)
    norm = np.sqrt(np.einsum("ij,ij->j", centered, centered))
    if np.any(norm <= np.finfo(float).eps):
        raise ValueError("A gene has zero within-group variance.")
    edges = ((centered / norm).T @ (centered / norm))[triangle]
    return float(np.dot(weights, np.abs(edges)) / weights.sum())


def correlation_matrix(loadings: np.ndarray, global_loading: float = 0.0) -> np.ndarray:
    """Positive-definite unit-variance one-plus-two-factor covariance."""
    residual = 1.0 - loadings**2 - global_loading**2
    if np.any(residual <= 0):
        raise ValueError("Invalid factor loading choice.")
    return np.outer(loadings, loadings) + global_loading**2 + np.diag(residual)


def population_magnitude(
    covariance: np.ndarray, triangle: tuple[np.ndarray, np.ndarray]
) -> float:
    return float(np.abs(covariance[triangle]).mean())


def scenarios() -> dict[str, tuple[np.ndarray, np.ndarray]]:
    signs = np.r_[np.ones(30), -np.ones(30)]
    reference = correlation_matrix(0.45 * signs)
    heterogeneous = np.r_[np.repeat(0.30, 30), np.repeat(0.60, 30)] * signs
    return {
        "equal": (reference, reference),
        "uniform_attenuation": (reference, correlation_matrix(0.30 * signs)),
        "uniform_increase": (reference, correlation_matrix(0.55 * signs)),
        "heterogeneous_compensation": (reference, correlation_matrix(heterogeneous)),
        "sign_reversal_same_magnitude": (
            reference,
            correlation_matrix(0.45 * np.ones(60)),
        ),
        "shared_latent_factor_change": (
            correlation_matrix(0.42 * signs, global_loading=0.10),
            correlation_matrix(0.42 * signs, global_loading=0.28),
        ),
    }


def draw_magnitude(
    rng: np.random.Generator,
    covariance: np.ndarray,
    n: int,
    triangle: tuple[np.ndarray, np.ndarray],
    weights: np.ndarray,
) -> tuple[np.ndarray, float]:
    values = rng.multivariate_normal(np.zeros(covariance.shape[0]), covariance, size=n)
    return values, upper_triangle_mean_abs(values, triangle, weights)


def simulate_condition(
    name: str,
    reference: np.ndarray,
    comparison: np.ndarray,
    n_reference: int,
    n_comparison: int,
    rng: np.random.Generator,
) -> list[dict[str, float | int | str]]:
    p = reference.shape[0]
    triangle = np.triu_indices(p, k=1)
    weights = np.ones(len(triangle[0]), dtype=float)
    truth = population_magnitude(comparison, triangle) - population_magnitude(
        reference, triangle
    )
    n_common = min(n_reference, n_comparison)
    direct, matched, matched_spread = [], [], []
    for _ in range(N_REPLICATES):
        ref_values, ref_magnitude = draw_magnitude(
            rng, reference, n_reference, triangle, weights
        )
        cmp_values, cmp_magnitude = draw_magnitude(
            rng, comparison, n_comparison, triangle, weights
        )
        direct.append(cmp_magnitude - ref_magnitude)
        estimates = []
        for _ in range(N_SUBSAMPLES):
            ref_index = rng.choice(n_reference, n_common, replace=False)
            cmp_index = rng.choice(n_comparison, n_common, replace=False)
            estimates.append(
                upper_triangle_mean_abs(cmp_values[cmp_index], triangle, weights)
                - upper_triangle_mean_abs(ref_values[ref_index], triangle, weights)
            )
        matched.append(float(np.mean(estimates)))
        matched_spread.append(float(np.std(estimates, ddof=1)))
    rows = []
    for strategy, estimates in (
        ("direct_full_cohort", np.array(direct)),
        ("matched_n_diagnostic", np.array(matched)),
    ):
        bias = float(estimates.mean() - truth)
        rows.append(
            {
                "scenario": name,
                "n_reference": n_reference,
                "n_comparison": n_comparison,
                "n_common": n_common,
                "strategy": strategy,
                "population_delta_m": truth,
                "mean_estimate": float(estimates.mean()),
                "bias": bias,
                "sd": float(estimates.std(ddof=1)),
                "rmse": float(np.sqrt(np.mean((estimates - truth) ** 2))),
                "sign_correct_rate": (
                    float(np.mean(np.sign(estimates) == np.sign(truth)))
                    if truth != 0
                    else np.nan
                ),
                "mean_within_replicate_subsample_sd": (
                    float(np.mean(matched_spread))
                    if strategy == "matched_n_diagnostic"
                    else np.nan
                ),
                "replicates": N_REPLICATES,
            }
        )
    return rows


def align_tcga(
    paths: dict[str, Path],
) -> tuple[np.ndarray, pd.DataFrame, dict[str, np.ndarray]]:
    shared = pd.read_csv(paths["shared_genes"])
    gene_metadata = pd.read_csv(paths["gene_metadata"])
    samples = pd.read_csv(paths["sample_metadata"]).sort_values(
        "final_sample_column_index"
    )
    weights_frame = pd.read_csv(paths["weights"])
    genes = shared["gene_symbol"].tolist()
    if len(genes) != 2389 or len(set(genes)) != 2389:
        raise ValueError("Shared universe must be exactly 2,389 unique genes.")
    selected_gene_metadata = gene_metadata.loc[
        gene_metadata["gene_name"].isin(genes), "gene_name"
    ]
    gene_index = pd.Series(
        selected_gene_metadata.index.to_numpy(), index=selected_gene_metadata
    )
    if gene_index.index.duplicated().any() or not set(genes).issubset(gene_index.index):
        raise ValueError("Frozen gene-to-expression mapping is not one-to-one.")
    row_index = gene_index.loc[genes].to_numpy()
    program_weights: dict[str, np.ndarray] = {}
    for program in PROGRAMS:
        program_frame = weights_frame.loc[
            weights_frame["consensus_program_id"] == program
        ]
        aligned = (
            program_frame.set_index("gene_symbol")
            .loc[genes, "consensus_weight"]
            .to_numpy(float)
        )
        if len(aligned) != 2389 or not np.isfinite(aligned).all():
            raise ValueError(f"Invalid frozen weights for {program}.")
        program_weights[program] = np.abs(aligned[None, :] * aligned[:, None])[
            np.triu_indices(2389, k=1)
        ]
    # h5py requires fancy row indices in ascending order; restore frozen gene order.
    sorted_order = np.argsort(row_index)
    inverse_order = np.argsort(sorted_order)
    with h5py.File(paths["expression"], "r") as handle:
        expression = handle["logcpm"][row_index[sorted_order], :][inverse_order, :]
    return expression, samples.reset_index(drop=True), program_weights


def tcga_size_diagnostic(
    expression: np.ndarray,
    samples: pd.DataFrame,
    program_weights: dict[str, np.ndarray],
    rng: np.random.Generator,
) -> list[dict[str, float | int | str]]:
    hns_index = np.flatnonzero(samples["project_id"].to_numpy() == "TCGA-HNSC")
    if len(hns_index) != 520:
        raise ValueError(f"Expected frozen HNSC n=520, observed {len(hns_index)}.")
    triangle = np.triu_indices(2389, k=1)
    rows = []
    for partition in range(N_TCGA_PARTITIONS):
        permuted = rng.permutation(hns_index)
        small_a, small_b, remainder = permuted[:36], permuted[36:72], permuted[72:]
        for program, weights in program_weights.items():
            a = upper_triangle_mean_abs(expression[:, small_a].T, triangle, weights)
            b = upper_triangle_mean_abs(expression[:, small_b].T, triangle, weights)
            full = upper_triangle_mean_abs(
                expression[:, remainder].T, triangle, weights
            )
            rows.extend(
                [
                    {
                        "program": program,
                        "partition": partition,
                        "comparison": "n36_vs_n484_same_origin",
                        "delta_comparison_minus_reference": a - full,
                    },
                    {
                        "program": program,
                        "partition": partition,
                        "comparison": "n36_vs_n36_same_origin",
                        "delta_comparison_minus_reference": a - b,
                    },
                ]
            )
    return rows


def weight_concentration(
    program_weights: dict[str, np.ndarray],
) -> list[dict[str, float | str]]:
    rows = []
    for program, weights in program_weights.items():
        normalized = weights / weights.sum()
        rows.append(
            {
                "program": program,
                "effective_weighted_pairs": float(1.0 / np.sum(normalized**2)),
                "top_1pct_pair_weight_share": float(
                    np.sort(normalized)[-int(np.ceil(0.01 * len(normalized))) :].sum()
                ),
                "top_10pct_pair_weight_share": float(
                    np.sort(normalized)[-int(np.ceil(0.10 * len(normalized))) :].sum()
                ),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    scenario_map = scenarios()
    rows: list[dict[str, float | int | str]] = []
    for name, (reference, comparison) in scenario_map.items():
        rows.extend(simulate_condition(name, reference, comparison, 103, 138, rng))
    reference, comparison = scenario_map["equal"]
    for n_reference, n_comparison in ((520, 36), (543, 56)):
        rows.extend(
            simulate_condition(
                "equal", reference, comparison, n_reference, n_comparison, rng
            )
        )
    pd.DataFrame(rows).to_csv(args.output_dir / "simulation_summary.csv", index=False)
    paths, hashes = load_artifacts(args.data_root)
    expression, samples, program_weights = align_tcga(paths)
    diagnostic = pd.DataFrame(
        tcga_size_diagnostic(expression, samples, program_weights, rng)
    )
    diagnostic.to_csv(args.output_dir / "tcga_hnsc_size_sensitivity.csv", index=False)
    pd.DataFrame(weight_concentration(program_weights)).to_csv(
        args.output_dir / "weight_concentration.csv", index=False
    )
    n_values = np.array([36, 56, 103, 138])
    null_abs_bias = gamma((n_values - 1) / 2) / (np.sqrt(np.pi) * gamma(n_values / 2))
    metadata = {
        "seed": args.seed,
        "n_simulation_replicates": N_REPLICATES,
        "n_matched_subsamples": N_SUBSAMPLES,
        "n_tcga_hnsc_partitions": N_TCGA_PARTITIONS,
        "simulation_genes": 60,
        "zero_correlation_exact_E_abs_r": dict(
            zip(n_values.astype(str), null_abs_bias.tolist(), strict=True)
        ),
        "artifacts_sha256": hashes,
        "python": sys.version,
        "platform": platform.platform(),
        "external_expression_opened": False,
    }
    (args.output_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
