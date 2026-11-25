import ast
import json
from functools import partial
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd
import pytest
from statsmodels.stats.multitest import multipletests

from pancancer_epigenetics import analysis_parameters
from pancancer_epigenetics.utils import artifact_registry
from pancancer_epigenetics.utils.file_checks import calculate_sha256

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = ROOT / "notebooks/phase6_pharmacogenomic_contexts"
PROGRAM_IDS = ("P2", "P1")
CATALOG_ID = "phase4.401.consensus_transcriptomic_program_catalog"


def notebook(number):
    path = next(NOTEBOOKS.glob(f"{number}_*.ipynb"))
    return path.relative_to(ROOT).as_posix(), [
        "".join(cell["source"]) for cell in json.loads(path.read_bytes())["cells"]
    ]


def run_cells(number, indices, env):
    path, cells = notebook(number)
    for index in indices:
        exec(compile(cells[index], f"{path} cell {index}", "exec"), env)


@pytest.fixture
def catalog(tmp_path, monkeypatch):
    catalog_path = tmp_path / "catalog.csv"
    catalog_path.write_text(
        "consensus_program_id,tumor_rna_axis,cell_line_program,orientation_multiplier\n"
        "P2,T2,C2,-1\nP1,T1,C1,1\n",
        encoding="utf-8",
    )
    entry = artifact_registry.load_artifact_registry()["artifacts"][CATALOG_ID]
    registry_path = tmp_path / "catalog_registry.json"
    registry_path.write_text(
        json.dumps(
            {
                "schema_version": 1,
                "artifacts": {
                    CATALOG_ID: {**entry, "path": catalog_path.name, "inputs": []}
                },
            }
        ),
        encoding="utf-8",
    )
    load_programs = partial(
        analysis_parameters.load_consensus_programs,
        root=tmp_path,
        registry_path=registry_path,
    )
    monkeypatch.setattr(analysis_parameters, "load_consensus_programs", load_programs)
    return {
        "align_program_columns": analysis_parameters.align_program_columns,
        "attribution_column": analysis_parameters.attribution_column,
        "load_consensus_programs": load_programs,
        "score_column": analysis_parameters.score_column,
        "np": np,
        "pd": pd,
        "json": json,
        "display": lambda *_: None,
    }


def test_600_transports_anchor_projection_and_preserves_model_ids(catalog, tmp_path):
    expression = np.array([[1.0, 0], [3, 1], [0, 3], [2, 4]])
    model_ids = ["M4", "M1", "M2", "M3"]
    weights = np.array([[-0.6, 0.2], [0.4, 0.8]])  # Already oriented.
    mean = expression.mean(axis=0)
    std = expression.std(axis=0, ddof=1)
    projected = ((expression - mean) / std) @ weights
    center = projected.mean(axis=0)
    scale = projected.std(axis=0, ddof=1)
    anchor_values = (projected - center) / scale
    cohort = pd.DataFrame({"ModelID": model_ids[::-1], "OncotreeLineage": "L"})
    anchor = pd.DataFrame(
        {"P1": anchor_values[:, 1], "ModelID": model_ids, "P2": anchor_values[:, 0]}
    )

    def write(name, frame):
        path = tmp_path / name
        if path.suffix == ".parquet":
            frame.to_parquet(path, index=False)
        else:
            frame.to_csv(path, index=False)
        return path

    catalog["upstream_artifact_paths"] = {
        "phase3.302.integrated_modeling_cohort": write("cohort.csv", cohort),
        "phase4.401.consensus_cellline_scores": write("scores.parquet", anchor),
        "phase3.303.harmonized_expression": write(
            "expression.parquet",
            pd.DataFrame(expression, columns=["g0", "g1"]).assign(ModelID=model_ids),
        ),
        "phase4.400.cross_system_shared_gene_universe": write(
            "universe.csv",
            pd.DataFrame(
                {"gene_symbol": ["a", "b"], "cell_line_gene_id": ["g0", "g1"]}
            ),
        ),
        "phase4.401.consensus_transcriptomic_gene_weights": write(
            "weights.csv",
            pd.DataFrame(
                {
                    "gene_symbol": ["a", "a", "b", "b"],
                    "consensus_program_id": ["P1", "P2", "P1", "P2"],
                    "consensus_weight": weights[:, ::-1].ravel(),
                }
            ),
        ),
    }
    external = np.array([[30.0, 60.0], [-5.0, 3.0]])
    external_ids = ["E2", "E1"]
    write(
        "OmicsExpressionProteinCodingGenesTPMLogp1.csv",
        pd.DataFrame(external, columns=["g0", "g1"]).assign(
            **{"Unnamed: 0": external_ids}
        ),
    )
    write(
        "Model.csv",
        pd.DataFrame({"ModelID": external_ids, "OncotreeLineage": ["L2", "L3"]}),
    )
    catalog.update(
        Paths=SimpleNamespace(depmap=tmp_path),
        external_expression_union_ids=set(external_ids),
    )
    run_cells(600, [5, 6, 7, 17, 21, 22, 64], catalog)
    assert catalog["PROGRAM_COLUMNS"] == list(PROGRAM_IDS)
    scores = catalog["phase6_program_score_universe"].set_index("ModelID")
    np.testing.assert_array_equal(
        scores.loc[model_ids, list(PROGRAM_IDS)], anchor_values
    )
    np.testing.assert_allclose(
        scores.loc[external_ids, list(PROGRAM_IDS)],
        ((((external - mean) / std) @ weights) - center) / scale,
    )
    assert scores.loc[model_ids, "score_origin"].eq("frozen_phase4").all()
    assert (
        scores.loc[external_ids, "score_origin"]
        .eq("projected_from_frozen_phase4")
        .all()
    )


