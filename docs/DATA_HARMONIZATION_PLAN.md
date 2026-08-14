# Data Harmonization Plan

## Purpose

This document defines the data-harmonization, identifier-standardization, interoperability, and leakage-prevention policies used by the Pan-Cancer Epigenetics Framework. It describes infrastructure and quality-control procedures, not biological conclusions or downstream analytical claims.

---

# 1. Integration Philosophy

Tumor and cell-line program discovery are analytically independent. Harmonization makes their representations comparable without making either system a projection target for the other.

Cross-system integration begins only after the tumor and cell-line candidate representations, including their within-system robustness assessments, are frozen. This ordering prevents conceptual leakage, circularity, and an artificial increase in apparent cross-system concordance.

The framework rejects naïve pan-cancer pooling and unstructured dataset concatenation.

---

# 2. Layered Integration Architecture

## 2.1 Tumor Discovery Layer — Phase 2

Primary resources:

* TCGA DNA methylation;
* TCGA RNA-seq.

Primary objective:

* independently identify candidate epigenetic-transcriptomic programs in primary tumors;
* characterize methylation-expression architectures; and
* produce a frozen tumor representation for later comparison.

Entity type: primary human tumors.

## 2.2 Cell-Line Discovery Layer — Phase 3

Primary resources:

* DepMap and CCLE expression resources;
* GDSC, after cell-line representation freezing where relevant, for resistance-like pharmacogenomic phenotype associations.

Primary objective:

* independently identify transcriptomic candidate programs in cancer cell models;
* assess internal robustness within the cell-line system; and
* produce a frozen cell-line representation for later comparison.

Entity type: cancer cell models.

Cell-line transcriptomic program extraction is phenotype-independent; the representation is frozen before the GDSC pharmacogenomic phenotype is introduced for association testing and candidate characterization. Cell-line discovery does not use tumor-program identities, tumor rankings, or tumor–cell-line matching to select cellular components. CRISPR and RNAi dependency data are reserved for downstream functional-vulnerability characterization.

## 2.3 Cross-System Comparison and Consensus — Phase 4

Primary objective:

* compare independently frozen tumor and cell-line representations through explicit multiview matching; and
* construct consensus programs only after that comparison.

Cross-system integration may report “not recoverable” outcomes. Component indices are not assumed to be portable between independently fitted representations.

## 2.4 Downstream Context Layers — Phases 5–8

Functional dependencies (Phase 5), pharmacogenomic contexts (Phase 6), perturbational hypotheses (Phase 7), and orthogonal or external validation (Phase 8) use harmonized inputs appropriate to their respective analyses.

---

# 3. Dataset Roles

| Dataset | Role | Entity type | Primary purpose |
| --- | --- | --- | --- |
| TCGA methylation | Tumor discovery | Tumors | Epigenetic program discovery |
| TCGA RNA-seq | Tumor discovery | Tumors | Transcriptomic and cross-omic discovery |
| DepMap / CCLE | Cell-line discovery | Cell models | Independent transcriptomic program discovery |
| GDSC | Pharmacogenomic phenotype and association context | Cell models and response measurements | Resistance-like phenotype associations after cell-line representation freezing and downstream pharmacogenomic context |
| DepMap CRISPR | Functional vulnerabilities | Cell models | Dependency profiling |
| DepMap RNAi | Functional vulnerabilities | Cell models | Dependency profiling |
| CTRP / PRISM | Pharmacogenomics | Drug-response measurements | Cross-screen pharmacogenomic context |
| LINCS / CMap | Perturbational hypotheses | Perturbational profiles | Perturbational hypothesis generation |

---

# 4. Harmonization Backbones

## 4.1 Gene Identifier Standardization

HGNC-approved symbols are the primary reference framework. Ensembl identifiers are mapped to HGNC symbols; deprecated aliases are resolved programmatically; ambiguous mappings are excluded from confirmatory analyses; and harmonization procedures are versioned.

