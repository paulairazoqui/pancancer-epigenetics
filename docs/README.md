# Project documentation

This directory contains the scientific, methodological, operational, and decision documentation for the `pancancer-epigenetics` framework.

The project is a lineage-aware computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like pharmacogenomic contexts, secondary genomic and locus-level methylation-expression context, putative functional vulnerabilities, explainable predictive-model behavior, perturbational hypotheses, and integrated therapeutic-prioritization evidence. The documentation is intentionally conservative: computational association or model attribution does not establish causality, clinical utility, therapeutic efficacy, or a validated target.

The broader approved scientific project includes experimental validation. Experimental work is intentionally outside this computational repository; the repository produces reproducible computational hypotheses and frozen evidence handoffs for possible downstream experimental evaluation.

This README is a navigation layer. It does not replace the individual documents, frozen analytical artifacts, or dataset-provenance records.

## Start here

For a new contributor or a new analytical session, the recommended reading order is:

1. [`../README.md`](../README.md) — repository overview, current project status, data organization, and reproducibility entry point.
2. [`../roadmap.md`](../roadmap.md) — roadmap v3.2, notebook sequence, Phase 4B secondary characterization, explicit XAI layer, integrated evidence phase, and current analytical progression.
3. [`PROJECT_DIRECTION.md`](PROJECT_DIRECTION.md) — scientific objective, central biological object, secondary characterization role, XAI role, scope, and claim boundaries.
4. [`PROJECT_ARCHITECTURE.md`](PROJECT_ARCHITECTURE.md) — analytical layers, dataset roles, independent discovery design, Phase 4B placement, XAI placement, and cross-evidence architecture.
5. [`MODELING_POLICY.md`](MODELING_POLICY.md) — mandatory modeling, confounder-control, secondary molecular-characterization, robustness, leakage-prevention, XAI/SHAP, biological-context, and evidence-integration policy.
6. [`TERMINOLOGY_GUIDE.md`](TERMINOLOGY_GUIDE.md) — mandatory reviewer-resistant terminology and evidence vocabulary.
7. [`ANALYSIS_EXECUTION_POLICY.md`](ANALYSIS_EXECUTION_POLICY.md) — execution strategy, interactive-analysis policy, Python/R guidance, and delegation boundaries.
8. [`NOTEBOOK_STYLE_GUIDE.md`](NOTEBOOK_STYLE_GUIDE.md) — notebook cell structure, documentation, reproducibility, and downstream-notebook conventions.

Read phase-specific contracts and decision records before modifying or extending the corresponding analysis.

## Core documentation map

| Document | Primary purpose |
| --- | --- |
| [`PROJECT_DIRECTION.md`](PROJECT_DIRECTION.md) | Defines the scientific question, central biological object, framework scope, Phase 4B role, explicit XAI role, biological contextualization, and prohibited overclaims. |
| [`PROJECT_ARCHITECTURE.md`](PROJECT_ARCHITECTURE.md) | Defines the tumor, cell-line, cross-system, secondary-characterization, functional, pharmacogenomic/XAI, perturbational, validation, integrated-evidence, and computational-to-experimental handoff layers. |
| [`DATA_HARMONIZATION_PLAN.md`](DATA_HARMONIZATION_PLAN.md) | Defines identifier harmonization, integration logic, dataset alignment, and leakage-aware harmonization principles. |
| [`MODELING_POLICY.md`](MODELING_POLICY.md) | Defines mandatory modeling safeguards, confounder control, secondary genomic and methylation-expression rules, evidence categories, XAI/SHAP requirements, biological-context rules, evidence integration, and leakage prevention. |
| [`TERMINOLOGY_GUIDE.md`](TERMINOLOGY_GUIDE.md) | Defines approved terminology for candidate programs, resistance-like contexts, putative vulnerabilities, perturbational hypotheses, and validation language. |
| [`ANALYSIS_EXECUTION_POLICY.md`](ANALYSIS_EXECUTION_POLICY.md) | Defines how analytical and repository work should be executed and when interactive analysis, Python, R, or delegated repository work is appropriate. |
| [`NOTEBOOK_STYLE_GUIDE.md`](NOTEBOOK_STYLE_GUIDE.md) | Defines notebook implementation and documentation conventions, including short single-responsibility cells and downstream reuse of frozen upstream artifacts. |
| [`workflow.md`](workflow.md) | Summarizes the operational handoff between phases, notebook series, inputs, outputs, Phase 4B boundaries, XAI boundaries, integrated evidence, and analytical boundaries. For the latest completion status, use the root README and `roadmap.md`. |

