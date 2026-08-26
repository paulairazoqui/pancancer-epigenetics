import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REQUIREMENTS_PATH = PROJECT_ROOT / "requirements.txt"
ENVIRONMENT_PATH = PROJECT_ROOT / "envs" / "environment.yml"
PYTHON_SNAPSHOT_PATH = PROJECT_ROOT / "envs" / "python_environment_snapshot.txt"
R_MANIFEST_PATH = PROJECT_ROOT / "envs" / "r_environment.json"


def _canonical_name(name: str) -> str:
    return re.sub(r"[-_.]+", "-", name).lower()


def _requirements() -> dict[str, str]:
    requirements = {}
    for line in REQUIREMENTS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        match = re.fullmatch(r"([A-Za-z0-9_.-]+)==([^\s]+)", line)
        assert match, f"requirement must use an exact pin: {line}"
        name = _canonical_name(match.group(1))
        assert name not in requirements, f"duplicate requirement: {name}"
        requirements[name] = match.group(2)
    return requirements


def _environment_pip_dependencies() -> dict[str, str]:
    dependencies = {}
    in_pip_section = False
    for line in ENVIRONMENT_PATH.read_text(encoding="utf-8").splitlines():
        if line == "  - pip:":
            in_pip_section = True
            continue
        if in_pip_section:
            match = re.fullmatch(r"\s{6}- ([A-Za-z0-9_.-]+)==([^\s]+)", line)
            if not match:
                continue
            name = _canonical_name(match.group(1))
            assert name not in dependencies, f"duplicate environment dependency: {name}"
            dependencies[name] = match.group(2)
    return dependencies


def test_direct_python_dependency_contracts_are_identical():
    assert _environment_pip_dependencies() == _requirements()


def test_stale_environment_only_dependencies_are_absent():
    packages = _requirements()
    for package in ("fastparquet", "lifelines", "shap", "tqdm", "xgboost"):
        assert package not in packages


def test_environment_manifests_are_present_and_structured():
    snapshot = PYTHON_SNAPSHOT_PATH.read_text(encoding="utf-8")
    assert "scope: current_reproduction_environment" in snapshot
    assert "historical_execution_claim: false" in snapshot
    assert re.search(r"(?m)^pip==[^\s]+$", snapshot)

    manifest = json.loads(R_MANIFEST_PATH.read_text(encoding="utf-8"))
    assert manifest["schema_version"] == 1
    assert manifest["scope"] == "current_reproduction_environment"
    assert manifest["historical_execution_claim"] is False
    assert set(manifest["packages"]) == {
        "edgeR",
        "rhdf5",
        "minfi",
        "IlluminaHumanMethylation450kanno.ilmn12.hg19",
    }
