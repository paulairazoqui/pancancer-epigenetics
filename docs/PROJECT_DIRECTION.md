## Working Project Direction

### Current Strategic Focus

The project is currently oriented toward identifying cross-cancer epigenetic-transcriptomic programs associated with resistance-like phenotypes, functional vulnerabilities, and perturbational reversibility. This approach leverages publicly available multi-omics and pharmacogenomic datasets by integrating:

* Pan-cancer transcriptomics
* Epigenetic profiles
* Pharmacogenomic response data
* Functional dependency metrics
* Perturbational transcriptomics
* Interpretable machine learning frameworks

**Core Objective:** The goal is not to directly infer clinical drug resistance solely from patient tumor profiles. Rather, the project aims to identify biologically coherent programs associated with resistance-related contexts across both patient tumors and experimental model systems.

---

## Original Conceptual Framework

### Initial Project Goals

* Identify epigenetic signatures associated with oncology drug resistance.
* Integrate transcriptomic and epigenetic modalities.
* Implement interpretable machine learning architectures.
* Uncover novel vulnerabilities and drug repurposing candidates.

### Candidate Datasets

* **Patient Frameworks:** TCGA
* **Cell Line & Functional Models:** DepMap / CCLE
* **Pharmacogenomics:** GDSC, CTRP, PRISM
* **Perturbational Resources:** LINCS / CMap

### Initial Theoretical Emphasis

* Pan-cancer resistance signatures
* Characterization of epigenetic regulators
* Interpretable predictive modeling
* Perturbational reversal strategies

---

## Conceptual Refinement via Literature Synthesis

A comprehensive literature review revealed several critical paradigm shifts currently shaping the field:

### Emerging Field Paradigms

The oncological landscape is increasingly shifting away from **mutation-centered resistance models** and moving toward **dynamic, adaptive cell-state models**. Key concepts include:

* Epigenetic plasticity
* Drug-tolerant persister (DTP) states
* Transcriptional state transitions
* Reversible resistance programs
* Non-genetic resistance mechanisms

> **Impact on Project Scope:** These shifts directly influence our hypothesis framing, terminology, dataset interpretation, and the boundary conditions of our biological claims.

---

## Key Methodological Nuances

### TCGA Limitations & Analytical Scope

TCGA does **not** directly measure therapy resistance longitudinally, meaning it cannot support strong causal claims regarding adaptive resistance. Consequently:

* TCGA data cannot be used to claim the direct discovery of *de novo* adaptive resistance states.
* TCGA data can support exploratory discovery of baseline epigenetic-transcriptomic programs associated with aggressive, therapy-relevant, or resistance-like tumor contexts, but cannot independently establish adaptive resistance.

Maintaining this analytical distinction is critical for the scientific validity of the project.

---

## Chosen Strategy: Hybrid Architecture

The project implements a two-tiered hybrid design to maximize discovery power while ensuring biological grounding:

```
┌────────────────────────────────────────────────────────┐
│ 1. Core Discovery Layer (Bulk Multi-Omics)             │
│    TCGA | DepMap/CCLE | GDSC | CTRP | PRISM | LINCS    │
└───────────────────────────┬────────────────────────────┘
                            │ (Program Extraction)
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. Secondary Validation Layer (Single-Cell/Chromatin)  │
│    scRNA-seq | ATAC-seq | Public Resistant Atlases     │
└────────────────────────────────────────────────────────┘

```

* **Core Discovery Layer (Large-Scale Bulk Multi-Omics):** Employs TCGA, DepMap/CCLE, GDSC, CTRP, PRISM, and LINCS/CMap as the primary engine for program extraction.
* **Secondary Validation Layer (Targeted Orthogonal Validation):** Utilizes single-cell RNA-seq, ATAC-seq, and public resistant-state atlases.

*Note: Single-cell datasets will not serve as the primary discovery engine. Instead, they will be used exclusively to validate whether bulk-derived programs are enriched within resistant or persister-like subpopulations.*

---

## Strategic Dataset Roles

### TCGA

* **Primary Role:** Patient-level biological discovery, identification of transcriptomic and epigenetic states, and characterization of subtype and survival associations.
* **Explicit Exclusion:** Will *not* be utilized as direct clinical resistance labels.

### DepMap / CCLE

* **Primary Role:** Functional dependency mapping, cross-modality molecular state transfer, and therapeutic vulnerability prioritization.

### GDSC / CTRP / PRISM

* **Primary Role:** Characterization of pharmacologic associations, mapping sensitivity/resistance contexts, and executing cross-screen validation.

### LINCS / CMap

* **Primary Role:** In silico perturbational reversal modeling, candidate compound prioritization, and mechanistic exploration.
* **Explicit Exclusion:** Will *not* be treated as definitive validation of clinical therapeutic efficacy.

### Single-Cell RNA-seq / ATAC-seq

