import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

NOTEBOOK = (
    Path(__file__).resolve().parents[1]
    / "notebooks/phase4b_secondary_molecular_characterization"
    / "451_locus_level_methylation_expression_characterization.ipynb"
)


@pytest.mark.parametrize(
    ("column", "replacement", "error"),
    [
        (None, None, None),
        ("estimate", 0.26, "within_project: estimate"),
        ("p_value", 0.0, "within_project: p_value"),
        ("q_value", 2e-190, "within_project: q_value"),
        ("supported", False, "within_project non-floating values"),
        ("annotation", "001", "within_project non-floating values"),
        ("count", 2**53, "within_project non-floating values"),
    ],
)
def test_451_verification_checks_values_before_publication(
    tmp_path, column, replacement, error
):
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    source = next(
        "".join(cell["source"])
        for cell in notebook["cells"]
        if "# Verify persisted notebook-451 outputs\n" in cell["source"]
    )
    pair_key = ["probe_id", "rna_gene_id_base"]
    frame = pd.DataFrame(
        {
            "probe_id": ["cg01", "cg02"],
            "rna_gene_id_base": ["ENSG001", None],
            "estimate": [0.25, np.nan],
            "p_value": [1e-200, np.nan],
            "q_value": pd.array([1e-190, pd.NA], dtype="Float64"),
            "supported": pd.array([True, pd.NA], dtype="boolean"),
            "annotation": pd.Categorical(["NA", None]),
            "count": pd.array([2**53 + 1, pd.NA], dtype="Int64"),
        },
        index=[8, 3],
    )
    output_objects = {
        "annotation_eligibility": frame.assign(annotation_gene_id_base="ENSG001"),
        "primary_associations": frame,
        "within_project": frame.assign(project_id="project-a"),
        "lopo": frame.assign(omitted_project_id="project-a"),
        "sensitivities": frame.assign(sensitivity_type="purity"),
        "final_evidence": frame,
    }

    def calculate_sha256(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    output_paths = {}
    outputs = {}
    for name, expected in output_objects.items():
        path = tmp_path / f"{name}.csv"
        persisted = expected.copy()
        if error and name == "within_project":
            if column == "annotation":
                persisted[column] = persisted[column].astype("string")
            persisted.loc[8, column] = replacement
        csv = persisted.to_csv(index=False).replace("1e-200", "1.0000000000000000e-200")
        path.write_text(csv, encoding="utf-8")
        output_paths[name] = path
        # Match the written bytes even when a non-key value was corrupted.
        outputs[name] = {"sha256": calculate_sha256(path)}

    analysis_metadata = {
        "outputs": outputs,
        "upstream_artifacts": {
            "phase2.205.rna_program_discovery_gene_metadata": {},
            "phase2.205.rna_program_discovery_sample_metadata": {},
        },
    }
    metadata_path = tmp_path / "metadata.json"
    metadata_path.write_text(json.dumps(analysis_metadata), encoding="utf-8")
    env = {
        "pd": pd,
        "np": np,
        "json": json,
        "pair_key": pair_key,
        "output_paths": output_paths,
        "output_objects": output_objects,
        "analysis_metadata": analysis_metadata,
        "metadata_path": metadata_path,
        "calculate_sha256": calculate_sha256,
    }
    verification = compile(source, str(NOTEBOOK), "exec")
    if error:
        with pytest.raises(AssertionError, match=error):
            exec(verification, env)
        assert output_paths["within_project"] not in env["verified_outputs"]
    else:
        exec(verification, env)
        assert env["verified_outputs"] == {
            **{path: output_objects[name].shape for name, path in output_paths.items()},
            metadata_path: None,
        }
