# ADR 003 — Explicit XAI and Integrated Evidence Architecture

## Status

Accepted for roadmap v3.1.

---

## Context

The approved scientific project is titled:

> *Firmas epigenéticas de resistencia en cáncer: análisis pan-cáncer, inteligencia artificial explicable y validación experimental.*

The computational repository intentionally excludes the experimental-validation component because that work belongs outside the repository's analytical remit. The computational architecture must nevertheless retain explicit alignment with the approved pan-cancer, epigenetic, resistance-associated, and explainable-AI objectives.

An architecture audit comparing the approved project with the current repository identified two issues:

1. explainable AI was present only as a nested modeling task in the planned pharmacogenomic phase and was not sufficiently explicit for a major objective named in the approved project title; and
2. the roadmap separated functional-genomics, pharmacogenomic, perturbational, and external-validation evidence but lacked a final analytical phase that recombined those evidence layers with direct drug–target knowledgebase mapping into the integrative candidate framework described by the approved project.

The audit did **not** identify a need to reopen the frozen tumor-discovery, cell-line-discovery, or cross-system-consensus phases.

---

## Decision

The project adopts roadmap **v3.1** with the following architecture changes.

### 1. Phase 6 explicitly contains the XAI objective

Phase 6 is renamed:

> **Pharmacogenomic Contexts and Explainable Modeling (XAI)**

The planned notebook sequence is:

* `600` — Program–Drug Associations
* `601` — Explainable Predictive Modeling
* `602` — SHAP Attribution and Stability Analysis
* `603` — Cross-Screen Replication

SHAP and related feature-attribution methods are applied only after the prediction target, feature space, leakage controls, evaluation design, and model-validity assessment are established.

Random pan-cancer train/test splitting is prohibited. Lineage-aware or appropriately grouped evaluation is mandatory, and cell-line-overlap, drug-family, preprocessing, and feature-selection leakage must be controlled.

SHAP explains fitted-model behavior. It does not establish biological causality, mechanistic regulation, validated biomarkers, therapeutic targets, or clinical predictiveness.

### 2. A final analytical integration phase is added

A new phase is added after orthogonal/external validation:

> **Phase 9 — Integrated Evidence Synthesis and Therapeutic Prioritization**

The planned notebook sequence is:

* `900` — Target–Drug Knowledgebase Mapping
* `901` — Cross-Evidence Integration
* `902` — Candidate Evidence Stratification
* `903` — Program–Vulnerability–Compound Map
* `904` — Final Candidate Catalog and Handoff

This phase integrates separately traceable evidence from:

* Phase 4 program and epigenetic-regulator characterization;
* Phase 5 CRISPR and RNAi associations;
* Phase 6 pharmacogenomic associations, predictive models, SHAP, and stability analyses;
* Phase 7 LINCS/CMap perturbational hypotheses;
* Phase 8 external or orthogonal support; and
* prespecified drug–target knowledgebases such as ChEMBL and DrugBank where accessible.

These evidence sources are not treated as interchangeable measurements or naively pooled. The preferred representation is a multidimensional evidence matrix and prespecified evidence strata rather than an opaque universal score.

### 3. Manuscript preparation moves to Phase 10

The previous Phase 9 manuscript-preparation block becomes:

> **Phase 10 — Manuscript Preparation**

with planned notebooks `1000`–`1004`.

### 4. Frozen upstream phases remain frozen

Phases 2–4 are not reopened or redefined by this decision. Downstream XAI, therapeutic mapping, or convergent evidence must not retrospectively rescue, exclude, reweight, rename, or redefine the frozen consensus programs.

---

## Experimental Validation Boundary

Experimental validation remains part of the broader approved scientific project but outside this computational repository.

The repository may produce a frozen candidate catalog and evidence handoff suitable for downstream experimental prioritization. It must not describe computational convergence as experimental validation.

---

## Consequences

### Advantages

* restores explicit architectural visibility to explainable AI;
* makes SHAP a prespecified analytical task rather than an optional visualization step;
* places XAI after valid pharmacogenomic target definition and leakage-aware model evaluation;
* closes the previously missing transition from separate evidence layers to an integrated program–vulnerability–compound framework;
* preserves the independence and frozen status of completed discovery phases; and
* aligns the computational work more transparently with the approved project while retaining conservative claim boundaries.

### Costs and constraints

* Phase 6 requires stricter model-evaluation and leakage-control planning before SHAP is calculated;
* weak predictive performance or unstable SHAP attribution must be retained as valid negative results;
* Phase 9 requires explicit evidence provenance and handling of partially dependent data sources;
* direct drug–target resources require dataset-specific acquisition, licensing/access review, and provenance before use; and
* the final candidate catalog may contain conflicting or incomplete evidence rather than a single clean ranking.

---

## Interpretation

Explainability is evidence about model behavior, not biological causality.

Integrated evidence is evidence convergence, not therapeutic validation.

The final outputs remain computational hypotheses requiring suitable downstream experimental evaluation before stronger mechanistic or translational claims can be made.
