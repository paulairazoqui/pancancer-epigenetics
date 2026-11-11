"""TCGA-only reference-stability audit for the Phase 8 candidate statistic.

This is an audit utility, not a Phase 8 analysis.  It reads only the frozen
TCGA expression representation and immutable Phase 4 program files.  It never
opens CPTAC-3 expression files.  The fixed CPTAC-3 lineage counts below are
publicly specified source metadata from the active Notebook 800 contract; they
are used only to choose outcome-blind, precision-relevant TCGA split sizes.

For each lineage, independent random disjoint TCGA halves are correlated at
the edge-vector level.  The retained per-half size is min(floor(n_TCGA / 2),
n_CPTAC3_source), which makes the diagnostic conservative when the external
cohort is smaller and explicitly records when an external-sized split is
impossible.  These internal split statistics measure reference reliability;
they are neither external replication nor a null distribution.
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

PROGRAM_IDS = ("CONSENSUS_TX_01", "CONSENSUS_TX_02", "CONSENSUS_TX_03")
LINEAGE_CPTAC3_SOURCE_N = {
    "TCGA-LUAD": 178,
    "TCGA-LUSC": 89,
    "TCGA-STAD": 142,
    "TCGA-SKCM": 138,
    "TCGA-PAAD": 88,
    "TCGA-UCEC": 56,
    "TCGA-HNSC": 36,
}
ARTIFACT_IDS = {
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


def verify_artifacts(registry_path: Path, data_root: Path) -> dict[str, dict]:
    registry = json.loads(registry_path.read_text(encoding="utf-8"))["artifacts"]
    resolved: dict[str, dict] = {}
    for label, artifact_id in ARTIFACT_IDS.items():
        artifact = registry[artifact_id]
        path = data_root / artifact["path"]
        if not path.exists():
            raise FileNotFoundError(f"Missing {artifact_id}: {path}")
        observed = sha256(path)
        if observed != artifact["sha256"]:
            raise ValueError(
                f"SHA-256 mismatch for {artifact_id}: {observed} != "
                f"{artifact['sha256']}"
            )
        resolved[label] = {
            "artifact_id": artifact_id,
            "path": str(path),
            "sha256": observed,
        }
    return resolved


def weighted_pearson(x: np.ndarray, y: np.ndarray, weight: np.ndarray) -> float:
    """Weighted Pearson correlation with frequency-like non-negative weights."""
    weight_sum = weight.sum(dtype=np.float64)
    if not np.isfinite(weight_sum) or weight_sum <= 0:
        return np.nan
    x_mean = np.dot(weight, x) / weight_sum
    y_mean = np.dot(weight, y) / weight_sum
    dx = x - x_mean
    dy = y - y_mean
    denominator = np.sqrt(np.dot(weight, dx * dx) * np.dot(weight, dy * dy))
    if not np.isfinite(denominator) or denominator <= np.finfo(np.float64).eps:
        return np.nan
    return float(np.dot(weight, dx * dy) / denominator)


def correlation_edges(
    samples_by_genes: np.ndarray, triangle: tuple[np.ndarray, np.ndarray]
) -> np.ndarray:
    if samples_by_genes.shape[0] < 3:
        raise ValueError(
            "At least three tumors are required to estimate Pearson correlations."
        )
    centered = samples_by_genes - samples_by_genes.mean(axis=0, keepdims=True)
    norm = np.sqrt(np.einsum("ij,ij->j", centered, centered))
    if np.any(norm <= np.finfo(np.float64).eps):
        raise ValueError("At least one frozen gene has zero within-lineage variance.")
    standardized = centered / norm
    correlation = standardized.T @ standardized
    return correlation[triangle]


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
        raise ValueError("Use at least two splits for a stability distribution.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    artifacts = verify_artifacts(args.registry, args.data_root)
    expression_path = Path(artifacts["expression"]["path"])
    gene_metadata = pd.read_csv(artifacts["gene_metadata"]["path"])
    sample_metadata = pd.read_csv(artifacts["sample_metadata"]["path"])
    shared_genes = pd.read_csv(artifacts["shared_genes"]["path"])
    weights = pd.read_csv(artifacts["weights"]["path"])

    if tuple(weights["consensus_program_id"].drop_duplicates()) != PROGRAM_IDS:
        raise ValueError("Unexpected frozen consensus-program identities or ordering.")
    genes = shared_genes["gene_symbol"].tolist()
    if len(genes) != 2389 or len(set(genes)) != len(genes):
        raise ValueError(
            "The shared gene universe is not the expected 2,389 unique genes."
        )
    # ``matrix_row_index`` addresses the pre-filter count matrix.  The HDF5
    # discovery representation is ordered by rows in this filtered metadata.
    gene_index = pd.Series(
        gene_metadata.index.to_numpy(), index=gene_metadata["gene_name"]
    )
    if not set(genes).issubset(gene_index.index):
        raise ValueError(
            "A frozen shared gene is absent from the TCGA discovery representation."
        )
    row_indices = gene_index.loc[genes].to_numpy()
    if len(np.unique(row_indices)) != len(genes):
        raise ValueError(
            "Frozen gene symbols do not map one-to-one to TCGA matrix rows."
        )
    read_order = np.argsort(row_indices)
    sorted_row_indices = row_indices[read_order]
    restore_frozen_order = np.argsort(read_order)

    weight_matrix = np.vstack(
        [
            weights.loc[
                weights["consensus_program_id"].eq(program), "consensus_weight"
            ].to_numpy()
            for program in PROGRAM_IDS
        ]
    )
    if weight_matrix.shape != (3, len(genes)) or not np.isfinite(weight_matrix).all():
        raise ValueError("Frozen consensus weights are malformed.")
    triangle = np.triu_indices(len(genes), k=1)
    pair_weights = np.abs(weight_matrix[:, triangle[0]] * weight_matrix[:, triangle[1]])
    pair_weight_sum = pair_weights.sum(axis=1)
    if np.any(pair_weight_sum <= 0):
        raise ValueError("A program has zero total pair weight.")
    normalized_pair_weights = pair_weights / pair_weight_sum[:, None]
    effective_pair_count = 1.0 / np.einsum(
        "ij,ij->i", normalized_pair_weights, normalized_pair_weights
    )
    program_diagnostics: list[dict[str, object]] = []
    for first in range(len(PROGRAM_IDS)):
        for second in range(first + 1, len(PROGRAM_IDS)):
            program_diagnostics.append(
                {
                    "program_a": PROGRAM_IDS[first],
                    "program_b": PROGRAM_IDS[second],
                    "pearson_correlation_of_pair_weights": float(
                        np.corrcoef(pair_weights[first], pair_weights[second])[0, 1]
                    ),
                }
            )
    pd.DataFrame(program_diagnostics).to_csv(
        args.output_dir / "program_pair_weight_overlap.csv", index=False
    )

    sample_metadata = sample_metadata.sort_values("final_sample_column_index")
    expected_columns = np.arange(sample_metadata.shape[0])
    if not np.array_equal(
        sample_metadata["final_sample_column_index"].to_numpy(), expected_columns
    ):
        raise ValueError("TCGA sample column indices are not contiguous and ordered.")
    lineage_indices = {
        lineage: sample_metadata.index[
            sample_metadata["project_id"].eq(lineage)
        ].to_numpy()
        for lineage in LINEAGE_CPTAC3_SOURCE_N
    }
    with h5py.File(expression_path, "r") as handle:
        dataset = handle["logcpm"]
        if dataset.shape != (gene_metadata.shape[0], sample_metadata.shape[0]):
            raise ValueError("TCGA HDF5 dimensions do not match its frozen metadata.")
        expression = dataset[sorted_row_indices, :]
    expression = np.asarray(expression[restore_frozen_order, :].T, dtype=np.float64)
    if not np.isfinite(expression).all():
        raise ValueError(
            "The selected TCGA expression matrix contains non-finite values."
        )

    rng = np.random.default_rng(args.seed)
    rows: list[dict[str, object]] = []
    lineage_summary: list[dict[str, object]] = []
    for lineage, external_n in LINEAGE_CPTAC3_SOURCE_N.items():
        indices = lineage_indices[lineage]
        tcga_n = len(indices)
        split_n = min(tcga_n // 2, external_n)
        external_sized_split_feasible = 2 * external_n <= tcga_n
        lineage_summary.append(
            {
                "lineage": lineage,
                "tcga_n": tcga_n,
                "contract_cptac3_source_n": external_n,
                "per_half_n": split_n,
                "external_sized_disjoint_split_feasible": external_sized_split_feasible,
            }
        )
        if split_n < 3:
            continue
        lineage_expression = expression[indices, :]
        for split in range(args.splits):
            chosen = rng.permutation(tcga_n)[: 2 * split_n]
            first_edges = correlation_edges(
                lineage_expression[chosen[:split_n], :], triangle
            )
            second_edges = correlation_edges(
                lineage_expression[chosen[split_n:], :], triangle
            )
            for program_index, program_id in enumerate(PROGRAM_IDS):
                rows.append(
                    {
                        "lineage": lineage,
                        "consensus_program_id": program_id,
                        "split": split,
                        "tcga_n": tcga_n,
                        "contract_cptac3_source_n": external_n,
                        "per_half_n": split_n,
                        "weighted_edge_pattern_correlation": weighted_pearson(
                            first_edges, second_edges, pair_weights[program_index]
                        ),
                    }
                )

    results = pd.DataFrame(rows)
    results.to_csv(args.output_dir / "tcga_reference_split_stability.csv", index=False)
    pd.DataFrame(lineage_summary).to_csv(
        args.output_dir / "tcga_reference_lineage_support.csv", index=False
    )
    summary = results.groupby(["lineage", "consensus_program_id"], as_index=False).agg(
        n_splits=("weighted_edge_pattern_correlation", "count"),
        median=("weighted_edge_pattern_correlation", "median"),
        mean=("weighted_edge_pattern_correlation", "mean"),
        sd=("weighted_edge_pattern_correlation", "std"),
        min=("weighted_edge_pattern_correlation", "min"),
        max=("weighted_edge_pattern_correlation", "max"),
    )
    summary.to_csv(
        args.output_dir / "tcga_reference_split_stability_summary.csv", index=False
    )
    metadata = {
        "purpose": "TCGA-only reference-reliability diagnostic; not external replication or null calibration.",
        "no_cptac3_expression_accessed": True,
        "seed": args.seed,
        "splits": args.splits,
        "split_design": "Disjoint random tumor subsets within lineage; per-half n=min(floor(TCGA n/2), contract CPTAC-3 source n).",
        "pair_count": int(len(triangle[0])),
        "program_effective_pair_counts": dict(
            zip(PROGRAM_IDS, effective_pair_count.tolist())
        ),
        "pair_weight_overlap_file": "program_pair_weight_overlap.csv",
        "artifacts": artifacts,
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "h5py": h5py.__version__,
    }
    (args.output_dir / "tcga_reference_stability_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
