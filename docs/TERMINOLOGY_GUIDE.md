## 1. Purpose & Scope

This document defines the mandatory scientific terminology, interpretive boundaries, and approved linguistic conventions for the pan-cancer epigenetics project.

The primary objectives of this guide are to:

* Maintain strict conceptual and epistemological consistency across all project branches.
* Mitigate the risk of overclaiming and properly contextualize computational discoveries.
* Standardize biological interpretation and decouple statistical association from mechanistic causality.
* Establish a **reviewer-resistant lexicon** across all repository outputs, including source-code documentation, Jupyter notebooks, figure legends, commit messages, and manuscript drafts.

> **Repository Alignment:** This document serves as a companion policy to `PROJECT_DIRECTION.md` and `MODELING_POLICY.md`. All contributors must adhere to these linguistic constraints to ensure seamless integration.

---

## 2. Core Philosophy

Our communicative framework prioritizes conservative biological interpretation, rigorous computational nomenclature, and hypothesis-generating framing. Definitive causal, mechanistic, or clinical terminology is restricted to claims directly supported by appropriate evidence beyond the current computational framework.

Whenever analytical uncertainty exists, our default linguistic posture must:

1. Attenuate causal implications.
2. Explicitly clarify observational and cross-sectional limitations.
3. Preserve the defined boundary conditions of our computational models.

Association does not establish causality. Stronger causal or mechanistic claims require evidence beyond this pipeline, such as suitable experimental designs and independent mechanistic support.

---

## 3. Preferred Conceptual Framing

When describing the overarching architecture of this project, contributors must use precise, boundary-aware definitions:

* **Approved Framework Description:**

  > "A computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like contexts, putative functional vulnerabilities, and perturbational hypotheses."

* **Prohibited Framework Descriptions:**

  Do not describe the framework as a clinical predictor, causal framework, biomarker discovery pipeline, target discovery pipeline, drug-repurposing engine, or adaptive-resistance reconstruction framework.

---

## 4. Lexicon Mapping: Approved vs. Discouraged Terminology

| Discouraged / Prohibited Terminology | Approved Technical Alternative |
| --- | --- |
| Drug resistance prediction | Resistance-like association modeling |
| Resistant tumors | Tumors enriched for resistance-associated programs |
| Resistance signature | Candidate resistance-associated program |
| Adaptive resistance state | Resistance-like or adaptive-like context, when supported by the design |
| Therapeutic target | Candidate or putative vulnerability, as supported by the evidence |
| Validated target | Candidate vulnerability; use validation language only when the design supports it |
| Drug repurposing candidate | Candidate compound under a perturbational hypothesis |
| Treatment reversal | Perturbational hypothesis or inverse-signature perturbational association |
| Causal mechanism | Computationally inferred association |
| Mechanistic proof | Hypothesis-supporting evidence |
| Resistance biomarker | Candidate therapy-associated marker |
| Pan-cancer mechanism | Cross-cancer recurrent program, when recurrence criteria are met |
| Clinical prediction | Computational association |
| Validated therapy | Candidate compound hypothesis |
| Resistant lineage | Lineage enriched for resistance-associated features |
| Definitive vulnerability | Putative vulnerability |
| Resistant phenotype | Resistance-like phenotype or context |
| Biological driver | Candidate associated regulator |
| Causal regulator | Prioritized associated regulator |

---

## 5. Domain-Specific Terminology Policies

### 5.1 Candidate, Cross-Cancer Recurrent, and Consensus Programs

* **Candidate program:** A program retained within a discovery system and still subject to the limits of its evidence. Candidate status does not imply recurrence, replication, causal function, or consensus.
* **Cross-cancer recurrent program:** Use only when recurrence is supported across multiple relevant lineages or contexts after considering lineage structure and confounding. It does not imply causality, external replication, or cross-system reproducibility by itself.
* **Consensus program:** Reserve for Phase 4, after explicit comparison of independently discovered tumor and cell-line candidate spaces and supported consensus construction. Do not apply this term to current Phase 2 or Phase 3 outputs.

### 5.2 Resistance-Like Terminology

**Resistance-like phenotype** or **resistance-like context** denotes a computational pharmacogenomic representation of relative baseline drug insensitivity. It does not imply acquired resistance, longitudinal adaptation, clinical treatment resistance, or patient-outcome prediction.

Use unqualified **resistance** only where the experimental design directly supports that meaning. Preferred modifiers include `resistance-like`, `therapy-associated`, `drug-tolerant-like`, `adaptive-like`, and `pharmacologically associated`, but modifiers must not be used to overstate the available evidence.

### 5.3 Functional Vulnerability Terminology

Prefer `putative vulnerability`, `candidate vulnerability`, and `vulnerability association`. Avoid `therapeutic target`, `validated target`, and `definitive vulnerability` unless the required evidence is independently present. Do not use `prioritized candidate vulnerability` as an automatic substitute for `validated target` when specific prioritization has not been demonstrated.

### 5.4 Perturbational Frameworks (LINCS / CMap)

Connectivity-based signatures represent context-dependent computational association structures, not biological guarantees. Prefer `perturbational hypothesis`, `inverse-signature perturbational association`, `perturbational association`, `candidate compound under a perturbational hypothesis`, and `inverse computational association`.

