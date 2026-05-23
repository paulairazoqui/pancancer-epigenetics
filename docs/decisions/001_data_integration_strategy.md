# 001 — Data Integration Strategy

## Status

Accepted

---

## Context

This project aims to build a reproducible and interpretable pan-cancer pipeline for:

1. prediction of drug resistance,
2. discovery of molecular/epigenetic resistance signatures,
3. prioritization of therapeutic targets,
4. drug repurposing.

The computational strategy must prioritize:

- reproducibility,
- interpretability,
- dataset traceability,
- biologically coherent integration,
- compatibility with future publication and public release.

The initial project scope focuses on public cancer cell line resources with experimentally measured drug sensitivity.

---

## Selected Releases

### DepMap

- Release: `DepMap Public 25Q3`
- Source: Broad Institute
- Portal: https://depmap.org/portal/

### GDSC

- Release: `GDSC release 8.5`
- Source: Sanger Institute
- Portal: https://www.cancerrxgene.org/

---

## Selected Datasets (Current MVP)

### DepMap

| Dataset | Purpose |
|---|---|
| `Model.csv` | Cell line metadata |
| `OmicsProfiles.csv` | Omics profile mapping and sequencing metadata |
| `OmicsExpressionTPMLogp1HumanProteinCodingGenes.csv` | Transcriptomic features |
| `OmicsSomaticMutations.csv` | Somatic mutation information |

### GDSC

| Dataset | Purpose |
|---|---|
| `GDSC2_fitted_dose_response_27Oct23.xlsx` | Drug sensitivity (LN_IC50, AUC) |

---

## Initial Exclusions

The following datasets are intentionally excluded from the MVP phase:

- methylation,
- CNV,
- CRISPR dependency,
- proteomics,
- fusion datasets,
- pathway-level derived matrices,
- preprocessed mutation matrices.

### Rationale

The initial bottleneck is not feature quantity but:

- correct integration,
- identifier consistency,
- robust joins,
- interpretable modeling,
- reproducible preprocessing.

Additional omics layers will be incorporated only after the transcriptomic-pharmacologic backbone is stable.

---

## Integration Strategy

### Primary Internal Identifier

The primary internal identifier for DepMap integration is:

```text
ModelID
```

### Sequencing-Level Identifier

Omics assays are internally identified by:

```SequencingID```

This identifier represents sequencing-level profiles and is necessary because some models contain multiple omics profiles.

### Cross-Dataset Bridge

The bridge between DepMap and GDSC is:

```text
DepMap: SangerModelID
↔
GDSC: SANGER_MODEL_ID
```

This strategy was selected because:
- high overlap,
- low missingness,
- higher stability than cell line names,
- avoidance of alias-related ambiguity.

--- 

### Overlap Analysis

Initial overlap analysis identified:

|Dataset|Unique models|
|-------|-------------|
|DepMap SangerModelID| 1217|
|GDSC SANGER_MODEL_ID| 969 |
|Shared IDs	| 967 |

This overlap is considered sufficient for the MVP pan-cancer modeling phase.

---

### Omics Selection Strategy
**Expression Data**

Selected subset:

```text
DataType == "rna"
AND
IsDefaultEntryForModel == "Yes"
```
Result:
- 1699 unique models,
- 1699 unique sequencing profiles.

This provides one canonical transcriptomic profile per model.

---

### Mutation Data

Current preferred strategy:

```text
DataType == "wgs"
AND
IsDefaultEntryForModel == "Yes"
```

Rationale:
- higher coverage than WES,
- broader future compatibility,
- alignment with modern cancer genomics pipelines.

However, only biologically filtered/interpretable mutation-derived features will be used in the MVP.

Raw variant-level modeling is intentionally avoided in early phases.

--- 

### Read-Only Raw Data Policy

All files under:

```text
data/raw/
```

are treated as immutable.

All processing outputs, filters, merges, and feature engineering steps must occur under:

```text
data/processed/
```

This policy guarantees:
- provenance,
- reproducibility,
- auditability.

---

### Current Pipeline Phase

Current active phase:
```text
Phase 2 — Exploratory Data Analysis (EDA)
```
Current focus:
- dataset inventory,
- identifier mapping,
- overlap analysis,
- integration planning.

---

### Future Planned Expansions

Future phases may include:
- methylation integration,
- CNV integration,
- CRISPR dependency integration,
- LINCS/CMap transcriptomic reversal,
- network-based target prioritization,
- TCGA external validation,
- interpretable multi-omics modeling.

These components are intentionally deferred until the MVP integration pipeline is fully stabilized.

---

### Decision Summary

The MVP computational backbone is defined as:
```text
DepMap transcriptomics + somatic mutations
+
GDSC drug sensitivity
+
integration through SangerModelID
+
interpretable ML/XAI workflows
```
This strategy prioritizes:
- robustness,
- interpretability,
- reproducibility,
- publication readiness.