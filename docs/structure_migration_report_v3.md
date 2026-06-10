# Roadmap v3.0 Repository Structure Migration Report

## Source of truth

This migration used `roadmap.md` v3.0 as the source of truth for the biological-phase notebook structure, the approved `data/interim`, `data/processed`, and `results` hierarchies, and the source-dataset organization under `data/raw`.

## Branch

- Created branch: `roadmap-v3-structure-migration`

## Ambiguities reported

- Roadmap v3.0 specifies notebook phases and data/results architecture, but does not explicitly specify whether `src/` should mirror the biological-phase terminology. To avoid leaving obsolete phase folder names in the repository structure, the existing `src/phase*_...` folders were migrated to the same v3.0 phase terminology as notebooks.
- Existing notebook filenames use earlier numbering (`10`, `20`-`27`, `30`) while roadmap v3.0 defines 100/200/300-series notebook labels. Because the task requested folder reorganization and folder renaming, notebook filenames were preserved and only moved to their best matching v3.0 phase folders.
- Existing audit artifacts were under `data/audit`, while roadmap v3.0 only approves `data/interim`, `data/processed`, and source-dataset `data/raw` organization. The audit notebook was preserved under the Phase 1 notebooks folder, while the consumable JSON audit artifact remains under `data/interim/qc`.

## Moved or renamed notebooks

- `notebooks/phase1_download/10_dataset_inventory.ipynb` → `notebooks/phase1_data_acquisition_and_auditing/10_dataset_inventory.ipynb`
- `notebooks/phase2_eda/20_cross_dataset_overlap_analysis.ipynb` → `notebooks/phase3_cell_line_discovery_layer/20_cross_dataset_overlap_analysis.ipynb`
- `notebooks/phase2_eda/21_identifier_landscape_and_harmonization_strategy.ipynb` → `notebooks/phase3_cell_line_discovery_layer/21_identifier_landscape_and_harmonization_strategy.ipynb`
- `notebooks/phase2_eda/22_integrated_modeling_cohort_construction.ipynb` → `notebooks/phase3_cell_line_discovery_layer/22_integrated_modeling_cohort_construction.ipynb`
- `notebooks/phase2_eda/23_expression_matrix_integration.ipynb` → `notebooks/phase3_cell_line_discovery_layer/23_expression_matrix_integration.ipynb`
- `notebooks/phase2_eda/24_expression_quality_control_and_variability_assessment.ipynb` → `notebooks/phase3_cell_line_discovery_layer/24_expression_quality_control_and_variability_assessment.ipynb`
- `notebooks/phase2_eda/25_global_transcriptomic_structure_analysis.ipynb` → `notebooks/phase3_cell_line_discovery_layer/25_global_transcriptomic_structure_analysis.ipynb`
- `notebooks/phase2_eda/26_gdsc_pharmacology_integration.ipynb` → `notebooks/phase3_cell_line_discovery_layer/26_gdsc_pharmacology_integration.ipynb`
- `notebooks/phase2_eda/27_pharmacological_phenotype_framework.ipynb` → `notebooks/phase3_cell_line_discovery_layer/27_pharmacological_phenotype_framework.ipynb`
- `notebooks/phase3_integration/30_model-level_transcriptome–phenotype_integration.ipynb` → `notebooks/phase3_cell_line_discovery_layer/30_model-level_transcriptome–phenotype_integration.ipynb`

## Created notebook phase directories

- `notebooks/phase0_infrastructure_and_reproducibility/`
- `notebooks/phase1_data_acquisition_and_auditing/`
- `notebooks/phase2_tumor_discovery_layer/`
- `notebooks/phase3_cell_line_discovery_layer/`
- `notebooks/phase4_consensus_programs/`
- `notebooks/phase5_functional_vulnerabilities/`
- `notebooks/phase6_pharmacogenomic_contexts/`
- `notebooks/phase7_perturbational_hypotheses/`
- `notebooks/phase8_orthogonal_validation/`
- `notebooks/phase9_manuscript_preparation/`

## Created or renamed data directories

### Raw source datasets

- `data/raw/lincs_cmap/` → `data/raw/lincs/`
- `data/raw/tcga_gdc/` → `data/raw/tcga/`
- Created `data/raw/ctrp/`
- Created `data/raw/cell_model_passports/`
- Preserved existing source-dataset folders `data/raw/depmap/`, `data/raw/gdsc/`, `data/raw/prism/`, `data/raw/chembl/`, and `data/raw/drugbank/`.

### Interim data

- Created `data/interim/metadata/`
- Created `data/interim/expression/`
- Created `data/interim/methylation/`
- Created `data/interim/dependencies/`
- Created `data/interim/pharmacology/`
- Created `data/interim/perturbational/`
- Created `data/interim/qc/`
- Moved `data/audit/audit.ipynb` → `notebooks/phase1_data_acquisition_and_auditing/audit.ipynb`
- Moved `data/audit/raw_file_audit.json` → `data/interim/qc/raw_file_audit.json`
- Confirmed `data/interim/qc/` contains consumable QC artifacts/placeholders only, not notebooks.

### Processed data