def test_600_requires_the_complete_gdsc_family(catalog):
    catalog.update(
        program_ids=PROGRAM_IDS,
        PROGRAM_COLUMNS=list(PROGRAM_IDS),
        phase6_score_universe=pd.DataFrame(
            {"ModelID": ["M2", "M1"], "P1": [2, 1], "P2": [3, 4]}
        ),
        gdsc_primary_universe=pd.DataFrame(
            {
                "DRUG_ID": [11, 29],
                "ModelID": ["M1", "M2"],
                "response_value": [3.0, -2.5],
                "OncotreeLineage": ["L1", "L2"],
            }
        ),
        gdsc_eligibility=pd.DataFrame(
            {"DRUG_ID": [29, 11, 53], "eligible": [True, True, False]}
        ),
    )
    run_cells(600, [42], catalog)
    keys = catalog["gdsc_hypothesis_keys"].to_frame(index=False)
    assert list(keys.itertuples(index=False, name=None)) == [
        (29, "P2"),
        (29, "P1"),
        (11, "P2"),
        (11, "P1"),
    ]
    validate = catalog["validate_gdsc_hypothesis_family"]
    validate(keys.iloc[::-1])
    for bad in (
        keys.iloc[:-1],
        pd.concat([keys.iloc[:-1], keys.iloc[[0]]]),
        keys.assign(program=["P2", "P1", "P2", "P3"]),
        keys.assign(DRUG_ID=[29, 29, 11, 53]),
    ):
        with pytest.raises(ValueError, match="complete eligible"):
            validate(bad)
    assert catalog["gdsc_primary_analysis"]["ModelID"].tolist() == ["M1", "M2"]


@pytest.mark.parametrize(
    "defect", [None, "missing", "duplicate", "unexpected", "stale"]
)
def test_601_aligns_complete_scores_and_joint_features(catalog, monkeypatch, defect):
    scores = pd.DataFrame(
        {
            "P1": [20.0, 10.0],
            "score_origin": ["frozen_phase4", "frozen_phase4"],
            "ModelID": ["M2", "M1"],
            "OncotreeLineage": ["L2", "L1"],
            "P2": [3.0, 4.0],
        }
    )
    if defect == "missing":
        scores = scores.drop(columns="P2")
    elif defect == "duplicate":
        scores = scores[
            ["ModelID", "OncotreeLineage", "score_origin", "P1", "P2", "P2"]
        ]
    elif defect:
        scores[{"unexpected": "extra", "stale": "CONSENSUS_TX_03"}[defect]] = 0.0
    monkeypatch.setattr(pd, "read_parquet", lambda _: scores)
    catalog.update(
        artifact_registry={},
        resolve_artifact_path=lambda *_: "scores",
        gdsc_universe=pd.DataFrame(
            {
                "ModelID": ["M1", "M2"],
                "DRUG_ID": [17, 17],
                "OncotreeLineage": ["L1", "L2"],
            }
        ),
    )
    if defect:
        with pytest.raises(ValueError):
            run_cells(601, [4], catalog)
        return

    run_cells(601, [1], catalog)
    catalog["resolve_artifact_path"] = lambda *_: "scores"
    run_cells(601, [4, 7, 11], catalog)
    result = catalog["gdsc_modeling"]
    assert result.columns.tolist() == [
        "ModelID",
        "DRUG_ID",
        "OncotreeLineage",
        *PROGRAM_IDS,
    ]
    assert result[["ModelID", "P2", "P1"]].values.tolist() == [
        ["M1", 4.0, 10.0],
        ["M2", 3.0, 20.0],
    ]
    model = catalog["make_program_model"]()
    assert model.named_steps["preprocessor"].transformers[1] == (
        "programs",
        "passthrough",
        list(PROGRAM_IDS),
    )


