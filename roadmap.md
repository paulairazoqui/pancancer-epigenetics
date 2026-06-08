# Pan-Cancer Epigenetics Framework

## Operational Analysis Roadmap (v2.0)

### Project Objective

Identify recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational reversibility across multiple cancer types using integrated public datasets.

### Scientific Positioning

This project is designed as a computational oncology framework for hypothesis generation and cross-dataset validation.

The project does **not** aim to:

* predict clinical resistance directly from patient cohorts,
* infer biological causality from observational associations,
* identify definitive biomarkers,
* establish validated therapeutic targets,
* claim therapeutic reversal based solely on in silico evidence.

All findings should be interpreted as computational associations requiring further validation.

---

# Phase 0 — Infrastructure and Reproducibility

## Objectives

Establish a reproducible and auditable data-analysis environment.

## Deliverables

* Repository structure
* Data provenance records
* Download manifests
* Versioned intermediate artifacts
* Reproducible notebook workflow

## Status

Completed.

---

# Phase 1 — Cohort Harmonization and Data Integration

## Objectives

Build a common modeling universe across DepMap and pharmacological resources.

## Core Principles

* ModelID is the canonical identifier.
* All identifier conflicts are resolved before integrating molecular data.
* Every integration step produces an audit artifact.

## Notebooks

### Notebook 20

Cross-dataset overlap analysis.

Outputs:

* shared model universe
* overlap statistics
* identifier consistency assessment

### Notebook 21

Harmonized model universe construction.

Outputs:

* harmonized model table
* unified identifiers
* lineage annotations

### Notebook 22

Integrated modeling cohort generation.

Outputs:

* final modeling cohort
* coverage reports
* cohort summary tables

### Notebook 23

Expression layer integration.

Outputs:

* harmonized transcriptomic matrix
* expression coverage audit
* transcriptomic integration report

## Status

Completed.

---

# Phase 2 — Exploratory Data Analysis (EDA)

## Objectives

Characterize the integrated transcriptomic and pharmacological layers before any modeling or biological association analyses.

## Notebook 20

Cross-dataset overlap analysis.

### Outputs

* shared model universe
* overlap statistics
* identifier consistency assessment

---

## Notebook 21

Harmonized model universe construction.

### Outputs

* harmonized model table
* unified identifiers
* lineage annotations

---

## Notebook 22

Integrated modeling cohort generation.

### Outputs

* final modeling cohort
* coverage reports
* cohort summary tables

---

## Notebook 23

Expression layer integration.

### Outputs

* harmonized transcriptomic matrix
* expression coverage audit
* transcriptomic integration report

---

## Notebook 24

Expression quality-control assessment.

### Tasks

* Expression distribution analysis
* Feature variance assessment
* Near-zero variance evaluation
* Sample-level distribution analysis
* Expression completeness audit
* Storage optimization and persistence

### Deliverables

* QC report
* variance summary
* candidate filtering thresholds

---

## Notebook 25

Global transcriptomic structure analysis.

### Tasks

* PCA
* Explained variance analysis
* UMAP visualization
* Clustering assessment
* Lineage-aware visualization

### Questions

* How strongly does lineage explain transcriptomic structure?
* Are there recurrent cross-lineage patterns?
* Are there potential confounding factors?

### Deliverables

* PCA embeddings
* UMAP embeddings
* clustering reports

---

## Notebook 26

Drug-response integration.

### Tasks

* ModelID ↔ COSMICID validation
* GDSC harmonization
* Coverage assessment
* Drug-family annotation
* Leakage-risk assessment

### Deliverables

* integrated pharmacology table
* coverage report
* drug metadata table

---

## Notebook 27

Pharmacological phenotype framework.

### Tasks

* AUC characterization
* LN_IC50 characterization
* Metric concordance assessment
* Lineage-aware normalization
* Phenotype robustness analysis
* Phenotype representation selection

### Deliverables

* phenotype tables
* phenotype QC report
* phenotype representation summary

### Methodological Notes

Phenotypes should remain continuous whenever possible.

Binarization is considered exploratory and secondary.

---

# Phase 3 — Transcriptome–Phenotype Integration

## Objectives

