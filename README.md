# pancancer-epigenetics

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Bioinformatics](https://img.shields.io/badge/Domain-Computational%20Oncology-blue.svg)]()
[![Reproducibility](https://img.shields.io/badge/Reproducibility-Snakemake%20%2F%20Conda-brightgreen.svg)]()

A lineage-aware computational oncology framework for discovering recurrent epigenetic-transcriptomic programs across diverse malignancies and evaluating their computational associations with resistance-like pharmacogenomic contexts, candidate functional vulnerabilities, and perturbational hypotheses.

---

## Project Overview

This repository integrates high-throughput, multi-omic, pharmacogenomic, functional dependency, and perturbational transcriptomic datasets to identify recurrent biological patterns across heterogeneous tumor and *in vitro* models.

### Core Data Integration

* **Primary tumors:** The Cancer Genome Atlas (TCGA)
* **Cancer cell models and functional genomics:** Cancer Dependency Map (DepMap) / Cancer Cell Line Encyclopedia (CCLE)
* **Pharmacogenomics:** GDSC, CTRP, and PRISM
* **Perturbational profiles:** LINCS L1000 / Connectivity Map (CMap)

The framework emphasizes biological interpretability, data leakage prevention, reproducible data provenance, and conservative scientific framing.

---

## Scientific Scope

The project is designed to generate computational associations and candidate hypotheses. It does **not** aim to:

* predict clinical resistance or patient outcomes,
* infer causal mechanisms from observational data,
* establish validated targets or definitive biomarkers,
* claim therapeutic reversal or translational efficacy from in silico analyses, or
* reconstruct longitudinal, adaptive, or clonal drug-resistance trajectories.

> [!NOTE]
> Outputs from this repository should be interpreted as computational associations and perturbational hypotheses that require downstream experimental validation before any biological or translational claim is made.

---

## Roadmap v3.0 Repository Structure

```text
├── config/                # Path and source-data registry configuration
├── data/                  # Immutable raw data and reproducible derived data tiers
│   ├── raw/               # Source-dataset folders such as depmap, gdsc, tcga, lincs
│   ├── interim/           # Harmonized analysis-ready inputs, metadata, and QC artifacts
│   └── processed/         # Program, vulnerability, context, hypothesis, and validation outputs
├── docs/                  # Project direction, architecture, policy, terminology, and workflow docs
├── envs/                  # Conda/Mamba environment definitions for reproducibility
├── notebooks/             # Roadmap v3.0 phase-organized computational notebooks
├── results/               # Manuscript-ready figures and tables by paper/supplement
├── src/                   # Reusable source code and path helpers
└── tests/                 # Test documentation and future automated checks
```

Publication-facing outputs belong under `results/paper1/`, `results/paper2/`, and `results/supplementary/`, each with `figures/` and `tables/` subfolders. Pipeline-intermediate outputs should remain under `data/interim/` or `data/processed/`.

---

## Documentation Map

The current roadmap v3.0 source-of-truth documents are:

* `roadmap.md` — operational analysis phases, manuscript milestones, and approved repository architecture.
* `docs/PROJECT_DIRECTION.md` — strategic biological objective and conservative scientific scope.
* `docs/PROJECT_ARCHITECTURE.md` — analytical layers, dataset roles, and lineage-aware framework design.
* `docs/MODELING_POLICY.md` — modeling boundaries, leakage prevention, and interpretation policy.
* `docs/TERMINOLOGY_GUIDE.md` — approved terminology for candidate vulnerabilities, resistance-like contexts, perturbational hypotheses, and validation language.
* `docs/workflow.md` — sequential workflow notes for data acquisition, auditing, integration planning, and downstream execution.

---

## Reproducibility & Rigor

* **Data immutability:** Files within `data/raw/` must remain unmodified after acquisition.
* **Deterministic derived data:** Outputs in `data/interim/` and `data/processed/` should be reproducible from raw source files using version-controlled code, notebooks, and environment definitions.
* **Conservative interpretation:** Results should be described as recurrent epigenetic-transcriptomic programs, resistance-like pharmacogenomic contexts, candidate functional vulnerabilities, perturbational hypotheses, or computational associations according to the evidence level.