- Created `data/processed/tumor_programs/`
- Created `data/processed/cellline_programs/`
- Created `data/processed/consensus_programs/`
- Created `data/processed/functional_vulnerabilities/`
- Created `data/processed/pharmacogenomic_contexts/`
- Created `data/processed/perturbational_hypotheses/`
- Created `data/processed/validation/`

## Created results directories

- Created `results/paper1/`
- Created `results/paper2/`
- Created `results/supplementary/`
- Follow-up cleanup added manuscript-ready subfolders under each result grouping: `figures/` and `tables/` for `paper1`, `paper2`, and `supplementary`.

## Created or moved `.gitkeep` files

`.gitkeep` files were added or moved to every empty roadmap directory that should remain tracked, including the new notebook, data, results, and source-code phase directories.

## Modified files

- `.gitignore`: updated ignored data paths and `.gitkeep` exceptions for the v3.0 directory names.
- `config/paths.yaml`: replaced legacy raw, processed, and results paths with v3.0 paths.
- `config/raw_data_registry.json`: renamed raw dataset registry keys from `lincs_cmap`/`tcga_gdc` to `lincs`/`tcga` and added placeholders for `ctrp` and `cell_model_passports`.
- `data/README.md`: documented roadmap v3.0 data conventions.
- `notebooks/phase1_data_acquisition_and_auditing/audit.ipynb`: moved out of `data/` and updated stale output text to the new raw dataset key names.
- `docs/language_normalization_audit.md`: updated the moved download script path.
- `docs/workflow.md`: renamed from the typo-named workflow document during follow-up cleanup and retains the updated audit manifest path to `data/interim/qc`.
- `notebooks/README.md`: documented v3.0 notebook phase directories.
- `notebooks/phase3_cell_line_discovery_layer/20_cross_dataset_overlap_analysis.ipynb`: updated the upstream notebook path reference and changed the created QC directory from the obsolete `reports/phase2_eda` path to `Paths.qc`.
- `notebooks/phase3_cell_line_discovery_layer/30_model-level_transcriptome–phenotype_integration.ipynb`: updated the output path reference from the removed `Paths.merged` alias to `Paths.interim`.
- `results/README.md`: documented manuscript-oriented result directories.
- `src/utils/paths.py`: updated path helper attributes for roadmap v3.0 raw, interim, processed, and results directories.

## Moved or renamed source-code structure

- `src/phase1_download/download_public_datasets.py` → `src/phase1_data_acquisition_and_auditing/download_public_datasets.py`
- Created or renamed `src/phase0_infrastructure_and_reproducibility/`
- Created or renamed `src/phase1_data_acquisition_and_auditing/`
- Created or renamed `src/phase2_tumor_discovery_layer/`
- Created or renamed `src/phase3_cell_line_discovery_layer/`
- Created or renamed `src/phase4_consensus_programs/`
- Created or renamed `src/phase5_functional_vulnerabilities/`
- Created or renamed `src/phase6_pharmacogenomic_contexts/`
- Created or renamed `src/phase7_perturbational_hypotheses/`
- Created or renamed `src/phase8_orthogonal_validation/`
- Created `src/phase9_manuscript_preparation/`

### Source-code structure recommendation

The `src/phase0_*`, `src/phase2_*`, `src/phase3_*`, `src/phase4_*`, `src/phase5_*`, `src/phase6_*`, `src/phase7_*`, `src/phase8_*`, and `src/phase9_*` folders currently contain only `.gitkeep` placeholders. The only phase folder with reusable source code is `src/phase1_data_acquisition_and_auditing/`, which contains `download_public_datasets.py`. Because placeholder-only source directories are safe but not operationally necessary today, the recommendation is to keep them for this roadmap migration PR to avoid scope churn, then remove or consolidate them in a follow-up cleanup if the project does not intend to mirror notebook phases in `src/`.

## Removed obsolete empty placeholder-only directories

No notebooks or data files were deleted. Empty placeholder-only directories from the previous structure were removed after their placeholders were moved or replaced in roadmap v3.0 locations, including the old notebook phase folders, old source phase folders, `data/external`, `data/audit`, and the old result subfolders (`results/figures`, `results/models`, `results/tables`, `results/drug_ranking`). No notebook files remain under `data/`.

## Validation summary

Validation commands were run after the migration:

- `git status --short --branch`
- `git diff --check`
- `rg -n "phase0_audit|phase1_download|phase2_eda|phase3_integration|phase4_modeling|phase5_signatures|phase6_targets|phase7_repurposing|phase8_validation|lincs_cmap|tcga_gdc|results/(figures|models|tables|drug_ranking)|data/processed/(merged|splits|signatures)|Paths\\.(merged|splits|signatures|figures|tables|models|drug_ranking)" . --glob '!.git/**' --glob '!docs/structure_migration_report_v3.md'`
- `find . -name "*.ipynb" -not -path "./notebooks/*" -not -path "./.git/*" -print` to confirm no notebooks remain outside `notebooks/`.
- `python -m json.tool`/`json.load` over all notebooks under `notebooks/`.
- `python - <<'PY' ... from src.utils.paths import Paths ... PY` to smoke-test path helper imports.
