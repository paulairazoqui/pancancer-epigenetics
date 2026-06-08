"""
utils/paths.py – Project path resolution.
Import from any script: from src.utils.paths import Paths
"""

from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def load_paths() -> dict:
    config_file = PROJECT_ROOT / "config" / "paths.yaml"
    with open(config_file) as f:
        return yaml.safe_load(f)

class Paths:
    root = PROJECT_ROOT
    _cfg = load_paths()

    # raw
    depmap   = root / _cfg["data"]["raw"]["depmap"]
    gdsc     = root / _cfg["data"]["raw"]["gdsc"]
    prism    = root / _cfg["data"]["raw"]["prism"]
    lincs    = root / _cfg["data"]["raw"]["lincs_cmap"]
    tcga     = root / _cfg["data"]["raw"]["tcga_gdc"]

    # processed
    merged     = root / _cfg["data"]["processed"]["merged"]
    splits     = root / _cfg["data"]["processed"]["splits"]
    signatures = root / _cfg["data"]["processed"]["signatures"]

    # audit
    audit = root / _cfg["data"]["audit"]

    # results
    figures      = root / _cfg["results"]["figures"]
    tables       = root / _cfg["results"]["tables"]
    models       = root / _cfg["results"]["models"]
    drug_ranking = root / _cfg["results"]["drug_ranking"]
