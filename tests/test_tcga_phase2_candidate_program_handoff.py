import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config/program_handoffs/tcga_phase2_candidate_program_handoff.csv"

EXPECTED_IDENTITIES = {
    "CROSS_OMIC_PAIR_02": ("RNA_IC083", "METH_IC232"),
    "CROSS_OMIC_PAIR_03": ("RNA_IC184", "METH_IC169"),
    "CROSS_OMIC_PAIR_04": ("RNA_IC150", "METH_IC128"),
    "CROSS_OMIC_PAIR_05": ("RNA_IC169", "METH_IC023"),
    "CROSS_OMIC_PAIR_06": ("RNA_IC175", "METH_IC013"),
    "CROSS_OMIC_PAIR_07": ("RNA_IC050", "METH_IC234"),
    "CROSS_OMIC_PAIR_08": ("RNA_IC151", "METH_IC050"),
    "CROSS_OMIC_PAIR_09": ("RNA_IC001", "METH_IC107"),
    "CROSS_OMIC_PAIR_10": ("RNA_IC001", "METH_IC241"),
    "CROSS_OMIC_PAIR_11": ("RNA_IC193", "METH_IC109"),
    "CROSS_OMIC_PAIR_12": ("RNA_IC184", "METH_IC128"),
    "CROSS_OMIC_PAIR_13": ("RNA_IC193", "METH_IC033"),
    "CROSS_OMIC_PAIR_14": ("RNA_IC158", "METH_IC013"),
}

EXPECTED_FAMILIES = {
    "PF01": {"CROSS_OMIC_PAIR_03", "CROSS_OMIC_PAIR_04", "CROSS_OMIC_PAIR_12"},
    "PF02": {"CROSS_OMIC_PAIR_06", "CROSS_OMIC_PAIR_14"},
    "PF03": {"CROSS_OMIC_PAIR_09", "CROSS_OMIC_PAIR_10"},
    "PF04": {"CROSS_OMIC_PAIR_11", "CROSS_OMIC_PAIR_13"},
    "PF05": {"CROSS_OMIC_PAIR_02"},
    "PF06": {"CROSS_OMIC_PAIR_05"},
    "PF07": {"CROSS_OMIC_PAIR_07"},
    "PF08": {"CROSS_OMIC_PAIR_08"},
}

EXPECTED_INTERPRETATIONS = {
    "CROSS_OMIC_PAIR_02": ("HIGH_PRIORITY_CANDIDATE", "HIGH", "SUPPORTED", "STATE_EXTREME_NONLINEAR"),
    "CROSS_OMIC_PAIR_03": ("METHOD_LIMITED", "CONDITIONAL_HIGH", "NOT_EVALUABLE", "CONTINUOUS_ASSOCIATION_HYPOTHESIS"),
    "CROSS_OMIC_PAIR_04": ("CONFOUNDED", "LOW", "SUPPORTED_SMALL_EFFECT", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_05": ("METHOD_LIMITED", "MEDIUM", "NOT_EVALUABLE", "CONTINUOUS_ASSOCIATION"),
    "CROSS_OMIC_PAIR_06": ("METHOD_LIMITED", "MEDIUM_LOW", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_07": ("METHOD_LIMITED", "MEDIUM", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_08": ("METHOD_LIMITED", "MEDIUM", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_09": ("METHOD_LIMITED", "MEDIUM_LOW", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_10": ("METHOD_LIMITED", "MEDIUM", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_11": ("METHOD_LIMITED", "LOW", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_12": ("CONFOUNDED", "LOW_CONDITIONAL", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_13": ("TECHNICAL_SIGNAL", "LOW", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
    "CROSS_OMIC_PAIR_14": ("CONFOUNDED", "LOW", "NOT_EVALUABLE", "NO_RECURRENT_NONLINEAR_RELATIONSHIP_IDENTIFIED"),
}

EXPECTED_COLUMNS = [
    "candidate_pair",
    "rna_component",
    "methylation_component",
    "structural_family",
    "final_audit_status",
    "scientific_priority",
    "strict_hm27_status",
    "relationship_form",
    "primary_limitation",
    "consensus_handling",
    "source_provenance",
]


def test_tcga_phase2_candidate_program_handoff_contract() -> None:
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    assert reader.fieldnames == EXPECTED_COLUMNS
    assert len(rows) == 13

    by_pair = {row["candidate_pair"]: row for row in rows}
    assert len(by_pair) == 13
    assert set(by_pair) == set(EXPECTED_IDENTITIES)

    actual_identities = {
        pair: (row["rna_component"], row["methylation_component"])
        for pair, row in by_pair.items()
    }
    assert actual_identities == EXPECTED_IDENTITIES

    actual_families = {
        family: {row["candidate_pair"] for row in rows if row["structural_family"] == family}
        for family in {row["structural_family"] for row in rows}
    }
    assert actual_families == EXPECTED_FAMILIES
    assert len(actual_families) == 8

    assert all(row["structural_family"] for row in rows)
    assert all(row["final_audit_status"] for row in rows)
    actual_interpretations = {
        pair: (
            row["final_audit_status"],
            row["scientific_priority"],
            row["strict_hm27_status"],
            row["relationship_form"],
        )
        for pair, row in by_pair.items()
    }
    assert actual_interpretations == EXPECTED_INTERPRETATIONS
    assert all(row["source_provenance"] for row in rows)

    pair_02 = by_pair["CROSS_OMIC_PAIR_02"]
    assert pair_02["relationship_form"] == "STATE_EXTREME_NONLINEAR"
    assert "uniform linear gradient" in pair_02["consensus_handling"]
    assert "demonstrated discrete subtype" in pair_02["consensus_handling"]
