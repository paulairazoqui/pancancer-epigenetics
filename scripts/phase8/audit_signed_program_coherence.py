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
        "relative_pattern_with_low_signed_coherence": edges_from_loadings(
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
    genes = pd.read_csv(artifacts["shared_genes"]["path"])["gene_symbol"].tolist()
    gene_metadata = pd.read_csv(artifacts["gene_metadata"]["path"])
    samples = pd.read_csv(artifacts["sample_metadata"]["path"]).sort_values(
        "final_sample_column_index"
    )
    weights_frame = pd.read_csv(artifacts["weights"]["path"])
    if (
        len(genes) != 2389
        or len(set(genes)) != 2389
        or tuple(weights_frame["consensus_program_id"].drop_duplicates()) != PROGRAMS
    ):
        raise ValueError("Unexpected frozen gene or program identity.")
    gene_index = pd.Series(
        gene_metadata.index.to_numpy(), index=gene_metadata["gene_name"]
    )
    row_indices = gene_index.loc[genes].to_numpy()
    read_order, restore_order = np.argsort(row_indices), np.argsort(
        np.argsort(row_indices)
    )
    matrix = np.vstack(
        [
            weights_frame.loc[
                weights_frame.consensus_program_id.eq(program), "consensus_weight"
            ].to_numpy()
            for program in PROGRAMS
        ]
    )
    if matrix.shape != (3, 2389) or not np.isfinite(matrix).all():
        raise ValueError("Malformed frozen weights.")
    triangle = np.triu_indices(2389, k=1)
    pair_weights = np.abs(matrix[:, triangle[0]] * matrix[:, triangle[1]])
    pair_signs = np.sign(matrix[:, triangle[0]] * matrix[:, triangle[1]])
    if np.any(pair_weights.sum(axis=1) <= 0) or np.any(pair_signs == 0):
        raise ValueError("Signed pair weights are degenerate.")
    with h5py.File(artifacts["expression"]["path"], "r") as handle:
        expression = np.asarray(
            handle["logcpm"][row_indices[read_order], :][restore_order, :].T,
            dtype=np.float64,
        )
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
            normalized = pair_weights[p] / pair_weights[p].sum()
            full_rows.append(
                {
                    "lineage": lineage,
                    "consensus_program_id": program,
                    "signed_weighted_mean": mean,
                    "signed_weighted_median": median,
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
    metadata = {
        "purpose": "TCGA-only descriptive signed-coherence audit; not external replication or hypothesis testing.",
        "no_cptac3_expression_accessed": True,
        "seed": args.seed,
        "splits": args.splits,
        "pair_count": int(len(triangle[0])),
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
