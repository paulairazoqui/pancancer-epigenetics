# PROJECT_DIRECTION.md

# Pan-Cancer Epigenetics Framework

## Project Vision

This project is a computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational hypotheses.

The framework is designed to generate biologically interpretable hypotheses and computational associations. It is not a clinical predictor, causal inference framework, adaptive-resistance reconstruction, pipeline for discovering biomarkers, pipeline for discovering treatment targets, or drug-repurposing engine.

---

## Central Biological Question

Do recurrent epigenetic-transcriptomic programs emerge across diverse malignancies, and are they associated with:

1. resistance-like pharmacogenomic contexts,
2. putative functional vulnerabilities, and
3. perturbational signatures consistent with program suppression?

---

## Central Biological Object

The primary analytical entity of this project is the:

> recurrent epigenetic-transcriptomic program.

Programs are coordinated representations that can involve DNA methylation states, transcriptomic modules, epigenetic-regulator activity, pathway-level activity, and integrated epigenetic-transcriptional structure. They are candidate biological representations, not discrete cell states, master regulators, or causal explanations.

---

## Scientific Architecture

The framework proceeds through the following ordered stages:

1. independent tumor discovery;
2. independent cell-line discovery;
3. cross-system comparison and consensus construction;
4. functional vulnerability characterization;
5. pharmacogenomic context characterization;
6. perturbational hypothesis generation; and
7. orthogonal or external validation.

Tumor and cell-line discoveries are intentionally independent. Cross-system matching and consensus construction occur only after each system has produced and frozen its own candidate-program representation and internal robustness assessment.

---

## Layer 1 — Tumor Discovery

**Phase 2 — closed and frozen**

Primary resources:

* TCGA RNA-seq
* TCGA DNA methylation

Purpose:

* identify candidate epigenetic-transcriptomic programs in primary tumors;
* characterize methylation-expression relationships;
* evaluate recurrence and confounding within the tumor system; and
* establish a frozen tumor candidate universe.

The completed cohort contains 9,965 TCGA primary-tumor cases with RNA-seq and DNA methylation. Thirteen candidate cross-omic programs were retained after the Phase 2 robustness workflow. These results are not used to select cellular discovery components.

---

## Layer 2 — Cell-Line Discovery

**Phase 3 — closed**

Primary resources:

* DepMap and CCLE expression resources;
* GDSC, where relevant to defining or evaluating resistance-like pharmacogenomic phenotype associations.

Purpose:

* independently discover transcriptomic candidate programs in cancer cell models;
* evaluate their internal robustness within the cell-line system; and
* characterize discovery-level phenotype associations without importing tumor-program identities or rankings.

The completed DepMap–GDSC cohort contains 713 models. Cellular discovery did not use tumor–cell-line matching, TCGA program identities, TCGA rankings, or Phase 2 information to select cellular components. Functional dependency analyses using CRISPR or RNAi are downstream work, not part of Phase 3 discovery.

---

## Layer 3 — Cross-System Comparison and Consensus

**Phase 4 — planned**

Purpose:

* compare the independently frozen tumor and cell-line candidate universes;
* evaluate cross-system reproducibility through explicit multiview matching;
* construct consensus programs only after matching; and
* retain explicit “not recoverable” outcomes.

Component indices are not assumed to be portable between systems. Future scoring or projection can be used as an analytical operation in this phase or downstream, but not as the mechanism of cell-line discovery.

---

## Layer 4 — Functional Vulnerability Characterization

**Phase 5 — planned**

Primary resources:

* DepMap CRISPR;
* DepMap RNAi.

Purpose:

* characterize associations between consensus or cross-system programs and functional dependency profiles; and
* generate putative vulnerability hypotheses.

These associations do not establish a causal role or a validated intervention.

---

## Layer 5 — Pharmacogenomic Context Characterization

**Phase 6 — planned**

Primary resources:

* GDSC;
* CTRP;
* PRISM.

Purpose:

* characterize associations between program activity and baseline drug-response profiles; and
* assess cross-screen reproducibility of resistance-like pharmacogenomic contexts.

Resistance-like context refers only to relative baseline drug insensitivity in pharmacogenomic datasets; it does not imply clinical treatment response.

---

## Layer 6 — Perturbational Hypothesis Generation

**Phase 7 — planned**

Primary resources:

* LINCS L1000;
* Connectivity Map.

Purpose:

* identify perturbational signatures inversely associated with candidate programs; and
* generate perturbational hypotheses for future investigation.

---

## Layer 7 — Orthogonal and External Validation

**Phase 8 — planned**

Purpose:

* assess cross-dataset replication in independent biological resources; and
* evaluate orthogonal support from additional tumor, cell-model, single-cell, or chromatin-context resources where appropriate.

---

## Scientific Positioning

The framework emphasizes internal robustness, cross-system reproducibility, and cross-dataset replication while maintaining conservative interpretation. Association does not establish causality. Findings remain computational associations and perturbational or putative-vulnerability hypotheses requiring future validation.
