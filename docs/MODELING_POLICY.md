# MODELING_POLICY.md

## 1. Purpose and Scope

This mandatory policy establishes methodological principles, evaluation constraints, leakage-prevention safeguards, robustness requirements, secondary molecular-characterization requirements, XAI requirements, and interpretive boundaries for the Pan-Cancer Epigenetics Framework. It applies to all phases and modalities.

The framework is a computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, secondary genomic and locus-level molecular context, functional vulnerabilities, explainable predictive-model behavior, perturbational hypotheses, and integrated therapeutic-prioritization evidence. It is not a clinical predictor, causal inference framework, adaptive-resistance reconstruction, pipeline for discovering definitive biomarkers, pipeline for validating treatment targets, or therapeutic-efficacy engine.

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

The central analytical entity is the recurrent epigenetic-transcriptomic program. Programs may include DNA-methylation architectures, methylation-expression coupling, epigenetic-regulator activity, transcriptomic modules, and pathway-level representations. Somatic mutations and locus-level methylation-expression relationships may be used to characterize frozen programs but do not redefine the primary discovery object. Programs are not assumed to be master regulators, causal explanations, validated biomarkers, or clinically actionable entities.

---

# 3. Phase and Dataset Roles

## Phase 2 — Tumor Discovery

TCGA RNA-seq and DNA methylation support independent tumor program discovery, multi-omic integration, lineage-aware assessment, and tumor-specific internal robustness.

## Phase 3 — Cell-Line Discovery

DepMap and CCLE expression resources support independent cell-line transcriptomic program discovery. Cell-line latent-program extraction is phenotype-independent, and its representation must be frozen before a predefined GDSC resistance-like pharmacogenomic phenotype is introduced for downstream association testing and candidate characterization. Tumor program identities, tumor–cell-line matching, tumor rankings, and Phase 2 information must not select cell-line discovery components.

## Phase 4 — Cross-System Reproducibility

Tumor–cell-line comparison, multiview matching, and consensus construction occur only after both candidate universes are frozen. “Not recoverable” is a valid result; component indices are not presumed portable.

## Phase 4B — Secondary Molecular Context Characterization

A single audited TCGA/GDC somatic-mutation resource and the frozen TCGA methylation/expression layers characterize the genomic and locus-level regulatory context of already frozen programs. Phase 4B is post-discovery characterization and cannot feed back into Phase 2–4 selection or consensus construction.

## Phase 5 — Functional Vulnerability Characterization

CRISPR and RNAi data characterize associations between frozen consensus programs and functional dependency profiles. These are putative-vulnerability associations, not validated dependencies or targets.

## Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI)

GDSC, CTRP, and PRISM characterize resistance-like pharmacogenomic contexts and provide the outcomes for prespecified explainable predictive modeling. Phase 6 contains the explicit XAI component of the project, including SHAP feature attribution and stability analysis after model validity and evaluation design are established.

## Phase 7 — Perturbational Hypotheses

LINCS or CMap generate inverse-signature perturbational hypotheses. These analyses do not establish therapeutic reversal or efficacy.

## Phase 8 — Orthogonal and External Validation

Independent resources support cross-dataset replication or orthogonal contextual evidence. This computational validation layer is distinct from experimental validation outside the repository.

## Phase 9 — Integrated Evidence Synthesis and Therapeutic Prioritization

Frozen evidence from Phase 4, Phase 4B, and Phases 5–8 is integrated into a transparent program–vulnerability–compound framework. Evidence dimensions remain separately traceable; convergence supports computational prioritization only.

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

## Secondary Molecular Context

Phase 4B evaluates whether frozen programs have interpretable somatic genomic contexts or locus-level methylation-expression relationships. This evidence is characterization, not independent validation and not a criterion for maintaining program eligibility.

A lack of robust recurrent mutation association or locus-level methylation-expression relationship is a valid result and must not be treated as failure of the frozen program itself.

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

## Secondary Somatic-Mutation Analyses

Evaluate, where applicable:

