# MODELING_POLICY.md

## 1. Purpose and Scope

This mandatory policy establishes methodological principles, evaluation constraints, leakage-prevention safeguards, robustness requirements, XAI requirements, and interpretive boundaries for the Pan-Cancer Epigenetics Framework. It applies to all phases and modalities.

The framework is a computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, explainable predictive-model behavior, perturbational hypotheses, and integrated therapeutic-prioritization evidence. It is not a clinical predictor, causal inference framework, adaptive-resistance reconstruction, pipeline for discovering definitive biomarkers, pipeline for validating treatment targets, or therapeutic-efficacy engine.

All findings are computational associations requiring further validation. Experimental validation belongs to the broader approved scientific project but is intentionally outside this repository.

---

# 2. Central Modeling Philosophy

The primary objective is not maximal predictive performance. It is the identification and characterization of biologically interpretable, robust, reproducible, and transparently explainable candidate programs and associations.

| Priority | Preferred characteristic |
| --- | --- |
| Highest | Biological interpretability |
| Highest | Internal robustness within the relevant system |
| Highest | Leakage prevention and lineage-aware evaluation |
| High | Cross-system reproducibility where applicable |
| High | Cross-dataset or external replication when elevating evidence |
| High | Transparent and stable model attribution where predictive modeling is used |
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

## Phase 5 — Functional Vulnerability Characterization

CRISPR and RNAi data characterize associations between frozen consensus programs and functional dependency profiles. These are putative-vulnerability associations, not validated dependencies or targets.

## Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI)

GDSC, CTRP, and PRISM characterize resistance-like pharmacogenomic contexts and provide the outcomes for prespecified explainable predictive modeling. Phase 6 contains the explicit XAI component of the project, including SHAP feature attribution and stability analysis after model validity and evaluation design are established.

## Phase 7 — Perturbational Hypotheses

LINCS or CMap generate inverse-signature perturbational hypotheses. These analyses do not establish therapeutic reversal or efficacy.

## Phase 8 — Orthogonal and External Validation

Independent resources support cross-dataset replication or orthogonal contextual evidence. This computational validation layer is distinct from experimental validation outside the repository.

## Phase 9 — Integrated Evidence Synthesis and Therapeutic Prioritization

Frozen evidence from Phases 4–8 is integrated into a transparent program–vulnerability–compound framework. Evidence dimensions remain separately traceable; convergence supports computational prioritization only.

## Phase 10 — Manuscript Preparation

Only frozen analytical outputs may feed manuscript assembly. Manuscript preparation must not redefine analytical eligibility, models, programs, or evidence strata after inspection of publication-facing results.

---

# 4. Robustness, Reproducibility, and Replication

These evidence categories are distinct and must not be conflated.

## Internal Robustness

Internal robustness evaluates whether a candidate representation is stable and interpretable within its own discovery system. Examples include notebook 206 for tumor programs and notebook 311 for cell-line programs.

Depending on the phase and available data, evaluations can include lineage-aware analysis, bootstrap procedures, leave-one-project-out or leave-one-lineage-out analyses, covariate sensitivity, negative controls, permutation tests, and failure documentation. Internal robustness is not independent validation.

## Cross-System Reproducibility

Phase 4 evaluates tumor–cell-line reproducibility after independent discovery through explicit multiview matching and possible consensus construction. This evidence is computational and does not establish biological validation or causality.

## Cross-Screen Reproducibility

Phase 6 evaluates whether pharmacogenomic associations and model behavior replicate across GDSC, CTRP, and PRISM where drug and model coverage permit. Cross-screen replication must explicitly account for non-independence caused by overlapping cell lines, related compounds, shared drug families, and shared upstream molecular features.

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

Random pan-cancer train/test splits are prohibited.

Analyses must evaluate and prevent, where relevant:

* lineage leakage;
* platform leakage;
* drug-family leakage;
* cell-line-overlap leakage;
* preprocessing leakage;
* post-split feature-selection leakage;
* perturbational leakage; and
* reuse of downstream evidence to redefine upstream frozen objects.

