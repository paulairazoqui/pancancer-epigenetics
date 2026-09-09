"""Utilities for deterministic JSON registry access and updates."""

import json
from pathlib import Path
from typing import Any


def load_json_registry(registry_path: Path) -> dict[str, Any]:
    """Load a JSON registry from disk."""
    registry_path = Path(registry_path)

    with registry_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def register_json_entry(
    registry_path: Path,
    key_path: tuple[str, ...],
    entry: dict[str, Any],
    *,
    allow_replace: bool = False,
) -> dict[str, Any]:
    """Insert one entry into an existing nested JSON registry atomically.

    Parent keys must already exist. Existing entries are protected from
    replacement unless allow_replace=True.
    """
    if not key_path:
        raise ValueError("key_path must contain at least one key.")

    registry_path = Path(registry_path)
    registry = load_json_registry(registry_path)

    parent = registry

    for key in key_path[:-1]:
        if key not in parent:
            raise KeyError(
                f"Registry parent key is absent: {key!r}"
            )

        if not isinstance(parent[key], dict):
            raise TypeError(
                f"Registry parent is not a mapping: {key!r}"
            )

        parent = parent[key]

    entry_key = key_path[-1]

    if entry_key in parent:
        existing_entry = parent[entry_key]

        if existing_entry == entry:
            return existing_entry

        if not allow_replace:
            raise ValueError(
                f"Registry entry already exists with different content: "
                f"{entry_key}"
            )

    parent[entry_key] = entry

    temporary_path = registry_path.with_suffix(
        registry_path.suffix + ".tmp"
    )

    temporary_path.write_text(
        json.dumps(
            registry,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    validated_registry = load_json_registry(
        temporary_path
    )

    validated_parent = validated_registry

    for key in key_path[:-1]:
        validated_parent = validated_parent[key]

    observed_entry = validated_parent[entry_key]

    if observed_entry != entry:
        temporary_path.unlink(missing_ok=True)
        raise ValueError(
            "Serialized registry entry does not match "
            "the requested entry."
        )

    temporary_path.replace(registry_path)

    return observed_entry