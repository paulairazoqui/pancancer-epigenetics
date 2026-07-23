from pathlib import Path

import pytest

from pancancer_epigenetics.utils.raw_data_registry import (
    get_cohort,
    get_dataset,
    get_file_by_role,
    resolve_canonical_dir,
    resolve_canonical_file_path,
)


def test_get_dataset_and_cohort() -> None:
    registry = {"tcga": {"cohorts": {"rnaseq_star_counts": {}}}}

    assert get_dataset(registry, "tcga") == registry["tcga"]
    assert get_cohort(registry, "tcga", "rnaseq_star_counts") == {}


@pytest.mark.parametrize("files", [{}, {"a.txt": {"role": "manifest"}, "b.txt": {"role": "manifest"}}])
def test_get_file_by_role_requires_exactly_one_match(files: dict) -> None:
    with pytest.raises(ValueError, match="Expected exactly one file with role 'manifest'"):
        get_file_by_role({"files": files}, "manifest")


def test_get_file_by_role_returns_filename_and_metadata() -> None:
    cohort = {"files": {"manifest.txt": {"role": "manifest", "description": "test"}}}

    file_name, metadata = get_file_by_role(cohort, "manifest")

    assert file_name == "manifest.txt"
    assert metadata == {"role": "manifest", "description": "test"}


def test_resolve_canonical_dir_rejects_absolute_path(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="canonical_dir must be repository-relative"):
        resolve_canonical_dir({"canonical_dir": str(tmp_path)}, root=tmp_path)


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