## Current analytical progression

Phase 2 tumor discovery is closed and frozen, Phase 3 independent cell-line discovery is closed, and Phase 4 cross-system integration is closed and frozen after completion of notebooks `400 — Cross-System Program Comparison` through `404 — Program Annotation`.

The frozen Phase 4 layer contains supported cross-system transcriptomic correspondences, three candidate cross-system transcriptomic consensus representations with tumor-side methylation context, lineage-aware internal robustness evidence, epigenetic-regulator enrichment results, and prespecified biological annotations. Notebooks 402–404 did not refit or reweight the consensus representations and did not use downstream robustness or annotation evidence to retrospectively redefine consensus eligibility.

Roadmap v3.2 adds **Phase 4B — Secondary Molecular Context Characterization** without reopening Phase 4. Planned notebook `108 — TCGA Somatic Mutation Acquisition and Audit` provides the mutation-resource prerequisite; notebook `450 — Secondary Genomic Context Characterization` evaluates lineage-aware somatic genomic context; notebook `451 — Locus-Level Methylation–Expression Characterization` evaluates CpG-to-gene and promoter/regulatory methylation-expression relationships. Positive, negative, lineage-specific, heterogeneous, or non-recurrent outcomes are all valid, and Phase 4B results cannot redefine frozen programs.

The historical input contract for notebook 401 remains available at [`PHASE4_401_INPUT_CONTRACT.md`](PHASE4_401_INPUT_CONTRACT.md). It preserves the provenance and interpretation rules that governed consensus construction, including the distinction between unique RNA correspondence events, tumor structural families, and tumor cross-omic arms.

Phase 1 notebook `107 — DepMap RNAi Acquisition and Audit` is complete. Its distinct historical DEMETER2 v5 RNAi resource combines Achilles, DRIVE, and Marcotte, and its audited, harmonized handoffs are frozen for downstream use. The 443-model RNAi overlap is lineage- and screen-source-dependent; no fuzzy identifier rescue was used.

Phase 5 — Functional Vulnerabilities has completed its analytical workflow through notebooks `500 — CRISPR Associations`, `501 — RNAi Associations`, and `502 — Integrated Vulnerability Mapping`. CRISPR and RNAi remain separate functional-genomics evidence dimensions with their own frozen eligibility criteria and effect scales. Notebook 502 preserves platform-specific coefficients, FDR values, coverage, and lineage-aware context without statistical pooling, a common post-hoc coverage threshold, joint cross-platform FDR, or a composite vulnerability ranking. Cross-platform concordance is interpreted as complementary computational evidence rather than independent validation because biological context and cell-line populations overlap. Formal registry synchronization of the newly generated Phase 5 derived artifacts remains a reproducibility task before declaring the phase repository-frozen.

Phase 6 is planned as **Pharmacogenomic Contexts and Explainable Modeling (XAI)**. It contains the explicit explainable-AI component of the project: lineage-aware predictive modeling, SHAP attribution, attribution/stability analysis, biological contextualization at the resolution supported by the actual model features, and cross-screen replication. SHAP is interpreted as model attribution only and cannot compensate for weak predictive validity or inadequate evaluation design.

Phase 7 generates perturbational hypotheses, Phase 8 evaluates orthogonal or external computational support, Phase 9 integrates the frozen evidence—including Phase 4B context where informative—into a transparent program–vulnerability–compound framework and freezes a structured computational-to-experimental evidence handoff, and Phase 10 is reserved for manuscript preparation.

Phase-specific contracts constrain only their declared scope and should not be generalized into new project-wide rules without an explicit documented decision.

## Decision records

Repository-level scientific and architectural decisions are stored under [`decisions/`](decisions/).

Current decision records:

- [`decisions/001_data_integration_strategy.md`](decisions/001_data_integration_strategy.md) — historical data-integration strategy; superseded by ADR 002.
- [`decisions/002_independent_discovery_and_cross_system_integration.md`](decisions/002_independent_discovery_and_cross_system_integration.md) — formalizes independent tumor and cell-line discovery followed by cross-system integration only after both representations are frozen.
- [`decisions/003_xai_and_integrated_evidence_architecture.md`](decisions/003_xai_and_integrated_evidence_architecture.md) — formalizes roadmap v3.1, the explicit Phase 6 XAI/SHAP layer, the new Phase 9 integrated-evidence layer, and the Phase 10 manuscript boundary.
- [`decisions/004_secondary_molecular_context_characterization.md`](decisions/004_secondary_molecular_context_characterization.md) — formalizes roadmap v3.2, planned notebook 108, Phase 4B notebooks 450–451, the post-freeze characterization boundary, and optional publication of secondary analyses.
- [`decisions/005_biological_xai_context_and_experimental_handoff.md`](decisions/005_biological_xai_context_and_experimental_handoff.md) — formalizes hierarchical biological contextualization of XAI attributions and the structured notebook-904 computational-to-experimental evidence handoff.

Decision records should document durable choices that affect multiple notebooks or downstream interpretation. Notebook-local implementation details should remain in the notebook unless they become project-wide policy.

## Configuration and provenance

Narrative documentation does not replace machine-readable configuration.

- [`../config/raw_data_registry.json`](../config/raw_data_registry.json) is the source for dataset releases, source files, and raw-data provenance used by the implemented workflow. Planned mutation provenance will be registered when notebook 108 selects and audits the concrete source resource.
- [`../config/artifact_registry.json`](../config/artifact_registry.json) records frozen derived-artifact identity and lineage.
- [`../envs/README.md`](../envs/README.md) describes the current software reproduction records and the scope of historical execution evidence.
- [`../config/paths.yaml`](../config/paths.yaml) defines repository paths consumed through the project path utilities, including `data/interim/genomics`, `data/processed/secondary_characterization`, and `data/processed/integrated_evidence`.
- Phase-specific tracked handoff manifests under `config/` may be authoritative for downstream interpretation when explicitly declared by the relevant contract.

Raw-data provenance, frozen derived-artifact lineage, software reproduction records, cohort definitions, and analytical results should be read from their versioned configuration, metadata, environment records, and processed/interim artifacts rather than reconstructed from prose summaries.

## Documentation principles

All documentation should preserve the same methodological boundaries as the analysis:

- tumor and cell-line discovery remain independent before Phase 4;
- Phase 4B is post-freeze characterization and cannot alter frozen Phase 4 programs;
- lineage, platform, batch, purity/cellularity, proliferation, mutation prevalence/caller provenance, drug-family, and cell-line-overlap leakage or confounding are considered where applicable;
- random pan-cancer splitting and naive cross-lineage pooling are not acceptable substitutes for lineage-aware evaluation;
- preprocessing, feature selection, and hyperparameter tuning for predictive models must remain inside the training/resampling structure;
- internal robustness, cross-system reproducibility, secondary molecular context, cross-screen reproducibility, cross-dataset replication, and orthogonal support are distinct evidence categories;
- `not recoverable`, partial correspondence, instability, weak predictive performance, unstable attribution, absent genomic associations, absent methylation-expression coupling, negative results, and unresolved confounding are valid outcomes and should be retained;
- SHAP, feature importance, enrichment, and latent-factor inspection are interpretive or predictive-attribution tools, not causal evidence;
- model attribution must not be reported at a finer resolution than the actual fitted feature space supports;
- biological annotation mapped downstream from program-level SHAP is contextualization, not gene-level SHAP evidence;
- Phase 9 evidence dimensions must remain separately traceable rather than being naively pooled;
- the notebook-904 computational-to-experimental handoff is an evidence package, not experimental validation or an assay prescription;
- terminology must remain consistent with [`TERMINOLOGY_GUIDE.md`](TERMINOLOGY_GUIDE.md).

## Supporting directories

- [`decisions/`](decisions/) — durable project decisions.
- [`protocols/`](protocols/) — reserved for reusable protocols when protocol-level documentation is required.
- [`references/`](references/) — reserved for project reference material that belongs in version control.

`scaffold_manifest.json` and `.gitkeep` files are repository-structure metadata, not scientific source-of-truth documents.

## Maintenance

When documentation changes:

1. update the narrowest authoritative document for the affected scope;
2. avoid duplicating notebook outputs or frozen analytical results across multiple prose files;
3. update this README only when the documentation map, reading order, phase-specific contracts, or durable navigation changes;
4. keep status claims synchronized with the root README and `roadmap.md`; and
5. preserve the conservative scientific framing defined by the project policies.
