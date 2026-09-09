from pathlib import Path
import json

import pytest

from pancancer_epigenetics.utils.registry import (
    load_json_registry,
    register_json_entry,
)


def _write_registry(
    path: Path,
    registry: dict,
) -> None:
    path.write_text(
        json.dumps(
            registry,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )


def test_load_json_registry(tmp_path: Path) -> None:
    registry_path = tmp_path / "registry.json"

    expected = {
        "tcga": {
            "external_resources": {},
        }
    }

    _write_registry(
        registry_path,
        expected,
    )

    assert load_json_registry(registry_path) == expected


def test_register_json_entry_inserts_nested_entry(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    registry = {
        "tcga": {
            "external_resources": {},
        }
    }

    entry = {
        "status": "acquired_and_used",
        "provider": "example",
    }

    _write_registry(
        registry_path,
        registry,
    )

    observed = register_json_entry(
        registry_path,
        (
            "tcga",
            "external_resources",
            "example_resource",
        ),
        entry,
    )

    persisted = load_json_registry(
        registry_path
    )

    assert observed == entry
    assert (
        persisted["tcga"]["external_resources"][
            "example_resource"
        ]
        == entry
    )

    temporary_path = registry_path.with_suffix(
        registry_path.suffix + ".tmp"
    )

    assert not temporary_path.exists()


def test_register_json_entry_rejects_missing_parent(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    registry = {
        "tcga": {},
    }

    _write_registry(
        registry_path,
        registry,
    )

    with pytest.raises(
        KeyError,
        match="Registry parent key is absent",
    ):
        register_json_entry(
            registry_path,
            (
                "tcga",
                "external_resources",
                "example_resource",
            ),
            {"status": "supporting"},
        )

    assert load_json_registry(registry_path) == registry


def test_register_json_entry_rejects_non_mapping_parent(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    registry = {
        "tcga": {
            "external_resources": "invalid",
        }
    }

    _write_registry(
        registry_path,
        registry,
    )

    with pytest.raises(
        TypeError,
        match="Registry parent is not a mapping",
    ):
        register_json_entry(
            registry_path,
            (
                "tcga",
                "external_resources",
                "example_resource",
            ),
            {"status": "supporting"},
        )

    assert load_json_registry(registry_path) == registry


def test_register_json_entry_protects_existing_entry(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    original_entry = {
        "status": "supporting",
        "value": 1,
    }

    registry = {
        "tcga": {
            "external_resources": {
                "example_resource": original_entry,
            }
        }
    }

    _write_registry(
        registry_path,
        registry,
    )

    with pytest.raises(
        ValueError,
        match="Registry entry already exists",
    ):
        register_json_entry(
            registry_path,
            (
                "tcga",
                "external_resources",
                "example_resource",
            ),
            {
                "status": "acquired_and_used",
                "value": 2,
            },
        )

    persisted = load_json_registry(
        registry_path
    )

    assert (
        persisted["tcga"]["external_resources"][
            "example_resource"
        ]
        == original_entry
    )


def test_register_json_entry_allows_explicit_replacement(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    registry = {
        "tcga": {
            "external_resources": {
                "example_resource": {
                    "status": "supporting",
                    "value": 1,
                }
            }
        }
    }

    replacement = {
        "status": "acquired_and_used",
        "value": 2,
    }

    _write_registry(
        registry_path,
        registry,
    )

    observed = register_json_entry(
        registry_path,
        (
            "tcga",
            "external_resources",
            "example_resource",
        ),
        replacement,
        allow_replace=True,
    )

    persisted = load_json_registry(
        registry_path
    )

    assert observed == replacement
    assert (
        persisted["tcga"]["external_resources"][
            "example_resource"
        ]
        == replacement
    )


def test_register_json_entry_requires_nonempty_key_path(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    registry = {
        "tcga": {
            "external_resources": {},
        }
    }

    _write_registry(
        registry_path,
        registry,
    )

    with pytest.raises(
        ValueError,
        match="key_path must contain at least one key",
    ):
        register_json_entry(
            registry_path,
            (),
            {"status": "supporting"},
        )

    assert load_json_registry(registry_path) == registry


def test_register_json_entry_preserves_utf8_content(
    tmp_path: Path,
) -> None:
    registry_path = tmp_path / "registry.json"

    registry = {
        "resources": {},
    }

    entry = {
        "provider": "Anotación génica",
        "description": "Recurso derivado en hg38",
    }

    _write_registry(
        registry_path,
        registry,
    )

    register_json_entry(
        registry_path,
        (
            "resources",
            "annotation",
        ),
        entry,
    )

    persisted = load_json_registry(
        registry_path
    )

    assert (
        persisted["resources"]["annotation"]
        == entry
    )