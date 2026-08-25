"""Utilities for resolving and validating the raw-data registry."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterator

from pancancer_epigenetics.utils.paths import Paths

Registry = dict[str, Any]

PROVENANCE_MODES = frozenset({"file_managed", "manifest_managed"})
STATUSES = frozenset(
    {
        "acquired_and_used",
        "supporting",
        "acquired_not_used",
        "planned",
    }
)
_SHA256_PATTERN = re.compile(r"^[0-9a-fA-F]{64}$")


def validate_provenance_mode(value: Any) -> str:
    """Validate and return a registry provenance-management mode."""
    if value not in PROVENANCE_MODES:
        raise ValueError(
            f"Invalid provenance_mode '{value}'. "
            f"Expected one of: {sorted(PROVENANCE_MODES)}."
        )
    return value


def validate_status(value: Any) -> str:
    """Validate and return a registry usage/status value."""
    if value not in STATUSES:
        raise ValueError(
            f"Invalid status '{value}'. Expected one of: {sorted(STATUSES)}."
        )
    return value


def validate_canonical_dir(value: Any) -> str:
    """Validate a repository-relative canonical directory."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("canonical_dir must be a non-empty repository-relative string.")

    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"canonical_dir must be repository-relative: {value}")

    return value


def validate_size_bytes(value: Any) -> int:
    """Validate a non-negative byte count."""
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError("size_bytes must be a non-negative integer.")
    return value


def validate_sha256(value: Any) -> str:
    """Validate a complete SHA256 hexadecimal digest."""
    if not isinstance(value, str) or _SHA256_PATTERN.fullmatch(value) is None:
        raise ValueError("sha256 must contain exactly 64 hexadecimal characters.")
    return value


def validate_file_identity(file_metadata: Registry, *, required: bool = False) -> None:
    """Validate the optional or required byte-level identity of a raw file."""
    if not isinstance(file_metadata, dict):
        raise ValueError("Raw file metadata must be an object.")

    has_size = "size_bytes" in file_metadata
    has_sha256 = "sha256" in file_metadata

    if has_size != has_sha256:
        raise ValueError("size_bytes and sha256 must be provided together.")

    if required and not (has_size and has_sha256):
        raise ValueError(
            "Acquired file-managed raw files require size_bytes and sha256."
        )

    if has_size:
        validate_size_bytes(file_metadata["size_bytes"])
        validate_sha256(file_metadata["sha256"])


def _resource_entries(registry: Registry) -> Iterator[tuple[str, str | None, Registry]]:
    """Yield dataset/resource entries that can own canonical raw files."""
    for dataset_id in sorted(registry):
        dataset = registry[dataset_id]
        if not isinstance(dataset, dict):
            raise ValueError(f"Dataset '{dataset_id}' registry entry must be an object.")

        if "provenance_mode" in dataset or "files" in dataset:
            yield dataset_id, None, dataset

        for collection_name in ("cohorts", "external_resources"):
            collection = dataset.get(collection_name, {})
            if not isinstance(collection, dict):
                raise ValueError(
                    f"Dataset '{dataset_id}' '{collection_name}' must be an object."
                )
            for resource_id in sorted(collection):
                resource = collection[resource_id]
                if not isinstance(resource, dict):
                    raise ValueError(
                        f"Resource '{dataset_id}.{resource_id}' must be an object."
                    )
                yield dataset_id, resource_id, resource


def validate_raw_data_registry(registry: Registry) -> Registry:
    """Validate provenance fields and file identity without touching raw files."""
    if not isinstance(registry, dict):
        raise ValueError("raw_data_registry.json must contain a top-level JSON object.")

    for dataset_id, resource_id, resource in _resource_entries(registry):
        label = dataset_id if resource_id is None else f"{dataset_id}.{resource_id}"
        mode = resource.get("provenance_mode")
        status = resource.get("status")

        if mode is not None:
            validate_provenance_mode(mode)
        if status is not None:
            validate_status(status)
        if "canonical_dir" in resource:
            validate_canonical_dir(resource["canonical_dir"])

        files = resource.get("files", {})
        if not isinstance(files, dict):
            raise ValueError(f"Resource '{label}' 'files' must be an object.")

        if mode == "file_managed":
            if "canonical_dir" not in resource:
                raise ValueError(f"File-managed resource '{label}' needs canonical_dir.")
            for file_name, file_metadata in files.items():
                if not isinstance(file_name, str) or not file_name:
                    raise ValueError(f"Resource '{label}' has an invalid file name.")
                if not isinstance(file_metadata, dict):
                    raise ValueError(
                        f"File '{label}.{file_name}' metadata must be an object."
                    )
                file_status = file_metadata.get("status", status)
                if file_status is not None:
                    validate_status(file_status)
                validate_file_identity(
                    file_metadata,
                    required=file_status in {
                        "acquired_and_used",
                        "supporting",
                        "acquired_not_used",
                    },
                )
        elif mode == "manifest_managed":
            for file_metadata in files.values():
                if isinstance(file_metadata, dict):
                    validate_file_identity(file_metadata, required=False)

    return registry