* **Primary Role:** Orthogonal validation, confirmation of adaptive cellular states, and resolution of cellular plasticity/persister dynamics.
* **Explicit Exclusion:** Will *not* be used as primary training or modeling datasets.

---

## Current Working Hypothesis

$$H_1: \text{Cross-cancer epigenetic-transcriptomic programs co-segregate with specific resistance-like phenotypes and functional dependencies.}$$

We hypothesize that conserved cross-cancer epigenetic-transcriptomic programs co-segregate with resistance-like phenotypes and functional dependency patterns across patient and model-system datasets. A subset of these programs may represent vulnerability-prone cellular states that can be prioritized for perturbational reversal using publicly available perturbational transcriptomic resources.

---

## Claims Explicitly Avoided

To maintain rigorous scientific standards, this project will **not** claim:

* Direct clinical resistance prediction derived solely from cross-sectional patient tumors (TCGA).
* Direct discovery of temporal, adaptive resistance states from static patient data.
* Direct mechanistic causality inferred from SHAP scores or feature attribution methods alone.
* Validated therapeutic repurposing candidates based exclusively on LINCS/CMap metrics.
* Universal pan-cancer biology when the underlying signal is predominantly lineage-specific.
* Mechanistic or physical causality derived from purely correlative computational analyses.

---

## Anticipated Reviewer Risks & Mitigation Framework

### Data Leakage Risks

* **Lineage/Tissue-of-Origin Leakage:** Confounding pan-cancer signals with tissue-specific baselines.
* **Platform/Batch Leakage:** Artifacts introduced by merging disparate sequencing technologies.
* **Drug-Family Leakage:** Overoptimistic evaluation performance due to highly correlated drug mechanisms.
* **Cell-Line Overlap:** Evaluative cross-contamination between discovery and validation screens.
* **Annotation Leakage:** Indirect inclusion of downstream clinical outcome data into feature spaces.

### Biological Confounders

* **Proliferation vs. Resistance:** Failure to decouple general cell-cycling speed from true drug-tolerant phenotypes.
* **Lineage vs. Adaptive State:** Misinterpreting cell-type lineage markers as active resistance programs.
* **Bulk Resolution Limits:** Overinterpreting averaged bulk transcriptomic signals without accounting for intra-tumor heterogeneity.
* **Perturbational Mismatch:** Overclaiming the physiological translation of *in vitro* perturbational reversals.

### Dataset Mismatch Risks

* **Translational Gap:** Divergence between patient tumor microenvironments and *in vitro* cell line models.
* **Assay Incompatibility:** Technical noise and metric discordance across heterogeneous pharmacogenomic screens.
* **Contextual Variance:** Disparities between steady-state baselines and active perturbational contexts.
* **Preprocessing Heterogeneity:** Confounders introduced by inconsistent data normalization pipelines.

---

## Required Validation Principles

Any proposed modeling architecture must strictly adhere to the following principles:

1. **Cross-Dataset Validation:** Mandatory evaluation on completely independent, unseen cohorts.
2. **Lineage-Aware Evaluation:** Strategic benchmarking stratified by tissue of origin to isolate true pan-cancer signals.
3. **Independent Pharmacogenomic Replication:** Cross-validation of drug-response signals between disparate screens (e.g., GDSC vs. CTRP).
4. **Confounder Sensitivity Analysis:** Explicit control for technological batches, cell proliferation rates, and lineage baselines.
5. **Orthogonal Single-Cell/Chromatin Validation:** When available, verification of bulk models against single-cell resolution and chromatin accessibility (ATAC-seq) profiles.
6. **Transparent Failure Analysis:** Documenting clear edge cases, negative results, and performance boundaries.

---

## Current Strategic Positioning

* **The project IS positioned as:** A computational oncology study focused on discovering pan-cancer epigenetic-transcriptomic programs that associate with resistance-related biological contexts, map to functional vulnerabilities, and can be systematically interrogated via perturbational reversal frameworks.
* **The project IS NOT positioned as:** A definitive model for clinical adaptive resistance, nor as a framework for the longitudinal reconstruction of evolutionary tumor dynamics.

---

## Immediate Next Steps

* [ ] Finalize the formal wording of the primary and secondary project hypotheses.
* [ ] Define the exact mathematical and biological discovery targets.
* [ ] Establish concrete proxies for the "resistance-like" phenotype.
* [ ] Finalize the feature space design and data modality selection criteria.
* [ ] Establish the concrete train/validation/test splitting strategy.
* [ ] Implement programmatic data leakage controls within the preprocessing pipeline.
* [ ] Standardize the evaluation and performance metrics.
* [ ] Categorize the project bibliography into structured thematic domains (Conceptual, Methodological, Computational, Translational, and Validation).
* [ ] Initiate the drafting of the detailed, step-by-step analysis plan.

---