def test_601_held_out_fit_reconstructs_exact_602_attribution(catalog):
    run_cells(601, [1], catalog)
    catalog.update(PROGRAM_COLUMNS=list(PROGRAM_IDS), program_ids=PROGRAM_IDS)
    run_cells(601, [7, 11, 12], catalog)
    rng = np.random.default_rng(19)
    data = pd.DataFrame(
        {
            "DRUG_ID": 101,
            "ModelID": [f"M{i}" for i in range(18)],
            "OncotreeLineage": ["A", "B"] * 9,
            "P1": rng.normal(size=18),
            "P2": rng.normal(size=18),
        }
    )
    data["response_value"] = (
        2 * data["P1"] - 4 * data["P2"] + data["OncotreeLineage"].eq("B")
    )
    predictions, fitted, lineage = catalog["fit_predict_primary_fold"](
        data.iloc[:12], data.iloc[12:], return_state=True
    )
    predictions = predictions.assign(repeat=1, fold=2)
    fitted = pd.DataFrame([{"DRUG_ID": 101, "repeat": 1, "fold": 2, **fitted}])
    lineage = lineage.assign(DRUG_ID=101, repeat=1, fold=2)
    catalog.update(
        oof_attribution_input=predictions,
        fold_parameter_input=fitted,
        fold_lineage_effect_input=lineage,
    )
    run_cells(602, [6, 7, 8, 9, 29], catalog)
    result = catalog["attribution_rows"]
    assert catalog["phi_program_columns"] == ["phi_P2", "phi_P1"]
    np.testing.assert_allclose(
        result["reconstructed_prediction"], predictions["prediction_program"]
    )
    np.testing.assert_allclose(
        result["phi_P1"], 2 * (data["P1"].iloc[12:] - data["P1"].iloc[:12].mean())
    )
    np.testing.assert_allclose(
        result["phi_program_block"], result["phi_P2"] + result["phi_P1"]
    )
    assert result["ModelID"].tolist() == predictions["ModelID"].tolist()
    assert result[["DRUG_ID", "repeat", "fold"]].drop_duplicates().values.tolist() == [
        [101, 1, 2]
    ]
    assert lineage["train_lineage_fraction"].sum() == 1.0


def test_602_rejects_incompatible_biological_context(catalog, monkeypatch):
    names = {
        "phase4.401.consensus_transcriptomic_program_catalog",
        "phase4.401.consensus_transcriptomic_gene_weights",
        "phase4.401.consensus_tumor_arm_context",
        "phase4.403.epigenetic_regulator_enrichment_summary",
        "phase4.403.epigenetic_regulator_gene_context",
        "phase4.404.program_annotation_enrichment",
        "phase4b.450.primary_gene_program_associations",
        "phase4b.451.locus_level_methylation_expression_evidence",
    }
    frames = {
        name: pd.DataFrame({"consensus_program_id": PROGRAM_IDS}) for name in names
    }
    mutation = "phase4b.450.primary_gene_program_associations"
    locus = "phase4b.451.locus_level_methylation_expression_evidence"
    frames[mutation] = pd.DataFrame({"program": ["P1"]})
    frames[locus] = pd.DataFrame({"consensus_program_memberships": ["P2;P1", None]})
    monkeypatch.setattr(pd, "read_csv", lambda name: frames[name])
    catalog.update(
        biological_context_paths={name: name for name in names}, program_ids=PROGRAM_IDS
    )
    run_cells(602, [22], catalog)
    frames[locus].loc[0, "consensus_program_memberships"] = "P2;CONSENSUS_TX_03"
    with pytest.raises(ValueError, match="locus.*CONSENSUS_TX_03"):
        run_cells(602, [22], catalog)


