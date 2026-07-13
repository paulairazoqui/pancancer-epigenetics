"""Checksum utilities for file-level provenance."""

from pathlib import Path


import hashlib


def calculate_sha256(file_path: Path, chunk_size: int = 8192) -> str:
    """Calculate the SHA256 checksum of a local file.

    Parameters
    ----------
    file_path
        Path to the file to hash.
    chunk_size
        Number of bytes read per chunk.

    Returns
    -------
    str
        Hexadecimal SHA256 digest.
    """
    file_path = Path(file_path)

    sha256 = hashlib.sha256()

    with file_path.open("rb") as handle:
        while chunk := handle.read(chunk_size):
            sha256.update(chunk)

    return sha256.hexdigest()