# Pan-Cancer Epigenetics: Operational Workflow (v3.2)

This workflow describes the operational sequence for the roadmap v3.2 framework. Provenance, release names, and canonical source filenames are maintained in `config/raw_data_registry.json`; repository paths are maintained in `config/paths.yaml`.

## Phase 0 — Infrastructure and Reproducibility

**Status:** completed.

- **Objective:** maintain an auditable, reproducible repository environment.
- **Primary inputs:** repository configuration, environment definitions, and provenance records.
- **Primary outputs:** version-controlled conventions, source manifests, and reproducible data-tier structure.
- **Handoff:** downstream notebooks consume immutable raw data and reproducible interim layers.

## Phase 1 — Data Acquisition and Auditing

**Status:** implemented for currently used inputs; notebook 107 — DepMap RNAi Acquisition and Audit is complete, and notebook 108 — TCGA Somatic Mutation Acquisition and Audit is planned as the acquisition prerequisite for Phase 4B.

- **Objective:** inventory, freeze, download, and audit source data required by the implemented or prespecified analysis.
- **Notebook series:** `100_dataset_inventory`, `101_raw_file_audit`, `102_tcga_rnaseq_cohort_freeze`, `103_tcga_rnaseq_download_validation`, `104_tcga_methylation_coverage_assessment`, `105_tcga_methylation_cohort_freeze`, `106_tcga_methylation_download_validation`, `107_depmap_rnai_acquisition_and_audit`, and planned `108_tcga_somatic_mutation_acquisition_and_audit`.
- **Primary inputs:** source datasets, manifests, and `config/raw_data_registry.json`.
- **Primary outputs:** audited source inventory, frozen TCGA RNA-seq and methylation cohorts, download-validation records, RNAi handoffs, coverage summaries, and—after notebook 108—a frozen somatic-mutation resource mapping compatible with the 9,965-case TCGA cohort.
- **Boundary / handoff:** mutation resources require one prespecified caller/workflow identity and explicit case/sample mapping; mutation calls from different pipelines must not be naively combined. Future CTRP, PRISM, LINCS, drug–target knowledgebase, or other resources require their own acquisition and audit work when needed.

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
- **Boundary / handoff:** Phase 4 reopens only for a concrete identified problem. Downstream characterization cannot redefine, rescue, exclude, reweight, reorient, or rename the frozen consensus programs.

## Phase 4B — Secondary Molecular Context Characterization

**Status:** planned.

- **Objective:** characterize frozen program representations through somatic genomic context and locus-level methylation-expression relationships without reopening discovery.
- **Notebook series:** `450` Secondary Genomic Context Characterization; `451` Locus-Level Methylation–Expression Characterization.
- **Primary inputs:** frozen Phase 4 programs; the audited TCGA/GDC somatic-mutation handoff from planned notebook 108; frozen TCGA methylation and RNA-seq data; prespecified CpG-to-gene and promoter/regulatory annotations.
- **Primary outputs:** lineage-aware mutation-context association tables, pathway-level genomic-context summaries, locus-level CpG–gene methylation-expression associations, promoter/regulatory summaries, and explicit negative-result/limitation reports under `data/processed/secondary_characterization`.
- **Genomic boundary:** mutation analyses are secondary characterization. Pan-cancer associations must be evaluated against project/lineage structure. Mutation-burden analyses are optional and require a defensible prespecified definition. Copy-number analysis is outside this block unless separately justified before implementation.
- **Methylation-expression boundary:** inverse promoter methylation-expression associations may be described as compatible with epigenetic regulation but not as mechanistic proof. TCGA tumors are not assigned resistant/sensitive labels for this analysis. Platform coverage, annotation uncertainty, purity, and other applicable confounders remain explicit.
- **Freeze boundary:** Phase 4B cannot modify frozen Phase 4 objects. Positive, negative, lineage-specific, heterogeneous, or non-recurrent outcomes are all valid. Publication is optional; the analysis may remain a documented project result if it does not strengthen a manuscript.

## Phase 5 — Functional Vulnerabilities

**Status:** **ANALYTICAL WORKFLOW COMPLETE THROUGH NOTEBOOK 502; FORMAL ARTIFACT-REGISTRY SYNCHRONIZATION PENDING**.