def load_raw_data_registry(registry_path: Path = Paths.raw_data_registry) -> Registry:
    """Load and validate the raw data registry JSON."""
    if not registry_path.is_file():
        raise FileNotFoundError(f"Raw data registry not found: {registry_path}")

    with registry_path.open("r", encoding="utf-8") as handle:
        registry = json.load(handle)

    return validate_raw_data_registry(registry)


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
    """Return one cohort registry entry by dataset and cohort IDs."""
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
    """Resolve a canonical directory relative to the repository root."""
    canonical_dir = cohort.get("canonical_dir")

    if not canonical_dir:
        raise KeyError("Cohort registry entry is missing 'canonical_dir'.")

    validate_canonical_dir(canonical_dir)
    return (root / canonical_dir).resolve()


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


def _file_record(
    dataset_id: str,
    resource_id: str | None,
    resource: Registry,
    file_name: str,
    file_metadata: Registry,
    root: Path,
) -> Registry:
    mode = validate_provenance_mode(resource["provenance_mode"])
    status = file_metadata.get("status", resource.get("status"))
    if status is None:
        raise ValueError(
            f"File-managed resource '{dataset_id}' requires status on the resource or file."
        )
    validate_status(status)
    validate_canonical_dir(resource["canonical_dir"])

    return {
        "dataset_id": dataset_id,
        "resource_id": resource_id,
        "provenance_mode": mode,
        "status": status,
        "canonical_dir": resource["canonical_dir"],
        "file_name": file_name,
        "role": file_metadata.get("role"),
        "metadata": file_metadata,
        "relative_path": f"{resource['canonical_dir'].rstrip('/')}/{file_name}",
        "path": (root / resource["canonical_dir"] / file_name).resolve(),
    }


def enumerate_file_managed_files(
    registry: Registry,
    root: Path = Paths.root,
) -> list[Registry]:
    """Enumerate acquired file-managed files in deterministic path order."""
    records: list[Registry] = []
    for dataset_id, resource_id, resource in _resource_entries(registry):
        if resource.get("provenance_mode") != "file_managed":
            continue
        files = resource.get("files", {})
        for file_name in sorted(files):
            file_metadata = files[file_name]
            if not isinstance(file_metadata, dict):
                raise ValueError(
                    f"File '{dataset_id}.{file_name}' metadata must be an object."
                )
            status = file_metadata.get("status", resource.get("status"))
            if status == "planned":
                continue
            records.append(
                _file_record(
                    dataset_id,
                    resource_id,
                    resource,
                    file_name,
                    file_metadata,
                    root,
                )
            )
    return sorted(records, key=lambda record: record["relative_path"])


def enumerate_manifest_managed_resources(registry: Registry) -> list[Registry]:
    """Enumerate manifest-managed resources excluded from individual hashing."""
    resources = []
    for dataset_id, resource_id, resource in _resource_entries(registry):
        if resource.get("provenance_mode") != "manifest_managed":
            continue
        resources.append(
            {
                "dataset_id": dataset_id,
                "resource_id": resource_id,
                "status": resource.get("status"),
                "canonical_dir": resource.get("canonical_dir"),
                "reason": resource.get(
                    "audit_exclusion_reason",
                    "Provider manifest/freeze/metadata governs payload identity; "
                    "individual payload SHA256 is not duplicated here.",
                ),
            }
        )
    return sorted(
        resources,
        key=lambda resource: (
            resource["dataset_id"],
            resource["resource_id"] or "",
        ),
    )


# Backward/reader-friendly alias for callers that prefer an iterator name.
iter_file_managed_files = enumerate_file_managed_files
