## Purpose

This document outlines the programmatic data harmonization strategy, cross-dataset integration logic, identifier mapping policies, and statistical leakage-prevention protocols implemented across this framework.

The primary objective is to establish an reproducible, version-controlled, and lineage-aware pipeline for integrating heterogeneous public oncology datasets spanning high-throughput transcriptomics, array-based epigenomics, functional dependencies, and perturbational profiles. This document focuses exclusively on formal data engineering, standardization principles, and analytical interoperability; it does not define downstream modeling architectures or draw biological conclusions.

---

## 1. Integration Philosophy & Layered Architecture

To preserve underlying biological signals and minimize technical artifacts, this framework rejects naïve pan-cancer data pooling (e.g., aggregating distinct studies into a single unadjusted matrix). Instead, it abstracts data integration into three complementary, decoupled analytical layers:

### 1.1 Patient Biology Layer

* **Primary Objective:** identify and characterize recurrent epigenetic-transcriptomic programs within human malignancies, enabling lineage-aware biological stratification.
* **Primary Resources:** The Cancer Genome Atlas (TCGA); engineered for extensibility to independent external validation cohorts.

### 1.2 Functional Translation Layer

* **Primary Objective:** Model baseline associations between patient-derived programs and cellular phenotypes, prioritizing candidate functional vulnerabilities and evaluating cross-dataset screening robustness.
* **Primary Resources:** Cancer Dependency Map (DepMap) / Cancer Cell Line Encyclopedia (CCLE), GDSC, CTRP, and PRISM.

### 1.3 Perturbational Layer

* **Primary Objective:** Evaluate perturbational signatures inversely associated with candidate programs.
* **Primary Resources:** Library of Integrated Network-Based Cellular Signatures (LINCS L1000) and the Connectivity Map (CMap).
* **Boundary Condition:** This layer serves strictly for *in silico* hypothesis generation and does not imply direct clinical or therapeutic validation.

---

## 2. Dataset Roles & Functional Layout

| Dataset | Analytical Role | Entity Type | Primary Curated Features |
| --- | --- | --- | --- |
| **TCGA** | Discovery Baseline | Primary Tumors | Epigenetic-transcriptomic program deconvolution |
| **DepMap / CCLE** | Functional Translation | Cancer Cell Lines | CRISPR/RNAi gene dependencies & baseline molecular profiles |
| **GDSC** | Pharmacogenomics | Cancer Cell Lines | Small-molecule dose-response curves & sensitivity profiles |
| **CTRP** | Pharmacogenomics | Cancer Cell Lines | High-throughput chemical sensitivity cross-validation |
| **PRISM** | Pharmacogenomics | Cancer Cell Lines | Repurposing-focused barcoded drug-screening profiles |
| **LINCS / CMap** | Perturbational Space | Cell Lines & Clones | High-dimensional differential expression signatures |

---

## 3. Reference Harmonization Backbones

### 3.1 Gene Identifier Standardization

Gene-level feature integration utilizes HUGO Gene Nomenclature Committee (**HGNC**)-approved official gene symbols as its foundational reference spine.

* **Nomenclature Alignment:** All Ensembl IDs are mapped to current HGNC nomenclature. Historical or deprecated aliases are resolved programmatically.
* **Conflict Resolution:** Ambiguous or duplicated gene aliases are resolved conservatively (e.g., prioritizing highest mean expression variance or excluding non-unique mappings from confirmatory analyses).
* **Dimensionality Policy:** Cross-dataset intersection prioritizes genes with robust, continuous representation across all primary modalities over the inflation of the feature space with sparse or missing variables.

### 3.2 Cell-Line Identifier Harmonization

To improve interoperability across functional and pharmacogenomic screening datasets, **DepMap Unique IDs** serve as the primary lookup reference.

* **Cross-Mapping Layers:** Downstream schemas ingest CCLE, Sanger, and COSMIC annotations, mapping them back to the core DepMap ID.
* **Rigor Checks:** The preprocessing pipeline flags and segregates cell lines characterized by lineage inconsistencies, historically documented cross-contamination, duplicate sub-clones, or model deprecation.

### 3.3 Drug Identifier Harmonization

Small-molecule perturbations and chemical screens are mapped onto a unified ontology containing:

* Standardized chemical names and synonyms (collapsed via conservative string-distance matching).
* Broad Institute IDs, PubChem Substance/Compound IDs (SIDs/CIDs).
* Mechanism of Action (MoA) classifications and explicit drug-family annotations.
* **Leakage Control:** Compounds sharing overlapping chemical scaffolds or target affinity profiles are grouped to monitor drug-family leakage during cross-validation partitioning.

---

## 4. Multi-Omic Preprocessing Principles

### 4.1 Transcriptomic Data

Raw count matrices and transcripts-per-million (TPM) inputs undergo standardized normalization steps including:

* $\log_2(\text{TPM} + 1)$ transformations.
* Variance-based filtering to isolate highly informative variable features.
* Lineage-stratified scaling.
* *Note on Batch Effects:* Computational batch-correction algorithms (e.g., ComBat) are evaluated against biological covariates to prevent the artificial deflation of true tissue-specific signals.

### 4.2 DNA Methylation Data

