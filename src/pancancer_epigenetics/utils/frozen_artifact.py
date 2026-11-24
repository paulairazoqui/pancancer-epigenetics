"""Stage and verify writes to frozen artifacts."""

import os
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from stat import S_ISREG
from tempfile import TemporaryDirectory

from pancancer_epigenetics.utils.artifact_registry import (
    load_artifact_registry,
    resolve_artifact_path,
)
from pancancer_epigenetics.utils.file_checks import calculate_sha256
from pancancer_epigenetics.utils.paths import PROJECT_ROOT, Paths


@contextmanager
def frozen_artifact_output(
    output_path: Path,
    *,
    registry_path: Path = Paths.artifact_registry,
    root: Path = PROJECT_ROOT,
) -> Iterator[Path]:
    """Yield a staging path and publish it only if the frozen destination is absent."""
    root = root.resolve()
    destination = Path(os.path.abspath(output_path))
    registry = load_artifact_registry(registry_path)
    for artifact_id, entry in registry["artifacts"].items():
        if destination == root / entry["path"]:
            break
    else:
        raise ValueError(f"Unregistered frozen artifact path: {destination}")

    if resolve_artifact_path(registry, artifact_id, root) != destination:
        raise ValueError(f"Frozen artifact path resolves elsewhere: {destination}")

    def require_identity(path: Path, source: str) -> None:
        identity = path.lstat()
        if (
            not S_ISREG(identity.st_mode)
            or identity.st_size != entry["size_bytes"]
            or calculate_sha256(path) != entry["sha256"]
        ):
            raise ValueError(
                f"{source} identity differs for frozen artifact {artifact_id}"
            )

    try:
        require_identity(destination, "Existing file")
    except FileNotFoundError:
        original_exists = False
    else:
        original_exists = True

    with TemporaryDirectory(dir=destination.parent, prefix=".frozen-") as directory:
        candidate = Path(directory) / destination.name
        yield candidate
        require_identity(candidate, "Candidate")
        if not original_exists:
            # Windows rename is atomic and refuses an existing destination.
            # On POSIX a hard link provides the same no-replacement guarantee.
            try:
                if os.name == "nt":
                    candidate.rename(destination)
                else:
                    os.link(candidate, destination)
            except FileExistsError:
                require_identity(destination, "Existing file")
