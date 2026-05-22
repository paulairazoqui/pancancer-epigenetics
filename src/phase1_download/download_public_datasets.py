"""
download_public_datasets.py
Fase 1 - Descarga/auditoria reproducible de datasets publicos.

Uso:
    python download_public_datasets.py
    python download_public_datasets.py --dataset gdsc_ic50
    python download_public_datasets.py --audit-only
"""

import argparse
import hashlib
import json
import logging
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from tqdm import tqdm


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


DATASETS = {
    "depmap_model": {
        "name": "DepMap model metadata",
        "source": "DepMap/Broad",
        "subdir": "depmap",
        "version": "DepMap Public 25Q3",
        "download_mode": "manual",
        "portal_url": "https://depmap.org/portal/data_page/?tab=allData&releasename=DepMap%20Public%2025Q3&filename=Model.csv",
        "filename": "Model.csv",
        "min_size_mb": 0.1,
        "expected_sha256": None,
        "license": "DepMap data terms",
        "citation": "DepMap, Broad (2025). DepMap Public 25Q3. Dataset. depmap.org",
        "description": "Metadata describing cancer models/cell lines.",
    },
    "depmap_omics_profiles": {
        "name": "DepMap omics profiles",
        "source": "DepMap/Broad",
        "subdir": "depmap",
        "version": "DepMap Public 25Q3",
        "download_mode": "manual",
        "portal_url": "https://depmap.org/portal/data_page/?tab=allData&releasename=DepMap%20Public%2025Q3&filename=OmicsProfiles.csv",
        "filename": "OmicsProfiles.csv",
        "min_size_mb": 0.1,
        "expected_sha256": None,
        "license": "DepMap data terms",
        "citation": "DepMap, Broad (2025). DepMap Public 25Q3. Dataset. depmap.org",
        "description": "Omics metadata and ID mapping information.",
    },
    "depmap_expression": {
        "name": "DepMap expression TPM log1p human protein-coding genes",
        "source": "DepMap/Broad",
        "subdir": "depmap",
        "version": "DepMap Public 25Q3",
        "download_mode": "manual",
        "portal_url": "https://depmap.org/portal/data_page/?tab=allData&releasename=DepMap%20Public%2025Q3&filename=OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv",
        "filename": "OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv",
        "min_size_mb": 500.0,
        "expected_sha256": None,
        "license": "DepMap data terms",
        "citation": "DepMap, Broad (2025). DepMap Public 25Q3. Dataset. depmap.org",
        "description": "Log-transformed TPM values for human protein-coding genes. Columns include ProfileID, is_default_entry, ModelID, then genes.",
    },
    "depmap_mutations": {
        "name": "DepMap somatic mutations",
        "source": "DepMap/Broad",
        "subdir": "depmap",
        "version": "DepMap Public 25Q3",
        "download_mode": "manual",
        "portal_url": "https://depmap.org/portal/data_page/?tab=allData&releasename=DepMap%20Public%2025Q3&filename=OmicsSomaticMutations.csv",
        "filename": "OmicsSomaticMutations.csv",
        "min_size_mb": 500.0,
        "expected_sha256": None,
        "license": "DepMap data terms",
        "citation": "DepMap, Broad (2025). DepMap Public 25Q3. Dataset. depmap.org",
        "description": "MAF-like somatic mutation file.",
    },
    "gdsc_ic50": {
        "name": "GDSC2 fitted dose-response",
        "source": "GDSC/Sanger",
        "subdir": "gdsc",
        "version": "8.5",
        "download_mode": "auto",
        "url": "https://cog.sanger.ac.uk/cancerrxgene/GDSC_release8.5/GDSC2_fitted_dose_response_27Oct23.xlsx",
        "filename": "GDSC2_fitted_dose_response_27Oct23.xlsx",
        "min_size_mb": 20.0,
        "expected_sha256": "f950a7027be265f8a7a74220a27fd18cbd368485349bd8c2048e88bb1cd07560",
        "license": "CC BY 4.0",
        "citation": "Yang et al. (2012) NAR; Iorio et al. (2016) Cell.",
        "description": "Drug sensitivity data. Includes LN_IC50 and AUC.",
    },
}


