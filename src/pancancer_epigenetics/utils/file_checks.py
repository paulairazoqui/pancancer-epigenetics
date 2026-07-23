"""Reusable file-level checks and provenance utilities."""

from pathlib import Path
import hashlib


def calculate_sha256(file_path: Path, chunk_size: int = 8192) -> str:
    """Calculate the SHA256 checksum of a local file."""
    file_path = Path(file_path)

    sha256 = hashlib.sha256()

    with file_path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            sha256.update(chunk)

    return sha256.hexdigest()


def get_file_size_mb(file_path: Path) -> float:
    """Return file size in megabytes."""
    return Path(file_path).stat().st_size / 1024**2


def to_project_relative_posix_path(path: Path, project_root: Path) -> str:
    """Return a project-relative path using POSIX separators."""
    return Path(path).relative_to(Path(project_root)).as_posix()