@pytest.mark.parametrize(
    "defect", [None, "missing", "extra", "duplicate", "stale_score"]
)
def test_602_validates_the_full_601_fitted_schema(catalog, monkeypatch, defect):
    oof = pd.DataFrame(
        {
            "DRUG_ID": [51],
            "ModelID": ["M3"],
            "OncotreeLineage": ["B"],
            "response_value": [4.2],
            "P1": [1.5],
            "P2": [2.5],
            "prediction_lineage": [3.0],
            "prediction_program": [4.1],
            "repeat": [2],
            "fold": [4],
        }
    )
    fitted = pd.DataFrame(
        {
            "DRUG_ID": [51],
            "repeat": [2],
            "fold": [4],
            "n_train": [12],
            "n_test": [1],
            "n_train_lineages": [2],
            "program_intercept": [3.0],
            "reference_lineage": ["A"],
            "train_mean_lineage_effect": [0.1],
            "beta_P1": [0.4],
            "train_mean_P1": [0.1],
            "beta_P2": [0.15],
            "train_mean_P2": [0.2],
        }
    )
    if defect == "missing":
        fitted = fitted.drop(columns="train_mean_P2")
    elif defect == "extra":
        fitted["beta_CONSENSUS_TX_03"] = 0.0
    elif defect == "duplicate":
        fitted = pd.concat([fitted, fitted[["beta_P1"]]], axis=1)
    elif defect == "stale_score":
        oof["CONSENSUS_TX_03"] = 0.0
    parquet = {
        "phase6.601.primary_oof_predictions": oof,
        "phase6.601.primary_program_fold_parameters": fitted,
        "phase6.601.primary_program_fold_lineage_effects": pd.DataFrame(),
    }
    monkeypatch.setattr(pd, "read_parquet", parquet.__getitem__)
    monkeypatch.setattr(pd, "read_csv", lambda _: pd.DataFrame())
    catalog["input_paths"] = {
        name: name for name in [*parquet, "phase6.601.drug_level_results"]
    }
    if defect:
        with pytest.raises(ValueError, match="program definitions|fitted parameters"):
            run_cells(602, [3], catalog)
    else:
        run_cells(602, [3], catalog)
        result = catalog["primary_oof_predictions"]
        assert result.columns.tolist()[-2:] == list(PROGRAM_IDS)
        assert result[
            ["DRUG_ID", "ModelID", "repeat", "fold", "P2", "P1"]
        ].values.tolist() == [[51, "M3", 2, 4, 2.5, 1.5]]


def test_603_rejects_stale_ids_and_preserves_partial_screen_families(catalog):
    # Exercise the actual local long-table validator without the loading cell.
    _, cells = notebook(603)
    validator = next(
        statement
        for statement in ast.parse(cells[3]).body
        if isinstance(statement, ast.FunctionDef)
        and statement.name == "validate_program_membership"
    )
    catalog["program_ids"] = PROGRAM_IDS
    exec(
        compile(ast.Module(body=[validator], type_ignores=[]), "<membership>", "exec"),
        catalog,
    )
    validate = catalog["validate_program_membership"]
    validate(pd.DataFrame({"program": ["P1"]}), "filtered")
    validate(pd.DataFrame({"program": []}), "empty subset")
    with pytest.raises(ValueError, match="missing=.*P2"):
        validate(pd.DataFrame({"program": ["P1"]}), "full GDSC", complete=True)
    with pytest.raises(ValueError, match="CONSENSUS_TX_03"):
        validate(pd.DataFrame({"program": ["CONSENSUS_TX_03"]}), "external")
    raw = pd.DataFrame(
        {
            "external_resource": ["CTRP", "PRISM", "CTRP", "PRISM"],
            "gdsc_drug_id": [825, 825, 422, 739],
            "external_drug_id": ["100", "BRD-100", "200", "BRD-300"],
            "program": ["P1"] * 4,
            "p_value": [0.03, 0.001, 0.04, 0.9],
            "beta": [1.0] * 4,
            "gdsc_direction": ["resistance_like"] * 4,
        }
    )
    catalog.update(
        multipletests=multipletests,
        primary_external_associations=raw.copy(),
        nonoverlap_external_associations=raw.loc[
            raw["external_resource"].eq("CTRP")
        ].copy(),
    )
    run_cells(603, [23, 24, 26], catalog)
    actual = catalog["primary_external_associations"]
    np.testing.assert_array_equal(actual["q_value"], [0.04, 0.002, 0.04, 0.9])
    pd.testing.assert_frame_equal(actual[raw.columns], raw)
    np.testing.assert_array_equal(
        catalog["nonoverlap_external_associations"]["q_value"], [0.04, 0.04]
    )