Array-based epigenomic profiles (e.g., Illumina HumanMethylation450/EPIC) are subjected to:

* Probe-level detection $p$-value and quality filtering.
* CpG annotation harmonization against current genome builds.
* Spatial aggregation across functional promoter regions and genomic islands.
* Systematic exclusion of cross-reactive probes and polymorphic CpGs.

### 4.3 Drug-Response Data

Pharmacogenomic metrics—including Area Under the Curve (AUC), Area Over the Curve (AOC), Half-Maximal Inhibitory Concentration ($IC_{50}$), and automated viability summaries—are kept unmerged during baseline normalization.

* **Calibration Assessment:** Metric distributions are evaluated for dataset-specific screening shifts before any mathematical synthesis.
* **Validation Standard:** Cross-dataset validation schemas are prioritized over direct, uncalibrated data concatenation.

---

## 5. Strict Data Leakage Prevention Framework

To protect against artificial performance inflation and overoptimistic generalization, the pipeline implements five explicit validation guardrails:

```
                  [ DATA INTEGRATION STREAM ]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
[ Lineage Safeguard ]  [ Model Separation ]   [ Class Separation ]
 No random pooling;     No shared cell lines   Group drugs by MoA
 Control for tissue      across Train / Eval    to prevent class
 cross-validation.       partitions.            leakage.

```

* **5.1 Lineage Leakage:** Random pan-cancer splitting strategies are disabled. Because tissue lineage exerts a dominant effect on transcriptional topology, evaluation splits must be structurally lineage-independent or explicitly controlled for lineage configuration.
* **5.2 Cell-Line Overlap Leakage:** Under no circumstances may identical biological models (cell lines) appear simultaneously in training and evaluation partitions across datasets. Shared lines across overlapping screens (e.g., GDSC and CTRP) are mapped and partitioned as singular validation units.
* **5.3 Drug-Family Leakage:** Compounds belonging to identical pharmacological classes or sharing explicit targets are segregated during partitioning. Model performance driven by highly correlated chemical classes is isolated from claims of generalized biological discovery.
* **5.4 Perturbational Leakage:** LINCS transcriptomic signatures induced by compounds directly under evaluation in pharmacogenomic validation modules are isolated to prevent circularity.
* **5.5 Feature Leakage:** Supervised filtering, post-hoc variable selection, or label-dependent transformations are completely restricted prior to split generation. All feature selection workflows must remain strictly unsupervised or confined strictly within training partitions.

---

## 6. Confounding Factor Controls

The framework implements explicit statistical controls to mitigate the following high-risk confounding variables:

* Tissue-of-origin lineage imbalances.
* Background baseline cellular proliferation rates.
* Tumor purity scores, stromal infiltration, and immune microenvironment contamination (primarily for TCGA primary tumors).
* Assay heterogeneity, plate-based batch effects, and platform-specific artifacts.
* Chemical dosage levels and variable drug exposure-time intervals.

All mathematically extracted associations are interpreted through these conservative control boundaries.

---

## 7. Data Completeness & Missingness Policy

Given the fragmented nature of overlapping cross-dataset arrays, the pipeline assumes incomplete data coverage. This framework prioritizes **reproducibility and features stability** over maximal feature retention.

* Feature spaces or modalities displaying critical sparsity or insufficient sample intersections will be analyzed as separate, independent validation modules rather than forced into low-confidence integration.
* Automated data coverage and missingness summary reports are dynamically compiled before any confirmatory downstream evaluation.

---

## 8. Planned Harmonized Outputs Structure

The harmonized and standardized outputs are strictly structured within the following directory tree:

```text
data/
├── raw/                             # Immutable raw source data dumps
├── interim/                         # Standardized and mapped data matrices
│   ├── metadata/                    # Unified sample and compound indices
│   ├── harmonized_expression/       # Transformed, log-scaled transcriptomics
│   ├── harmonized_methylation/      # Filtered CpG promoter-aggregated matrices
│   ├── harmonized_drug_response/    # Standardized pharmacogenomic profiles
│   ├── lineage_annotations/         # Curated tissue ontologies
│   ├── overlap_tables/              # Calculated intersections across layers
│   └── quality_control/             # Profiling and pre-filtered quality reports
└── processed/                       # Ready-to-model analytical inputs
    ├── signatures/                  # Extracted continuous gene sets
    ├── program_scores/              # Quantified matrix factorization weights
    ├── perturbational_results/      # Small-molecule connectivity mappings
    └── modeling_inputs/             # Lineage-controlled matrix configurations

```

---

## 9. Scope Limitations & Boundary Declarations

In alignment with our conservative scientific framing, this integration plan is explicitly **restricted** from:

* Inferring definitive causal or single-gene biological mechanisms.
* Reconstructing longitudinal or clonal adaptive evolutionary trajectories.
* Directly predicting real-world patient survival curves or clinical outcomes.
* Establishing or claiming clinical biomarker utility and therapeutic drug efficacy.

This framework functions exclusively to identify robust, recurrent computational associations across public high-throughput datasets. All downstream interpretations remain restricted to hypothesis-generating frameworks tailored to survive rigorous, reviewer-level scrutiny.