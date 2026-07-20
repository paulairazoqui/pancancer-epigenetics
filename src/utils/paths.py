"""
utils/paths.py – Project path resolution.
Import from any script: from src.utils.paths import Paths
"""

from pathlib import Path

from src.utils.file_checks import to_project_relative_posix_path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def load_paths() -> dict:
    """Load the repository path configuration.

    The project path file intentionally uses a small YAML subset: nested mapping
    keys with string values. Keeping the parser local avoids requiring notebooks
    and lightweight validation commands to import an external YAML dependency.
    """

    config_file = PROJECT_ROOT / "config" / "paths.yaml"
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]

    for raw_line in config_file.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        key, separator, value = raw_line.strip().partition(":")
        if not separator:
            raise ValueError(f"Invalid path configuration line: {raw_line}")

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]
        value = value.strip()
        if value:
            parent[key] = value
        else:
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))

    return root


class Paths:
    root = PROJECT_ROOT
    _cfg = load_paths()

    # configuration
    config = root / "config"
    paths_config = config / "paths.yaml"
    raw_data_registry = config / "raw_data_registry.json"

    # raw source datasets
    depmap = root / _cfg["data"]["raw"]["depmap"]
    gdsc = root / _cfg["data"]["raw"]["gdsc"]
    ctrp = root / _cfg["data"]["raw"]["ctrp"]
    prism = root / _cfg["data"]["raw"]["prism"]
    tcga = root / _cfg["data"]["raw"]["tcga"]
    lincs = root / _cfg["data"]["raw"]["lincs"]
    cell_model_passports = root / _cfg["data"]["raw"]["cell_model_passports"]
    chembl = root / _cfg["data"]["raw"]["chembl"]
    drugbank = root / _cfg["data"]["raw"]["drugbank"]

    # interim analysis-ready inputs
    interim = root / _cfg["data"]["interim"]["root"]
    metadata = root / _cfg["data"]["interim"]["metadata"]
    expression = root / _cfg["data"]["interim"]["expression"]
    methylation = root / _cfg["data"]["interim"]["methylation"]
    dependencies = root / _cfg["data"]["interim"]["dependencies"]
    pharmacology = root / _cfg["data"]["interim"]["pharmacology"]
    perturbational = root / _cfg["data"]["interim"]["perturbational"]
    qc = root / _cfg["data"]["interim"]["qc"]

    # processed biological entities and analytical outputs
    tumor_programs = root / _cfg["data"]["processed"]["tumor_programs"]
    cellline_programs = root / _cfg["data"]["processed"]["cellline_programs"]
    consensus_programs = root / _cfg["data"]["processed"]["consensus_programs"]
    functional_vulnerabilities = root / _cfg["data"]["processed"]["functional_vulnerabilities"]
    pharmacogenomic_contexts = root / _cfg["data"]["processed"]["pharmacogenomic_contexts"]
    perturbational_hypotheses = root / _cfg["data"]["processed"]["perturbational_hypotheses"]
    validation = root / _cfg["data"]["processed"]["validation"]

    # manuscript-ready results
    paper1 = root / _cfg["results"]["paper1"]
    paper2 = root / _cfg["results"]["paper2"]
    supplementary = root / _cfg["results"]["supplementary"]

    # backward-compatible audit alias
    audit = qc


def project_relative_path(path: Path) -> str:
    """Return a portable project-relative path."""
    return to_project_relative_posix_path(
        path,
        PROJECT_ROOT,
    )


def find_repo_root(start_path: Path = Path.cwd()) -> Path:
    current = start_path.resolve()
    while current != current.parent:
        if (current / "src").is_dir() and (current / "config").is_dir():
            return current
        current = current.parent
    raise FileNotFoundError("Repository root not found from %s" % start_path)