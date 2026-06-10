# MODELING_POLICY.md

## 1. Purpose & Scope

This document establishes the mandatory methodological principles, evaluation constraints, leakage-prevention safeguards, robustness requirements, and interpretive boundaries governing the Pan-Cancer Epigenetics Framework.

The objectives of this policy are to:

* maintain rigorous statistical and computational standards,
* prevent biological overinterpretation,
* minimize technical artifacts and confounding,
* ensure reproducibility across datasets and environments,
* preserve conceptual consistency across all analytical layers.

Compliance with this document is mandatory for all downstream analyses.

---

# 2. Scientific Positioning

This framework is explicitly designed as:

> a computational oncology framework for identifying recurrent epigenetic-transcriptomic programs and evaluating their associations with functional, pharmacogenomic, and perturbational contexts.

The framework is not designed as:

* a clinical prediction system,
* a causal inference framework,
* a therapeutic recommendation engine,
* a resistance forecasting model,
* a reconstruction of adaptive evolutionary trajectories.

All findings must be interpreted as computational associations requiring further validation.

---

# 3. Central Modeling Philosophy

The primary objective of modeling within this project is not maximal predictive performance.

The primary objective is:

> identification of biologically interpretable and reproducible epigenetic-transcriptomic programs.

Priority hierarchy:

| Priority | Preferred Characteristics          |
| -------- | ---------------------------------- |
| Highest  | Biological interpretability        |
| Highest  | Cross-dataset reproducibility      |
| Highest  | Lineage-aware robustness           |
| High     | Confounder resistance              |
| Moderate | Statistical predictive performance |
| Low      | Black-box optimization             |
| Low      | Clinical deployment readiness      |

A simpler and interpretable model with robust biological consistency is preferred over a more accurate but opaque model.

---

# 4. Central Biological Entity

All analyses should be centered on:

> recurrent epigenetic-transcriptomic programs.

These programs may include:

* DNA methylation architectures,
* methylation-expression coupling,
* epigenetic regulator activity states,
* transcriptomic modules,
* pathway-level biological representations.

Programs should not be interpreted as:

* causal mechanisms,
* master regulators,
* validated biomarkers,
* clinically actionable entities.

---

# 5. Permitted vs Prohibited Claims

## Permitted Claims

* recurrence of epigenetic-transcriptomic programs,
* methylation-expression associations,
* associations with resistance-like contexts,
* associations with functional dependencies,
* candidate vulnerability hypotheses,
* perturbational hypotheses,
* cross-dataset reproducibility.

## Prohibited Claims

* direct clinical resistance prediction,
* therapeutic efficacy prediction,
* mechanistic causality,
* validated repurposing claims,
* adaptive resistance reconstruction,
* universal pan-cancer mechanisms without lineage-aware validation.

---

# 6. Dataset-Specific Roles

## TCGA

Permitted:

* program discovery,
* methylation-expression integration,
* epigenetic architecture characterization,
* lineage-aware stratification.

Prohibited:

* resistance labeling,
* treatment-response prediction,
* temporal trajectory inference.

---

## DepMap / CCLE

Permitted:

* program projection,
* dependency associations,
* vulnerability prioritization.

Limitations:

* culture artifacts,
* lineage distortion,
* absence of tumor microenvironment.

---

## GDSC / CTRP / PRISM

Permitted:

* resistance-like context characterization,
* pharmacogenomic association analyses,
* cross-screen validation.

Prohibited:

* clinical efficacy inference.

---

## LINCS / CMap

Permitted:

* perturbational hypothesis generation,
* inverse-signature analyses,
* compound prioritization.

Prohibited:

* claims of therapeutic reversal.

---

## Single-Cell & ATAC Resources

Permitted:

* orthogonal validation,
* chromatin-context evaluation,
* subpopulation enrichment analyses.

Prohibited:

* primary discovery engine,
* causal proof.

---

# 7. Robustness & Validation Requirements

All major findings must undergo evaluation across multiple robustness dimensions.

Mandatory evaluations include:

* lineage-aware analyses,
* cross-dataset replication,
* confounder sensitivity analyses,
* stability analyses,
* negative controls,
* permutation tests,
* failure-case documentation.

Where appropriate, additional evaluations may include:

* Leave-One-Lineage-Out analyses,
* external validation cohorts,
* transcriptomic representation robustness,
* perturbational reproducibility.

No single validation strategy is considered sufficient in isolation.

---

# 8. Confounder Control Policy

Every candidate program must be evaluated against:

## Biological Confounders

* lineage,
* proliferation,
* tumor purity,
* stromal infiltration,
* immune infiltration,
* cell-stress responses.

## Technical Confounders

* batch structure,
* sequencing depth,
* processing center,
* platform effects.

Programs failing confounder assessments must be:

* classified as lineage-restricted,
* or classified as unresolved confounded signals.

Such programs must not be presented as cross-cancer entities.

---

# 9. Interpretability Policy

Interpretability methods are used exclusively for:

* prioritization,
* biological interpretation,
* hypothesis generation.

Methods may include:

* SHAP,
* feature importance analyses,
* latent-factor inspection,
* enrichment analyses.

Interpretability outputs do not constitute evidence of causality.

---

# 10. Drug Response Policy

Drug-response analyses must be interpreted as:

> associations between molecular programs and baseline pharmacogenomic contexts.

Drug-response metrics:

* LN_IC50
* AUC
* related viability metrics

must not be interpreted as direct measurements of clinical resistance.

Compound prioritization remains hypothesis-generating.

---

# 11. Negative Results Policy

Negative findings represent valid scientific outputs.

The following must be documented:

* failed replications,
* unstable programs,
* lineage-specific failures,
* cross-dataset inconsistencies,
* sensitivity to preprocessing choices.

Negative evidence is considered equally important as positive findings.

---

# 12. Technical Reproducibility Standards

All analyses must:

* maintain version-controlled preprocessing,
* preserve data provenance,
* use deterministic execution whenever possible,
* document software environments,
* maintain strict separation between raw, interim, and processed data.

Undocumented manual interventions are prohibited.

---

# 13. Success Criteria

The framework will be considered scientifically successful if it identifies:

1. recurrent epigenetic-transcriptomic programs reproducible across independent cohorts;
2. robust methylation-expression architectures;
3. candidate functional vulnerabilities associated with these programs;
4. reproducible resistance-like pharmacogenomic contexts;
5. coherent perturbational hypotheses.

Success does not require:

* clinical deployment,
* biomarker qualification,
* therapeutic validation,
* mechanistic proof,
* universal pan-cancer applicability.

The primary deliverable is a reproducible and biologically interpretable map of recurrent epigenetic-transcriptomic programs across human cancers.
