"""TCGA-only audit of signed program coherence for Phase 8.

This exploratory utility reads only hash-verified frozen TCGA/Phase 4 artifacts.
Contractual CPTAC-3 *counts* are used solely for outcome-blind split sizes; no
CPTAC-3 expression path is accepted or opened.
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

PROGRAMS = ("CONSENSUS_TX_01", "CONSENSUS_TX_02", "CONSENSUS_TX_03")
LINEAGES = {
    "TCGA-LUAD": 178,
    "TCGA-LUSC": 89,
    "TCGA-STAD": 142,
    "TCGA-SKCM": 138,
    "TCGA-PAAD": 88,
    "TCGA-UCEC": 56,
    "TCGA-HNSC": 36,
}
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


def resolve_artifacts(registry_path: Path, data_root: Path) -> dict[str, dict]:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))["artifacts"]
    resolved: dict[str, dict] = {}
    for label, artifact_id in ARTIFACTS.items():
        artifact = registry[artifact_id]
        path = data_root / artifact["path"]
        observed = sha256(path)
        if observed != artifact["sha256"]:
            raise ValueError(f"SHA-256 mismatch for {artifact_id}.")
        resolved[label] = {
            "artifact_id": artifact_id,
            "path": str(path),
            "sha256": observed,
        }
    return resolved


def edge_correlations(
    values: np.ndarray, triangle: tuple[np.ndarray, np.ndarray]
) -> np.ndarray:
    if values.shape[0] < 3:
        raise ValueError("At least three tumors are required.")
    centered = values - values.mean(axis=0, keepdims=True)
    norm = np.sqrt(np.einsum("ij,ij->j", centered, centered))
    if np.any(norm <= np.finfo(np.float64).eps):
        raise ValueError("A frozen gene has zero within-lineage variance.")
    return ((centered / norm).T @ (centered / norm))[triangle]


def weighted_median(values: np.ndarray, weights: np.ndarray) -> float:
    """Exact weighted median without sorting every one of 2.85M edges.

    Successive count-medians discard roughly half the candidates; accumulating
    their weights preserves the weighted-quantile definition while avoiding a
    full O(m log m) sort for every split.
    """
    remaining_values = values
    remaining_weights = weights
    target = weights.sum(dtype=np.float64) / 2.0
    while True:
        pivot = np.partition(remaining_values, len(remaining_values) // 2)[
            len(remaining_values) // 2
        ]
        lower = remaining_values < pivot
        lower_weight = remaining_weights[lower].sum(dtype=np.float64)
        equal = remaining_values == pivot
        equal_weight = remaining_weights[equal].sum(dtype=np.float64)
        if target <= lower_weight:
            remaining_values = remaining_values[lower]
            remaining_weights = remaining_weights[lower]
        elif target <= lower_weight + equal_weight:
            return float(pivot)
        else:
            upper = remaining_values > pivot
            target -= lower_weight + equal_weight
            remaining_values = remaining_values[upper]
            remaining_weights = remaining_weights[upper]


def weighted_pearson(x: np.ndarray, y: np.ndarray, weights: np.ndarray) -> float:
    total = weights.sum(dtype=np.float64)
    x_delta = x - np.dot(weights, x) / total
    y_delta = y - np.dot(weights, y) / total
    denominator = np.sqrt(
        np.dot(weights, x_delta * x_delta) * np.dot(weights, y_delta * y_delta)
    )
    return (
        float(np.dot(weights, x_delta * y_delta) / denominator)
        if denominator > np.finfo(float).eps
        else np.nan
    )


def coherence(
    edges: np.ndarray, weights: np.ndarray, signs: np.ndarray
) -> tuple[float, float]:
    oriented = edges * signs
    return float(np.dot(weights, oriented) / weights.sum()), weighted_median(
        oriented, weights
    )


def score_variance_identity(
    values: np.ndarray,
    weights: np.ndarray,
    pair_weights: np.ndarray,
    coherence_mean: float,
) -> tuple[float, float]:
    """Check Var(w'Z) = sum(w^2) + 2 sum_{i<j} w_i w_j r_ij."""
    standardized = (values - values.mean(axis=0, keepdims=True)) / values.std(
        axis=0, ddof=1, keepdims=True
    )
    observed = float(np.var(standardized @ weights, ddof=1))
    reconstructed = float(
        np.dot(weights, weights) + 2.0 * pair_weights.sum() * coherence_mean
    )
    return observed, reconstructed


def validate_and_align_inputs(
    shared_genes: pd.DataFrame,
    gene_metadata: pd.DataFrame,
    sample_metadata: pd.DataFrame,
    weights_frame: pd.DataFrame,
    expression_shape: tuple[int, int],
) -> tuple[list[str], np.ndarray, pd.DataFrame, np.ndarray]:
    """Fail closed unless frozen identifiers define one exact alignment."""
    required_gene_columns = {"gene_symbol"}
    required_weight_columns = {
        "consensus_program_id",
        "gene_symbol",
        "consensus_weight",
    }
    required_sample_columns = {
        "final_sample_column_index",
        "case_submitter_id",
        "sample_submitter_id",
        "project_id",
    }
    if not required_gene_columns.issubset(shared_genes.columns):
        raise ValueError("Shared-gene artifact lacks gene_symbol.")
    if not required_weight_columns.issubset(weights_frame.columns):
        raise ValueError("Weight artifact lacks required identity columns.")
    if not required_sample_columns.issubset(sample_metadata.columns):
        raise ValueError("Sample metadata lacks required identity columns.")
    genes = shared_genes["gene_symbol"].tolist()
    if len(genes) != 2389 or pd.isna(genes).any() or len(set(genes)) != len(genes):
        raise ValueError("Shared genes are not exactly 2,389 unique identifiers.")
    selected_gene_metadata = gene_metadata.loc[
        gene_metadata["gene_name"].isin(genes), "gene_name"
    ]
    if selected_gene_metadata.isna().any() or selected_gene_metadata.duplicated().any():
        raise ValueError(
            "Frozen shared genes have missing or duplicated TCGA expression mappings."
        )
    gene_index = pd.Series(
        selected_gene_metadata.index.to_numpy(), index=selected_gene_metadata
    )
    missing_expression_genes = set(genes).difference(gene_index.index)
    if missing_expression_genes or len(gene_index) != len(genes):
        raise ValueError(
            "A frozen shared gene is absent from TCGA expression metadata."
        )
    row_indices = gene_index.loc[genes].to_numpy()
    if len(np.unique(row_indices)) != len(genes):
        raise ValueError("Frozen genes do not map one-to-one to TCGA expression rows.")
    if expression_shape[0] != len(gene_metadata):
        raise ValueError("TCGA expression rows do not match gene metadata rows.")
    samples = sample_metadata.sort_values("final_sample_column_index").reset_index(
        drop=True
    )
    expected_columns = np.arange(expression_shape[1])
    if len(samples) != expression_shape[1] or not np.array_equal(
        samples["final_sample_column_index"].to_numpy(), expected_columns
    ):
        raise ValueError(
            "Sample metadata does not exactly index TCGA expression columns."
        )
    if (
        samples["case_submitter_id"].isna().any()
        or samples["sample_submitter_id"].isna().any()
    ):
        raise ValueError("TCGA sample metadata has missing sample identities.")
    if (
        samples["case_submitter_id"].duplicated().any()
        or samples["sample_submitter_id"].duplicated().any()
    ):
        raise ValueError(
            "TCGA sample metadata has duplicated case or sample identities."
        )
    if tuple(weights_frame["consensus_program_id"].drop_duplicates()) != PROGRAMS:
        raise ValueError("Unexpected frozen consensus-program identities or ordering.")
    aligned_weights = []
    frozen_gene_set = set(genes)
    for program in PROGRAMS:
        program_weights = weights_frame.loc[
            weights_frame["consensus_program_id"].eq(program)
        ].copy()
        program_genes = program_weights["gene_symbol"].tolist()
        if len(program_weights) != len(genes) or pd.isna(program_genes).any():
            raise ValueError(f"{program} does not contain exactly 2,389 gene weights.")
        if len(set(program_genes)) != len(program_genes):
            raise ValueError(f"{program} has duplicated gene identifiers.")
        if set(program_genes) != frozen_gene_set:
            raise ValueError(f"{program} has missing or additional frozen genes.")
        if program_genes != genes:
            raise ValueError(
                f"{program} gene order differs from the frozen shared universe."
            )
        explicit = program_weights.set_index("gene_symbol").loc[
            genes, "consensus_weight"
        ]
        if not np.array_equal(explicit.index.to_numpy(), np.asarray(genes)):
            raise ValueError(f"{program} failed explicit gene-symbol alignment.")
        aligned_weights.append(explicit.to_numpy())
    matrix = np.vstack(aligned_weights)
    if matrix.shape != (len(PROGRAMS), len(genes)) or not np.isfinite(matrix).all():
        raise ValueError("Frozen consensus weights are malformed.")
    return genes, row_indices, samples, matrix


def synthetic_scenarios(seed: int) -> pd.DataFrame:
    """Model demonstrations, computed from declared population correlations."""
    rng = np.random.default_rng(seed)
    n_genes = 80
    signs = np.r_[np.ones(n_genes // 2), -np.ones(n_genes // 2)]
    loading = rng.uniform(0.20, 0.55, n_genes)
    triangle = np.triu_indices(n_genes, k=1)
    pair_sign = signs[triangle[0]] * signs[triangle[1]]
    pair_weight = loading[triangle[0]] * loading[triangle[1]]
    reference = (np.outer(signs * loading, signs * loading))[triangle]

    def edges_from_loadings(vector: np.ndarray) -> np.ndarray:
        return np.outer(vector, vector)[triangle]

    rewired_signs = signs.copy()
    rewired_signs[rng.choice(n_genes, size=12, replace=False)] *= -1
    scenarios = {
        "near_preservation": edges_from_loadings(signs * (loading * 0.98)),
        "uniform_attenuation": edges_from_loadings(signs * (loading * 0.55)),
        "local_rewiring": edges_from_loadings(rewired_signs * loading),
        "opposite_sign_relation_inversion": edges_from_loadings(loading),
        "shared_global_latent_factor": edges_from_loadings(signs * loading + 0.28),
        "low_signed_coherence_mixed_factor": edges_from_loadings(
            signs * loading * 0.35 + 0.42
        ),
    }
    rows = []
    for name, comparison in scenarios.items():
        mean, median = coherence(comparison, pair_weight, pair_sign)
        rows.append(
            {
                "scenario": name,
                "weighted_relative_edge_concordance": weighted_pearson(
                    reference, comparison, pair_weight
                ),
                "signed_weighted_mean": mean,
                "signed_weighted_median": median,
            }
        )
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument(
        "--registry", type=Path, default=Path("config/artifact_registry.json")
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20261111)
    parser.add_argument("--splits", type=int, default=8)
    args = parser.parse_args()
    if args.splits < 2:
        raise ValueError("At least two predeclared splits are required.")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    artifacts = resolve_artifacts(args.registry, args.data_root)
    shared_genes = pd.read_csv(artifacts["shared_genes"]["path"])
    gene_metadata = pd.read_csv(artifacts["gene_metadata"]["path"])
    sample_metadata = pd.read_csv(artifacts["sample_metadata"]["path"])
    weights_frame = pd.read_csv(artifacts["weights"]["path"])
    with h5py.File(artifacts["expression"]["path"], "r") as handle:
        if "logcpm" not in handle:
            raise ValueError("TCGA expression artifact lacks the logcpm dataset.")
        expression_shape = handle["logcpm"].shape
    genes, row_indices, samples, matrix = validate_and_align_inputs(
        shared_genes,
        gene_metadata,
        sample_metadata,
        weights_frame,
        expression_shape,
    )
    read_order, restore_order = np.argsort(row_indices), np.argsort(
        np.argsort(row_indices)
    )
    triangle = np.triu_indices(len(genes), k=1)
    pair_weights = np.abs(matrix[:, triangle[0]] * matrix[:, triangle[1]])
    pair_signs = np.sign(matrix[:, triangle[0]] * matrix[:, triangle[1]])
    if np.any(pair_weights.sum(axis=1) <= 0) or np.any(pair_signs == 0):
        raise ValueError("Signed pair weights are degenerate.")
    with h5py.File(artifacts["expression"]["path"], "r") as handle:
        expression = np.asarray(
            handle["logcpm"][row_indices[read_order], :][restore_order, :].T,
            dtype=np.float64,
        )
    if expression.shape != (len(samples), len(genes)):
        raise ValueError("Aligned TCGA expression has an unexpected shape.")
    if not np.isfinite(expression).all():
        raise ValueError("Non-finite TCGA expression.")
    rng = np.random.default_rng(args.seed)
    full_rows, split_rows, support = [], [], []
    for lineage, external_n in LINEAGES.items():
        indices = samples.index[samples.project_id.eq(lineage)].to_numpy()
        lineage_values = expression[indices]
        edges = edge_correlations(lineage_values, triangle)
        split_n = min(len(indices) // 2, external_n)
        support.append(
            {
                "lineage": lineage,
                "tcga_n": len(indices),
                "contract_cptac3_source_n": external_n,
                "per_half_n": split_n,
                "external_sized_disjoint_split_feasible": 2 * external_n
                <= len(indices),
            }
        )
        for p, program in enumerate(PROGRAMS):
            mean, median = coherence(edges, pair_weights[p], pair_signs[p])
            score_variance, reconstructed_variance = score_variance_identity(
                lineage_values, matrix[p], pair_weights[p], mean
            )
            normalized = pair_weights[p] / pair_weights[p].sum()
            full_rows.append(
                {
                    "lineage": lineage,
                    "consensus_program_id": program,
                    "signed_weighted_mean": mean,
                    "signed_weighted_median": median,
                    "score_variance_standardized_within_lineage": score_variance,
                    "score_variance_from_signed_mean": reconstructed_variance,
                    "score_variance_identity_abs_error": abs(
                        score_variance - reconstructed_variance
                    ),
                    "effective_pair_count": float(1.0 / np.dot(normalized, normalized)),
                    "top_10pct_gene_weight_energy": float(
                        np.sort(np.abs(matrix[p]))[-239:].dot(
                            np.sort(np.abs(matrix[p]))[-239:]
                        )
                        / np.dot(matrix[p], matrix[p])
                    ),
                }
            )
        for split in range(args.splits):
            chosen = rng.permutation(len(indices))[: 2 * split_n]
            for half, selected in enumerate((chosen[:split_n], chosen[split_n:])):
                half_edges = edge_correlations(lineage_values[selected], triangle)
                for p, program in enumerate(PROGRAMS):
                    mean, median = coherence(half_edges, pair_weights[p], pair_signs[p])
                    split_rows.append(
                        {
                            "lineage": lineage,
                            "consensus_program_id": program,
                            "split": split,
                            "half": half + 1,
                            "per_half_n": split_n,
                            "signed_weighted_mean": mean,
                            "signed_weighted_median": median,
                        }
                    )
    full = pd.DataFrame(full_rows)
    splits = pd.DataFrame(split_rows)
    summary = splits.groupby(["lineage", "consensus_program_id"], as_index=False).agg(
        mean_median=("signed_weighted_mean", "median"),
        mean_min=("signed_weighted_mean", "min"),
        mean_max=("signed_weighted_mean", "max"),
        median_median=("signed_weighted_median", "median"),
        median_min=("signed_weighted_median", "min"),
        median_max=("signed_weighted_median", "max"),
    )
    full.to_csv(args.output_dir / "tcga_signed_coherence_full.csv", index=False)
    summary.to_csv(
        args.output_dir / "tcga_signed_coherence_split_summary.csv", index=False
    )
    pd.DataFrame(support).to_csv(
        args.output_dir / "tcga_signed_coherence_lineage_support.csv", index=False
    )
    synthetic_scenarios(args.seed + 1).to_csv(
        args.output_dir / "signed_coherence_synthetic_scenarios.csv", index=False
    )
    identity_max_abs_error = float(full["score_variance_identity_abs_error"].max())
    metadata = {
        "purpose": "TCGA-only descriptive signed-coherence audit; not external replication or hypothesis testing.",
        "no_cptac3_expression_accessed": True,
        "seed": args.seed,
        "splits": args.splits,
        "pair_count": int(len(triangle[0])),
        "alignment_checks": {
            "shared_gene_count": len(genes),
            "exact_gene_order_verified_for_each_program": True,
            "tcga_expression_column_alignment_verified": True,
        },
        "score_variance_identity": {
            "standardization": "within-lineage gene mean 0 and sample SD 1 (ddof=1)",
            "n_program_lineage_checks": int(len(full)),
            "max_absolute_error": identity_max_abs_error,
        },
        "artifacts": artifacts,
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "h5py": h5py.__version__,
    }
    (args.output_dir / "signed_coherence_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