* lineage/project structure;
* mutation prevalence and sparse-event instability;
* caller/workflow provenance;
* case/sample mapping;
* sequencing/coverage comparability when required by the chosen summary;
* multiple-testing burden; and
* pathway or driver-annotation provenance.

A pooled pan-cancer mutation association cannot be interpreted as recurrent unless it remains supported after lineage-aware evaluation. Mutation-burden summaries require a prespecified and technically defensible denominator/definition; they must not be improvised after inspecting associations.

## Locus-Level Methylation–Expression Analyses

Evaluate, where applicable:

* lineage/project structure;
* methylation platform;
* probe-to-gene/promoter annotation uncertainty;
* tumor purity;
* expression and methylation technical factors;
* probe coverage and missingness; and
* multiplicity across CpG–gene relationships.

Inverse methylation-expression association is compatible with regulatory coupling but does not establish direct epigenetic regulation. Promoter annotation must be defined before result-driven filtering.

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
* perturbational leakage;
* result-driven genomic annotation or mutation-burden definition;
* result-driven CpG/promoter annotation filtering; and
* reuse of downstream evidence to redefine upstream frozen objects.

For predictive modeling, preprocessing, scaling, imputation, feature selection, hyperparameter tuning, and any data-driven transformation must be fitted exclusively within the training partition or within properly nested resampling. External screens used for replication must not influence training choices intended to be evaluated on those same screens.

The discovery phases must remain independent: no tumor-derived program identity, ranking, or matching result can select Phase 3 components. Cross-system operations are restricted to Phase 4 or later.

Phase 4B is explicitly downstream of the Phase 4 freeze. Mutation or locus-level methylation-expression results cannot rescue, exclude, reorient, reweight, rename, or redefine Phase 4 programs.

---

# 7. Secondary Molecular Characterization Policy

## 7.1 Somatic Mutation Resource Policy

Notebook 108 must acquire and audit one prespecified TCGA/GDC somatic-mutation resource before notebook 450 is implemented.

Required provenance includes, at minimum:

* source and release/access date;
* mutation-calling or aggregation workflow identity;
* sample and case identifiers;
* compatibility with the frozen TCGA cohort;
* duplicate/multi-sample handling; and
* inclusion/exclusion rules.

Mutation calls from different callers or workflows must not be naively pooled to increase coverage.

## 7.2 Genomic-Context Analysis Policy

Notebook 450 is characterization of frozen programs, not genomic program discovery.

Allowed analysis families may include:

* prespecified driver-gene mutation status;
* prespecified pathway-level mutation context;
* lineage-aware mutation–program associations;
* heterogeneity analysis across projects/lineages; and
* mutation-burden summaries only when prespecified and technically defensible.

Copy-number alterations are outside the default scope and require a separate documented justification if later added.

Negative, sparse, unstable, lineage-specific, or heterogeneous results are valid outcomes.

## 7.3 Locus-Level Methylation–Expression Policy

Notebook 451 may characterize CpG-to-gene relationships relevant to frozen programs using prespecified genomic annotations.

Allowed analysis families may include:

* promoter CpG–gene expression association;
* other annotated regulatory CpG–gene relationships when prespecified;
* inverse methylation-expression relationships;
* lineage-aware or project-stratified effect estimation; and
* sensitivity analyses for platform, purity, and annotation coverage.

The analysis must not create resistant versus sensitive TCGA tumor labels solely to reproduce the wording of the approved proposal. TCGA does not provide a defensible universal resistance ground truth for that purpose.

Observed inverse relationships may be described as compatible with epigenetic regulatory coupling. They must not be described as proving gene silencing, direct regulation, or causal mediation.

## 7.4 Publication and Freeze Boundary

Phase 4B analyses are part of the research program but are not publication obligations. If they are uninformative, they may remain as documented reproducible analyses without appearing in a primary paper.

No Phase 4B result may alter the identity or eligibility of the frozen Phase 4 programs.

---

# 8. Explainable AI and SHAP Policy

