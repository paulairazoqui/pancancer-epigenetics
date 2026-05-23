## 1. Purpose & Scope

This document defines the mandatory scientific terminology, interpretive boundaries, and approved linguistic conventions for the pan-cancer epigenetics project.

The primary objectives of this guide are to:

* Maintain strict conceptual and epistemological consistency across all project branches.
* Mitigate the risk of overclaiming and properly contextualize computational discoveries.
* Standardize biological interpretation and decouple statistical association from mechanistic causality.
* Establish a **reviewer-resistant lexicon** across all repository outputs, including source code documentation, Jupyter notebooks, figure legends, commit messages, and manuscript drafts.

> **Repository Alignment:** This document serves as a companion policy to `PROJECT_DIRECTION.md` and `MODELING_POLICY.md`. All contributors must adhere to these linguistic constraints to ensure seamless integration.

---

## 2. Core Philosophy

Our communicative framework prioritizes conservative biological interpretation, rigorous computational nomenclature, and hypothesis-generating framing.

Definitive causal, mechanistic, or clinical terminology is strictly restricted. Such language may only be deployed when directly supported by longitudinal experimental evidence or independent, orthogonal mechanistic validation.

Whenever analytical uncertainty exists, our default linguistic posture must:

1. Attenuate causal implications.
2. Explicitly clarify observational and cross-sectional limitations.
3. Preserve the defined boundary conditions of our computational models.

---

## 3. Preferred Conceptual Framing

When describing the overarching architecture of this project, contributors must use precise, boundary-aware definitions:

* **Approved Framework Description:**
> "A computational oncology framework designed to identify conserved, cross-cancer epigenetic-transcriptomic programs associated with resistance-like contexts, functional vulnerabilities, and perturbational reversibility."


* **Prohibited Framework Description:**
> "A clinical drug resistance prediction system or biomarker discovery pipeline."



---

## 4. Lexicon Mapping: Approved vs. Discouraged Terminology

The following nomenclature matrix details mandatory vocabulary substitutions across all project assets:

| ❌ Discouraged / Prohibited Terminology | Approved Technical Alternative |
| --- | --- |
| Drug resistance prediction | Resistance-like association modeling |
| Resistant tumors | Tumors enriched for resistance-associated programs |
| Resistance signature | Candidate resistance-associated program |
| Adaptive resistance state | Resistance-like or adaptive-like context |
| Therapeutic target | Candidate vulnerability |
| Validated target | Prioritized candidate vulnerability |
| Drug repurposing candidate | Perturbational hypothesis |
| Treatment reversal | Perturbational reversal hypothesis |
| Causal mechanism | Computationally inferred association |
| Mechanistic proof | Hypothesis-supporting evidence |
| Resistance biomarker | Candidate therapy-associated marker |
| Pan-cancer mechanism | Cross-cancer recurrent program |
| Clinical prediction | Computational association |
| Validated therapy | Candidate compound hypothesis |
| Resistant lineage | Lineage enriched for resistance-associated features |
| Definitive vulnerability | Putative vulnerability |
| Resistant phenotype | Resistance-like phenotype |
| Biological driver | Candidate associated regulator |
| Causal regulator | Prioritized associated regulator |

---

## 5. Domain-Specific Terminology Policies

### 5.1 Resistance Terminology

The term **"resistance"** carries heavy clinical and evolutionary implications and must be qualified systematically. Unless explicit, functional validation is present, contributors must avoid implying direct clinical resistance, active temporal adaptation, or definitive causal mechanics.

* *Preferred modifiers:* `resistance-like`, `therapy-associated`, `drug-tolerant-like`, `adaptive-like`, `pharmacologically associated`, or `vulnerability-associated`.

### 5.2 Pan-Cancer Nomenclature

The prefix **"pan-cancer"** shall be strictly reserved for signals that recurrently emerge across multiple independent lineages, clear all lineage-confounder controls, and are not statistically driven by a single dominant tumor type.

* *Preferred alternatives for sub-universal signals:* `cross-lineage`, `multi-lineage`, `partially shared`, `recurrent across selected malignancies`, or `lineage-enriched`.

### 5.3 Post-Hoc Interpretability Metrics

Outputs from feature attribution and embedding frameworks (including SHAP values, feature importance vectors, latent spaces, and attention weights) must be framed strictly as computational prioritization aids.

* *Approved descriptors:* `statistical associations`, `prioritization metrics`, `interpretive aids`, or `hypothesis-generation layers`.
* *Prohibited descriptors:* `mechanistic proof`, `causal biology`, `definitive pathway activation`, or `validated regulatory circuits`.

### 5.4 Perturbational Frameworks (LINCS / CMap)

Connectivity-based signatures represent context-dependent computational similarity structures, not biological guarantees.

