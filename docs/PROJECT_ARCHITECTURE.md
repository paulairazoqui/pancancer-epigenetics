# PROJECT_ARCHITECTURE.md

## Project Overview

This project is a lineage-aware computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, secondary genomic and locus-level molecular context, functional vulnerabilities, explainable predictive-model behavior, perturbational hypotheses, and convergent therapeutic-prioritization evidence.

It integrates public multi-omic, pharmacogenomic, dependency, perturbational, and drug–target knowledgebase resources while prioritizing biological interpretability, internal robustness, cross-dataset replication, leakage prevention, transparent XAI, and conservative scientific framing. All findings are computational associations and candidate hypotheses requiring future validation.

The framework does not provide clinical prediction, causal inference, adaptive-resistance reconstruction, definitive biomarker development, validated treatment-target development, or therapeutic-efficacy claims.

The broader approved scientific project includes experimental validation. Experimental work is intentionally outside this repository; the computational framework produces reproducible hypotheses and evidence handoffs that can support later experimental evaluation.

---

# Core Scientific Question

Can independently discovered epigenetic-transcriptomic programs in tumors and cancer cell models be compared reproducibly across systems and then characterized through secondary genomic and locus-level methylation-expression context, functional dependencies, resistance-like pharmacogenomic contexts, explainable predictive models, perturbational signatures, external evidence, and integrated program–vulnerability–compound relationships?

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
                                      v
                    [ Secondary molecular context ]
                           Phase 4B (450–451)
                 somatic mutations + locus-level
                   methylation-expression context
                                      |
          +---------------------------+---------------------------+
          |                           |                           |
          v                           v                           v
 [ Functional vulnerabilities ] [ Pharmacogenomics + XAI ] [ Perturbational hypotheses ]
          Phase 5                    Phase 6                     Phase 7
                                      |
                         model attribution + biological
                              contextualization
          |                           |                           |
          +---------------------------+---------------------------+
                                      |
                                      v
                    [ Orthogonal / external validation ]
                                  Phase 8
                                      |
                                      v
                [ Integrated evidence synthesis / prioritization ]
                                  Phase 9
                         structured evidence handoff
                                      |
                                      v
                         [ Manuscript preparation ]
                                 Phase 10
