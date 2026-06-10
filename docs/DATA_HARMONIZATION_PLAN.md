## Purpose

This document defines the data harmonization strategy, integration logic, identifier standardization policies, and leakage-prevention safeguards implemented throughout the Pan-Cancer Epigenetics Framework.

The objective is to establish a reproducible, version-controlled, lineage-aware infrastructure capable of integrating heterogeneous public oncology datasets spanning:

* DNA methylation,
* transcriptomics,
* functional dependencies,
* pharmacogenomics,
* perturbational transcriptomics.

This document focuses exclusively on data engineering, harmonization, interoperability, and quality-control procedures.

It does not define biological interpretations, modeling architectures, or downstream analytical claims.

---

# 1. Integration Philosophy

The framework is designed around a central principle:

> Biological discovery should originate from primary human tumors and subsequently be translated into functional, pharmacogenomic, and perturbational contexts.

Consequently, the framework rejects naïve pan-cancer pooling and unstructured dataset concatenation.

Instead, integration is organized into four complementary analytical layers.

---

# 2. Layered Integration Architecture

## 2.1 Tumor Discovery Layer

Primary resources:

* TCGA DNA methylation
* TCGA RNA-seq

Primary objective:

* identify recurrent epigenetic-transcriptomic programs,
* characterize methylation-expression architectures,
* quantify lineage-specific and lineage-independent biological variation.

Entity type:

* primary human tumors

Outputs:

* harmonized methylation matrices,
* harmonized transcriptomic matrices,
* integrated tumor multi-omic cohorts.

---

## 2.2 Functional Translation Layer

Primary resources:

* DepMap
* CCLE

Primary objective:

* project tumor-derived programs into cellular models,
* evaluate candidate functional vulnerabilities,
* establish biological correspondence between tumors and cell lines.

Entity type:

* cancer cell lines

Outputs:

* harmonized expression matrices,
* dependency matrices,
* tumor-to-cell-line mapping tables.

---

## 2.3 Pharmacogenomic Layer

Primary resources:

* GDSC
* CTRP
* PRISM

Primary objective:

* characterize resistance-like pharmacogenomic contexts,
* evaluate program–drug associations,
* assess reproducibility across pharmacological screens.

Entity type:

* drug-response measurements

Outputs:

* harmonized pharmacology tables,
* drug annotations,
* cross-screen overlap reports.

---

## 2.4 Perturbational Layer

Primary resources:

* LINCS L1000
* Connectivity Map

Primary objective:

* identify perturbational signatures inversely associated with candidate programs.

Entity type:

* perturbational transcriptional profiles

Outputs:

* harmonized perturbational signatures,
* connectivity resources.

---

# 3. Dataset Roles

| Dataset          | Role                   | Entity Type | Primary Purpose                      |
| ---------------- | ---------------------- | ----------- | ------------------------------------ |
| TCGA Methylation | Discovery              | Tumors      | Epigenetic program discovery         |
| TCGA RNA-seq     | Discovery              | Tumors      | Transcriptomic program discovery     |
| DepMap / CCLE    | Functional Translation | Cell lines  | Functional vulnerability mapping     |
| DepMap CRISPR    | Functional Translation | Cell lines  | Dependency profiling                 |
| DepMap RNAi      | Functional Translation | Cell lines  | Dependency profiling                 |
| GDSC             | Pharmacogenomics       | Cell lines  | Drug-response profiling              |
| CTRP             | Pharmacogenomics       | Cell lines  | Drug-response replication            |
| PRISM            | Pharmacogenomics       | Cell lines  | Drug-response replication            |
| LINCS / CMap     | Perturbational         | Cell lines  | Perturbational hypothesis generation |

---

# 4. Harmonization Backbones

## 4.1 Gene Identifier Standardization

HGNC-approved symbols constitute the primary reference framework.

Policies:

* Ensembl IDs mapped to HGNC symbols.
* Deprecated aliases resolved programmatically.
* Ambiguous mappings excluded from confirmatory analyses.
* Harmonization procedures fully versioned.

---

## 4.2 Tumor Sample Harmonization

TCGA barcodes serve as canonical identifiers.

Metadata layers include:

* lineage,
* tumor type,
* sample type,
* purity metrics,
* clinical annotations when relevant.

---

