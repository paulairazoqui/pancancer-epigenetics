## 1. Purpose & Scope

This document establishes the mandatory methodological principles, evaluation constraints, data-leakage controls, and interpretive boundaries for the pan-cancer epigenetics project.

The core objectives of this policy are to:

* Enforce rigorous scientific and statistical standards across all analytical pipelines.
* Mitigate overclaiming and maintain strict boundary conditions for biological interpretation.
* Ensure high computational reproducibility across independent environments.
* Systematically eliminate latent data leakage and confounding variables.
* Maintain conceptual and philosophical alignment across all sub-projects and computational layers.

> **Compliance:** This document serves as the primary governing framework. All downstream computational analyses, modeling architectures, and biological interpretations must strictly comply with the directives outlined herein.

---

## 2. Scientific Positioning

To maintain academic integrity and prevent misconstruction by peer reviewers, the scientific boundaries of this project are explicitly defined below:

* **The project SHALL NOT be positioned or evaluated as:** A direct clinical resistance prediction framework, a system for causal biological inference, or a definitive framework for reconstructing temporal, adaptive resistance dynamics.
* **The project IS explicitly positioned as:** A computational oncology framework designed to identify conserved, cross-cancer epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational reversibility.

---

## 3. Core Modeling Philosophy

Computational development within this project operates under a strict hierarchy of priorities, favoring robust biological utility over raw metrics.

| Priority Level | Valued Attributes | Deprioritized Attributes |
| --- | --- | --- |
| **High Priority** | Biological interpretability, cross-dataset reproducibility, lineage-aware generalization, and algorithmic robustness. | Maximal predictive performance at the cost of interpretability, black-box optimization, and clinical deployment readiness. |

We explicitly acknowledge that a model with modest, generalizable predictive power backed by interpretable biology is vastly superior to an uninterpretable, over-optimized architecture prone to out-of-distribution failure.

---

## 4. Permitted vs. Prohibited Biological Claims

To ensure rigorous reporting, all manuscripts and abstracts derived from this project must adhere to the following taxonomy of assertions:

### Permitted Claims (May Assert)

* Statistical association with resistance-like or drug-tolerant contexts.
* Transcriptomic/epigenetic enrichment within therapy-relevant oncology states.
* Functional associations with pharmacologic response metrics ($IC_{50}$, $\text{AUC}$).
* Conserved molecular program recurrence across structurally distinct datasets.
* In silico perturbational reversibility hypotheses.
* Prioritized candidate programs representing putative pan-cancer vulnerabilities.

### Prohibited Claims (Must NOT Assert)

* Direct clinical drug resistance prediction utilizing cross-sectional patient tumors (e.g., TCGA).
* Causal biological mechanisms or signaling pathways derived from correlation-only analyses.
* Validated therapeutic or clinical efficacy inferred solely from in silico perturbation matrices (e.g., LINCS/CMap).
* Universal pan-cancer mechanisms without exhaustive, lineage-aware stratified validation.
* Direct reconstruction of longitudinal, adaptive resistance dynamics from static, cross-sectional datasets.

---

## 5. Strategic Dataset Roles & Boundary Conditions

### 5.1 TCGA (The Cancer Genome Atlas)

* **Permitted Applications:** Discovery of baseline patient-level transcriptomic and epigenetic states, patient subtype stratification, survival-context associations, and macro-level pathway enrichment.
* **Prohibited Applications:** Generation of direct clinical resistance labels, inference of adaptive temporal transitions, or direct prediction of patient-level treatment response.

### 5.2 DepMap / CCLE (Cancer Dependency Map)

* **Permitted Applications:** Systematic functional dependency mapping, cross-modality molecular state transfer, vulnerability prioritization, and in vitro model validation.
* **Acknowledged Limitations:** Computational designs must explicitly account for cell-line culture artifacts, lineage distortion, and the absence of a realistic tumor microenvironment (TME).

### 5.3 GDSC / CTRP / PRISM

* **Permitted Applications:** Pharmacologic association mapping, cross-screen reproducibility benchmarking, and evaluation of baseline sensitivity or resistance-like contexts.
* **Prohibited Interpretations:** Extrapolation to direct clinical efficacy or patient-level therapeutic response prediction.

### 5.4 LINCS / CMap

* **Permitted Applications:** High-throughput perturbational hypothesis generation, candidate drug-reversal prioritization, and exploratory mechanism-of-action analysis.
* **Prohibited Interpretations:** Claims of validated therapeutic repurposing or definitive causal proof of state reversal.

### 5.5 Single-Cell RNA-seq / ATAC-seq

* **Permitted Applications:** Orthogonal validation of bulk-derived signatures, verification of adaptive-state enrichment within cellular subpopulations, and orthogonal confirmation of chromatin accessibility patterns.
* **Prohibited Applications:** Use as the primary discovery engine or as standalone proof of mechanistic causality.

---

## 6. Data Leakage & Evaluation Policy

The elimination of data leakage is a mandatory prerequisite for model validation. Every pipeline must maintain a transparent, documented lineage of feature provenance, splitting strategies, and normalization boundaries.

### 6.1 Prohibited Evaluation Designs

The following modeling practices introduce severe risk of artificial performance inflation and are strictly prohibited:

1. **Unstratified Pan-Cancer Splitting:** Executing random train/test splits without explicit blocking or controlling for tissue-of-origin/lineage composition.
2. **Cell-Line Overlap:** Reusing the same cell-line identifiers across both the discovery (training) and validation (testing) phases.
3. **Chemical/Drug-Family Leakage:** Evaluating predictive capacity on molecules belonging to identical chemical families or targeting identical nodes without proper holdout protocols.
4. **Premature Data Preprocessing:** Performing feature scaling, normalization, imputation, or batch correction *before* partitioning datasets into train, validation, and test splits.
5. **Post-Hoc Feature Selection:** Selecting predictive features or multi-omics modalities using metrics computed across the entire dataset prior to splitting.
6. **Naïve Cross-Screen Merging:** Conflating pharmacogenomic screens without explicit, documented harmonization of response metrics.

