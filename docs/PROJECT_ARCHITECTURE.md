# PROJECT_ARCHITECTURE.md

## Project Overview

This project is a lineage-aware computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational hypotheses.

It integrates public multi-omic, pharmacogenomic, dependency, and perturbational datasets while prioritizing biological interpretability, internal robustness, cross-dataset replication, leakage prevention, and conservative scientific framing. All findings are computational associations and candidate hypotheses requiring future validation.

The framework does not provide clinical prediction, causal inference, adaptive-resistance reconstruction, biomarker-development, treatment-target-development, or therapeutic-efficacy claims.

---

# Core Scientific Question

Can independently discovered epigenetic-transcriptomic programs in tumors and cancer cell models be compared reproducibly across systems and then characterized in functional, pharmacogenomic, and perturbational contexts?

---

# Conceptual Framework

```text
[ Tumor Discovery: Phase 2 ]             [ Cell-Line Discovery: Phase 3 ]
       TCGA multi-omic data              DepMap / CCLE expression; GDSC phenotype context
                  \                                      /
                   \                                    /
                    +-- Cross-System Comparison: Phase 4 --+
                         multiview matching / consensus
                                      |
          +---------------------------+---------------------------+
          |                           |                           |
          v                           v                           v
 [ Functional vulnerabilities ] [ Pharmacogenomic contexts ] [ Perturbational hypotheses ]
          Phase 5                    Phase 6                     Phase 7
                                      |
                                      v
                    [ Orthogonal / external validation ]
                                  Phase 8
```

The two discovery layers are analytically independent. Cross-system comparison starts only after tumor and cell-line candidate universes and their within-system robustness assessments are frozen. Scoring or projection may be useful later as an analytic operation, but it is not a cell-line discovery mechanism.

---

# Phase 2 — Tumor Epigenetic-Transcriptomic Discovery

Primary datasets:

* TCGA DNA methylation;
* TCGA RNA-seq.

Purpose:

* identify candidate epigenetic-transcriptomic programs in primary tumors;
* characterize methylation-expression relationships;
* quantify lineage-aware and lineage-independent structure; and
* assess internal robustness before cross-system comparison.

Phase 2 is closed and frozen. Its final cohort comprises 9,965 primary tumors with RNA-seq and DNA methylation, and 13 candidate cross-omic programs retained after the completed robustness workflow.

---

# Phase 3 — Cell-Line Discovery

Primary datasets:

* DepMap and CCLE expression resources;
* GDSC for resistance-like pharmacogenomic phenotype definition and downstream association evaluation where relevant.

Purpose:

* independently discover transcriptomic candidate programs in cancer cell models;
* assess within-system robustness of discovery-level, phenotype-associated candidates; and
* preserve a frozen cell-line candidate universe for later comparison.

Phase 3 is closed. Its final DepMap–GDSC cohort comprises 713 models. Cell-line transcriptomic program extraction was phenotype-independent: the representation was frozen before the pharmacogenomic phenotype was introduced for association testing and candidate characterization. Cell-line program discovery did not use TCGA identities, tumor-derived rankings, tumor–cell-line matching, or Phase 2 information to select cellular components. CRISPR and RNAi dependency analysis belong to Phase 5.

---

# Phase 4 — Cross-System Comparison and Consensus Construction

Phase 4 compares independently discovered tumor and cell-line candidate programs. It supports multiview matching and consensus construction only after both representations are frozen.

The comparison must:

* allow explicit “not recoverable” outcomes;
* avoid assuming ICA component indices are portable;
* preserve tumor structural-family metadata;
* prevent double-counting of shared axes;
* consider state or extreme relationships as well as continuous relationships when relevant; and
* keep technical or unresolved-confounded signals downgraded rather than rehabilitating them through partial support.

Cross-system concordance is computational evidence of reproducibility, not biological or causal validation.

---

# Downstream Characterization and Validation

## Phase 5 — Functional Vulnerabilities

DepMap CRISPR and RNAi data are used to characterize associations between consensus or cross-system programs and dependency profiles. Outputs are putative vulnerability hypotheses, not validated interventions.

## Phase 6 — Pharmacogenomic Contexts

GDSC, CTRP, and PRISM are used to characterize baseline drug-response associations and cross-screen reproducibility. Resistance-like contexts denote relative drug insensitivity in these datasets and do not imply clinical response.

## Phase 7 — Perturbational Hypotheses

LINCS L1000 and Connectivity Map support inverse-signature analyses and perturbational hypothesis generation. They do not establish therapeutic efficacy or reversal.

## Phase 8 — Orthogonal and External Validation

Independent tumor cohorts, cell-model resources, single-cell data, and chromatin-context resources can provide cross-dataset replication and orthogonal support.

---

# Central Biological Object

The central entity is the recurrent epigenetic-transcriptomic program: a computationally derived, biologically interpretable representation that may include methylation patterns, transcriptomic modules, epigenetic-regulator activity, methylation-expression relationships, and pathway-associated context.

Programs are not assumed to be master regulators, causal explanations, clinically actionable entities, or definitive biomarkers.

---

# Pan-Cancer and Methodological Principles

The framework is lineage-aware: tissue lineage is treated as a major confounding structure, naïve pan-cancer pooling is avoided, and random pan-cancer train/test splits are prohibited. Analyses must evaluate relevant lineage, platform, batch, proliferation, tumor-purity, and cell-model confounding.

Preference is given to interpretable representations, transparent models, and reproducible workflows. Feature-attribution methods, including SHAP, are exclusively interpretive or predictive-attribution tools for prioritization and hypothesis generation; they are not evidence of causality.

Conservative terminology includes recurrent program, candidate program, resistance-like context, putative vulnerability, computational association, internal robustness, cross-system reproducibility, and cross-dataset replication.
