from pathlib import Path

import pytest

from pancancer_epigenetics.utils.raw_data_registry import (
    enumerate_file_managed_files,
    get_cohort,
    get_dataset,
    get_file_by_role,
    load_raw_data_registry,
    resolve_canonical_dir,
    resolve_canonical_file_path,
    validate_canonical_dir,
    validate_file_identity,
    validate_provenance_mode,
    validate_raw_data_registry,
    validate_sha256,
    validate_size_bytes,
    validate_status,
)


def test_get_dataset_and_cohort() -> None:
    registry = {"tcga": {"cohorts": {"rnaseq_star_counts": {}}}}

    assert get_dataset(registry, "tcga") == registry["tcga"]
    assert get_cohort(registry, "tcga", "rnaseq_star_counts") == {}


@pytest.mark.parametrize(
    "files",
    [{}, {"a.txt": {"role": "manifest"}, "b.txt": {"role": "manifest"}}],
)
def test_get_file_by_role_requires_exactly_one_match(files: dict) -> None:
    with pytest.raises(ValueError, match="Expected exactly one file with role 'manifest'"):
        get_file_by_role({"files": files}, "manifest")


def test_get_file_by_role_returns_filename_and_metadata() -> None:
    cohort = {"files": {"manifest.txt": {"role": "manifest", "description": "test"}}}

    file_name, metadata = get_file_by_role(cohort, "manifest")

    assert file_name == "manifest.txt"
    assert metadata == {"role": "manifest", "description": "test"}


def test_valid_provenance_mode_and_status() -> None:
    assert validate_provenance_mode("file_managed") == "file_managed"
    assert validate_provenance_mode("manifest_managed") == "manifest_managed"
    assert validate_status("acquired_and_used") == "acquired_and_used"
    assert validate_status("supporting") == "supporting"


def test_invalid_provenance_mode_and_status_are_rejected() -> None:
    with pytest.raises(ValueError, match="Invalid provenance_mode"):
        validate_provenance_mode("recursive")
    with pytest.raises(ValueError, match="Invalid status"):
        validate_status("maybe")


def test_canonical_dir_must_be_repository_relative(tmp_path: Path) -> None:
    assert validate_canonical_dir("data/raw/example") == "data/raw/example"

    with pytest.raises(ValueError, match="canonical_dir must be repository-relative"):
        validate_canonical_dir(str(tmp_path))

    with pytest.raises(ValueError, match="canonical_dir must be repository-relative"):
        validate_canonical_dir("../outside")

    with pytest.raises(ValueError, match="canonical_dir must be repository-relative"):
        resolve_canonical_dir({"canonical_dir": str(tmp_path)}, root=tmp_path)


def test_size_bytes_and_sha256_validation() -> None:
    assert validate_size_bytes(0) == 0
    assert validate_size_bytes(123) == 123
    assert validate_sha256("a" * 64) == "a" * 64

    with pytest.raises(ValueError, match="size_bytes"):
        validate_size_bytes(-1)
    with pytest.raises(ValueError, match="size_bytes"):
        validate_size_bytes("123")
    with pytest.raises(ValueError, match="sha256"):
        validate_sha256("a" * 63)
    with pytest.raises(ValueError, match="sha256"):
        validate_sha256("g" * 64)


def test_acquired_file_identity_requires_complete_pair() -> None:
    identity = {"size_bytes": 3, "sha256": "b" * 64}
    validate_file_identity(identity, required=True)

    with pytest.raises(ValueError, match="provided together"):
        validate_file_identity({"size_bytes": 3}, required=False)
    with pytest.raises(ValueError, match="require size_bytes and sha256"):
        validate_file_identity({}, required=True)


def test_manifest_payloads_do_not_require_individual_identity() -> None:
    registry = {
        "tcga": {
            "cohorts": {
                "rnaseq_star_counts": {
                    "provenance_mode": "manifest_managed",
                    "status": "acquired_and_used",
                    "canonical_dir": "data/raw/tcga/star_counts",
                    "files": {"payload": {"role": "cohort_payload"}},
                }
            }
        }
    }

    assert validate_raw_data_registry(registry) == registry
    assert enumerate_file_managed_files(registry, root=Path("/tmp/unused")) == []


def test_planned_dataset_does_not_require_file_identity() -> None:
    registry = {
        "future": {
            "status": "planned",
            "files": {},
        }
    }

    assert validate_raw_data_registry(registry) == registry
    assert enumerate_file_managed_files(registry, root=Path("/tmp/unused")) == []


def test_file_managed_enumeration_is_deterministic_and_root_independent(tmp_path: Path) -> None:
    registry = {
        "z_dataset": {
            "provenance_mode": "file_managed",
            "canonical_dir": "data/raw/z",
            "files": {
                "b.txt": {"role": "second", "status": "supporting", "size_bytes": 1, "sha256": "b" * 64},
                "a.txt": {"role": "first", "status": "supporting", "size_bytes": 1, "sha256": "a" * 64},
            },
        },
        "a_dataset": {
            "provenance_mode": "file_managed",
            "canonical_dir": "data/raw/a",
            "files": {
                "c.txt": {"role": "third", "status": "acquired_not_used", "size_bytes": 1, "sha256": "c" * 64},
            },
        },
    }

    paths = [record["relative_path"] for record in enumerate_file_managed_files(registry, root=tmp_path)]

    assert paths == ["data/raw/a/c.txt", "data/raw/z/a.txt", "data/raw/z/b.txt"]
    assert all(record["path"].is_absolute() for record in enumerate_file_managed_files(registry, root=tmp_path))


def test_actual_registry_management_modes_and_statuses() -> None:
    registry = load_raw_data_registry()

    assert registry["tcga"]["cohorts"]["rnaseq_star_counts"]["provenance_mode"] == "manifest_managed"
    assert registry["tcga"]["cohorts"]["methylation_array_sesame_beta_values"]["provenance_mode"] == "manifest_managed"
    assert registry["tcga"]["external_resources"]["estimate"]["provenance_mode"] == "file_managed"
    assert registry["depmap"]["provenance_mode"] == "file_managed"
    assert registry["gdsc"]["provenance_mode"] == "file_managed"
    assert registry["epifactors"]["provenance_mode"] == "file_managed"
    assert registry["msigdb"]["provenance_mode"] == "file_managed"
    assert registry["ctrp"]["status"] == "planned"

    files = enumerate_file_managed_files(registry, root=Path("/not/the/raw/data"))
    paths = {record["relative_path"] for record in files}
    assert "data/raw/tcga/confounders/41467_2013_BFncomms3612_MOESM489_ESM.xlsx" in paths
    assert not any("star_counts" in path or "methylation" in path for path in paths)
    assert len(files) == 22


def test_resolve_canonical_file_path_uses_registry_filename(tmp_path: Path) -> None:
    registry = {
        "tcga": {
            "cohorts": {
                "rnaseq_star_counts": {
                    "canonical_dir": "config/manifests/tcga_rna",
                    "files": {
                        "manifest.txt": {"role": "manifest"},
                    },
                }
            }
        }
    }

    resolved_path = resolve_canonical_file_path(
        registry,
        "tcga",
        "rnaseq_star_counts",
        "manifest",
        root=tmp_path,
    )

    assert resolved_path == (tmp_path / "config/manifests/tcga_rna/manifest.txt").resolve()
