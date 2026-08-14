# MODELING_POLICY.md

## 1. Purpose and Scope

This mandatory policy establishes methodological principles, evaluation constraints, leakage-prevention safeguards, robustness requirements, and interpretive boundaries for the Pan-Cancer Epigenetics Framework. It applies to all phases and modalities.

The framework is a computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational hypotheses. It is not a clinical predictor, causal inference framework, adaptive-resistance reconstruction, pipeline for discovering biomarkers, pipeline for discovering treatment targets, or drug-repurposing engine.

All findings are computational associations requiring further validation.

---

# 2. Central Modeling Philosophy

The primary objective is not maximal predictive performance. It is the identification of biologically interpretable, robust, and reproducible candidate programs.

| Priority | Preferred characteristic |
| --- | --- |
| Highest | Biological interpretability |
| Highest | Internal robustness within the relevant system |
| Highest | Leakage prevention and lineage-aware evaluation |
| High | Cross-system reproducibility where applicable |
| High | Cross-dataset or external replication when elevating evidence |
| Moderate | Statistical predictive performance |
| Low | Black-box optimization or clinical deployment readiness |

The central analytical entity is the recurrent epigenetic-transcriptomic program. Programs may include DNA-methylation architectures, methylation-expression coupling, epigenetic-regulator activity, transcriptomic modules, and pathway-level representations. They are not assumed to be master regulators, causal explanations, validated biomarkers, or clinically actionable entities.

---

# 3. Phase and Dataset Roles

## Phase 2 — Tumor Discovery

TCGA RNA-seq and DNA methylation support independent tumor program discovery, multi-omic integration, lineage-aware assessment, and tumor-specific internal robustness.

## Phase 3 — Cell-Line Discovery

DepMap and CCLE expression resources support independent cell-line transcriptomic program discovery. Cell-line latent-program extraction is phenotype-independent, and its representation must be frozen before a predefined GDSC resistance-like pharmacogenomic phenotype is introduced for downstream association testing and candidate characterization. Tumor program identities, tumor–cell-line matching, tumor rankings, and Phase 2 information must not select cell-line discovery components.

## Phase 4 — Cross-System Reproducibility

Tumor–cell-line comparison, multiview matching, and consensus construction occur only after both candidate universes are frozen. “Not recoverable” is a valid result; component indices are not presumed portable.

## Phases 5–8 — Downstream Characterization and Validation

Phase 5 uses CRISPR and RNAi data for functional-vulnerability characterization. Phase 6 characterizes pharmacogenomic contexts using GDSC, CTRP, and PRISM. Phase 7 generates perturbational hypotheses with LINCS or CMap. Phase 8 evaluates cross-dataset replication and orthogonal support. No downstream association establishes clinical efficacy or causality.

---

# 4. Robustness, Reproducibility, and Replication

These evidence categories are distinct and must not be conflated.

## Internal Robustness

Internal robustness evaluates whether a candidate representation is stable and interpretable within its own discovery system. Examples include notebook 206 for tumor programs and notebook 311 for cell-line programs.

Depending on the phase and available data, evaluations can include lineage-aware analysis, bootstrap procedures, leave-one-project-out or leave-one-lineage-out analyses, covariate sensitivity, negative controls, permutation tests, and failure documentation. Internal robustness is not independent validation.

## Cross-System Reproducibility

Phase 4 evaluates tumor–cell-line reproducibility after independent discovery through explicit multiview matching and possible consensus construction. This evidence is computational and does not establish biological validation or causality.

## Cross-Dataset and External Replication

Cross-dataset replication, particularly in Phase 8, is required to elevate the level of evidence for a finding. It is not a prerequisite that must already have been met by the individual discovery or within-system robustness notebook.

Failed replication, partial correspondence, instability, and “not recoverable” outcomes must be reported.

---

# 5. Confounder Control Policy

Every relevant analysis must document its applicable confounders, available representations, sensitivity analyses, and unresolved limitations.

## Tumor Analyses

Evaluate, where applicable:

* lineage and project structure;
* purity;
* immune and stromal infiltration;
* proliferation; and
* technical, batch, and platform factors.

## Cell-Line Analyses

Evaluate, where applicable:

* lineage;
* available biological, culture, and provenance metadata;
* pharmacological ascertainment when relevant;
* technical factors; and
* proliferation when a valid frozen representation exists.

If a relevant covariate is unavailable in a previously defined and defensible form, the limitation must be reported as unresolved confounding. Covariates must not be constructed post hoc solely to remove a limitation.

Signals that remain technically confounded or unresolved must be downgraded and must not be represented as cross-cancer recurrent programs merely because they receive partial supporting evidence.

---

# 6. Leakage Prevention

Random pan-cancer train/test splits are prohibited. Analyses must evaluate and prevent lineage, platform, drug-family, cell-line-overlap, feature-selection, and perturbational leakage.

The discovery phases must remain independent: no tumor-derived program identity, ranking, or matching result can select Phase 3 components. Cross-system operations are restricted to Phase 4 or later.

---

# 7. Interpretability and Claim Boundaries

Permitted language includes recurrent program, candidate program, resistance-like context, putative vulnerability, computational association, perturbational hypothesis, internal robustness, cross-system reproducibility, and cross-dataset replication.

Feature-attribution methods such as SHAP, feature importance, latent-factor inspection, and enrichment analysis are exclusively interpretive or predictive-attribution tools. They support prioritization, biological interpretation, and hypothesis generation; they are not evidence of causality.

Drug-response analyses describe associations with baseline pharmacogenomic contexts. Relative drug insensitivity in a screen must not be interpreted as direct measurement of clinical resistance. Perturbational analyses must not be described as proof that a therapy-resistant context can be reversed.

---

# 8. Technical Reproducibility and Negative Results

All analyses must maintain version-controlled preprocessing, data provenance, deterministic execution where possible, documented software environments, and strict separation of raw, interim, and processed data. Undocumented manual interventions are prohibited.

Negative findings are valid outputs. Failed replications, unstable programs, lineage-specific failures, cross-dataset inconsistencies, preprocessing sensitivity, and unresolved confounding must be documented.
