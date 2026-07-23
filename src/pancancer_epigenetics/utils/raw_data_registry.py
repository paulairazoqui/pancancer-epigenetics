"""Utilities for resolving canonical raw-data registry cohorts and files."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pancancer_epigenetics.utils.paths import Paths

Registry = dict[str, Any]


def load_raw_data_registry(registry_path: Path = Paths.raw_data_registry) -> Registry:
    """Load and minimally validate the raw data registry JSON."""
    if not registry_path.is_file():
        raise FileNotFoundError(f"Raw data registry not found: {registry_path}")

    with registry_path.open("r", encoding="utf-8") as handle:
        registry = json.load(handle)

    if not isinstance(registry, dict):
        raise ValueError("raw_data_registry.json must contain a top-level JSON object.")

    return registry


def get_dataset(registry: Registry, dataset_id: str) -> Registry:
    """Return one dataset registry entry by ID."""
    try:
        dataset = registry[dataset_id]
    except KeyError as error:
        raise KeyError(f"Dataset '{dataset_id}' is missing from raw_data_registry.json.") from error

    if not isinstance(dataset, dict):
        raise ValueError(f"Dataset '{dataset_id}' registry entry must be an object.")

    return dataset


def get_cohort(registry: Registry, dataset_id: str, cohort_id: str) -> Registry:
    """Return one cohort registry entry by dataset and cohort ID."""
    dataset = get_dataset(registry, dataset_id)
    cohorts = dataset.get("cohorts")

    if not isinstance(cohorts, dict):
        raise KeyError(f"Dataset '{dataset_id}' is missing a 'cohorts' object.")

    try:
        cohort = cohorts[cohort_id]
    except KeyError as error:
        raise KeyError(
            f"Cohort '{cohort_id}' is missing from dataset '{dataset_id}'."
        ) from error

    if not isinstance(cohort, dict):
        raise ValueError(
            f"Cohort '{cohort_id}' in dataset '{dataset_id}' must be an object."
        )

    return cohort


def get_file_by_role(cohort: Registry, role: str) -> tuple[str, Registry]:
    """Return the only file registry entry matching a role."""
    files = cohort.get("files")

    if not isinstance(files, dict):
        raise KeyError("Cohort registry entry is missing a 'files' object.")

    matches = [
        (file_name, file_metadata)
        for file_name, file_metadata in files.items()
        if isinstance(file_metadata, dict) and file_metadata.get("role") == role
    ]

    if len(matches) != 1:
        raise ValueError(f"Expected exactly one file with role '{role}', found {len(matches)}.")

    return matches[0]


def resolve_canonical_dir(cohort: Registry, root: Path = Paths.root) -> Path:
    """Resolve a cohort canonical directory relative to the repository root."""
    canonical_dir = cohort.get("canonical_dir")

    if not canonical_dir:
        raise KeyError("Cohort registry entry is missing 'canonical_dir'.")

    canonical_dir_path = Path(canonical_dir)

    if canonical_dir_path.is_absolute():
        raise ValueError(f"canonical_dir must be repository-relative: {canonical_dir}")

    return (root / canonical_dir_path).resolve()


def resolve_canonical_file_path(
    registry: Registry,
    dataset_id: str,
    cohort_id: str,
    role: str,
    root: Path = Paths.root,
) -> Path:
    """Resolve the canonical path for a cohort file role."""
    cohort = get_cohort(registry, dataset_id, cohort_id)
    file_name, _file_metadata = get_file_by_role(cohort, role)
    return resolve_canonical_dir(cohort, root=root) / file_name
