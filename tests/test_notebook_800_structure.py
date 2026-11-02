"""Static guards for the Phase 8 input-readiness notebook.

These checks do not read source payloads or evaluate biological outcomes.
"""

import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = (
    ROOT
    / "notebooks"
    / "phase8_orthogonal_validation"
    / "800_external_bulk_cohorts.ipynb"
)


def _cells():
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    return notebook["cells"]


def test_phase8_notebook_code_cells_parse_individually():
    for index, cell in enumerate(_cells(), start=1):
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        ast.parse(source, filename=f"{NOTEBOOK.name}:cell-{index}")


def test_phase8_code_cells_have_single_focused_scope():
    for cell in _cells():
        if cell["cell_type"] != "code":
            continue
        lines = "".join(cell["source"]).splitlines()
        assert len(lines) <= 50, (cell["id"], len(lines))
        assert all(len(line) <= 88 for line in lines), cell["id"]


def test_phase8_notebook_narrates_analysis_not_development_history():
    markdown = "\n".join(
        "".join(cell["source"])
        for cell in _cells()
        if cell["cell_type"] == "markdown"
    ).casefold()
    for word in ("migration", "historical", "original 800", "old 800"):
        assert word not in markdown


def test_phase8_notebook_has_distinct_full_source_and_cohort_scopes():
    code = "\n".join(
        "".join(cell["source"])
        for cell in _cells()
        if cell["cell_type"] == "code"
    )
    assert "E_SCAN_PERFORMED" in code
    assert "e_frozen_exact" in code
    assert "source_112" in code
    assert "n_proposed_source_cases" in code
    assert '"cohort_frozen": False' in code
    assert '"biological_replication_executed": False' in code
