"""Loading, validation, and local identity checks for derived artifacts."""

from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from typing import Any

from pancancer_epigenetics.utils.file_checks import calculate_sha256
from pancancer_epigenetics.utils.paths import PROJECT_ROOT, Paths

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_ROLES = {"data", "metadata", "handoff"}
_PRODUCER_TYPES = {"notebook", "tracked_handoff"}
_INPUT_TYPES = {"artifact", "raw_registry"}


def load_artifact_registry(path: Path = Paths.artifact_registry) -> dict[str, Any]:
    """Load and validate the versioned derived-artifact registry."""
    with Path(path).open(encoding="utf-8") as handle:
        return validate_artifact_registry(json.load(handle))


def _resolve_pointer(document: Any, pointer: str) -> Any:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("raw_registry ref must be a JSON Pointer starting with '/'")
    current = document
    for part in pointer[1:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        if not isinstance(current, dict) or part not in current:
            raise ValueError(f"raw_registry ref does not resolve: {pointer}")
        current = current[part]
    return current


def _validate_relative_path(value: Any) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("artifact path must be a non-empty POSIX-style string")
    path = PurePosixPath(value)
    if value.startswith("/") or path.is_absolute() or ".." in path.parts:
        raise ValueError("artifact path must be repository-relative")
    if value.startswith("data/raw/"):
        raise ValueError("artifact registry cannot include derived paths under data/raw")
    return value


def _validate_cycles(artifacts: dict[str, dict[str, Any]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(artifact_id: str) -> None:
        if artifact_id in visiting:
            raise ValueError("artifact dependency cycle detected")
        if artifact_id in visited:
            return
        visiting.add(artifact_id)
        for item in artifacts[artifact_id]["inputs"]:
            if item["type"] == "artifact":
                visit(item["artifact_id"])
        visiting.remove(artifact_id)
        visited.add(artifact_id)

    for artifact_id in artifacts:
        visit(artifact_id)


def validate_artifact_registry(
    registry: dict[str, Any], raw_registry: dict[str, Any] | None = None
) -> dict[str, Any]:
    """Validate schema, references, and the dependency DAG without artifact files."""
    if not isinstance(registry, dict) or set(registry) != {"schema_version", "artifacts"}:
        raise ValueError("artifact registry must contain only schema_version and artifacts")
    if registry["schema_version"] != 1:
        raise ValueError("Unsupported artifact registry schema_version")
    artifacts = registry["artifacts"]
    if not isinstance(artifacts, dict):
        raise ValueError("artifacts must be a mapping")
    raw_registry = raw_registry if raw_registry is not None else json.loads(Paths.raw_data_registry.read_text(encoding="utf-8"))
    paths: set[str] = set()
    for artifact_id, artifact in artifacts.items():
        if not isinstance(artifact_id, str) or not artifact_id:
            raise ValueError("artifact IDs must be non-empty strings")
        if not isinstance(artifact, dict):
            raise ValueError(f"artifact {artifact_id} must be a mapping")
        path = _validate_relative_path(artifact.get("path"))
        if path in paths:
            raise ValueError(f"duplicate artifact path: {path}")
        paths.add(path)
        if not isinstance(artifact.get("phase"), int) or isinstance(artifact["phase"], bool) or artifact["phase"] < 1:
            raise ValueError("phase must be a positive integer")
        if artifact.get("status") != "frozen":
            raise ValueError("artifact status must be frozen")
        if artifact.get("artifact_role") not in _ROLES:
            raise ValueError("invalid artifact_role")
        producer = artifact.get("producer")
        if not isinstance(producer, dict) or producer.get("type") not in _PRODUCER_TYPES:
            raise ValueError("invalid producer")
        if producer["type"] == "notebook":
            notebook_path = producer.get("path")
            if not isinstance(notebook_path, str) or not notebook_path.startswith("notebooks/") or not notebook_path.endswith(".ipynb"):
                raise ValueError("notebook producer requires a notebook path")
        elif set(producer) != {"type"}:
            raise ValueError("tracked_handoff producer must only declare type")
        size = artifact.get("size_bytes")
        if not isinstance(size, int) or isinstance(size, bool) or size < 0:
            raise ValueError("size_bytes must be a non-negative integer")
        checksum = artifact.get("sha256")
        if not isinstance(checksum, str) or not _SHA256.fullmatch(checksum):
            raise ValueError("sha256 must be a full lowercase 64-character hexadecimal checksum")
        if artifact.get("shape") is not None and (not isinstance(artifact["shape"], list) or not all(isinstance(dimension, int) and dimension >= 0 for dimension in artifact["shape"])):
            raise ValueError("shape must be null or a list of non-negative integers")
        inputs = artifact.get("inputs")
        if not isinstance(inputs, list):
            raise ValueError("inputs must be a list")
        for item in inputs:
            if not isinstance(item, dict) or item.get("type") not in _INPUT_TYPES:
                raise ValueError("invalid input type")
            if item["type"] == "artifact":
                reference = item.get("artifact_id")
                if not isinstance(reference, str) or reference not in artifacts:
                    raise ValueError("artifact input ref does not exist")
                if reference == artifact_id:
                    raise ValueError("artifact cannot depend on itself")
            else:
                _resolve_pointer(raw_registry, item.get("ref"))
    _validate_cycles(artifacts)
    return registry


def get_artifact(registry: dict[str, Any], artifact_id: str) -> dict[str, Any]:
    """Return one registered artifact by its stable ID."""
    try:
        return registry["artifacts"][artifact_id]
    except KeyError as error:
        raise KeyError(f"Unknown artifact ID: {artifact_id}") from error


def resolve_artifact_path(registry: dict[str, Any], artifact_id: str, root: Path = PROJECT_ROOT) -> Path:
    """Resolve a registered repository-relative artifact path deterministically."""
    return (Path(root) / get_artifact(registry, artifact_id)["path"]).resolve()


def verify_artifact_identity(registry: dict[str, Any], root: Path = PROJECT_ROOT) -> list[dict[str, Any]]:
    """Return local missing, size, or checksum discrepancies for registered artifacts."""
    findings: list[dict[str, Any]] = []
    for artifact_id in sorted(registry["artifacts"]):
        artifact = get_artifact(registry, artifact_id)
        path = resolve_artifact_path(registry, artifact_id, root)
        if not path.is_file():
            findings.append({"artifact_id": artifact_id, "issue": "missing"})
        elif path.stat().st_size != artifact["size_bytes"]:
            findings.append({"artifact_id": artifact_id, "issue": "size_mismatch"})
        elif calculate_sha256(path) != artifact["sha256"]:
            findings.append({"artifact_id": artifact_id, "issue": "sha256_mismatch"})
    return findings


# Backwards-compatible spelling for callers written during initial scaffolding.
verify_artifact_files = verify_artifact_identity
