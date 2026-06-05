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

# Phase 2 — Transcriptomic Quality Control

## Objectives

Characterize the integrated transcriptomic layer before any biological interpretation.

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

# Phase 3 — Global Transcriptomic Structure

## Objectives

Characterize the major sources of transcriptomic variation within the integrated cohort.

## Notebook 25

Transcriptomic structure analysis.

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

# Phase 4 — Pharmacological Integration

## Objectives

Integrate GDSC pharmacological measurements with the harmonized cohort.

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

# Phase 5 — Resistance-Like Phenotype Construction

## Objectives

Define pharmacological phenotypes suitable for downstream association analyses.

## Notebook 27

Pharmacological phenotype framework.

### Tasks

* AUC characterization
* LN_IC50 characterization
* Lineage-aware normalization
* Phenotype robustness analysis

### Deliverables

* phenotype tables
* phenotype QC report

## Methodological Notes

Phenotypes should remain continuous whenever possible.

Binarization is considered exploratory and secondary.

---

# Phase 6 — Program Discovery

## Objectives

Identify recurrent transcriptomic programs associated with resistance-like contexts.

## Notebook Series 30

### Tasks

* Gene filtering
* Feature selection
* Co-expression analysis
* Dimensionality reduction
* Program extraction

### Candidate Methods

* PCA-derived components
* NMF
* ICA
* Consensus approaches

### Deliverables

* candidate transcriptomic programs
* reproducibility assessments
* lineage-aware validation

---

# Phase 7 — Functional Association Analysis

## Objectives

Evaluate associations between candidate programs and functional dependencies.

## Data Sources

* DepMap CRISPR
* DepMap RNAi
* Additional functional screens when available

### Tasks

* Program–dependency associations
* Lineage-aware validation
* Cross-dataset replication

### Deliverables

* candidate vulnerabilities
* robustness analyses

---

# Phase 8 — Perturbational Reversibility

## Objectives

Evaluate whether candidate programs show evidence of perturbational reversibility.

## Data Sources

* LINCS L1000
* Connectivity Map

### Tasks

* Program signature construction
* Connectivity analyses
* Perturbational ranking
* Compound prioritization

### Deliverables

* perturbational hypotheses
* candidate compound rankings

## Methodological Notes

Perturbational connectivity does not imply therapeutic efficacy.

All findings remain hypothesis-generating.

---

# Phase 9 — Cross-Dataset Validation

## Objectives

Assess reproducibility across independent datasets.

## Potential Resources

* TCGA
* External cell-line collections
* scRNA-seq datasets
* ATAC-seq datasets

### Tasks

* Replication analyses
* Concordance assessment
* Sensitivity analyses

### Deliverables

* validation reports
* robustness summaries

---

# Phase 10 — Manuscript and Preprint Preparation

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

# Phase 9B — Transcriptomic Representation Robustness

## Objectives

Evaluate whether candidate transcriptomic programs remain reproducible across alternative transcriptomic representations derived from overlapping model universes.

## Scientific Rationale

The primary discovery workflow is performed using the harmonized DepMap transcriptomic layer. However, transcriptomic programs may be sensitive to upstream processing decisions, normalization procedures, quantification pipelines, and data-provider-specific representations.

This phase evaluates the robustness of discovered programs under alternative transcriptomic data sources without altering the overall analytical framework.

## Potential Resources

* Cell Model Passports RNA-seq
* Sanger transcriptomic releases
* Alternative harmonized transcriptomic representations when available

## Tasks

* Reconstruct an independent transcriptomic cohort
* Repeat preprocessing and quality-control workflows
* Re-run program discovery analyses
* Compare program structure and composition
* Assess concordance of program-level associations
* Quantify sensitivity to transcriptomic representation

## Key Questions

* Do candidate programs reappear across transcriptomic representations?
* Are core genes preserved across datasets?
* Are resistance-like associations consistent?
* Are discovered programs robust to transcriptomic processing choices?

## Deliverables

* Transcriptomic robustness report
* Program concordance metrics
* Sensitivity analyses
* Representation-specific comparison tables

## Interpretation Notes

Successful replication within this phase should be interpreted as evidence of robustness to transcriptomic representation and preprocessing choices.

This phase does not constitute orthogonal biological validation and should not be interpreted as independent biological confirmation.