## 4.2 Tumor Sample Harmonization

TCGA barcodes are canonical identifiers. Metadata include lineage, tumor type, sample type, and available project and quality-control annotations.

## 4.3 Cell-Line Harmonization

DepMap ModelID is the canonical identifier. Supporting mappings can include CCLE, Sanger, and COSMIC identifiers. Quality-control procedures flag duplicate or deprecated models, lineage inconsistencies, and available contamination reports.

## 4.4 Drug Harmonization

Drug entities are harmonized using standardized compound names, available public identifiers, mechanism-of-action annotations, and drug-family annotations. Drug-family information is retained to support leakage prevention.

---

# 5. Modality-Specific Harmonization Principles

## 5.1 Transcriptomic Data

Processing is documented per dataset and analysis. Where applicable, it includes log2(TPM + 1) transformation, variance filtering, lineage-aware normalization, and batch-effect evaluation. Any batch-correction procedure must preserve biological lineage structure.

## 5.2 TCGA DNA Methylation Data

The executed Phase 2 conceptual pipeline comprises:

* GDC SeSAMe beta values;
* HM27/HM450 platform-aware quality control;
* probe-missingness assessment;
* shared HM27/HM450 probe space where required;
* platform-aware filtering;
* within-platform probe-median imputation where applied;
* beta-to-M-value transformation for program discovery;
* variance-based feature selection;
* project-aware centering; and
* PCA/ICA program discovery.

This document does not represent detection-p-value filtering, removal of cross-reactive probes, removal of polymorphic CpGs, promoter aggregation, or gene-level methylation summarization as executed standard processing. Such steps require explicit evidence in the pipeline before being documented as performed.

## 5.3 Methylation–Expression Integration

The tumor multi-omic integration layer evaluates methylation-expression relationships and supports discovery of epigenetic-transcriptomic architectures. It remains distinct from later cross-system comparison.

## 5.4 Functional Dependency Data

CRISPR and RNAi dependency matrices remain separated by technology. Cross-platform replication is preferred to naïve merging.

## 5.5 Drug-Response Data

Response metrics, including LN_IC50, AUC, and viability summaries, remain separated during preprocessing. Cross-screen evaluation is preferred to metric fusion.

---

# 6. Data Leakage Prevention Framework

The framework explicitly guards against lineage, platform, drug-family, feature, perturbational, and cell-line-overlap leakage. Random pan-cancer partitioning is prohibited. Feature selection, filtering, normalization, and transformation must respect the relevant discovery, robustness, and validation boundaries.

Cross-system matching is not performed during either discovery phase. Shared models across datasets must be tracked so that a biological model does not simultaneously occupy incompatible discovery and validation roles.

---

# 7. Confounder and Missingness Policy

Relevant tumor confounders include lineage, project structure, purity, immune or stromal infiltration, proliferation, and technical or platform factors. Relevant cell-line confounders include lineage, available biological, culture, and provenance metadata, pharmacological ascertainment where relevant, technical factors, and proliferation only when a valid frozen representation exists.

Coverage and missingness reports are generated for harmonized datasets. Sparse modalities may remain separate rather than being forced into low-confidence integration.

---

# 8. Conceptual Output Structure

```text
data/
├── raw/
├── interim/
│   ├── metadata/
│   ├── expression/
│   ├── methylation/
│   ├── dependencies/
│   ├── pharmacology/
│   ├── perturbational/
│   └── qc/
└── processed/
    ├── tumor_programs/
    ├── cellline_programs/
    ├── consensus_programs/
    ├── functional_vulnerabilities/
    ├── pharmacogenomic_contexts/
    ├── perturbational_hypotheses/
    └── validation/
```

---

# 9. Scope Limitations

This infrastructure does not support causal inference, clinical outcome prediction, therapeutic-efficacy claims, biomarker validation, or adaptive evolutionary reconstruction. Its purpose is to provide reproducible, comparable inputs for independent discovery and subsequent cross-system and downstream characterization.
