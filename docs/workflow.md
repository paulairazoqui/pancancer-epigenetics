# Pan-Cancer Epigenetics: Operational Workflow (v3.0)

This workflow describes the operational sequence for the roadmap v3.0 framework. Provenance, release names, and canonical source filenames are maintained in `config/raw_data_registry.json`; repository paths are maintained in `config/paths.yaml`.

## Phase 0 — Infrastructure and Reproducibility

**Status:** completed.

- **Objective:** maintain an auditable, reproducible repository environment.
- **Primary inputs:** repository configuration, environment definitions, and provenance records.
- **Primary outputs:** version-controlled conventions, source manifests, and reproducible data-tier structure.
- **Handoff:** downstream notebooks consume immutable raw data and reproducible interim layers.

## Phase 1 — Data Acquisition and Auditing

**Status:** implemented; acquisition and auditing remain dataset-specific when future phases require additional resources.

- **Objective:** inventory, freeze, download, and audit source data required by the implemented analysis.
- **Notebook series:** `100_dataset_inventory`, `101_raw_file_audit`, `102_tcga_rnaseq_cohort_freeze`, `103_tcga_rnaseq_download_validation`, `104_tcga_methylation_coverage_assessment`, `105_tcga_methylation_cohort_freeze`, and `106_tcga_methylation_download_validation`.
- **Primary inputs:** source datasets, manifests, and `config/raw_data_registry.json`.
- **Primary outputs:** audited source inventory, frozen TCGA RNA-seq and methylation cohorts, download-validation records, and coverage summaries.
- **Handoff:** frozen, audited inputs are supplied to the independent tumor and cell-line discovery phases. Future CTRP, PRISM, LINCS, dependency, or other resources require their own acquisition and audit work when needed.

## Phase 2 — Independent Tumor Discovery

**Status:** **CLOSED / FROZEN**.

- **Objective:** discover candidate cross-omic programs in TCGA primary tumors.
- **Notebook series:** `200_tcga_multiomic_candidate_cohort_construction`, `201_tcga_rnaseq_quality_control`, `202_tcga_methylation_quality_control`, `203_tcga_multiomic_integration`, `204_tcga_confounder_assessment`, `205_tcga_epigenetic_transcriptomic_program_discovery`, and `206_tcga_tumor_program_robustness`.
- **Primary inputs:** frozen TCGA primary-tumor RNA-seq and DNA-methylation layers.
- **Primary outputs:** the frozen 9,965-case cohort and 13 retained candidate cross-omic programs after robustness assessment, stored under `data/processed/tumor_programs`.
- **Boundary / handoff:** tumor candidates are frozen before cross-system comparison. This phase is independent of cell-line discovery and reopens only for a concrete identified problem. There is no notebook 207.

## Phase 3 — Independent Cell-Line Discovery

**Status:** **CLOSED**.

- **Objective:** independently discover latent transcriptomic programs in cancer cell models.
- **Notebook series:** `300_cross_dataset_overlap_analysis`, `301_identifier_landscape_and_harmonization_strategy`, `302_integrated_modeling_cohort_construction`, `303_expression_matrix_integration`, `304_expression_quality_control_and_variability_assessment`, `305_global_transcriptomic_structure_analysis`, `306_gdsc_pharmacology_integration`, `307_pharmacological_phenotype_framework`, `308_model_level_transcriptome_phenotype_integration`, `309_phenotype_sensitivity_analysis`, `310_program_discovery`, and `311_program_robustness`.
- **Primary inputs:** DepMap and GDSC data with provenance defined exclusively in `config/raw_data_registry.json`; the frozen cohort contains 713 models.
- **Primary outputs:** independently discovered cell-line program representations, internal robustness results, and frozen candidate-program outputs under `data/processed/cellline_programs`.
- **Boundary / handoff:** the sequence is transcriptomic representation discovery → representation freeze → pharmacogenomic phenotype association → internal robustness. Latent-program extraction in notebook 310 is phenotype-independent; the phenotype did not select the latent programs. The frozen cell-line candidates enter Phase 4 without being refit to tumor candidates.

## Phase 4 — Cross-System Comparison and Consensus

**Status:** **CLOSED / FROZEN — notebooks 400–404 complete**.

