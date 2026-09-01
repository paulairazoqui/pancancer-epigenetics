# ADR 005 — Biological XAI Context and Computational-to-Experimental Handoff

## Status

Accepted as a refinement within roadmap v3.2.

---

## Context

Review of the two external evaluations of the approved project did not identify a missing computational phase after roadmap v3.2. The evaluations did, however, reinforce two aspects that should be explicit in the computational architecture:

1. explainable modeling should contribute biological interpretation in addition to predictive characterization; and
2. the final integrative computational product should provide a clear starting point for downstream experimental evaluation.

The approved project also places the computational and experimental components in sequence. Experimental validation is outside this repository, but the computational repository should produce an evidence handoff that is usable by the broader project without overstating computational findings.

These refinements do not change the frozen discovery objects, add a new analytical phase, or alter the conservative interpretation of SHAP.

---

## Decision

### 1. Notebook 602 will include hierarchical biological contextualization

Notebook `602 — SHAP Attribution and Stability Analysis` remains the primary XAI interpretation notebook.

Model attribution must be reported at the resolution of the features actually supplied to the fitted model.

Therefore:

* a model using consensus-program scores produces program-level SHAP attribution;
* a model using gene-level features may produce gene-level SHAP only if those features were included under the same leakage-safe training and evaluation design;
* downstream mapping from an attributed program to genes, pathways, epigenetic regulators, methylation context, or Phase 4B context is biological contextualization rather than additional SHAP attribution.

Where informative, stable attributed programs may be contextualized through the following frozen hierarchy:

1. attributed model feature or consensus program;
2. frozen program gene loadings or member genes;
3. Phase 4 pathway and biological annotations;
4. Phase 4 epigenetic-regulator enrichment;
5. tumor-side methylation context; and
6. Phase 4B locus-level methylation-expression or genomic context.

This design prevents pseudo-resolution, such as redistributing program-level SHAP values across constituent genes and presenting the result as gene-level attribution.

### 2. Notebook 904 will produce a structured computational-to-experimental handoff

Notebook `904 — Final Candidate Catalog and Handoff` will freeze a structured evidence package for retained candidate relationships.

Where information exists, candidate records should include:

* frozen program identity;
* putative vulnerability or target context;
* candidate compound and known target/mechanism annotation;
* expected association or perturbational direction;
* CRISPR/RNAi evidence;
* pharmacogenomic association and cross-screen evidence;
* predictive-model and XAI attribution/stability context;
* perturbational evidence;
* drug–target knowledgebase evidence;
* secondary genomic or locus-level methylation-expression context;
* lineage breadth and heterogeneity;
* external or orthogonal support;
* explicit missing, conflicting, or unresolved evidence; and
* a concise computational rationale for possible downstream experimental evaluation.

Because the broader approved project includes experimental work in sarcoma models, RMS or OS relevance may be annotated when directly supported by the available computational datasets. Lack of sarcoma/RMS/OS coverage or evidence must be recorded explicitly rather than inferred from unrelated lineages.

The handoff is not an experimental protocol. It must not prescribe assay design, concentration, dose, schedule, clinical actionability, or expected therapeutic efficacy.

---

## Boundaries

* SHAP remains model attribution, not causal or mechanistic evidence.
* Biological contextualization cannot create attribution at a finer resolution than the fitted model supports.
* Phase 4, Phase 4B, and downstream evidence remain separately traceable.
* The experimental handoff cannot retrospectively redefine candidate eligibility or frozen consensus programs.
* Absence of RMS/OS-specific evidence is a valid and reportable outcome.
* Experimental validation remains outside this repository.

---

## Consequences

### Advantages

* makes the XAI component biologically interpretable without conflating annotation with attribution;
* aligns the computational implementation more clearly with the approved project's emphasis on interpretation in addition to prediction;
* creates a reproducible bridge between computational prioritization and downstream experimental work;
* preserves lineage-aware and leakage-resistant modeling boundaries; and
* prevents the final candidate catalog from becoming a manuscript-only ranking without explicit evidentiary provenance.

### Costs and constraints

* notebook 602 must preserve the exact resolution of the fitted feature space when reporting attribution;
* hierarchical contextualization requires traceable links to frozen Phase 4 and Phase 4B annotations;
* notebook 904 must preserve missing and conflicting evidence rather than forcing complete candidate stories; and
* sarcoma/RMS/OS relevance may remain unavailable for many candidates because computational coverage is dataset-dependent.

---

## Interpretation

Biological contextualization explains how an attributed model feature relates to the frozen biological framework; it does not increase the causal or attribution resolution of SHAP.

The computational-to-experimental handoff organizes evidence for downstream study design; it is not experimental validation itself.
