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