An inverse LINCS/CMap signature is a computational perturbational hypothesis and does not demonstrate biological reversal, therapeutic efficacy, or drug repurposing. Do not use therapeutic or treatment reversal as approved framing.

### 5.5 Pan-Cancer Nomenclature

`Pan-cancer` may name the framework and its scope. A `pan-cancer signal` or biological claim, however, requires evidence across multiple lineages and adequate control of lineage structure; the project name is not evidence that every candidate program is pan-cancer.

For less broad signals, prefer `cross-lineage`, `multi-lineage`, `partially shared`, `recurrent across selected malignancies`, or `lineage-enriched` as appropriate.

### 5.6 Feature Attribution and Interpretability

SHAP, feature importance, latent-factor inspection, and equivalent tools are interpretive aids, predictive attribution, and prioritization tools. They are not causal biology, mechanistic proof, or validated regulation.

### 5.7 Validation and Evidence Terminology

`Validation` must always be qualified by study design and never be read as causal confirmation. Avoid ambiguous labels such as `computational validation`, `exploratory validation`, or `secondary validation` when a more precise evidence category is available.

* **Internal robustness:** Within-system stability or sensitivity evidence, such as the Phase 2 notebook 206 and Phase 3 notebook 311 analyses. It is not independent validation.
* **Cross-system reproducibility:** Phase 4 comparison between independently discovered tumor and cell-line candidate spaces. It is computational reproducibility evidence, not causal or biological validation.
* **Cross-dataset replication:** Replication in independent datasets or resources.
* **Orthogonal support:** Support from biologically or technologically distinct resources, such as scRNA-seq, ATAC-seq, or other appropriate orthogonal modalities.

---

## 6. Evidence Vocabulary and Calibration

The following categories describe different dimensions of evidence; they are not a universal ordinal confidence ladder and do not define universal quantitative thresholds.

| Term | Evidence that permits the term | What it does not imply |
| --- | --- | --- |
| **Exploratory** | Preliminary analysis or hypothesis-generating observation. | Robustness, recurrence, replication, or causal support. |
| **Candidate** | A feature or program retained within a discovery system for further evaluation. | Recurrence, replication, consensus, or causal function. |
| **Internally robust** | Within-system stability or sensitivity evidence. | Independent validation or external replication. |
| **Recurrent** | Support for recurrence across relevant lineages or contexts with appropriate consideration of lineage structure and confounding. | Causality, external replication, or cross-system reproducibility. |
| **Cross-system reproducible** | Explicit Phase 4 comparison of independently discovered tumor and cell-line candidate spaces. | Causal or biological validation. |
| **Cross-dataset replicated** | Replication in an independent dataset or resource. | Mechanistic proof or generalizability beyond the tested datasets. |
| **Orthogonally supported** | Support from a biologically or technologically distinct resource or modality. | Causal confirmation unless the supporting design establishes it. |

Claim strength must reflect study design, independence of evidence, robustness, confounder control, and replication structure.

---

## 7. Statistical & Rhetorical Posture

Software logs and manuscripts must avoid absolute declarative verbs in favor of probabilistic, associative language.

| Prohibited Declaratives | Approved Associatives |
| --- | --- |
| Proves | Suggests / Is consistent with |
| Demonstrates definitively | Is associated with |
| Confirms causality | Supports the hypothesis that |
| Establishes mechanism | May indicate / Is compatible with |
| Validates therapeutic effect | Describes a perturbational hypothesis |

---

## 8. Artifact & Codebase Naming Conventions

### 8.1 Figure Legends & Notebook Markdown

Visual and inline documentation must enforce clean separation between association and causality.

* *Approved Heading Examples:* `Candidate resistance-associated program`, `Cross-cancer recurrent program profile`, `Putative vulnerability association`, `Perturbational association profile`.
* *Prohibited Heading Examples:* `Master regulator of resistance`, `Universal resistance mechanism`, `Validated adaptive state`, `Therapeutic target`.

### 8.2 Programmatic Variables & Object Naming

Whenever feasible, variable definitions, class names, and file outputs should reinforce conservative framing.

* *Approved Naming Patterns:* `candidate_programs`, `recurrent_program_profiles`, `program_associations`, `resistance_like_scores`, `vulnerability_associations`, `perturbational_hypotheses`, `association_outputs`.
* *Prohibited Naming Patterns:* `resistance_classifier`, `therapy_predictor`, `causal_signature`, `validated_targets`, `master_regulators`.

---

## 9. Manuscript Imperatives

Any manuscript, abstract, or conference submission derived from this repository must:

1. Maintain an unyielding separation between statistical association and biological causality.
2. Explicitly distinguish computational prioritization from biological validation.
3. Formally outline the cross-sectional limitations of TCGA and the resolution boundaries inherent to bulk transcriptomics.
4. Use resistance-like terminology consistently and distinguish it from experimentally supported adaptive or clinical resistance.
5. Calibrate validation, reproducibility, replication, and orthogonal-support language to the evidence design.

---

## 10. Final Governing Principle

> **The Golden Rule of Project Nomenclature:** When linguistic uncertainty arises, default to the structurally defensible over the rhetorically aggressive. A weaker, statistically sound claim will survive peer review; a fragile, overextended claim will not. Reviewer-resistant phrasing is the baseline standard of this project.