@pytest.mark.parametrize("number", [600, 601, 602, 603])
@pytest.mark.parametrize(
    "defect",
    [None, "missing", "parquet", "metadata", "misidentified", "csv_number", "csv_text"],
)
def test_phase6_verifies_declared_outputs_before_refresh(
    tmp_path, monkeypatch, number, defect
):
    if number == 603 and defect in {"csv_number", "csv_text"}:
        pytest.skip("Notebook 603 publishes Parquet and JSON")
    notebook_path, _ = notebook(number)
    registry = artifact_registry.load_artifact_registry()
    entries = {
        key: value
        for key, value in registry["artifacts"].items()
        if value["producer"].get("path") == notebook_path
    }
    assert len(entries) == {600: 9, 601: 8, 602: 7, 603: 6}[number]
    registry_path = tmp_path / "artifact_registry.json"
    registry_path.write_text(json.dumps(registry), encoding="utf-8")
    initial = registry_path.read_bytes()
    real_load = artifact_registry.load_artifact_registry
    real_refresh = artifact_registry.refresh_notebook_artifacts
    calls = []

    def refresh(producer, verified_outputs, *, require_unchanged):
        calls.append((producer, verified_outputs, require_unchanged))
        return real_refresh(
            producer,
            verified_outputs,
            registry_path=registry_path,
            root=tmp_path,
            require_unchanged=require_unchanged,
        )

    monkeypatch.setattr(
        artifact_registry,
        "load_artifact_registry",
        lambda path=registry_path: real_load(path),
    )
    monkeypatch.setattr(artifact_registry, "refresh_notebook_artifacts", refresh)
    paths = {
        artifact_id: tmp_path / entry["path"] for artifact_id, entry in entries.items()
    }
    names = {
        artifact_id.rsplit(".", 1)[-1]: path for artifact_id, path in paths.items()
    }
    metadata_path = names.pop("analysis_metadata")
    frame = pd.DataFrame(
        {"number": [0.15625, 42.0], "identity": ["00031", 'NA,"line"\ncontinued']}
    )
    metadata = {"producer_notebook": notebook_path, "payload": [1, True]}
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.suffix == ".parquet":
            frame.to_parquet(path, index=False)
        elif path.suffix == ".csv":
            options = {"lineterminator": "\n"} if number == 600 else {}
            frame.to_csv(path, index=False, **options)
        else:
            path.write_text(json.dumps(metadata), encoding="utf-8")

    if defect == "missing":
        next(path for path in names.values() if path.suffix == ".parquet").unlink()
    elif defect == "parquet":
        path = next(path for path in names.values() if path.suffix == ".parquet")
        frame.assign(number=[0.15626, 42.0]).to_parquet(path, index=False)
    elif defect == "metadata":
        metadata_path.write_text(
            json.dumps({**metadata, "payload": [1, 1]}), encoding="utf-8"
        )
    elif defect in {"csv_number", "csv_text"}:
        path = next(path for path in names.values() if path.suffix == ".csv")
        old, new = (
            ("0.15625", "0.15626") if defect == "csv_number" else ("00031", "00032")
        )
        path.write_bytes(path.read_bytes().replace(old.encode(), new.encode()))

    env = {
        "pd": pd,
        "np": np,
        "json": json,
        "analysis_metadata": metadata,
        "calculate_sha256": calculate_sha256,
        "metadata_path": metadata_path,
        "Paths": SimpleNamespace(root=tmp_path),
    }
    if number == 600:
        env["phase6_600_analysis_metadata"] = metadata
        env["artifact_payloads"] = {
            artifact_id: {
                "path": path,
                "data": metadata if path == metadata_path else frame,
                "format": path.suffix[1:],
            }
            for artifact_id, path in paths.items()
        }
        if defect == "misidentified":
            a, b = [key for key, value in paths.items() if value.suffix == ".parquet"][
                :2
            ]
            env["artifact_payloads"][a]["path"], env["artifact_payloads"][b]["path"] = (
                paths[b],
                paths[a],
            )
        # Take identities of the files as written, even for the corruption cases.
        # The content comparison must still catch corruption with matching hashes.
        env["phase6_600_artifact_manifest"] = pd.DataFrame(
            [
                {
                    "artifact_id": artifact_id,
                    "size_bytes": path.stat().st_size,
                    "sha256": calculate_sha256(path),
                }
                for artifact_id, item in env["artifact_payloads"].items()
                if (path := item["path"]).exists()
            ]
        )
        cells = [76, 77, 78]
    elif number in {601, 602}:
        if number == 601:
            names["cv_partitions"] = names.pop("primary_cv_partitions")
        if defect == "misidentified":
            a, b = (
                list(names)[:2]
                if number == 601
                else [name for name, path in names.items() if path.suffix == ".csv"][:2]
            )
            names[a], names[b] = names[b], names[a]
        env["output_paths"] = names
        env.update(
            {name + ("_output" if number == 602 else ""): frame for name in names}
        )
        cells = [36, 37, 38, 39, 40] if number == 601 else [41]
    else:
        path_variables = {
            "replication_hypothesis_manifest": "replication_manifest_path",
            "cell_line_overlap_manifest": "cell_line_overlap_path",
            "primary_external_associations": "primary_external_path",
            "nonoverlap_external_associations": "nonoverlap_external_path",
            "replication_summary": "replication_summary_path",
        }
        if defect == "misidentified":
            a, b = list(names)[:2]
            names[a], names[b] = names[b], names[a]
        env.update({path_variables[name]: path for name, path in names.items()})
        env.update({name: frame for name in names})
        env.update(
            replication_summary=frame.assign(identity="intermediate"),
            replication_summary_final=frame,
            analysis_metadata_path=metadata_path,
        )
        cells = [55, 56, 57, 58, 59]
        # Analytical validation is tested independently below.
        _, sources = notebook(number)
        publication = sources[62][
            sources[62].index("registered = load_artifact_registry()") :
        ]

    def execute():
        run_cells(number, cells, env)
        if number == 603:
            exec(compile(publication, "<603 publication>", "exec"), env)

    if defect:
        with pytest.raises((AssertionError, ValueError, FileNotFoundError, KeyError)):
            execute()
        assert calls == []
        assert registry_path.read_bytes() == initial
        return

    execute()
    assert len(calls) == 1
    producer, verified, require_unchanged = calls[0]
    assert producer == notebook_path
    assert not require_unchanged
    assert set(verified) == {path.resolve() for path in paths.values()}
    refreshed = real_load(registry_path)["artifacts"]
    for artifact_id, before in entries.items():
        path = paths[artifact_id]
        after = refreshed[artifact_id]
        assert after == {
            **before,
            "shape": None if path == metadata_path else list(frame.shape),
            "size_bytes": path.stat().st_size,
            "sha256": calculate_sha256(path),
        }


