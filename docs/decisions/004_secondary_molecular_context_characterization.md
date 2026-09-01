# ADR 004 — Secondary Molecular Context Characterization

## Status

Accepted for roadmap v3.2.

---

## Context

The approved scientific project explicitly includes public multi-omic integration spanning DNA methylation, transcriptomics, somatic mutations, and preclinical drug-sensitivity information. It also describes locus-level methylation-expression relationships, including inverse promoter-methylation/expression patterns, as one component of the computational characterization.

The implemented framework has already frozen the primary discovery architecture:

* Phase 2 — tumor epigenetic-transcriptomic discovery;
* Phase 3 — independent cell-line transcriptomic discovery; and
* Phase 4 — cross-system comparison and consensus construction.

Those phases produced three frozen candidate cross-system transcriptomic consensus representations with tumor-side methylation context. Reopening discovery to incorporate mutations or locus-level methylation-expression results would introduce avoidable post hoc selection risk and would weaken the separation between discovery and characterization.

At the same time, omitting the mutation layer entirely would leave an explicit component of the approved project unexplored, and the existing component-level RNA–methylation integration does not fully address the approved project's locus-level promoter/CpG-to-gene characterization.

---

## Decision

Roadmap v3.2 adds a new downstream characterization block:

> **Phase 4B — Secondary Molecular Context Characterization**

This phase does not reopen Phase 4 and does not create a second discovery workflow.

### 1. TCGA somatic-mutation acquisition is added to Phase 1

A planned notebook is added:

* `108` — TCGA Somatic Mutation Acquisition and Audit

Notebook 108 will acquire and audit one prespecified TCGA/GDC somatic-mutation resource with explicit provenance, workflow/caller identity, sample/case mapping, coverage, duplicate handling, and compatibility with the frozen tumor cohort.

Mutation-call resources must not be naively combined across callers or processing pipelines.

### 2. Secondary genomic-context characterization is added

A planned notebook is added:

* `450` — Secondary Genomic Context Characterization

Its purpose is to ask whether already frozen tumor/consensus program scores are associated with recurrent somatic genomic contexts after accounting for lineage/project structure.

Potential analyses include prespecified cancer-driver mutation status, pathway-level mutation context, and mutation-burden summaries only when the latter can be defined comparably and defensibly before inspecting results.

Somatic mutations are treated as contextual evidence, not as a new latent-program discovery modality.

### 3. Locus-level methylation-expression characterization is added

A planned notebook is added:

* `451` — Locus-Level Methylation–Expression Characterization

Its purpose is to characterize CpG-to-gene and promoter/regulatory methylation-expression relationships relevant to the frozen programs, including inverse relationships compatible with promoter hypermethylation and reduced gene expression where annotation and coverage permit.

Project/lineage structure, methylation platform, tumor purity, annotation uncertainty, and other applicable confounders must remain explicit.

Inverse methylation-expression association is compatible with epigenetic regulation but does not establish mechanistic regulation or causality.

### 4. Frozen-program boundary

Neither notebook 450 nor notebook 451 may:

* rescue a previously unsupported program;
* exclude a frozen program;
* alter program orientation or weights;
* redefine consensus eligibility;
* rename programs on the basis of downstream results; or
* feed results back into Phase 2–4 discovery decisions.

Positive, negative, heterogeneous, lineage-specific, or non-recurrent results are all valid outcomes.

### 5. Publication is optional

Phase 4B is part of the research program, not a publication obligation. Analyses may remain as documented negative or contextual results if they do not materially strengthen a manuscript.

Downstream Phase 9 may use Phase 4B outputs as separately traceable contextual evidence when scientifically relevant.

### 6. Copy-number alterations are not automatically added

The approved project explicitly mentions mutations, not a comprehensive genomic-aberration layer. Copy-number alteration analysis is therefore not included by default in Phase 4B. It may be added later only if a concrete biological question and prespecified analysis justify it.

---

## Consequences

### Advantages

* closes the remaining mutation-layer gap relative to the approved computational project;
* adds the locus-level methylation-expression characterization explicitly described in the approved methodology;
* preserves the frozen status and independence of the existing discovery architecture;
* treats negative findings as legitimate research outputs rather than forcing publication-oriented signal seeking;
* provides a clearer separation between discovery, secondary molecular characterization, and downstream functional/pharmacological evidence.

### Costs and constraints

* notebook 108 requires a new dataset-specific acquisition and provenance audit;
* somatic-mutation associations are highly vulnerable to lineage confounding and require lineage-aware analysis;
* locus-level methylation-expression work requires careful probe annotation, platform handling, and purity/confounder control;
* multiple-testing burden and sparse mutation prevalence may substantially limit interpretable associations;
* Phase 4B may produce no robust recurrent result, which is an acceptable outcome.

---

## Interpretation

Secondary genomic context is characterization, not rediscovery.

Inverse methylation-expression association is regulatory-context evidence, not mechanistic proof.

A negative Phase 4B result does not weaken the validity of the frozen Phase 4 consensus programs; it indicates that the tested secondary molecular context did not provide robust additional support under the prespecified analysis.
