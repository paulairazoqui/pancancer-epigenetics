# PROJECT_DIRECTION.md

# Pan-Cancer Epigenetics Framework

## Project Vision

Cancer drug resistance remains one of the major challenges in oncology. Although resistance mechanisms are highly heterogeneous, accumulating evidence suggests that recurrent epigenetic and transcriptional alterations may contribute to therapy-associated cellular states across multiple malignancies.

The long-term goal of this project is to establish a reproducible computational oncology framework capable of identifying recurrent epigenetic-transcriptomic programs across cancer types and evaluating their associations with resistance-like pharmacogenomic contexts, candidate functional vulnerabilities, and perturbational hypotheses.

The framework is designed to generate biologically interpretable hypotheses rather than clinical predictions or mechanistic claims.

---

## Central Biological Question

Do recurrent epigenetic-transcriptomic programs emerge across diverse malignancies, and are these programs consistently associated with:

1. resistance-like pharmacogenomic contexts,
2. candidate functional vulnerabilities,
3. and perturbational signatures suggestive of program suppression?

---

## Central Biological Object

The primary analytical entity of this project is the:

> recurrent epigenetic-transcriptomic program.

These programs are defined as coordinated patterns involving multiple biological layers, including:

* DNA methylation states,
* expression of epigenetic regulators,
* transcriptomic modules,
* pathway-level biological activity,
* and integrated epigenetic-transcriptional signatures.

The project does not assume that these programs represent discrete cell states, master regulators, causal mechanisms, or clinically actionable biomarkers.

---

## Biological Rationale

The framework is motivated by the hypothesis that resistance-associated biology is not exclusively driven by isolated genetic events, but may also involve recurrent epigenetic-transcriptomic architectures that appear across multiple tumor contexts.

Potential contributors include:

* promoter hypermethylation and hypomethylation patterns,
* altered expression of epigenetic regulators,
* coordinated transcriptomic reprogramming,
* pathway-level adaptations associated with therapy tolerance or drug insensitivity.

The objective is not to prove causality, but to identify reproducible computational associations that remain robust after controlling for lineage effects and other major confounders.

---

## Multi-Layer Architecture

The project is organized into four complementary analytical layers.

### Layer 1 — Tumor Program Discovery

Primary resources:

* TCGA
* future external tumor cohorts

Purpose:

* identify recurrent epigenetic-transcriptomic programs in primary tumors,
* characterize methylation-expression relationships,
* evaluate recurrence across lineages,
* establish the biological foundation of the framework.

---

### Layer 2 — Functional Translation

Primary resources:

* DepMap
* CCLE

Purpose:

* project tumor-derived programs into cellular models,
* evaluate associations with CRISPR and RNAi dependencies,
* identify candidate functional vulnerabilities.

No causal interpretation is implied.

---

### Layer 3 — Pharmacogenomic Contexts

Primary resources:

* GDSC
* CTRP
* PRISM

Purpose:

* evaluate associations between candidate programs and baseline drug-response profiles,
* identify resistance-like pharmacogenomic contexts,
* assess reproducibility across independent screening platforms.

Resistance-like contexts refer exclusively to relative baseline drug insensitivity observed in pharmacogenomic datasets.

No direct clinical resistance claims are made.

---

### Layer 4 — Perturbational Hypotheses

Primary resources:

* LINCS L1000
* Connectivity Map

Purpose:

* identify perturbational signatures inversely associated with candidate programs,
* generate candidate perturbational hypotheses,
* prioritize compounds for future investigation.

Connectivity results are interpreted strictly as computational associations.

---

## Epigenetic Focus

A central emphasis of this project is the integration of:

* DNA methylation patterns,
* epigenetic regulator activity,
* transcriptomic states.

Particular attention will be given to recurrent alterations involving major epigenetic regulatory systems, including:

* DNMT family members,
* TET family members,
* HDAC family members,
* histone methyltransferases,
* histone demethylases,
* chromatin remodeling regulators.

These regulators are treated as biologically informed interpretation layers rather than pre-assumed causal drivers.

---

## Scientific Positioning

This project is designed as a hypothesis-generating computational oncology framework.

The framework is intended to:

* identify recurrent candidate programs,
* quantify reproducibility across datasets,
* generate candidate vulnerability hypotheses,
* generate perturbational hypotheses.

The framework is not intended to:

* predict clinical treatment response,
* infer causal biological mechanisms,
* reconstruct adaptive evolutionary trajectories,
* establish therapeutic efficacy,
* produce validated biomarkers.

---

## Long-Term Deliverable

The ultimate objective is to construct an interpretable epigenetic-transcriptomic map of resistance-associated biology across cancer types.

This map should integrate:

* recurrent molecular programs,
* candidate functional vulnerabilities,
* resistance-like pharmacogenomic contexts,
* and perturbational hypotheses,

while maintaining strict methodological rigor and conservative biological interpretation.