@pytest.mark.parametrize(
    "invalid", [None, "overlap", "family", "classification", "corroboration", "dual"]
)
def test_603_checks_overlap_families_and_status_before_publishing(invalid):
    keys = ["gdsc_drug_id", "external_resource", "external_drug_id", "program"]
    manifest = pd.DataFrame(
        {
            "gdsc_drug_id": [19, 19, 45, 45],
            "external_resource": ["CTRP", "PRISM", "CTRP", "PRISM"],
            "external_drug_id": ["001", "BRD-001", "045", pd.NA],
            "program": ["P2"] * 4,
            "primary_evaluable": [True, True, True, False],
            "nonoverlap_eligible": [True, False, True, False],
            "preanalysis_status": ["PRIMARY_EVALUABLE"] * 3 + ["NO_EXACT_MATCH"],
        }
    )
    primary = manifest.iloc[:3][keys].assign(
        p_value=[0.001, 0.002, 0.8],
        q_value=[0.002, 0.002, 0.8],
        fdr_05=[True, True, False],
        direction_concordant=[True, True, True],
        replication_status=["SCREEN_REPLICATED"] * 2
        + ["TESTED_DIRECTION_CONCORDANT_NOT_FDR"],
    )
    nonoverlap = manifest.iloc[[0, 2]][keys].assign(
        p_value=[0.001, 0.002],
        q_value=[0.002, 0.002],
        fdr_05=True,
        direction_concordant=True,
        nonoverlap_model_corroboration=[True, False],
    )
    summary = manifest[keys].assign(
        final_screen_status=[*primary["replication_status"], "NO_EXACT_MATCH"],
        nonoverlap_support_label=[
            "NONOVERLAP_MODEL_CORROBORATION",
            pd.NA,
            pd.NA,
            pd.NA,
        ],
        dual_external_status=["REPLICATED_IN_BOTH_EXTERNAL_SCREENS"] * 2
        + [pd.NA, pd.NA],
        median_repeat_mean_abs_shap=[0.2, 0.2, 0.1, 0.1],
    )
    if invalid == "family":
        primary = primary.iloc[:-1]
    elif invalid == "classification":
        summary.loc[3, "final_screen_status"] = "SCREEN_REPLICATED"
    elif invalid == "corroboration":
        nonoverlap.loc[2, "nonoverlap_model_corroboration"] = True
    elif invalid == "dual":
        summary.loc[2, "dual_external_status"] = "REPLICATED_IN_BOTH_EXTERNAL_SCREENS"
    calls = []

    def stop_before_io(*args, **kwargs):
        calls.append((args, kwargs))
        raise RuntimeError("publication boundary")

    env = {
        "pd": pd,
        "np": np,
        "multipletests": multipletests,
        "display": lambda *_: None,
        "overlap_set_check": invalid != "overlap",
        "replication_hypothesis_manifest": manifest,
        "primary_external_associations": primary,
        "nonoverlap_external_associations": nonoverlap,
        "replication_summary_final": summary,
        "producer_path": "603",
        "output_files": {},
        "verified_outputs": {},
        "load_artifact_registry": lambda: {"artifacts": {}},
        "refresh_notebook_artifacts": stop_before_io,
    }
    if invalid:
        with pytest.raises((ValueError, AssertionError)):
            run_cells(603, [61, 62], env)
        assert not calls
    else:
        with pytest.raises(RuntimeError, match="publication boundary"):
            run_cells(603, [61, 62], env)
        assert len(calls) == 1