* *Approved descriptors:* `perturbational hypotheses`, `candidate reversal signatures`, `exploratory perturbational associations`, or `computational reversal prioritization`.
* *Prohibited descriptors:* `therapeutic reversal`, `validated drug repurposing`, `confirmed treatment strategy`, or `in vivo efficacy claims`.

### 5.5 The Term "Validation"

Computational replication is not biological confirmation. The term **"validation"** must be qualified to prevent overclaiming.

* *Approved variants:* `orthogonal validation`, `cross-dataset replication`, `independent cohort replication`, `secondary validation`, `computational validation`, or `exploratory validation`.
* *Prohibited implications:* `experimental proof`, `clinical validation`, or `definitive causal confirmation`.

### 5.6 Confidence Scaling & Evidence Calibration Policy

To prevent rhetorical inflation, all confidence qualifiers deployed in manuscripts, code comments, and plot annotations must be explicitly and mathematically proportional to the depth of the available data matrix. Contributors must strictly adhere to the following hierarchical progression of scientific confidence:

```
[ LOW CONFIDENCE ]
       │
       ▼  Exploratory          (Single-dataset correlation / Unadjusted baseline analysis)
       │
       ▼  Candidate            (Feature cleared initial filters; prioritized for testing)
       │
       ▼  Putative             (Biologically plausible context with preliminary support)
       │
       ▼  Associated           (Statistically robust co-segregation across multiple screens)
       │
       ▼  Recurrent            (Conserved multi-omics signal observed across divergent lineages)
       │
       ▼  Replicated           (Independently verified in an unseen external bulk cohort)
       │
       ▼  Orthogonally Supported (Validated via single-cell resolution or chromatin accessibility data)
       │
[ HIGH CONFIDENCE ]

```

### Analytical Bounds

* **Proportional Claims:** Evaluative statements must never escalate past the tier directly supported by the underlying **dataset structure**, **cross-validation depth**, and **mechanistic evidence**.
* **Strict Restraint:** A molecular program shall not be described as "recurrent" or "replicated" if the signal is derived from a single data resource, nor shall it be termed "orthogonally supported" without explicit verification via single-cell profiles ($\text{scRNA-seq}$) or chromatin state assays ($\text{ATAC-seq}$).

---

## 6. Statistical & Rhetorical Posture

To build an airtight scientific narrative, software logs and manuscripts must avoid absolute declarative verbs in favor of probabilistic, associative language.

| ❌ Prohibited Declaratives | 🟢 Approved Associatives |
| --- | --- |
| Proves | Suggests / Implies |
| Demonstrates definitively | Is associated with |
| Confirms causality | Is consistent with |
| Establishes mechanism | Supports the hypothesis that |
| Validates therapeutic effect | May indicate / Is compatible with |

---

## 7. Artifact & Codebase Naming Conventions

### 7.1 Figure Legends & Notebook Markdown

Visual and inline documentation must enforce clean separation between association and causality.

* *Approved Heading Examples:* `"Candidate resistance-associated program"`, `"Cross-dataset recurrent transcriptomic state"`, `"Putative vulnerability-associated signature"`, `"Perturbational association profile"`.
* *Prohibited Heading Examples:* `"Master regulator of resistance"`, `"Universal resistance mechanism"`, `"Validated adaptive state"`, `"Therapeutic target"`.

### 7.2 Programmatic Variables & Object Naming

The software architecture should structurally reinforce our conservative framing. Whenever feasible, avoid overly deterministic or causal terminology in variable definitions, class names, and file outputs.

* *Approved Naming Patterns:* `candidate_programs`, `resistance_like_scores`, `vulnerability_associations`, `perturbational_hypotheses`, `association_outputs`, `recurrent_state_profiles`.
* *Prohibited Naming Patterns:* `resistance_classifier`, `therapy_predictor`, `causal_signature`, `validated_targets`, `master_regulators`.

---

## 8. Manuscript Imperatives

Any manuscript, abstract, or conference submission derived from this repository must adhere to four baseline criteria:

1. Maintain an unyielding separation between statistical association and biological causality.
2. Explicitly distinguish between abstract computational prioritization and bench-side biological validation.
3. Formally outline the cross-sectional limitations of TCGA and the resolution boundaries inherent to bulk transcriptomics.
4. Rigorously isolate the definitions of `resistance-like contexts`, `adaptive resistance`, and `clinically validated resistance`.

---

## 9. Final Governing Principle

> **The Golden Rule of Project Nomenclature:** When linguistic uncertainty arises, always default to the structurally defensible over the rhetorically aggressive. A weaker, statistically sound claim will survive peer review; a fragile, overextended claim will not. Reviewer-resistant phrasing is the baseline standard of this project.

---