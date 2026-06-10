# PROJECT_ARCHITECTURE.md

## Project Overview

This project aims to develop a lineage-aware computational oncology framework to identify recurrent epigenetic-transcriptomic programs across multiple cancer types and evaluate their associations with resistance-like pharmacogenomic contexts, candidate functional vulnerabilities, and perturbational hypotheses.

The framework integrates public multi-omic, pharmacogenomic, dependency, and perturbational datasets while prioritizing:

* biological interpretability,
* reproducibility,
* lineage-aware evaluation,
* conservative scientific framing,
* cross-dataset consistency.

The framework is not intended to:

* predict clinical outcomes,
* infer causal biological mechanisms,
* reconstruct adaptive evolutionary trajectories,
* establish therapeutic efficacy.

All findings should be interpreted as computational associations and candidate hypotheses requiring future validation.

---

# Core Scientific Question

Can recurrent epigenetic-transcriptomic programs be identified through the integration of DNA methylation, epigenetic regulator activity, and transcriptomic states across human tumors, and are these programs associated with:

* resistance-like pharmacogenomic contexts,
* candidate functional vulnerabilities,
* perturbational signatures suggestive of program suppression?

---

# Conceptual Framework

The project is organized into four biological and analytical layers.

```text
[ Layer 1: Tumor Epigenetic-Transcriptomic Discovery ]
                     (TCGA)

                          │
                          ▼

[ Layer 2: Functional Translation ]
                 (DepMap / CCLE)

                          │
                          ▼

[ Layer 3: Pharmacogenomic Contexts ]
              (GDSC / CTRP / PRISM)

                          │
                          ▼

[ Layer 4: Perturbational Hypotheses ]
                (LINCS / CMap)
```

---

# Layer 1 — Tumor Epigenetic-Transcriptomic Discovery

Primary datasets:

* TCGA DNA methylation
* TCGA RNA-seq

Future extensions:

* independent bulk tumor cohorts

Purpose:

* identify recurrent epigenetic-transcriptomic programs,
* characterize methylation-expression relationships,
* quantify lineage-specific and lineage-independent biological signals,
* evaluate recurrence across multiple malignancies,
* construct the biological foundation of the framework.

Outputs:

* candidate epigenetic-transcriptomic programs,
* methylation-expression modules,
* recurrent epigenetic maps,
* lineage-aware biological representations.

This layer serves as the primary discovery engine of the project.

---

# Layer 2 — Functional Translation

Primary datasets:

* DepMap
* CCLE

Purpose:

* project tumor-derived programs into experimentally characterized cancer cell lines,
* quantify program activity across models,
* evaluate associations with functional dependency profiles,
* identify candidate functional vulnerabilities.

Outputs:

* program activity matrices,
* dependency associations,
* candidate vulnerability maps.

This layer does not establish causality.

All findings remain statistical associations requiring future validation.

---

# Layer 3 — Pharmacogenomic Contexts

Primary datasets:

* GDSC
* CTRP
* PRISM

Purpose:

* evaluate associations between candidate program activity and drug-response phenotypes,
* characterize resistance-like pharmacogenomic contexts,
* assess reproducibility across independent pharmacological screens.

Outputs:

* resistance-like associations,
* pharmacogenomic context maps,
* cross-screen reproducibility analyses.

Operational definition:

> Resistance-like contexts correspond to relative baseline drug insensitivity observed in large-scale pharmacogenomic datasets.

No direct clinical resistance claims are implied.

---

# Layer 4 — Perturbational Hypotheses

Primary datasets:

* LINCS L1000
* Connectivity Map (CMap)

Purpose:

* identify perturbational signatures inversely associated with candidate programs,
* generate perturbational hypotheses,
* prioritize compounds for future investigation.

Outputs:

* perturbational hypotheses,
* candidate compound rankings,
* perturbational context maps.

Connectivity associations do not constitute therapeutic validation, causal reversal, or mechanistic proof.

---

# Central Biological Object

The primary analytical entity of this framework is:

> recurrent epigenetic-transcriptomic programs.

Programs may comprise:

* coordinated DNA methylation patterns,
* transcriptomic modules,
* epigenetic regulator activity states,
* methylation-expression regulatory architectures,
* pathway-associated biological contexts.

Programs are interpreted as computationally derived biological representations rather than:

* discrete cell states,
* causal mechanisms,
* master regulators,
* validated therapeutic targets,
* clinically actionable biomarkers.

---

# Epigenetic Integration Principles

## DNA Methylation Layer

Purpose:

* identify recurrent promoter methylation patterns,
* characterize lineage-aware methylation states,
* evaluate methylation-expression coupling,
* detect recurrent epigenetic architectures.

DNA methylation represents a core discovery modality rather than a secondary validation layer.

---

## Epigenetic Regulator Layer

Particular attention is given to major epigenetic regulatory systems, including:

* DNMT family
* TET family
* HDAC family
* KDM family
* histone methyltransferases
* histone demethylases
* chromatin remodeling regulators

These regulators serve as biologically informed interpretation layers and prioritization features.

No causal role is assumed.

---

## Transcriptomic Layer

Purpose:

* quantify downstream biological programs,
* characterize pathway activity,
* define integrated molecular states,
* support methylation-transcriptomic integration.

Transcriptomic signals are interpreted jointly with epigenetic context whenever possible.

---

# Pan-Cancer Strategy

The project follows a:

> lineage-aware pan-cancer framework.

This means:

* tissue lineage is treated as a major confounding structure,
* analyses explicitly control for lineage effects,
* naïve pan-cancer pooling is avoided whenever possible.

Cross-lineage recurrence is only claimed after controlling for:

* tissue identity,
* proliferation effects,
* tumor purity,
* batch effects,
* platform-specific confounding factors.

---

# Methodological Principles

## Interpretability First

Preference is given to:

* biologically interpretable representations,
* transparent statistical models,
* explainable feature spaces,
* reproducible computational workflows.

Preferred methods include:

* NMF
* ICA
* GSVA
* module scoring
* sparse regression
* stability selection

Black-box approaches are not prioritized in the initial framework.

---

## Explainability

Feature attribution methods may include:

* SHAP
* feature importance analyses
* model interpretation frameworks

These methods are used exclusively for:

* prioritization,
* biological interpretation,
* hypothesis generation.

They are not interpreted as evidence of causality.

---

## Conservative Scientific Framing

The framework avoids:

* causal claims,
* biomarker claims,
* clinical prediction framing,
* therapeutic efficacy claims.

Preferred terminology includes:

* resistance-like context
* candidate vulnerability
* perturbational hypothesis
* computational association
* recurrent program

---

## Leakage Prevention

The framework explicitly evaluates:

* lineage leakage,
* platform leakage,
* drug-family leakage,
* cell-line overlap,
* proliferation confounding,
* tumor purity confounding,
* batch effects.

Random pan-cancer train/test splitting strategies are prohibited.

---

# Initial Paper Scope

The first manuscript is intended as:

> a reproducible lineage-aware framework for discovering recurrent epigenetic-transcriptomic programs and characterizing their associated functional, pharmacogenomic, and perturbational landscapes.

Primary goals:

* establish the computational framework,
* identify robust candidate programs,
* characterize epigenetic-transcriptomic architectures,
* demonstrate cross-dataset reproducibility,
* generate biologically coherent hypotheses.

Secondary goals:

* candidate vulnerability prioritization,
* perturbational prioritization,
* candidate repurposing hypotheses.

The first manuscript is not intended to:

* provide therapeutic recommendations,
* produce clinical predictors,
* establish mechanistic causality.

---

# Long-Term Expansion

Future directions may include:

* independent tumor-cohort replication,
* scRNA-seq validation,
* ATAC-seq validation,
* longitudinal resistance models,
* perturbational validation,
* experimental collaborations,
* lineage-specific mechanistic investigations.

The first paper establishes the methodological and biological foundation for these future studies.