- **Objective:** compare the separately frozen tumor and cell-line candidates across systems, construct consensus transcriptomic representations only for supported correspondence events, and characterize those frozen representations without downstream redefinition.
- **Notebook series:** `400` Cross-System Program Comparison; `401` Consensus Program Construction; `402` Cross-Lineage Robustness; `403` Epigenetic Regulator Enrichment; and `404` Program Annotation.
- **Primary inputs:** frozen outputs from `data/processed/tumor_programs` and `data/processed/cellline_programs`, followed by the frozen cross-system correspondence and consensus artifacts under `data/processed/consensus_programs`.
- **Primary outputs:** cross-system comparison results; three candidate cross-system transcriptomic consensus representations with tumor-side methylation context; lineage-aware robustness summaries; epigenetic-regulator enrichment results; and prespecified biological annotations under `data/processed/consensus_programs`.
- **Boundary / handoff:** notebook 400 froze supported versus ambiguous transcriptomic correspondences without phenotype-based rescue; notebook 401 constructed consensus representations without reoptimizing orientation, gene weights, or eligibility from robustness, phenotype, biological annotation, or methylation context; notebook 402 assessed lineage structure, within-lineage variation, lineage-specific source-program fidelity, and leave-one-lineage-out influence without refitting, reweighting, or categorical robustness promotion; notebook 403 characterized curated epigenetic-regulator enrichment without using the results to rescue or exclude consensus representations; notebook 404 added a prespecified Hallmark, Reactome, and GO Biological Process annotation layer without redefining, reweighting, excluding, rescuing, or renaming the frozen programs. Phase 4 reopens only for a concrete identified problem.

## Phase 5 — Functional Vulnerabilities

**Status:** **ACTIVE — notebook 500 complete**.

- **Objective:** evaluate computational associations between consensus programs and functional dependencies.
- **Notebook series:** `500`–`502`; notebook `500` — CRISPR Associations is complete. Notebook `501` — RNAi Associations is next only after the required RNAi dependency input has been acquired, audited, and frozen for use.
- **Primary inputs:** frozen consensus programs and functional-genomics resources. DepMap Public 24Q4 CRISPR gene effect is now an acquired-and-used input through notebook 500; RNAi remains a future dataset-specific acquisition/audit requirement before notebook 501.
- **Primary outputs:** putative vulnerability-oriented dependency associations and dependency maps under `data/processed/functional_vulnerabilities`.
- **Boundary / handoff:** notebook 500 provides computational dependency associations and putative functional-vulnerability evidence, not validated targets or causal dependencies. Later RNAi or integrated-vulnerability analyses must not retrospectively redefine the frozen Phase 4 consensus representations or the completed CRISPR analysis.

## Phase 6 — Pharmacogenomic Contexts

**Status:** planned.

- **Objective:** characterize resistance-like pharmacogenomic contexts associated with consensus programs.
- **Notebook series:** `600`–`603`.
- **Primary inputs:** consensus programs and pharmacogenomic data, acquired and audited for the relevant resource.
- **Primary outputs:** computational association maps, predictive-association modeling summaries, feature-attribution and interpretive-support results, and cross-screen replication outputs in `data/processed/pharmacogenomic_contexts`.
- **Boundary:** predictive modeling and SHAP/feature attribution are interpretive support only; they do not constitute clinical prediction or causal interpretation.

## Phase 7 — Perturbational Hypotheses

**Status:** planned.

- **Objective:** generate perturbational hypotheses from inverse computational associations with consensus programs.
- **Notebook series:** `700`–`703`.
- **Primary inputs:** consensus-program signatures and perturbational resources.
- **Primary outputs:** perturbational hypotheses, candidate compounds, and mechanism-of-action summaries in `data/processed/perturbational_hypotheses`.
- **Boundary:** compound prioritization is limited to perturbational hypothesis generation from inverse computational associations.

## Phase 8 — Orthogonal Validation

**Status:** planned.

- **Objective:** assess cross-dataset replication and orthogonal support in independent biological resources.
- **Notebook series:** `800`–`804`.
- **Primary inputs:** frozen program representations and independent bulk cohorts, Cell Model Passports where applicable, scRNA-seq, ATAC-seq, and other orthogonal resources.
- **Primary outputs:** validation reports, robustness assessments, and cross-resource concordance analyses in `data/processed/validation`.
- **Boundary:** TCGA is the tumor discovery system, not an external validation cohort.

## Phase 9 — Manuscript Preparation

**Status:** planned.

- **Objective:** prepare figures, supplementary materials, methods documentation, and reproducibility packages.
- **Notebook series:** `900`–`904`.
- **Primary inputs:** frozen analytical results from the preceding phases.
- **Primary outputs:** manuscript-ready materials under `results/`.