```

The two discovery layers are analytically independent. Cross-system comparison starts only after tumor and cell-line candidate universes and their within-system robustness assessments are frozen. Phase 4B is a post-freeze characterization layer: its results cannot feed back into discovery or consensus eligibility. Scoring or projection may be useful later as an analytic operation, but it is not a cell-line discovery mechanism.

---

# Phase 2 — Tumor Epigenetic-Transcriptomic Discovery

Primary datasets:

* TCGA DNA methylation;
* TCGA RNA-seq.

Purpose:

* identify candidate epigenetic-transcriptomic programs in primary tumors;
* characterize component-level methylation-expression relationships;
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

# Phase 4B — Secondary Molecular Context Characterization

Phase 4B begins only after Phase 4 consensus representations are frozen. It addresses two explicit molecular-context questions without creating a new discovery universe.

## 450 — Secondary Genomic Context Characterization

Primary input:

* one prespecified and audited TCGA/GDC somatic-mutation resource acquired through notebook 108.

Purpose:

* test whether frozen tumor/consensus program activity is associated with recurrent somatic alterations or pathway-level genomic contexts;
* separate project/lineage-driven mutation structure from cross-lineage recurrent associations;
* retain lineage-specific, heterogeneous, and negative findings as valid outputs.

Mutation associations must be lineage-aware. Mutation resources from different callers or workflows must not be naively pooled. Mutation-burden summaries are optional and require a defensible prespecified definition. Copy-number analysis is not included automatically.

## 451 — Locus-Level Methylation–Expression Characterization

Primary inputs:

* frozen TCGA methylation and RNA-seq data;
* frozen program definitions;
* prespecified CpG-to-gene and promoter/regulatory annotations.

Purpose:

* map relevant CpGs to genes and regulatory annotations;
* characterize locus-level methylation-expression associations;
* evaluate inverse promoter methylation-expression relationships compatible with epigenetic regulation where coverage and annotation permit;
* account for lineage/project structure, methylation platform, tumor purity, and applicable technical/confounding factors.

Inverse methylation-expression association is contextual evidence, not mechanistic proof. TCGA tumors are not converted into resistant/sensitive labels for this analysis.

## Frozen-program boundary

Phase 4B may characterize but cannot rescue, exclude, reweight, rename, reorient, or redefine any frozen Phase 4 program. Its outputs may remain unpublished if they are negative or peripheral to a manuscript. They can enter Phase 9 only as separately traceable contextual evidence.

---

# Downstream Characterization, XAI, Validation, and Integration

## Phase 5 — Functional Vulnerabilities

DepMap CRISPR and historical DEMETER2 RNAi data are used to characterize associations between frozen consensus or cross-system programs and dependency profiles. Outputs are putative vulnerability hypotheses, not validated interventions.

## Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI)

GDSC, CTRP, and PRISM are used to characterize baseline drug-response associations and cross-screen reproducibility. Resistance-like contexts denote relative drug insensitivity in these datasets and do not imply clinical response.

This phase contains the explicit explainable-AI component of the project. Lineage-aware predictive models may use Elastic Net, Random Forest, XGBoost, or other prespecified interpretable or explainable approaches where justified. SHAP attribution and stability analyses are applied only after the evaluation design and feature space are frozen and model validity is assessed.

Biological interpretation follows a hierarchical rule: model attribution is reported only at the resolution of actual model features. A model using consensus-program scores produces program-level SHAP attribution. Stable attributed programs can then be contextualized through frozen gene loadings, pathway annotations, epigenetic-regulator enrichment, tumor-side methylation context, and Phase 4B molecular context. This mapping is biological contextualization, not additional SHAP evidence. Gene-level SHAP requires a model that actually contains gene-level features under the same leakage-safe evaluation design.

Random pan-cancer train/test splits are prohibited. Cell-line overlap, drug-family leakage, preprocessing leakage, and post-split feature-selection leakage must be controlled. SHAP describes model attribution; it is not evidence of biological causality or therapeutic actionability.

## Phase 7 — Perturbational Hypotheses

LINCS L1000 and Connectivity Map support inverse-signature analyses and perturbational hypothesis generation. They do not establish therapeutic efficacy or reversal. Compound ranking in this phase is perturbational evidence only and is not the final integrated therapeutic-prioritization step.

## Phase 8 — Orthogonal and External Validation

Independent tumor cohorts, cell-model resources, single-cell data, and chromatin-context resources can provide cross-dataset replication and orthogonal support. This computational validation layer is distinct from experimental validation outside the repository.

## Phase 9 — Integrated Evidence Synthesis and Therapeutic Prioritization

Frozen evidence from Phase 4, Phase 4B, and Phases 5–8 is integrated into a transparent program–vulnerability–compound framework. Candidate vulnerabilities and associated epigenetic regulators may be mapped to known compounds through prespecified drug–target resources such as ChEMBL and DrugBank where accessible.

Evidence dimensions remain explicit rather than being treated as interchangeable observations. Secondary genomic context, locus-level methylation-expression context, functional-genomics support, pharmacogenomic/XAI support, perturbational support, drug–target knowledgebase support, lineage heterogeneity, external replication, and unresolved limitations are retained separately before any candidate evidence stratification.

The preferred output is a multidimensional evidence map and candidate catalog rather than an opaque universal score. Notebook 904 additionally freezes a structured computational-to-experimental evidence handoff containing the relevant program, vulnerability/target context, compound and mechanism annotation, evidence directions, lineage heterogeneity, external support, missing/conflicting evidence, and limitations. RMS/OS or broader sarcoma relevance is annotated only where directly supported by available computational data.

Convergent computational evidence supports prioritization and hypothesis generation only. The handoff is not an experimental result, assay prescription, dose recommendation, or claim of therapeutic efficacy.

## Phase 10 — Manuscript Preparation

Frozen outputs from the preceding phases are transformed into figures, supplementary tables, methods documentation, reproducibility packages, and manuscript drafts. Manuscript preparation must not redefine analytical objects or eligibility rules after results are known.

---

# Central Biological Object

The central entity is the recurrent epigenetic-transcriptomic program: a computationally derived, biologically interpretable representation that may include methylation patterns, transcriptomic modules, epigenetic-regulator activity, methylation-expression relationships, pathway-associated context, and secondary genomic context.

Programs are not assumed to be master regulators, causal explanations, clinically actionable entities, or definitive biomarkers.

---

# Pan-Cancer and Methodological Principles

The framework is lineage-aware: tissue lineage is treated as a major confounding structure, naïve pan-cancer pooling is avoided, and random pan-cancer train/test splits are prohibited. Analyses must evaluate relevant lineage, platform, batch, proliferation, tumor-purity, cell-model, drug-family, mutation-prevalence, and overlap confounding.

Preference is given to interpretable representations, transparent models, and reproducible workflows. Feature-attribution methods, including SHAP, are exclusively interpretive or predictive-attribution tools for prioritization and hypothesis generation; they are not evidence of causality. Biological contextualization of model attribution must preserve the distinction between the model feature level and downstream annotation layers.

Conservative terminology includes recurrent program, candidate program, resistance-like context, secondary genomic context, locus-level methylation-expression association, putative vulnerability, computational association, explainable model attribution, biological contextualization, perturbational hypothesis, internal robustness, cross-system reproducibility, cross-dataset replication, computational-to-experimental handoff, and integrated evidence prioritization.
