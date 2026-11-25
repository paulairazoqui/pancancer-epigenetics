"""Shared names and artifact-backed identities for consensus analyses.

The Phase 4 catalog contains the consensus programs produced for the current
run, in authoritative row order. These helpers do not decide eligibility or
alter any downstream analytical contract. For example::

    programs = load_consensus_programs()
    ids = tuple(p.program_id for p in programs)
    aligned = align_program_columns(score_frame, ids, metadata_columns=("ModelID",))

Registry paths may be supplied for isolated tests or alternate project roots.
Artifact identity and reconstruction status remain the caller's responsibility.
"""

from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from pandas import DataFrame


@dataclass(frozen=True)
class ConsensusProgram:
    """A catalog program and its Phase 4 source orientation metadata."""

    program_id: str
    tumor_rna_axis: str
    cell_line_program: str
    orientation_multiplier: int


def _artifact_path(
    artifact_id: str, registry_path: Path | None, root: Path | None
) -> Path:
    # Paths initializes from configuration on import; defer that read until use.
    from pancancer_epigenetics.utils.artifact_registry import (
        load_artifact_registry,
        resolve_artifact_path,
    )
    from pancancer_epigenetics.utils.paths import PROJECT_ROOT

    registry = (
        load_artifact_registry()
        if registry_path is None
        else load_artifact_registry(registry_path)
    )
    path = resolve_artifact_path(
        registry, artifact_id, PROJECT_ROOT if root is None else root
    )
    if not path.is_file():
        raise FileNotFoundError(
            f"Required artifact {artifact_id!r} is unavailable: {path}"
        )
    return path


def _rows(path: Path, required: tuple[str, ...]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if len(headers) != len(set(headers)):
            raise ValueError(f"Duplicate column names in {path}")
        missing = set(required) - set(headers)
        if missing:
            raise ValueError(f"Missing required columns in {path}: {sorted(missing)}")
        return list(reader)


def _identifiers(values: Iterable[str], label: str) -> tuple[str, ...]:
    ids = tuple(values)
    if not ids:
        raise ValueError(f"{label} must contain at least one identifier")
    if any(not isinstance(v, str) or not v.strip() or v != v.strip() for v in ids):
        raise ValueError(f"{label} contains a missing or invalid identifier")
    duplicates = sorted(k for k, count in Counter(ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"{label} contains duplicate identifiers: {duplicates}")
    return ids


def load_consensus_programs(
    *, registry_path: Path | None = None, root: Path | None = None
) -> tuple[ConsensusProgram, ...]:
    """Read ordered program IDs and source orientations from the Phase 4 catalog.

    Every catalog row is a produced consensus program; its status is not an
    instruction for this interface to apply a new downstream eligibility rule.
    """
    path = _artifact_path(
        "phase4.401.consensus_transcriptomic_program_catalog", registry_path, root
    )
    rows = _rows(
        path,
        (
            "consensus_program_id",
            "tumor_rna_axis",
            "cell_line_program",
            "orientation_multiplier",
        ),
    )
    ids = _identifiers((r["consensus_program_id"] for r in rows), "Program catalog")
    programs = []
    for program_id, row in zip(ids, rows):
        axis, source = row["tumor_rna_axis"], row["cell_line_program"]
        if (
            not axis
            or not axis.strip()
            or axis != axis.strip()
            or not source
            or not source.strip()
            or source != source.strip()
        ):
            raise ValueError(
                f"Missing or invalid source orientation metadata for {program_id}"
            )
        try:
            multiplier = int(row["orientation_multiplier"])
        except (ValueError, TypeError) as exc:
            raise ValueError(
                f"Invalid orientation multiplier for {program_id}"
            ) from exc
        if multiplier not in (-1, 1):
            raise ValueError(
                f"Invalid orientation multiplier for {program_id}: {multiplier}"
            )
        programs.append(ConsensusProgram(program_id, axis, source, multiplier))
    return tuple(programs)


def load_model_ids(
    *,
    artifact_id: str = "phase3.302.integrated_modeling_cohort",
    registry_path: Path | None = None,
    root: Path | None = None,
) -> tuple[str, ...]:
    """Read ordered unique ModelIDs from a registered CSV cohort.

    The default is the Phase 3 integrated modeling cohort. Select another
    registered cohort explicitly when its analytical contract requires it;
    its count is ``len(load_model_ids(...))``.
    """
    path = _artifact_path(artifact_id, registry_path, root)
    return _identifiers(
        (row["ModelID"] for row in _rows(path, ("ModelID",))), f"Cohort {artifact_id}"
    )


def score_column(program_id: str) -> str:
    """Return the Phase 4/6 wide score column for a program ID."""
    return _identifiers((program_id,), "Program")[0]


def attribution_column(program_id: str) -> str:
    """Return the Phase 6 program-level SHAP attribution column."""
    return f"phi_{score_column(program_id)}"


def align_program_columns(
    frame: DataFrame,
    program_ids: Iterable[str],
    *,
    metadata_columns: Iterable[str] = (),
    attribution: bool = False,
) -> DataFrame:
    """Validate and align a wide matrix to the supplied program order.

    Declare every non-program column in ``metadata_columns``. Unknown columns,
    missing columns, duplicates, and duplicate program IDs raise ValueError;
    Set attribution=True for Phase 6 ``phi_`` columns. Return a new DataFrame
    with metadata columns first in their declared order, followed by program
    columns in program_ids order. The input and its values are not changed.
    This checks identity, not scientific eligibility.
    """
    ids = _identifiers(program_ids, "Program definitions")
    cols = _identifiers(frame.columns, "Matrix columns")
    metadata = tuple(metadata_columns)
    if metadata:
        _identifiers(metadata, "Metadata columns")
    ordered_programs = tuple(
        attribution_column(p) if attribution else score_column(p) for p in ids
    )
    expected_programs = set(ordered_programs)
    if expected_programs & set(metadata):
        raise ValueError("Metadata columns overlap program columns")
    expected = expected_programs | set(metadata)
    missing, unexpected = expected - set(cols), set(cols) - expected
    if missing or unexpected:
        raise ValueError(
            f"Matrix columns disagree with program definitions: missing={sorted(missing)}, unexpected={sorted(unexpected)}"
        )
    return frame.loc[:, [*metadata, *ordered_programs]].copy()