- **Objective:** evaluate computational associations between consensus programs and functional dependencies while preserving platform-specific evidence and interpretation boundaries.
- **Notebook series:** `500` CRISPR Associations; `501` RNAi Associations; `502` Integrated Vulnerability Mapping. All three analytical notebooks are complete.
- **Primary inputs:** frozen Phase 4 consensus programs; DepMap Public 24Q4 CRISPR gene effect; and the distinct historical DEMETER2 v5 RNAi resource combining Achilles, DRIVE, and Marcotte through the frozen notebook-107 handoff.
- **Primary outputs:** platform-specific CRISPR and RNAi program–dependency association layers, lineage-aware contextual summaries, RNAi prespecified sensitivities, and a platform-aware integrated program × gene evidence map under `data/processed/functional_vulnerabilities`, with the cross-platform gene map under `data/interim/dependencies`.
- **Platform boundary:** CRISPR and RNAi retain separate dependency scales, primary eligibility criteria, FDR families, coverage properties, and model composition. Notebook 502 does not pool dependency scores or regression coefficients, combine p/q values, impose a common post-hoc coverage threshold, recalculate joint cross-platform FDR, or construct a composite vulnerability score or ranking.
- **Concordance boundary:** cross-platform agreement is complementary computational evidence rather than independent validation because biological context and cell-line populations overlap. Single-platform and directionally discordant findings remain valid platform-specific observations and are not discarded or resolved through post-hoc platform preference.
- **Lineage / sensitivity boundary:** lineage-aware summaries and RNAi source-adjusted or ≥90% coverage analyses remain descriptive or sensitivity context only. They do not redefine platform-specific primary significance, eligibility, or cross-platform comparability.
- **Repository handoff:** the analytical outputs are ready for downstream use under their frozen notebook contracts, but formal machine-readable registration of the newly generated Phase 5 derived artifacts must be completed before the phase is declared repository-frozen.

## Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI)

**Status:** planned.

- **Objective:** characterize resistance-like pharmacogenomic contexts associated with frozen consensus programs and perform lineage-aware explainable predictive modeling as the explicit XAI component of the project.
- **Notebook series:** `600` Program–Drug Associations; `601` Explainable Predictive Modeling; `602` SHAP Attribution and Stability Analysis; `603` Cross-Screen Replication.
- **Primary inputs:** consensus programs and GDSC, CTRP, and PRISM pharmacogenomic data, acquired and audited for each relevant resource.
- **Primary outputs:** lineage-aware computational association maps, predictive-model performance summaries, SHAP attribution outputs, stability-selection summaries, hierarchical biological-context tables linking valid model attributions back to frozen program biology, attribution-sensitivity analyses, and cross-screen replication results under `data/processed/pharmacogenomic_contexts`.
- **Modeling requirements:** random pan-cancer splits are prohibited; lineage-aware or grouped evaluation is mandatory; preprocessing and feature selection must be fitted within training partitions; cell-line-overlap and drug-family leakage must be controlled; transparent baselines must accompany more flexible models.
- **XAI biological-context requirement:** attribution must remain at the level of features actually supplied to the fitted model. If the model uses consensus-program scores, SHAP is program-level attribution. Biological interpretation may then map an attributed program to its frozen gene loadings, pathway annotations, epigenetic-regulator context, tumor-side methylation context, and Phase 4B locus-level context where applicable. This downstream mapping is biological contextualization, not additional SHAP evidence. Gene-level SHAP may be reported only for models that actually include gene-level features under the same leakage-safe evaluation design.
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

- **Objective:** integrate frozen evidence from secondary molecular characterization, epigenetic-regulatory, functional-genomics, pharmacogenomic/XAI, perturbational, and external-validation layers into a transparent program–vulnerability–compound evidence framework.
- **Notebook series:** `900` Target–Drug Knowledgebase Mapping; `901` Cross-Evidence Integration; `902` Candidate Evidence Stratification; `903` Program–Vulnerability–Compound Map; `904` Final Candidate Catalog and Handoff.
- **Primary inputs:** frozen outputs from Phase 4, Phase 4B, and Phases 5–8 plus prespecified drug–target knowledgebase resources such as ChEMBL and DrugBank where accessible.
- **Primary outputs:** target–drug mappings, cross-evidence matrices, multidimensional candidate evidence strata, integrated program–vulnerability–compound maps, a frozen manuscript-facing candidate catalog, and a structured computational-to-experimental handoff under `data/processed/integrated_evidence`.
- **Experimental-handoff requirement:** notebook 904 should preserve, for each retained candidate relationship where information exists, the frozen program identity, putative vulnerability or target context, candidate compound and mechanism/target annotation, expected association or perturbational direction, functional-genomics support, pharmacogenomic support, XAI attribution/stability context, perturbational support, target–drug support, secondary molecular context, lineage breadth/heterogeneity, external or orthogonal support, unresolved limitations, and a concise computational rationale for possible downstream experimental evaluation. Sarcoma, RMS, or OS relevance may be annotated when the available datasets directly support it; absence of such evidence must remain explicit rather than inferred.
- **Boundary:** evidence sources remain traceable and must not be naively pooled as interchangeable evidence. Prefer explicit multidimensional evidence over an opaque single score. Convergent computational evidence supports prioritization and hypothesis generation only; it does not establish therapeutic efficacy or validated targets. The handoff is not a therapeutic recommendation, assay prescription, dosing recommendation, or substitute for experimental design.

## Phase 10 — Manuscript Preparation

**Status:** planned.

- **Objective:** prepare figures, supplementary materials, methods documentation, reproducibility packages, and manuscript drafts.
- **Notebook series:** `1000`–`1004`.
- **Primary inputs:** frozen analytical results from the preceding phases.
- **Primary outputs:** manuscript-ready materials under `results/`.
