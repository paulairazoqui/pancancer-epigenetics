## Project Overview

This framework establishes a lineage-aware computational oncology pipeline designed to identify recurrent epigenetic-transcriptomic programs across diverse malignancies. Furthermore, it systematically evaluates their associations with resistance-like pharmacogenomic contexts, candidate functional dependencies, and perturbational hypotheses.

The architecture integrates public multi-omic, pharmacogenomic, functional dependency, and perturbational transcriptomic datasets, adhering to the following core methodological tenets:

* **Biological Interpretability:** Prioritizing models that yield transparent, biologically extractable features.
* **Reproducibility:** Ensuring robust cross-dataset consistency through standardized workflows.
* **Lineage-Aware Evaluation:** Explicitly accounting for tissue-of-origin confounding effects.
* **Conservative Scientific Framing:** Defining boundaries between computational association and biological causality.

### Out-of-Scope Declarations

To maintain strict scientific validity, this framework is **not** designed or intended to:

* Predict clinical patient outcomes.
* Infer definitive causal biological mechanisms.
* Reconstruct adaptive evolutionary or clonal trajectories.
* Establish clinical therapeutic efficacy.

All outputted findings must be interpreted strictly as computational associations and candidate hypotheses requiring downstream experimental validation.

---

## Core Scientific Question

Can recurrent epigenetic-transcriptomic programs be robustly identified across heterogeneous malignancies using a lineage-aware framework, and are these candidate programs significantly associated with specific:

1. Resistance-like pharmacogenomic contexts?
2. Candidate genetic dependencies (functional vulnerabilities)?
3. Perturbational signatures consistent with candidate program suppression?

---

## Conceptual Framework & Analytical Layers

The architecture is structured into four sequential biological and analytical layers:

```
[ Layer 1: Tumor Program Discovery ] (TCGA / Primary Cohorts)
                 │
                 ▼
[ Layer 2: Functional Translation ] (DepMap / CCLE)
                 │
                 ▼
[ Layer 3: Pharmacogenomic Layer ] (PRISM / GDSC / CTRP)
                 │
                 ▼
[ Layer 4: Perturbational Hypothesis ] (LINCS L1000 / CMap)

```

### 1. Tumor Program Discovery Layer

* **Primary Datasets:** The Cancer Genome Atlas (TCGA); extensible to future public validation cohorts.
* **Objective:** Identify and characterize recurrent epigenetic-transcriptomic modules within primary human tumors, quantify the lineage-specific versus lineage-independent signal components, and evaluate recurrence across lineages. This layer serves as the biological baseline for the entire pipeline.

### 2. Functional Translation Layer

* **Primary Datasets:** Cancer Dependency Map (DepMap), Cancer Cell Line Encyclopedia (CCLE).
* **Objective:** Project tumor-derived candidate programs into deeply characterized *in vitro* models. This layer evaluates statistical associations with functional gene dependency profiles (e.g., CRISPR/RNAi screens) to map candidate vulnerabilities without asserting direct mechanistic causality.

### 3. Pharmacogenomic Layer

* **Primary Datasets:** PRISM, Genomic Sensitivity in Cancer (GDSC), Cancer Therapeutics Response Portal (CTRP).
* **Objective:** Interrogate whether the activation of identified programs correlates with multi-drug insensitivity or distinct sensitivity profiles.

> **Operational Definition:** The term **"resistance-like"** is defined strictly as baseline relative drug insensitivity observed across large-scale screening panels, distinct from clinically acquired resistance. No direct translation to clinical drug resistance is implied.

### 4. Perturbational Hypothesis Layer

* **Primary Datasets:** Library of Integrated Network-Based Cellular Signatures (LINCS L1000), Connectivity Map (CMap).
* **Objective:** Query small-molecule and genetic perturbational signatures that display inverse expression profiles relative to the identified tumor programs. This generates perturbational hypotheses regarding candidate program modulation. These associations do not constitute therapeutic validation or definitive mechanistic proof.

---

## Central Biological Object

The primary analytical entity of this framework is the **recurrent epigenetic-transcriptomic program**. These programs may be represented as:

* Coordinated transcriptional modules or gene sets.
* Epigenetic-transcriptional covarying states.
* Biological patterns extracted via matrix factorization or related dimensionality-reduction approaches.
* Pathway-associated cellular contexts.

Crucially, the pipeline does not pre-suppose discrete cell states, specific master causal regulators, or immediately actionable clinical biomarkers.

---

## Pan-Cancer Analytical Strategy

This project implements a strict **lineage-aware pan-cancer framework**. Tissue lineage represents a massive confounding structure in pan-cancer multi-omic integration. Consequently:

* Naïve pan-cancer data pooling is systematically avoided.
* Statistical models will explicitly control for tissue-of-origin/lineage main effects.
* Cross-lineage recurrence is only claimed if the signal persists after rigorous adjustment for tissue identity, background proliferation rates, tumor purity (microenvironment contamination), and dataset-specific batch effects.

---

## Methodological Principles

### Interpretability First

Preference is given to highly interpretable unsupervised and supervised modeling approaches over uninterpretable deep black-box models. The initial implementation prioritizes:

* Non-Negative Matrix Factorization (NMF)
* Independent Component Analysis (ICA)
* Gene Set Variation Analysis (GSVA) and continuous module scoring
* Regularized, sparse regression models (e.g., Lasso, Elastic Net)

### Data Leakage Prevention & Confounding Control

To guarantee statistical rigor and generalization, the framework integrates explicit guardrails against:

* **Lineage Leakage:** Ensuring train/test partitions or cross-validation schemes account for tissue-type clustering.
* **Platform & Batch Effects:** Standardizing across diverse sequencing and profiling technologies.
* **Drug-Family Leakage:** Accounting for chemical structural similarities and shared mechanisms of action in pharmacogenomic modeling.
* **Cell Line Overlap:** Tracking identical cell line identities across disparate functional and small-molecule screening datasets.

---

## Project Scope

### Initial Manuscript Scope

The primary objective is to deliver a reproducible, open-source computational framework that successfully maps robust cross-dataset epigenetic-transcriptomic programs and defines their corresponding functional and pharmacogenomic landscapes.

* **Primary Deliverables:** Establish the computational infrastructure, isolate reproducible cross-lineage candidate programs, and generate high-confidence, biologically coherent hypotheses.
* **Secondary Deliverables:** Prioritize candidate perturbational compounds for potential drug-repurposing hypotheses.
* **Exclusions:** The initial paper will not provide clinical therapeutic guidelines, validate predictive diagnostic tools, or dissect single-gene mechanistic biochemistry.

### Long-Term Roadmap

The architectural design accommodates modular scalability to support future expansion into:

* Multi-omic layering (e.g., single-cell RNA-seq/ATAC-seq integration).
* Longitudinal, explicitly acquired therapeutic resistance models.
* Prospective experimental validation of prioritized perturbational hypotheses.
* Deep-dive mechanistic evaluation of highly conserved individual programs.