### 6.2 Mandatory Evaluation Frameworks

Wherever technically applicable, computational workflows must incorporate:

* **Lineage-Aware Validation:** Systematic evaluation of model performance within specific lineages to decouple tissue-specific baselines from pan-cancer signals.
* **Leave-One-Lineage-Out (LOLO) Cross-Validation:** Evaluating model generalization by systematically holding out entire cancer types during training.
* **Cross-Dataset External Replication:** Validating profiles derived from one resource (e.g., GDSC) directly onto independent resources (e.g., CTRP/PRISM).
* **Confounder Sensitivity Analyses:** Actively probing whether models are capturing unwanted technical or biological artifacts (e.g., sequencing depth, tumor purity, or baseline proliferation rates).
* **Negative Controls & Permutation Tests:** Implementing target shuffling or synthetic negative controls to establish robust statistical baselines.
* **Transparent Failure-Case Analysis:** Documenting explicit boundary conditions, performance degradations, and specific biological contexts where the model fails to generalize.

---

## 7. Domain-Specific Policies

### 7.1 Drug Response Analysis

All drug-response modeling must explicitly decouple baseline association from dynamic prediction. Authors must avoid overinterpreting raw summary statistics ($IC_{50}$ or $\text{AUC}$) without reporting screen-to-screen variability and assay-specific limitations. Compound prioritization frameworks must be explicitly framed as **hypotheses for downstream experimental testing**, never as computational validation of therapeutic efficacy.

### 7.2 Post-Hoc Interpretability

Feature attribution methods—including SHAP (SHapley Additive exPlanations), integrated gradients, random forest feature importances, and latent space embeddings—**shall not be interpreted as indicators of direct biological causality**. Feature importances represent mathematical associations within a specific computational construct and must be framed strictly as hypothesis-generating evidence.

### 7.3 Negative Results

The documentation of negative results, model instability, and boundaries of non-generalizability is considered a core scientific contribution to this project. Computational dead-ends and failed cross-dataset replications must be documented with the same level of rigor as positive findings to prevent publication bias within the repository.

### 7.4 Confounder Control & Robustness Policy

To guarantee that discovered molecular programs reflect true, conserved oncology biology rather than technical or biological artifacts, all major analytical pipelines must explicitly evaluate and isolate the effects of known confounding variables.

#### **Mandatory Confounder Assessment**

Before any discovered epigenetic-transcriptomic program can be categorized as a true cross-cancer entity, it must be robustly evaluated against the following confounding axes:

* **Lineage & Tissue-of-Origin:** Ensuring signatures are not merely tracking baseline histological identities or lineage-specific markers.
* **Proliferation Rates:** Decoupling true resistance-associated states from generalized cellular growth or cell-cycling speed metrics.
* **Tumor Microenvironment (TME) Architecture:** Controlling for variations driven by **tumor purity**, **stromal infiltration**, and **immune infiltration** profiles within bulk sequencing samples.
* **Technical Artifacts:** Actively probing for **batch structure**, platform-specific sequencing depth, and processing-site variations.
* **Non-Specific Cellular Distress:** Verifying that the signature does not merely capture generic, non-specific cell-stress or apoptotic-response pathways.

#### **Analytical Requirements & Sensitivity Frameworks**

* Wherever technically feasible, researchers must implement **confounder-adjusted modeling architectures** (e.g., partial correlation frameworks, linear mixed models, or adversarial de-confounding neural approaches) alongside rigorous sensitivity evaluations.
* **Strict Exclusion Criterion:** Any molecular program or feature set that fails these confounder robustness checks **shall not be interpreted or reported as a pan-cancer adaptive program**. Such programs must either be explicitly qualified as lineage-restricted or labeled as unresolvable confounding artifacts.

---

## 8. Technical Reproducibility Standards

To guarantee that all computational pipelines remain fully auditable and reproducible by external researchers, every analysis must:

* **Enforce Versioned Preprocessing:** Maintain immutable, scripted pipelines for data cleaning; manual or undocumented interventions within datasets are strictly forbidden.
* **Document Precise Data Provenance:** Clearly specify release versions, cell line annotations, and repository freeze dates for all multi-omics sources.
* **Maintain Deterministic Execution:** Enforce strict random seed management across all stochastic algorithms, neural network initializations, and data splitters.
* **Enforce Strict Directory Architecture:** Segregate data structures into isolated directories (`/data/raw`, `/data/interim`, and `/data/processed`) to preserve the integrity of baseline data.

---

## 9. Project Success Criteria

The success of this project is decoupled from commercial or clinical deployment metrics. The project will be deemed scientifically successful upon the identification and validation of:

1. **Conserved, cross-cancer epigenetic-transcriptomic programs** that exhibit statistically significant recurrence across completely independent patient and cell-line cohorts.
2. **Identifiable functional vulnerabilities** robustly linked to these molecular states across multiple functional genomics platforms.
3. **Biologically interpretable resistance-like contexts** that clear rigorous confounder controls (lineage, proliferation, and batch effects).
4. **Coherent perturbational hypotheses** that remain reproducible across independent perturbational or pharmacogenomic resources.

Conversely, the project **does not require** the generation of clinically deployable diagnostic classifiers, perfect pan-cancer universality across all known lineages, or definitive mechanistic proof of evolutionary resistance dynamics.

---