For predictive modeling, preprocessing, scaling, imputation, feature selection, hyperparameter tuning, and any data-driven transformation must be fitted exclusively within the training partition or within properly nested resampling. External screens used for replication must not influence training choices intended to be evaluated on those same screens.

The discovery phases must remain independent: no tumor-derived program identity, ranking, or matching result can select Phase 3 components. Cross-system operations are restricted to Phase 4 or later.

---

# 7. Explainable AI and SHAP Policy

Explainable artificial intelligence is an explicit analytical component of this project and is operationalized in Phase 6.

## 7.1 Preconditions for XAI

SHAP or other feature-attribution methods must not be treated as a substitute for model validation. Attribution analysis is scientifically interpretable only after:

* the prediction target has been defined without leakage;
* the feature universe has been prespecified or selected within training data only;
* evaluation partitions are lineage-aware or otherwise appropriately grouped;
* model performance is reported against transparent baselines; and
* major leakage and confounding risks have been assessed.

Models with inadequate or unstable predictive validity may still be reported as negative results, but their SHAP patterns must not be promoted as biological findings.

## 7.2 Required XAI Components

Where model class and data coverage permit, Phase 6 should evaluate:

* global SHAP attribution;
* local SHAP attribution only when it addresses a prespecified scientific question;
* attribution stability across resampling partitions;
* attribution consistency across lineages;
* attribution consistency across pharmacogenomic screens;
* sensitivity of feature ranking to model class; and
* agreement or disagreement between SHAP and simpler model coefficients or effect estimates.

## 7.3 Interpretation Boundary

SHAP values explain a fitted model's predictions conditional on the model, features, data distribution, and attribution assumptions. They do **not** demonstrate:

* biological causality;
* mechanistic regulation;
* therapeutic dependency;
* clinical predictiveness;
* validated biomarker status; or
* therapeutic efficacy.

SHAP must never be described as identifying a master regulator or causal driver. It can support prioritization, model interpretation, and hypothesis generation only.

---

# 8. Integrated Evidence Policy

Phase 9 combines evidence generated by different analytical modalities, but those modalities must remain separately traceable.

Functional-genomics associations, pharmacogenomic associations, XAI attributions, perturbational inverse signatures, drug–target knowledgebase mappings, and external replication are not interchangeable measurements and must not be naively pooled.

The preferred integration strategy is a multidimensional evidence matrix or prespecified evidence strata. A single composite score may be used only if its construction, weighting, missing-data handling, and sensitivity analysis are defined before inspecting candidate rankings and if the score does not obscure conflicting evidence.

Downstream convergence must never be used to retrospectively rescue, redefine, reweight, or exclude the frozen Phase 4 consensus programs or earlier prespecified hypothesis families.

---

# 9. Interpretability and Claim Boundaries

Permitted language includes recurrent program, candidate program, resistance-like context, putative vulnerability, computational association, explainable model attribution, perturbational hypothesis, integrated evidence, internal robustness, cross-system reproducibility, and cross-dataset replication.

Feature-attribution methods such as SHAP, feature importance, latent-factor inspection, and enrichment analysis are exclusively interpretive or predictive-attribution tools. They support prioritization, biological interpretation, and hypothesis generation; they are not evidence of causality.

Drug-response analyses describe associations with baseline pharmacogenomic contexts. Relative drug insensitivity in a screen must not be interpreted as direct measurement of clinical resistance. Perturbational analyses must not be described as proof that a therapy-resistant context can be reversed.

Integrated program–vulnerability–compound evidence may support computational prioritization but must not be labeled as validated therapeutic targeting.

---

# 10. Technical Reproducibility and Negative Results

All analyses must maintain version-controlled preprocessing, data provenance, deterministic execution where possible, documented software environments, and strict separation of raw, interim, and processed data. Undocumented manual interventions are prohibited.

Negative findings are valid outputs. Failed replications, unstable programs, weak predictive performance, unstable SHAP attribution, lineage-specific failures, cross-dataset inconsistencies, preprocessing sensitivity, and unresolved confounding must be documented.
