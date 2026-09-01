# PROJECT_DIRECTION.md

# Pan-Cancer Epigenetics Framework

## Project Vision

This project is a computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, explainable predictive-model behavior, perturbational hypotheses, and convergent therapeutic-prioritization evidence.

The framework is designed to generate biologically interpretable hypotheses and computational associations. It is not a clinical predictor, causal inference framework, adaptive-resistance reconstruction, pipeline for discovering definitive biomarkers, pipeline for validating treatment targets, or therapeutic-efficacy engine.

The broader approved project includes experimental validation in its title and overall scientific program. Experimental validation is intentionally outside the scope of this computational repository; this repository produces frozen computational hypotheses and evidence handoffs that may support downstream experimental work performed elsewhere.

---

## Central Biological Question

Do recurrent epigenetic-transcriptomic programs emerge across diverse malignancies, and are they associated with:

1. resistance-like pharmacogenomic contexts,
2. putative functional vulnerabilities,
3. explainable and stable predictive-model attributions,
4. perturbational signatures consistent with program suppression, and
5. convergent program–vulnerability–compound evidence suitable for computational prioritization?

---

## Central Biological Object

The primary analytical entity of this project is the:

> recurrent epigenetic-transcriptomic program.

Programs are coordinated representations that can involve DNA methylation states, transcriptomic modules, epigenetic-regulator activity, pathway-level activity, and integrated epigenetic-transcriptional structure. They are candidate biological representations, not discrete cell states, master regulators, or causal explanations.

---

## Role of Explainable Artificial Intelligence

Explainable artificial intelligence is an explicit project objective rather than a manuscript-only interpretive add-on.

XAI is operationalized in **Phase 6 — Pharmacogenomic Contexts and Explainable Modeling**, after resistance-like pharmacogenomic outcomes and evaluation partitions have been prespecified. The planned workflow includes interpretable predictive models, SHAP feature attribution, stability analysis, and attribution comparison across lineages, resampling partitions, model classes, and pharmacogenomic screens where coverage permits.

SHAP values and other feature-attribution outputs describe how a fitted model uses its inputs. They do not demonstrate that a feature is causal, mechanistically necessary, clinically predictive, or therapeutically actionable. XAI findings must therefore be interpreted jointly with predictive validity, stability, lineage structure, and independent evidence layers.

---

## Scientific Architecture

The framework proceeds through the following ordered stages:

1. independent tumor discovery;
2. independent cell-line discovery;
3. cross-system comparison and consensus construction;
4. functional vulnerability characterization;
5. pharmacogenomic context characterization and explainable predictive modeling (XAI);
6. perturbational hypothesis generation;
7. orthogonal or external validation; and
8. integrated evidence synthesis and therapeutic prioritization.

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

**Phase 4 — closed and frozen**

Purpose:

* compare the independently frozen tumor and cell-line candidate universes;
* evaluate cross-system reproducibility through explicit multiview matching;
* construct consensus programs only after matching; and
* retain explicit “not recoverable” outcomes.

Phase 4 completed notebooks 400–404 and froze three candidate cross-system transcriptomic consensus representations with tumor-side methylation context. Cross-lineage robustness, epigenetic-regulator enrichment, and biological annotation were used for characterization only and did not retrospectively redefine, rescue, exclude, reweight, or rename the frozen consensus representations.

Component indices are not assumed to be portable between systems. Scoring or projection can be used as an analytical operation downstream, but not as the mechanism of cell-line discovery. Cross-system correspondence remains computational reproducibility evidence rather than biological or causal validation.

---

## Layer 4 — Functional Vulnerability Characterization

**Phase 5 — active**

Primary resources:

* DepMap CRISPR;
* historical DEMETER2 RNAi.

Purpose:

* characterize associations between frozen consensus programs and functional dependency profiles; and
* generate putative vulnerability hypotheses.

Notebook 500 — CRISPR Associations is complete/frozen. The RNAi acquisition and audit prerequisite is complete through notebook 107, and notebook 501 — RNAi Associations is next.

These associations do not establish a causal role or a validated intervention.

---

## Layer 5 — Pharmacogenomic Context Characterization and XAI

**Phase 6 — planned**

Primary resources:

* GDSC;
* CTRP;
* PRISM.

Purpose:

* characterize associations between frozen consensus-program activity and baseline drug-response profiles;
* assess cross-screen reproducibility of resistance-like pharmacogenomic contexts;
* fit lineage-aware predictive models under explicit leakage controls; and
* use SHAP and stability analyses to characterize which model features drive reproducible predictions.

Resistance-like context refers only to relative baseline drug insensitivity in pharmacogenomic datasets; it does not imply clinical treatment response. Predictive modeling is not a clinical-prediction objective, and SHAP is not causal inference.

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

This computational validation layer is distinct from the experimental validation component of the broader approved project.

---

## Layer 8 — Integrated Evidence Synthesis and Therapeutic Prioritization

**Phase 9 — planned**

Purpose:

* map candidate vulnerabilities and associated regulators to known compounds through curated drug–target resources;
* integrate functional-genomics, pharmacogenomic/XAI, perturbational, regulatory, and external-validation evidence without treating them as interchangeable measurements;
* stratify candidate program–vulnerability–compound relationships using prespecified multidimensional criteria; and
* freeze a final integrated evidence map for manuscript preparation and possible downstream experimental handoff.

This layer produces prioritized computational hypotheses, not validated targets or proven therapeutic strategies.

---

## Scientific Positioning

The framework emphasizes internal robustness, cross-system reproducibility, explainable model behavior, cross-dataset replication, and transparent evidence synthesis while maintaining conservative interpretation. Association does not establish causality. Findings remain computational associations, model-attribution results, and perturbational or putative-vulnerability hypotheses requiring future validation.