Construct modeling-ready datasets linking transcriptomic profiles with pharmacology-derived phenotypes.

---

## Notebook 30

Model-level transcriptome–phenotype integration.

### Tasks

* Phenotype integration
* Transcriptomic alignment
* Sample matching validation
* Integration QC
* Modeling-cohort persistence

### Deliverables

* integrated analysis matrix
* integration audit report
* modeling-ready cohort

---

## Notebook 31

Phenotype sensitivity analysis.

### Tasks

* Alternative phenotype representations
* Sensitivity analyses
* Lineage-aware robustness assessment

### Deliverables

* phenotype robustness report
* sensitivity-analysis tables

---

# Phase 4 — Program Discovery and Modeling

## Objectives

Identify recurrent transcriptomic programs associated with resistance-like contexts.

---

## Notebook 40

Gene filtering and feature selection.

### Tasks

* Expression filtering
* Variance-based filtering
* Feature selection assessment

### Deliverables

* filtered expression matrix
* feature-selection report

---

## Notebook 41

Dimensionality reduction.

### Tasks

* PCA-derived representations
* Dimensionality assessment
* Latent-space evaluation

### Deliverables

* reduced-dimensional representations
* variance-explained reports

---

## Notebook 42

Program extraction.

### Candidate Methods

* NMF
* ICA
* PCA-derived components

### Deliverables

* candidate transcriptomic programs
* program loading matrices

---

## Notebook 43

Program reproducibility assessment.

### Tasks

* Stability analysis
* Resampling analyses
* Cross-method comparison

### Deliverables

* reproducibility report
* stability metrics

---

## Notebook 44

Lineage-aware program robustness.

### Tasks

* Lineage-confounding assessment
* Cross-lineage reproducibility
* Sensitivity analyses

### Deliverables

* lineage robustness report
* cross-lineage comparison tables

---

# Phase 5 — Signature Refinement

## Objectives

Refine and consolidate transcriptomic programs into robust signatures suitable for downstream analyses.

## Notebook Series 50

### Tasks

* Consensus signature construction
* Signature refinement
* Gene-loading analysis
* Stability assessment

### Deliverables

* refined transcriptomic signatures
* consensus signature tables

---

# Phase 6 — Functional Association Analysis

## Objectives

Evaluate associations between candidate programs and functional dependencies.

## Data Sources

* DepMap CRISPR
* DepMap RNAi
* Additional functional screens when available

## Notebook Series 60

### Tasks

* Program–dependency associations
* Lineage-aware validation
* Cross-dataset replication

### Deliverables

* candidate vulnerabilities
* robustness analyses

---

# Phase 7 — Perturbational Reversibility

## Objectives

Evaluate whether candidate programs show evidence of perturbational reversibility.

## Data Sources

* LINCS L1000
* Connectivity Map

## Notebook Series 70

### Tasks

* Program signature construction
* Connectivity analyses
* Perturbational ranking
* Compound prioritization

### Deliverables

* perturbational hypotheses
* candidate compound rankings

### Methodological Notes

Perturbational connectivity does not imply therapeutic efficacy.

All findings remain hypothesis-generating.

---

# Phase 8 — Cross-Dataset Validation

## Objectives

Assess reproducibility across independent datasets and alternative transcriptomic representations.

## Potential Resources

* TCGA
* External cell-line collections
* scRNA-seq datasets
* ATAC-seq datasets
* Cell Model Passports RNA-seq
* Alternative transcriptomic representations

## Notebook Series 80

### Tasks

* Replication analyses
* Concordance assessment
* Sensitivity analyses
* Transcriptomic representation robustness
* Cross-dataset validation

### Deliverables

* validation reports
* robustness summaries
* program concordance metrics
* representation-specific comparison tables

### Interpretation Notes

Successful replication should be interpreted as evidence of robustness and reproducibility.

Replication does not imply causal validation or biological confirmation.

---

# Phase 9 — Manuscript and Preprint Preparation

## Objectives

Prepare a publication-ready computational framework.

### Deliverables

* Figures
* Supplementary tables
* Methods documentation
* Reproducibility package
* Preprint draft

## Final Output

A reproducible framework for identifying cross-cancer recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational reversibility.
