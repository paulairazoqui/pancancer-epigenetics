# Pan-Cancer Epigenetics Framework

## Operational Analysis Roadmap (v3.0)

### Project Objective

Identify recurrent epigenetic-transcriptomic programs through the integration of DNA methylation, epigenetic regulator activity, and transcriptomic states across human cancers, and evaluate their associations with candidate functional vulnerabilities, resistance-like pharmacogenomic contexts, and perturbational hypotheses.

---

# Phase 0 — Infrastructure and Reproducibility

Status: Completed.

Deliverables:

* repository structure
* data provenance records
* download manifests
* reproducible workflows
* version-controlled artifacts

---

# Phase 1 — Tumor Discovery Layer

## Objective

Construct the primary tumor-based epigenetic-transcriptomic discovery framework.

Primary Resources:

* TCGA RNA-seq
* TCGA DNA methylation

---

### Notebook 10

TCGA cohort construction.

Outputs:

* harmonized tumor cohort
* lineage annotations
* sample metadata

---

### Notebook 11

RNA-seq quality control.

Outputs:

* QC reports
* expression summaries
* filtering thresholds

---

### Notebook 12

DNA methylation quality control.

Outputs:

* methylation QC reports
* promoter-level methylation matrices
* coverage assessments

---

### Notebook 13

Methylation-expression integration.

Outputs:

* integrated multi-omic cohort
* methylation-expression coupling analyses

---

### Notebook 14

Confounder assessment.

Tasks:

* lineage effects
* tumor purity
* immune infiltration
* proliferation
* batch effects

Outputs:

* confounder reports

---

### Notebook 15

Epigenetic-transcriptomic program discovery.

Candidate methods:

* NMF
* ICA
* consensus factorization approaches

Outputs:

* candidate programs
* program loadings
* program scores

---

### Notebook 16

Program robustness assessment.

Outputs:

* stability metrics
* reproducibility analyses
* lineage-aware robustness reports

---

# Phase 2 — Functional Translation Layer

## Objective

Construct a harmonized cancer cell-line universe and prepare program translation into functional model systems.

Primary Resources:

* DepMap
* CCLE

Status: In Progress

---

### Notebook 20

Cross-dataset overlap analysis.

Completed.

---

### Notebook 21

Harmonized model universe construction.

Completed.

---

### Notebook 22

Integrated modeling cohort generation.

Completed.

---

### Notebook 23

Expression layer integration.

Completed.

---

### Notebook 24

Expression quality-control assessment.

Completed.

---

### Notebook 25

Global transcriptomic structure analysis.

Completed.

---

### Notebook 26

Drug-response integration.

Completed.

---

### Notebook 27

Pharmacological phenotype framework.

Completed.

---

### Notebook 30

Model-level transcriptome–phenotype integration.

Completed.

---

### Notebook 31

Phenotype sensitivity analysis.

Completed.

---

# Phase 3 — Program Discovery in Cellular Models

## Objective

Project tumor-derived programs into cell-line models and quantify program activity.

---

### Notebook 32

Program projection.

Outputs:

* program activity matrix
* program score distributions

---

### Notebook 33

Cross-platform program consistency.

Outputs:

* reproducibility reports
* projection robustness metrics

---

# Phase 4 — Program Characterization

## Objective

Refine and biologically characterize candidate epigenetic-transcriptomic programs.

---

### Notebook 40

Consensus program construction.

---

### Notebook 41

Program annotation.

Tasks:

* pathway enrichment
* hallmark enrichment
* biological interpretation

---

### Notebook 42

Epigenetic regulator enrichment.

Focus:

* DNMT
* TET
* HDAC
* KDM
* chromatin remodeling systems

---

### Notebook 43

Cross-lineage robustness.

---

# Phase 5 — Functional Vulnerability Analysis

## Objective

Evaluate associations between candidate programs and functional dependencies.

Primary Resources:

* DepMap CRISPR
* DepMap RNAi

---

### Notebook 50

CRISPR dependency associations.

---

### Notebook 51

RNAi dependency associations.

---

### Notebook 52

Integrated vulnerability mapping.

Outputs:

* candidate vulnerabilities
* vulnerability association maps

---

# Phase 6 — Pharmacogenomic Contexts

## Objective

Characterize resistance-like pharmacogenomic contexts associated with candidate programs.

Primary Resources:

* GDSC
* CTRP
* PRISM

---

### Notebook 60

Program–drug associations.

---

### Notebook 61

Predictive modeling.

Candidate methods:

* Elastic Net
* Random Forest
* XGBoost

Purpose:

* evaluate predictive signal
* prioritize candidate programs

---

### Notebook 62

Model interpretation.

Methods:

* SHAP
* feature attribution
* stability selection

---

### Notebook 63

Cross-screen replication.

Outputs:

* replicated associations
* robustness assessments

---

# Phase 7 — Perturbational Hypotheses

## Objective

Identify perturbational signatures inversely associated with candidate programs.

Primary Resources:

* LINCS L1000
* Connectivity Map

---

### Notebook 70

Program signature construction.

---

### Notebook 71

Connectivity analysis.

---

### Notebook 72

Compound prioritization.

Outputs:

* perturbational hypotheses
* candidate compounds

---

### Notebook 73

Mechanism-of-action aggregation.

---

# Phase 8 — Orthogonal Validation

## Objective

Assess reproducibility across independent biological resources.

---

### Notebook 80

Independent bulk-cohort replication.

---

### Notebook 81

Cell Model Passports replication.

---

### Notebook 82

scRNA-seq validation.

---

### Notebook 83

ATAC-seq validation.

---

### Notebook 84

Transcriptomic representation robustness.

Purpose:

* evaluate sensitivity to transcriptomic processing choices

---

# Phase 9 — Manuscript and Preprint Preparation

## Objective

Prepare publication-ready outputs.

Deliverables:

* figures
* supplementary tables
* methods documentation
* reproducibility package
* manuscript draft

---

## Final Deliverable

A reproducible computational oncology framework for identifying recurrent epigenetic-transcriptomic programs and characterizing their associated functional vulnerabilities, resistance-like pharmacogenomic contexts, and perturbational hypotheses across human cancers.