Explainable artificial intelligence is an explicit analytical component of this project and is operationalized in Phase 6.

## 8.1 Preconditions for XAI

SHAP or other feature-attribution methods must not be treated as a substitute for model validation. Attribution analysis is scientifically interpretable only after:

* the prediction target has been defined without leakage;
* the feature universe has been prespecified or selected within training data only;
* evaluation partitions are lineage-aware or otherwise appropriately grouped;
* model performance is reported against transparent baselines; and
* major leakage and confounding risks have been assessed.

Models with inadequate or unstable predictive validity may still be reported as negative results, but their SHAP patterns must not be promoted as biological findings.

## 8.2 Required XAI Components

Where model class and data coverage permit, Phase 6 should evaluate:

* global SHAP attribution;
* local SHAP attribution only when it addresses a prespecified scientific question;
* attribution stability across resampling partitions;
* attribution consistency across lineages;
* attribution consistency across pharmacogenomic screens;
* sensitivity of feature ranking to model class; and
* agreement or disagreement between SHAP and simpler model coefficients or effect estimates.

## 8.3 Interpretation Boundary

SHAP values explain a fitted model's predictions conditional on the model, features, data distribution, and attribution assumptions. They do **not** demonstrate:

* biological causality;
* mechanistic regulation;
* therapeutic dependency;
* clinical predictiveness;
* validated biomarker status; or
* therapeutic efficacy.

SHAP must never be described as identifying a master regulator or causal driver. It can support prioritization, model interpretation, and hypothesis generation only.

---

# 9. Integrated Evidence Policy

Phase 9 combines evidence generated by different analytical modalities, but those modalities must remain separately traceable.

Secondary genomic context, locus-level methylation-expression associations, functional-genomics associations, pharmacogenomic associations, XAI attributions, perturbational inverse signatures, drug–target knowledgebase mappings, and external replication are not interchangeable measurements and must not be naively pooled.

The preferred integration strategy is a multidimensional evidence matrix or prespecified evidence strata. A single composite score may be used only if its construction, weighting, missing-data handling, and sensitivity analysis are defined before inspecting candidate rankings and if the score does not obscure conflicting evidence.

Downstream convergence must never be used to retrospectively rescue, redefine, reweight, or exclude the frozen Phase 4 consensus programs or earlier prespecified hypothesis families.

---

# 10. Interpretability and Claim Boundaries

Permitted language includes recurrent program, candidate program, resistance-like context, secondary genomic context, locus-level methylation-expression association, putative vulnerability, computational association, explainable model attribution, perturbational hypothesis, integrated evidence, internal robustness, cross-system reproducibility, and cross-dataset replication.

Feature-attribution methods such as SHAP, feature importance, latent-factor inspection, and enrichment analysis are exclusively interpretive or predictive-attribution tools. They support prioritization, biological interpretation, and hypothesis generation; they are not evidence of causality.

Drug-response analyses describe associations with baseline pharmacogenomic contexts. Relative drug insensitivity in a screen must not be interpreted as direct measurement of clinical resistance. Perturbational analyses must not be described as proof that a therapy-resistant context can be reversed.

Somatic-mutation associations are contextual genomic evidence, not proof of a genomic driver of a program. Inverse methylation-expression associations are compatible with regulatory coupling, not proof of causal epigenetic silencing.

Integrated program–vulnerability–compound evidence may support computational prioritization but must not be labeled as validated therapeutic targeting.

---

# 11. Technical Reproducibility and Negative Results

All analyses must maintain version-controlled preprocessing, data provenance, deterministic execution where possible, documented software environments, and strict separation of raw, interim, and processed data. Undocumented manual interventions are prohibited.

Negative findings are valid outputs. Failed replications, unstable programs, weak predictive performance, unstable SHAP attribution, lineage-specific failures, absent recurrent genomic associations, absent or heterogeneous methylation-expression coupling, cross-dataset inconsistencies, preprocessing sensitivity, and unresolved confounding must be documented.