## 4.3 Cell-Line Harmonization

DepMap ModelID serves as the canonical identifier.

Additional mappings include:

* CCLE identifiers,
* Sanger identifiers,
* COSMIC identifiers.

Quality-control procedures flag:

* duplicated models,
* deprecated models,
* lineage inconsistencies,
* contamination reports.

---

## 4.4 Drug Harmonization

Drug entities are harmonized through:

* standardized compound names,
* PubChem identifiers,
* Broad identifiers,
* mechanism-of-action annotations,
* drug-family annotations.

Drug-family information is retained explicitly to support leakage prevention.

---

# 5. Multi-Omic Harmonization Principles

## 5.1 Transcriptomic Data

Standard processing includes:

* log2(TPM + 1) transformation when applicable,
* variance filtering,
* lineage-aware normalization,
* batch-effect evaluation.

Batch-correction procedures must preserve biological lineage structure.

---

## 5.2 DNA Methylation Data

Standard processing includes:

* probe-level QC,
* detection p-value filtering,
* removal of cross-reactive probes,
* removal of polymorphic CpGs,
* promoter-level aggregation,
* gene-level methylation summaries.

Special emphasis is placed on preserving methylation-expression interoperability.

---

## 5.3 Methylation–Expression Integration

A dedicated integration layer is implemented to evaluate:

* promoter methylation versus gene expression,
* methylation-expression coupling,
* recurrent epigenetic-transcriptomic architectures.

This integration constitutes a core discovery component rather than a downstream validation exercise.

---

## 5.4 Functional Dependency Data

Dependency matrices remain separated by technology:

* CRISPR
* RNAi

Cross-platform replication is preferred over naïve merging.

---

## 5.5 Drug-Response Data

Response metrics remain separated during preprocessing.

Examples:

* LN_IC50
* AUC
* viability summaries

Cross-screen validation is prioritized over metric fusion.

---

# 6. Data Leakage Prevention Framework

The framework explicitly guards against:

## 6.1 Lineage Leakage

Random pan-cancer partitioning is prohibited.

Lineage-aware evaluation strategies are required.

---

## 6.2 Cell-Line Overlap Leakage

Shared cell lines across datasets must be tracked and controlled.

A biological model cannot appear simultaneously in discovery and validation partitions.

---

## 6.3 Drug-Family Leakage

Compounds sharing targets or mechanisms must be grouped during validation procedures.

---

## 6.4 Perturbational Leakage

Compounds evaluated in pharmacogenomic analyses must be isolated from perturbational evaluation procedures when circularity risks exist.

---

## 6.5 Feature Leakage

Feature selection, filtering, normalization, and transformation procedures must respect training/validation boundaries.

---

# 7. Confounder Control Framework

Major confounders explicitly tracked include:

* lineage,
* proliferation,
* tumor purity,
* immune infiltration,
* stromal contamination,
* batch effects,
* sequencing platform effects,
* drug-exposure variables.

All downstream analyses must document how these factors were evaluated.

---

# 8. Missingness Policy

The framework prioritizes:

> reproducibility and biological robustness over maximal feature retention.

Sparse modalities may be analyzed as independent validation layers rather than forced into low-confidence integrations.

Coverage reports are generated for every harmonized dataset.

---

# 9. Harmonized Output Structure

```text
data/
├── raw/
├── interim/
│   ├── metadata/
│   ├── harmonized_expression/
│   ├── harmonized_methylation/
│   ├── harmonized_dependencies/
│   ├── harmonized_drug_response/
│   ├── harmonized_perturbational/
│   ├── lineage_annotations/
│   ├── overlap_tables/
│   └── quality_control/
│
└── processed/
    ├── tumor_programs/
    ├── methylation_expression_modules/
    ├── program_scores/
    ├── vulnerability_associations/
    ├── pharmacogenomic_associations/
    ├── perturbational_results/
    └── modeling_inputs/
```

---

# 10. Scope Limitations

This harmonization framework is explicitly restricted from:

* causal inference,
* clinical outcome prediction,
* therapeutic efficacy claims,
* biomarker validation,
* adaptive evolutionary reconstruction.

The sole purpose of this infrastructure is to provide a reproducible foundation for identifying recurrent epigenetic-transcriptomic programs and evaluating their associations across multiple independent biological layers.