@pytest.mark.parametrize(
    ("screen", "gdsc_fdr", "single_experiment_models", "shared_models"),
    [
        ("PRISM", True, 0, 40),
        ("CTRP", True, 10, 40),
        ("CTRP", True, 40, 40),
        ("CTRP", True, 120, 120),
        (None, True, 0, 40),
        (None, False, 0, 40),
    ],
    ids=[
        "prism-only",
        "ctrp-only-no-single-experiment-fit",
        "ctrp-only-small-single-experiment-fit",
        "eligible-diagnostics",
        "no-evaluable-screens",
        "no-gdsc-fdr-hypotheses",
    ],
)
def test_603_empty_diagnostics_and_replication_boundaries(
    catalog,
    tmp_path,
    monkeypatch,
    screen,
    gdsc_fdr,
    single_experiment_models,
    shared_models,
):
    from statsmodels.formula.api import ols

    path, cells = notebook(603)
    definitions = [
        node
        for node in ast.parse(cells[3]).body
        if isinstance(node, ast.FunctionDef)
        and node.name in {"catalog_order", "validate_program_membership"}
    ]
    catalog.update(
        program_ids=PROGRAM_IDS,
        program_order={pid: i for i, pid in enumerate(PROGRAM_IDS)},
        PROGRAM_COLUMNS=list(PROGRAM_IDS),
    )
    exec(compile(ast.Module(body=definitions, type_ignores=[]), path, "exec"), catalog)

    rng = np.random.default_rng(603)
    model_ids = [f"EXT-{i}" for i in range(120)]
    external = pd.DataFrame(
        {
            "ModelID": model_ids,
            "OncotreeLineage": np.repeat(["A", "B", "C"], 40),
            "P2": rng.normal(size=120),
        }
    )
    external["response_value"] = 2 * external["P2"] + rng.normal(scale=0.1, size=120)
    gdsc = pd.concat(
        [
            external[["ModelID", "OncotreeLineage"]].iloc[:shared_models],
            pd.DataFrame(
                {
                    "ModelID": [f"GDSC-{i}" for i in range(120 - shared_models)],
                    "OncotreeLineage": np.repeat(
                        ["D", "E"], (120 - shared_models) // 2
                    ),
                }
            ),
        ],
        ignore_index=True,
    ).assign(DRUG_ID=19)

    context_artifact_ids = {
        "predictive": "phase6.601.drug_level_results",
        "attribution": "phase6.602.drug_program_attribution_summary",
    }
    catalog.update(
        Paths=SimpleNamespace(root=tmp_path),
        project_relative_path=lambda file: file.relative_to(tmp_path).as_posix(),
        ols=ols,
        multipletests=multipletests,
        INPUT_ARTIFACT_IDS=(),
        context_artifact_ids=context_artifact_ids,
        gdsc_associations=pd.DataFrame(
            {
                "DRUG_ID": [19, 19],
                "DRUG_NAME": ["Example", "Example"],
                "program": ["P2", "P1"],
                "beta": [0.5, 0.0],
                "p_value": [0.001, 0.9],
                "q_value": [0.002, 0.9],
                "association_direction": ["resistance_like", "sensitivity_like"],
                "fdr_05": [gdsc_fdr, False],
            }
        ),
        compound_catalog=pd.DataFrame(
            {
                "drug_name_key": ["EXAMPLE"],
                "gdsc_drug_id": [19],
                "ctrp_master_cpd_id": [None if screen == "PRISM" else 121],
                "ctrp_drug_name": ["Example"],
                "prism_broad_id": ["BRD-19"],
                "prism_drug_name": ["Example"],
                "resources_present": [3],
                "screen_pattern": ["MTS010"],
                "primary_prism_screen": ["MTS010"],
            }
        ),
        drug_eligibility=pd.DataFrame(
            {
                "resource": ["CTRP", "PRISM_exact_cross_resource"],
                "resource_drug_id": ["121", "BRD-19"],
                "supported_lineages": [3, 3],
                "supported_models": [120, 120],
                "eligible": [screen == "CTRP", screen == "PRISM"],
                "analysis_universe": ["CTRP", "PRISM"],
            }
        ),
        gdsc_universe=gdsc,
        ctrp_universe=external.drop(columns="P2").assign(
            master_cpd_id=121,
            n_experiments=np.where(
                np.arange(len(external)) < single_experiment_models, 1, 2
            ),
        ),
        prism_universe=external.drop(columns="P2").assign(broad_id="BRD-19"),
        program_scores=pd.concat(
            [
                external[["ModelID", "P2"]],
                gdsc.loc[~gdsc["ModelID"].isin(model_ids), ["ModelID"]].assign(P2=0.0),
            ],
            ignore_index=True,
        ).assign(P1=0.0, score_origin="frozen_phase4"),
        predictive_context=pd.DataFrame(
            {
                "DRUG_ID": [19],
                "median_r2_program": [0.6],
                "median_delta_r2": [0.2],
                "positive_delta_repeats": [5],
                "shap_eligible": [True],
            }
        ),
        attribution_context=pd.DataFrame(
            {
                "DRUG_ID": [19],
                "program": ["P2"],
                "median_repeat_mean_abs_shap": [0.2],
                "dominant_repeat_fraction": [1.0],
                "median_coefficient": [0.35],
                "fraction_positive": [1.0],
                "fraction_negative": [0.0],
            }
        ),
    )
    # Execute selected code cells with synthetic handoffs and temporary output paths.
    run_cells(603, [*range(4, 18), *range(19, 34)], catalog)
    primary = catalog["primary_external_associations"].copy(deep=True)
    run_cells(603, list(range(34, 47)), catalog)
    pd.testing.assert_frame_equal(catalog["primary_external_associations"], primary)

    diagnostic_keys = [
        "gdsc_drug_id",
        "external_resource",
        "external_drug_id",
        "program",
    ]
    for name, keys, direction, expected_rows in (
        (
            "shared_only_associations",
            diagnostic_keys,
            "shared_direction",
            int(shared_models == 120),
        ),
        (
            "shared_lineage_associations",
            diagnostic_keys,
            "shared_lineage_direction",
            int(shared_models == 120),
        ),
        (
            "ctrp_single_experiment_associations",
            ["gdsc_drug_id", "external_drug_id", "program"],
            "sensitivity_direction",
            int(screen == "CTRP" and single_experiment_models >= 20),
        ),
    ):
        result = catalog[name]
        assert len(result) == expected_rows
        assert result.columns[: len(keys) + 5].tolist() == [
            *keys,
            "n_models",
            "n_lineages",
            "beta",
            "beta_standardized",
            direction,
        ]
        assert result["matches_primary_direction"].eq(True).all()

    run_cells(603, [*range(48, 54), *range(55, 59)], catalog)
    summary = catalog["replication_summary_final"]
    assert len(summary) == (2 if gdsc_fdr else 0)
    assert len(primary) == int(screen is not None)
    assert summary["final_screen_status"].eq("SCREEN_REPLICATED").sum() == len(primary)
    assert summary["dual_external_status"].isna().all()
    assert catalog["nonoverlap_external_associations"].empty
    assert catalog["analysis_metrics"]["replicated_both_external_screens"] == 0
    assert catalog["diagnostic_summary"]["primary_family_sizes"] == (
        {screen: 1} if screen else {}
    )

    registry = artifact_registry.load_artifact_registry()
    registry_path = tmp_path / "artifact_registry.json"
    registry_path.write_text(json.dumps(registry), encoding="utf-8")
    real_load = artifact_registry.load_artifact_registry
    monkeypatch.setattr(
        artifact_registry,
        "load_artifact_registry",
        lambda location=registry_path: real_load(location),
    )
    monkeypatch.setattr(
        artifact_registry,
        "refresh_notebook_artifacts",
        partial(
            artifact_registry.refresh_notebook_artifacts,
            registry_path=registry_path,
            root=tmp_path,
        ),
    )
    run_cells(603, [59, 60, 61, 62], catalog)
    assert catalog["registered_count"] == 6
    shapes = {
        artifact_id.rsplit(".", 1)[-1]: record["shape"]
        for artifact_id, record in catalog["refreshed_entries"].items()
    }
    assert {name: shape[1] for name, shape in shapes.items() if shape is not None} == {
        "replication_hypothesis_manifest": 39,
        "cell_line_overlap_manifest": 47,
        "primary_external_associations": 24,
        "nonoverlap_external_associations": 27,
        "replication_summary": 55,
    }