def compute_sha256(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def download_file(url: str, dest: Path, min_size_mb: float, retries: int = 3) -> bool:
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".tmp")

    headers = {"User-Agent": "Mozilla/5.0 research-downloader"}

    for attempt in range(1, retries + 1):
        try:
            log.info(f"Intento {attempt}/{retries}: {url}")
            r = requests.get(url, stream=True, timeout=180, headers=headers)
            r.raise_for_status()

            content_type = r.headers.get("content-type", "")
            if any(x in content_type.lower() for x in ["text/html", "application/json", "application/xml"]):
                log.error(f"Respuesta no válida. Content-Type: {content_type}")
                return False

            total = int(r.headers.get("content-length", 0))

            with open(tmp, "wb") as f, tqdm(
                total=total or None,
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                desc=dest.name[:40],
            ) as bar:
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
                        bar.update(len(chunk))

            size_mb = tmp.stat().st_size / 1e6
            if size_mb < min_size_mb:
                tmp.unlink(missing_ok=True)
                log.error(f"Archivo demasiado pequeño: {size_mb:.2f} MB < {min_size_mb} MB")
                return False

            tmp.replace(dest)
            return True

        except Exception as e:
            tmp.unlink(missing_ok=True)
            log.warning(f"Error: {e}")
            if attempt < retries:
                time.sleep(10)

    return False


def build_record(key: str, meta: dict, path: Path, status: str) -> dict:
    record = {
        "key": key,
        "name": meta["name"],
        "source": meta["source"],
        "version": meta["version"],
        "download_mode": meta["download_mode"],
        "filename": meta["filename"],
        "path": str(path),
        "license": meta["license"],
        "citation": meta["citation"],
        "description": meta["description"],
        "portal_url": meta.get("portal_url"),
        "url": meta.get("url"),
        "status": status,
        "sha256": None,
        "size_bytes": None,
        "audited_at": datetime.now(timezone.utc).isoformat(),
    }

    if path.exists():
        record["sha256"] = compute_sha256(path)
        record["size_bytes"] = path.stat().st_size

    return record


def process_dataset(key: str, meta: dict, output_dir: Path, audit_only: bool) -> dict:
    path = output_dir / meta["subdir"] / meta["filename"]
    min_size_mb = meta["min_size_mb"]

    if meta["download_mode"] == "manual":
        if not path.exists():
            log.warning(f"[{key}] Falta archivo manual: {path}")
            log.warning(f"Descargar desde: {meta['portal_url']}")
            return build_record(key, meta, path, "missing_manual_download")

        size_mb = path.stat().st_size / 1e6
        if size_mb < min_size_mb:
            log.error(f"[{key}] Archivo demasiado pequeño: {size_mb:.2f} MB")
            return build_record(key, meta, path, "too_small")

        log.info(f"[{key}] OK manual auditado: {path} ({size_mb:.2f} MB)")
        return build_record(key, meta, path, "verified_manual")

    if meta["download_mode"] == "auto":
        if path.exists():
            size_mb = path.stat().st_size / 1e6
            h = compute_sha256(path)
            expected = meta.get("expected_sha256")

            if size_mb >= min_size_mb and (not expected or h == expected):
                log.info(f"[{key}] Ya existe y es válido: {path}")
                return build_record(key, meta, path, "already_exists")

            log.warning(f"[{key}] Existe, pero no pasa validación. Se descargará de nuevo.")

        if audit_only:
            log.warning(f"[{key}] No se descarga porque audit_only=True")
            return build_record(key, meta, path, "missing_auto_download")

        ok = download_file(meta["url"], path, min_size_mb=min_size_mb)
        if not ok:
            return build_record(key, meta, path, "download_failed")

        expected = meta.get("expected_sha256")
        if expected and compute_sha256(path) != expected:
            log.error(f"[{key}] Hash incorrecto.")
            return build_record(key, meta, path, "hash_mismatch")

        log.info(f"[{key}] Descarga OK: {path}")
        return build_record(key, meta, path, "downloaded")

    raise ValueError(f"download_mode no reconocido: {meta['download_mode']}")


def load_manifest(path: Path) -> dict:
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {"created_at": datetime.now(timezone.utc).isoformat(), "downloads": {}}


def save_manifest(manifest: dict, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    manifest["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    log.info(f"Manifiesto guardado: {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=list(DATASETS.keys()) + ["all"], default="all")
    parser.add_argument("--output-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--audit-dir", type=Path, default=Path("data/audit"))
    parser.add_argument("--audit-only", action="store_true")
    args = parser.parse_args()

    targets = DATASETS if args.dataset == "all" else {args.dataset: DATASETS[args.dataset]}
    manifest_path = args.audit_dir / "download_manifest.json"
    manifest = load_manifest(manifest_path)

    summary = {"ok": 0, "failed": 0, "missing": 0}

    for key, meta in targets.items():
        record = process_dataset(key, meta, args.output_dir, args.audit_only)
        manifest["downloads"][key] = record

        if record["status"] in ["verified_manual", "already_exists", "downloaded"]:
            summary["ok"] += 1
        elif "missing" in record["status"]:
            summary["missing"] += 1
        else:
            summary["failed"] += 1

        save_manifest(manifest, manifest_path)

    log.info("=" * 60)
    log.info(f"OK: {summary['ok']}")
    log.info(f"Missing: {summary['missing']}")
    log.info(f"Failed: {summary['failed']}")
    log.info("=" * 60)

    if summary["failed"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()