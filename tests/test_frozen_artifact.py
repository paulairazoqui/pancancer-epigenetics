import json
import os
from hashlib import sha256

import pandas as pd
import pytest

from pancancer_epigenetics.utils.frozen_artifact import frozen_artifact_output
from pancancer_epigenetics.utils.paths import Paths


@pytest.fixture
def frozen_output(tmp_path, monkeypatch):
    raw_registry = tmp_path / "raw_data_registry.json"
    raw_registry.write_text("{}", encoding="utf-8")
    monkeypatch.setattr(Paths, "raw_data_registry", raw_registry)
    registry = tmp_path / "artifact_registry.json"

    def prepare(expected, existing=None, name="artifact.csv"):
        output = tmp_path / "outputs" / name
        output.parent.mkdir()
        entry = {
            "path": output.relative_to(tmp_path).as_posix(),
            "phase": 3,
            "status": "frozen",
            "artifact_role": "data",
            "producer": {"type": "notebook", "path": "notebooks/example.ipynb"},
            "size_bytes": len(expected),
            "sha256": sha256(expected).hexdigest(),
            "shape": None,
            "inputs": [],
        }
        registry.write_text(
            json.dumps({"schema_version": 1, "artifacts": {"example": entry}}),
            encoding="utf-8",
        )
        if existing is not None:
            output.write_bytes(existing)
        return output

    def stage(output):
        return frozen_artifact_output(output, registry_path=registry, root=tmp_path)

    yield prepare, stage
    assert not list(tmp_path.rglob(".frozen-*"))


def test_identical_candidate_keeps_existing_file(frozen_output):
    prepare, stage = frozen_output
    original = b"frozen"
    output = prepare(original, existing=original)
    os.utime(output, (1_700_000_000, 1_700_000_000))
    before = output.stat()

    with stage(output) as candidate:
        assert candidate.parent.parent == output.parent
        candidate.write_bytes(original)

    assert output.read_bytes() == original
    assert output.stat().st_mtime_ns == before.st_mtime_ns
    assert output.stat().st_ino == before.st_ino


@pytest.mark.parametrize("existing", [None, b"frozen"])
@pytest.mark.parametrize("incompatible", [b"wrong!", b"short"])
def test_different_candidate_is_rejected(frozen_output, existing, incompatible):
    prepare, stage = frozen_output
    output = prepare(b"frozen", existing=existing)

    with pytest.raises(ValueError, match="Candidate identity differs"):
        with stage(output) as candidate:
            candidate.write_bytes(incompatible)

    if existing is None:
        assert not output.exists()
    else:
        assert output.read_bytes() == existing


def test_wrong_existing_identity_is_rejected_before_serialization(frozen_output):
    prepare, stage = frozen_output
    output = prepare(b"frozen", existing=b"wrong!")

    with pytest.raises(ValueError, match="Existing file identity differs"):
        with stage(output):
            pytest.fail("The serializer ran with a mismatched existing file")

    assert output.read_bytes() == b"wrong!"


@pytest.mark.parametrize("error", [RuntimeError, OSError, KeyboardInterrupt])
def test_interrupted_serialization_keeps_original(frozen_output, error):
    prepare, stage = frozen_output
    output = prepare(b"frozen", existing=b"frozen")

    with pytest.raises(error, match="write interrupted"):
        with stage(output) as candidate:
            candidate.write_bytes(b"partial")
            raise error("write interrupted")

    assert output.read_bytes() == b"frozen"


@pytest.mark.parametrize("suffix", ["csv", "parquet", "json"])
def test_matching_serialization_publishes_missing_file(frozen_output, tmp_path, suffix):
    prepare, stage = frozen_output
    table = pd.DataFrame(
        {"gene": ["BRCA1", "BRCA2"], "value": [0.123456789012345, 2.0]}
    )

    def serialize(path):
        if suffix == "csv":
            table.to_csv(path, index=False)
        elif suffix == "parquet":
            table.to_parquet(path, index=False)
        else:
            with path.open("w", encoding="utf-8") as handle:
                json.dump({"shape": table.shape}, handle, indent=2)

    reference = tmp_path / f"reference.{suffix}"
    serialize(reference)
    expected = reference.read_bytes()
    output = prepare(expected, name=f"artifact.{suffix}")

    with stage(output) as candidate:
        assert not output.exists()
        serialize(candidate)

    assert output.read_bytes() == expected


def test_unregistered_path_is_rejected_before_serialization(frozen_output):
    prepare, stage = frozen_output
    registered = prepare(b"frozen", existing=b"frozen")
    unregistered = registered.with_name("unregistered.csv")
    unregistered.write_bytes(b"frozen")

    with pytest.raises(ValueError, match="Unregistered frozen artifact path"):
        with stage(unregistered):
            pytest.fail("The serializer ran for an unregistered destination")

    assert registered.read_bytes() == unregistered.read_bytes() == b"frozen"


@pytest.mark.parametrize("concurrent_bytes", [b"frozen", b"wrong!"])
def test_publish_preserves_file_created_during_serialization(
    frozen_output, concurrent_bytes
):
    prepare, stage = frozen_output
    output = prepare(b"frozen")

    def serialize():
        with stage(output) as candidate:
            candidate.write_bytes(b"frozen")
            output.write_bytes(concurrent_bytes)

    if concurrent_bytes == b"frozen":
        serialize()
    else:
        with pytest.raises(ValueError, match="Existing file identity differs"):
            serialize()

    assert output.read_bytes() == concurrent_bytes
