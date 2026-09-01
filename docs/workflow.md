# Pan-Cancer Epigenetics: Operational Workflow (v3.1)

This workflow describes the operational sequence for the roadmap v3.1 framework. Provenance, release names, and canonical source filenames are maintained in `config/raw_data_registry.json`; repository paths are maintained in `config/paths.yaml`.

## Phase 0 — Infrastructure and Reproducibility

**Status:** completed.

- **Objective:** maintain an auditable, reproducible repository environment.
- **Primary inputs:** repository configuration, environment definitions, and provenance records.
- **Primary outputs:** version-controlled conventions, source manifests, and reproducible data-tier structure.
- **Handoff:** downstream notebooks consume immutable raw data and reproducible interim layers.

## Phase 1 — Data Acquisition and Auditing

**Status:** implemented; notebook 107 — DepMap RNAi Acquisition and Audit is complete for the historical DEMETER2 resource. The DEMETER2 v5 input combines Achilles, DRIVE, and Marcotte and is acquired, audited, harmonized, and frozen for downstream use; future resources remain dataset-specific.

- **Objective:** inventory, freeze, download, and audit source data required by the implemented analysis.
- **Notebook series:** `100_dataset_inventory`, `101_raw_file_audit`, `102_tcga_rnaseq_cohort_freeze`, `103_tcga_rnaseq_download_validation`, `104_tcga_methylation_coverage_assessment`, `105_tcga_methylation_cohort_freeze`, `106_tcga_methylation_download_validation`, and `107_depmap_rnai_acquisition_and_audit`.
- **Primary inputs:** source datasets, manifests, and `config/raw_data_registry.json`.
- **Primary outputs:** audited source inventory, frozen TCGA RNA-seq and methylation cohorts, download-validation records, and coverage summaries.
- **Handoff:** frozen, audited inputs are supplied to the independent tumor and cell-line discovery phases. Future CTRP, PRISM, LINCS, dependency, drug–target knowledgebase, or other resources require their own acquisition and audit work when needed.

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

**Status:** **ACTIVE — notebook 500 complete/frozen; RNAi prerequisite complete through notebook 107; notebook 501 next**.

- **Objective:** evaluate computational associations between consensus programs and functional dependencies.
- **Notebook series:** `500`–`502`; notebook `500` — CRISPR Associations remains complete/frozen, and notebook `501` — RNAi Associations is next. Its acquisition/audit prerequisite is complete through notebook 107, with 443 frozen models available.
- **Primary inputs:** frozen consensus programs and functional-genomics resources. DepMap Public 24Q4 CRISPR gene effect is an acquired-and-used input through notebook 500; the distinct historical DEMETER2 v5 RNAi resource combines Achilles, DRIVE, and Marcotte.
- **Primary outputs:** putative vulnerability-oriented dependency associations and dependency maps under `data/processed/functional_vulnerabilities`.
- **Boundary / handoff:** notebook 500 provides computational dependency associations and putative functional-vulnerability evidence, not independent biological validation, validated targets, or causal dependencies. RNAi is an orthogonal/complementary layer and must not be naively pooled with CRISPR. Notebook 501 must prespecify gene eligibility and its association-testing framework before inspecting results; later analyses must not retrospectively redefine the frozen Phase 4 consensus representations or completed CRISPR analysis.

## Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI)

**Status:** planned.

- **Objective:** characterize resistance-like pharmacogenomic contexts associated with frozen consensus programs and perform lineage-aware explainable predictive modeling as the explicit XAI component of the project.
- **Notebook series:** `600` Program–Drug Associations; `601` Explainable Predictive Modeling; `602` SHAP Attribution and Stability Analysis; `603` Cross-Screen Replication.
- **Primary inputs:** consensus programs and GDSC, CTRP, and PRISM pharmacogenomic data, acquired and audited for each relevant resource.
- **Primary outputs:** lineage-aware computational association maps, predictive-model performance summaries, SHAP attribution outputs, stability-selection summaries, attribution-sensitivity analyses, and cross-screen replication results under `data/processed/pharmacogenomic_contexts`.
- **Modeling requirements:** random pan-cancer splits are prohibited; lineage-aware or grouped evaluation is mandatory; preprocessing and feature selection must be fitted within training partitions; cell-line-overlap and drug-family leakage must be controlled; transparent baselines must accompany more flexible models.
- **XAI boundary:** SHAP and related feature-attribution methods explain model behavior. They do not establish causal mechanisms, validated biomarkers, therapeutic targets, or clinical prediction. XAI interpretation is only meaningful for models with adequate and transparently reported predictive validity.

## Phase 7 — Perturbational Hypotheses

**Status:** planned.

- **Objective:** generate perturbational hypotheses from inverse computational associations with consensus programs.
- **Notebook series:** `700`–`703`.
- **Primary inputs:** consensus-program signatures and perturbational resources.
- **Primary outputs:** perturbational hypotheses, candidate compounds, and mechanism-of-action summaries in `data/processed/perturbational_hypotheses`.
- **Boundary:** compound prioritization in this phase is limited to perturbational hypothesis generation from inverse computational associations. It is not the final cross-evidence therapeutic prioritization step.

## Phase 8 — Orthogonal Validation

**Status:** planned.

- **Objective:** assess cross-dataset replication and orthogonal support in independent biological resources.
- **Notebook series:** `800`–`804`.
- **Primary inputs:** frozen program representations and independent bulk cohorts, Cell Model Passports where applicable, scRNA-seq, ATAC-seq, and other orthogonal resources.
- **Primary outputs:** validation reports, robustness assessments, and cross-resource concordance analyses in `data/processed/validation`.
- **Boundary:** TCGA is the tumor discovery system, not an external validation cohort.

## Phase 9 — Integrated Evidence Synthesis and Therapeutic Prioritization

**Status:** planned.

- **Objective:** integrate frozen evidence from the epigenetic-regulatory, functional-genomics, pharmacogenomic/XAI, perturbational, and external-validation layers into a transparent program–vulnerability–compound evidence framework.
- **Notebook series:** `900` Target–Drug Knowledgebase Mapping; `901` Cross-Evidence Integration; `902` Candidate Evidence Stratification; `903` Program–Vulnerability–Compound Map; `904` Final Candidate Catalog and Handoff.
- **Primary inputs:** frozen outputs from Phases 4–8 plus prespecified drug–target knowledgebase resources such as ChEMBL and DrugBank where accessible.
- **Primary outputs:** target–drug mappings, cross-evidence matrices, multidimensional candidate evidence strata, integrated program–vulnerability–compound maps, and a frozen manuscript-facing candidate catalog under `data/processed/integrated_evidence`.
- **Boundary:** evidence sources remain traceable and must not be naively pooled as interchangeable evidence. Prefer explicit multidimensional evidence over an opaque single score. Convergent computational evidence supports prioritization and hypothesis generation only; it does not establish therapeutic efficacy or validated targets.

## Phase 10 — Manuscript Preparation

**Status:** planned.

- **Objective:** prepare figures, supplementary materials, methods documentation, reproducibility packages, and manuscript drafts.
- **Notebook series:** `1000`–`1004`.
- **Primary inputs:** frozen analytical results from the preceding phases.
- **Primary outputs:** manuscript-ready materials under `results/`.
