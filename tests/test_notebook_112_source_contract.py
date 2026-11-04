"""Static source, dependency and downstream-interface tests for Notebook 112."""

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = (
    ROOT
    / "notebooks/phase1_data_acquisition_and_auditing"
    / "112_cptac3_qc_source_provenance.ipynb"
)
EVIDENCE = ROOT / "docs/evidence/phase1/notebook112"


def _notebook_code() -> list[str]:
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    return [
        "".join(cell["source"])
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    ]


def _snapshot(name: str) -> dict:
    return json.loads((EVIDENCE / name).read_text(encoding="utf-8"))


def _query_digest(payload: dict) -> str:
    query = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(query).hexdigest()


def test_notebook_112_all_code_cells_parse() -> None:
    code_cells = _notebook_code()
    assert len(code_cells) >= 18
    for index, source in enumerate(code_cells, start=1):
        ast.parse(source, filename=f"notebook112:cell{index}")


def test_notebook_112_has_upstream_only_dependencies() -> None:
    text = "\n".join(_notebook_code())
    assert "111_cptac3_acquisition_audit_summary.json" in text
    assert "111_cptac3_file_index.csv" in text
    assert "111_cptac3_provisional_primary_tumor_files.csv" in text
    assert "112_gdc_star_output_pilot_snapshot.json" in text
    assert "112_gdc_upstream_input_pilot_snapshot.json" in text
    assert "112_cptac3_rna_simple_primary_technical_inventory.csv" in text
    assert "112_cptac3_qc_provenance_handoff.json" in text
    assert '"technical_inventory"' in text
    assert "calculate_sha256(SCAN_OUTPUT)" in text
    assert "800_preflight_" not in text
    assert "113_proposed_external_source_cohort.csv" not in text
    assert "requests.Session(" not in text
    assert "session.post(" not in text
    assert '"PUBLIC_GDC_FILE_METADATA_ONLY"' not in text
    assert '"AUDITED_LOCAL_STAR_COUNTS_AND_VERSIONED_GDC_METADATA"' in text


def test_notebook_112_versioned_snapshot_provenance() -> None:
    star_path = EVIDENCE / "112_gdc_star_output_pilot_snapshot.json"
    star = _snapshot(star_path.name)
    upstream = _snapshot("112_gdc_upstream_input_pilot_snapshot.json")

    assert len(star["hits"]) == 12
    assert len(upstream["hits"]) == 12
    assert len(upstream["requested_input_file_ids"]) == 12

    star_hash = hashlib.sha256(star_path.read_bytes()).hexdigest()
    assert upstream["upstream_H_snapshot_sha256"] == star_hash
    assert star["query_sha256"] == _query_digest(star["query"])
    assert upstream["query_sha256"] == _query_digest(upstream["query"])

    star_ids = {hit["file_id"] for hit in star["hits"]}
    assert star_ids == set(star["query"]["filters"]["content"]["value"])
    upstream_ids = {hit["file_id"] for hit in upstream["hits"]}
    assert upstream_ids == set(upstream["requested_input_file_ids"])
