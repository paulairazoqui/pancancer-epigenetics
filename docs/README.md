# Project documentation

This directory contains the scientific, methodological, operational, and decision documentation for the `pancancer-epigenetics` framework.

The project is a lineage-aware computational oncology framework oriented toward identifying recurrent epigenetic-transcriptomic programs associated with resistance-like pharmacogenomic contexts, putative functional vulnerabilities, and perturbational hypotheses. The documentation is intentionally conservative: computational association does not establish causality, clinical utility, therapeutic efficacy, or a validated target.

This README is a navigation layer. It does not replace the individual documents, frozen analytical artifacts, or dataset-provenance records.

## Start here

For a new contributor or a new analytical session, the recommended reading order is:

1. [`../README.md`](../README.md) — repository overview, current project status, data organization, and reproducibility entry point.
2. [`../roadmap.md`](../roadmap.md) — operational roadmap, notebook sequence, phase boundaries, and current analytical progression.
3. [`PROJECT_DIRECTION.md`](PROJECT_DIRECTION.md) — scientific objective, central biological object, scope, and claim boundaries.
4. [`PROJECT_ARCHITECTURE.md`](PROJECT_ARCHITECTURE.md) — analytical layers, dataset roles, independent discovery design, and cross-system architecture.
5. [`MODELING_POLICY.md`](MODELING_POLICY.md) — mandatory modeling, confounder-control, robustness, leakage-prevention, and interpretation policy.
6. [`TERMINOLOGY_GUIDE.md`](TERMINOLOGY_GUIDE.md) — mandatory reviewer-resistant terminology and evidence vocabulary.
7. [`ANALYSIS_EXECUTION_POLICY.md`](ANALYSIS_EXECUTION_POLICY.md) — execution strategy, interactive-analysis policy, Python/R guidance, and delegation boundaries.
8. [`NOTEBOOK_STYLE_GUIDE.md`](NOTEBOOK_STYLE_GUIDE.md) — notebook cell structure, documentation, reproducibility, and downstream-notebook conventions.

Read phase-specific contracts and decision records before modifying or extending the corresponding analysis.

## Core documentation map

| Document | Primary purpose |
| --- | --- |
| [`PROJECT_DIRECTION.md`](PROJECT_DIRECTION.md) | Defines the scientific question, central biological object, framework scope, and prohibited overclaims. |
| [`PROJECT_ARCHITECTURE.md`](PROJECT_ARCHITECTURE.md) | Defines the tumor, cell-line, cross-system, functional, pharmacogenomic, perturbational, and validation layers. |
| [`DATA_HARMONIZATION_PLAN.md`](DATA_HARMONIZATION_PLAN.md) | Defines identifier harmonization, integration logic, dataset alignment, and leakage-aware harmonization principles. |
| [`MODELING_POLICY.md`](MODELING_POLICY.md) | Defines mandatory modeling safeguards, confounder control, evidence categories, robustness, and leakage prevention. |
| [`TERMINOLOGY_GUIDE.md`](TERMINOLOGY_GUIDE.md) | Defines approved terminology for candidate programs, resistance-like contexts, putative vulnerabilities, perturbational hypotheses, and validation language. |
| [`ANALYSIS_EXECUTION_POLICY.md`](ANALYSIS_EXECUTION_POLICY.md) | Defines how analytical and repository work should be executed and when interactive analysis, Python, R, or delegated repository work is appropriate. |
| [`NOTEBOOK_STYLE_GUIDE.md`](NOTEBOOK_STYLE_GUIDE.md) | Defines notebook implementation and documentation conventions, including short single-responsibility cells and downstream reuse of frozen upstream artifacts. |
| [`workflow.md`](workflow.md) | Summarizes the operational handoff between phases, notebook series, inputs, outputs, and analytical boundaries. For the latest completion status, use the root README and `roadmap.md`. |

## Phase 4 closure and Phase 5 handoff

Phase 2 tumor discovery is closed and frozen, Phase 3 independent cell-line discovery is closed, and Phase 4 cross-system integration is now closed and frozen after completion of notebooks `400 — Cross-System Program Comparison` through `404 — Program Annotation`.

The frozen Phase 4 layer contains supported cross-system transcriptomic correspondences, three candidate cross-system transcriptomic consensus representations with tumor-side methylation context, lineage-aware internal robustness evidence, epigenetic-regulator enrichment results, and prespecified biological annotations. Notebooks 402–404 did not refit or reweight the consensus representations and did not use downstream robustness or annotation evidence to retrospectively redefine consensus eligibility.

The historical input contract for notebook 401 remains available at [`PHASE4_401_INPUT_CONTRACT.md`](PHASE4_401_INPUT_CONTRACT.md). It preserves the provenance and interpretation rules that governed consensus construction, including the distinction between unique RNA correspondence events, tumor structural families, and tumor cross-omic arms.

Phase 5 — Functional Vulnerabilities is the next planned analytical phase. Notebook `500 — CRISPR Associations` should consume the frozen consensus layer only after the required functional-dependency inputs have been acquired, audited, harmonized where necessary, and frozen. Downstream dependency associations are putative vulnerability evidence and must not be used to retrospectively redefine Phase 4 programs.

Phase-specific contracts constrain only their declared scope and should not be generalized into new project-wide rules without an explicit documented decision.

## Decision records

Repository-level scientific and architectural decisions are stored under [`decisions/`](decisions/).

Current decision records:

- [`decisions/001_data_integration_strategy.md`](decisions/001_data_integration_strategy.md) — data-integration strategy and dataset-role decisions.
- [`decisions/002_independent_discovery_and_cross_system_integration.md`](decisions/002_independent_discovery_and_cross_system_integration.md) — formalizes independent tumor and cell-line discovery followed by cross-system integration only after both representations are frozen.

Decision records should document durable choices that affect multiple notebooks or downstream interpretation. Notebook-local implementation details should remain in the notebook unless they become project-wide policy.

## Configuration and provenance

Narrative documentation does not replace machine-readable configuration.

- [`../config/raw_data_registry.json`](../config/raw_data_registry.json) is the source for dataset releases, source files, and raw-data provenance used by the implemented workflow.
- [`../config/paths.yaml`](../config/paths.yaml) defines repository paths consumed through the project path utilities.
- Phase-specific tracked handoff manifests under `config/` may be authoritative for downstream interpretation when explicitly declared by the relevant contract.

Raw-data provenance, frozen cohort definitions, and analytical results should be read from their versioned configuration, metadata, and processed/interim artifacts rather than reconstructed from prose summaries.

## Documentation principles

All documentation should preserve the same methodological boundaries as the analysis:

- tumor and cell-line discovery remain independent before Phase 4;
- lineage, platform, batch, purity/cellularity, proliferation, drug-family, and cell-line-overlap leakage or confounding are considered where applicable;
- random pan-cancer splitting and naive cross-lineage pooling are not acceptable substitutes for lineage-aware evaluation;
- internal robustness, cross-system reproducibility, cross-dataset replication, and orthogonal support are distinct evidence categories;
- `not recoverable`, partial correspondence, instability, negative results, and unresolved confounding are valid outcomes and should be retained;
- SHAP, feature importance, enrichment, and latent-factor inspection are interpretive or predictive-attribution tools, not causal evidence;
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
