# PROJECT_ARCHITECTURE.md

## Project Overview

This project aims to develop a lineage-aware computational oncology framework to identify recurrent epigenetic-transcriptomic programs across cancer types and explore their associations with resistance-like pharmacogenomic contexts, candidate functional vulnerabilities, and perturbational hypotheses.

The project integrates public multi-omic, pharmacogenomic, dependency, and perturbational transcriptomic datasets, with a strong emphasis on:

* biological interpretability,
* reproducibility,
* lineage-aware evaluation,
* conservative scientific framing,
* and cross-dataset consistency.

The framework is not intended to:

* predict clinical outcomes,
* infer causal biological mechanisms,
* reconstruct adaptive evolutionary trajectories,
* or establish therapeutic efficacy.

All findings should be interpreted as computational associations and candidate hypotheses requiring future validation.

---

# Core Scientific Question

Can recurrent epigenetic-transcriptomic programs be identified across multiple cancer types in a lineage-aware manner, and are these programs associated with:

* resistance-like pharmacogenomic contexts,
* candidate genetic dependencies,
* and perturbational signatures suggestive of functional reversibility?

---

# Conceptual Framework

The project is organized into four biological and analytical layers.

## 1. Tumor Program Discovery Layer

Primary datasets:

* TCGA
* additional public tumor cohorts (future)

Purpose:

* identify recurrent epigenetic-transcriptomic programs in human tumors,
* characterize their recurrence across lineages,
* quantify lineage-specific versus lineage-independent signal.

This layer represents the biological foundation of the project.

---

## 2. Functional Translation Layer

Primary datasets:

* DepMap
* CCLE

Purpose:

* map tumor-derived programs into experimentally characterized cancer cell lines,
* evaluate associations with gene dependency profiles,
* identify candidate functional vulnerabilities.

This layer does not establish causality.
Associations will be interpreted conservatively.

---

## 3. Pharmacogenomic Layer

Primary datasets:

* PRISM
* GDSC
* CTRP

Purpose:

* evaluate whether identified programs are associated with relative multi-drug insensitivity or sensitivity patterns,
* characterize resistance-like pharmacogenomic contexts.

The term "resistance-like" refers operationally to:

* relative baseline drug insensitivity observed in large-scale pharmacogenomic datasets,
* not to clinically validated acquired resistance.

No direct clinical resistance claims will be made.

---

## 4. Perturbational Hypothesis Layer

Primary datasets:

* LINCS L1000
* Connectivity Map (CMap)

Purpose:

* identify perturbational signatures inversely associated with candidate programs,
* generate perturbational hypotheses for future investigation.

Perturbational associations do not constitute:

* therapeutic validation,
* causal reversal,
* or mechanistic proof.

---

# Central Biological Object

The primary analytical object of the project is:

> recurrent epigenetic-transcriptomic programs.

Programs may represent:

* coordinated transcriptional modules,
* epigenetic-transcriptional states,
* recurrent latent biological patterns,
* or pathway-associated cellular contexts.

The project does not initially assume:

* discrete cell states,
* causal regulators,
* or clinically actionable biomarkers.

---

# Pan-Cancer Strategy

The project follows a:

> lineage-aware pan-cancer framework.

This means:

* tissue lineage is treated as a major confounding structure,
* analyses will explicitly control for lineage effects,
* naïve pan-cancer pooling will be avoided whenever possible.

Cross-lineage recurrence will only be claimed after controlling for:

* tissue identity,
* proliferation effects,
* and dataset-specific confounding factors.

---

# Methodological Principles

## Interpretability First

Preference will be given to:

* interpretable factorization methods,
* transparent statistical models,
* biologically explainable features.

Examples:

* NMF
* ICA
* GSVA
* module scoring
* sparse regression

Black-box approaches will not be prioritized in the initial paper.

---

## Conservative Scientific Framing

The project avoids:

* causal claims,
* biomarker claims,
* clinical prediction framing,
* therapeutic efficacy claims.

Preferred terminology:

* resistance-like context
* candidate vulnerability
* perturbational hypothesis
* computational association
* recurrent program

---

## Leakage Prevention

The framework explicitly considers:

* lineage leakage,
* platform leakage,
* drug-family leakage,
* cell-line overlap,
* proliferation confounding,
* batch effects,
* tumor purity effects.

Random naïve pan-cancer splitting strategies should be avoided.

---

# Initial Paper Scope

The first paper is intended as:

> a reproducible lineage-aware computational framework identifying recurrent epigenetic-transcriptomic programs and their associated candidate functional and pharmacogenomic contexts.

Primary goals:

* establish the computational framework,
* identify robust candidate programs,
* demonstrate cross-dataset reproducibility,
* generate biologically coherent hypotheses.

Secondary goals:

* perturbational prioritization,
* candidate repurposing hypotheses.

The first manuscript is not intended to:

* provide definitive therapeutic recommendations,
* produce clinical predictors,
* or establish mechanistic causality.

---

# Long-Term Expansion

Future project directions may include:

* additional omic layers,
* single-cell validation,
* ATAC-seq integration,
* longitudinal resistance models,
* perturbational validation,
* prospective experimental collaborations,
* lineage-specific mechanistic deep dives.

The first paper is designed to establish the methodological and biological foundation for these future studies.
