# Notebook 113 — CPTAC-3 External Cohort Construction and Source-Provenance Contract

**Lifecycle:** ARCHITECTURAL RESPONSIBILITY TRANSFER APPROVED 2026-10-27; IMPLEMENTATION AND COHORT FREEZE NOT AUTHORIZED YET.
**Owner:** Phase 1 / Notebook 113 (new), upstream of Phase 8 / Notebook 800.
**Normative Phase 8 policy source:** `docs/contracts/phase8/NOTEBOOK_800_ELIGIBILITY_AND_REPLICATION_CONTRACT_DRAFT.md` G2 decision and G3–G8 guardrails; this contract does not retroactively change their scientific standards.
**Inputs:** immutable 111 CPTAC-3 source universe and audited outputs, applicable 112 handoff if accepted/fingerprint-verifiable, frozen TCGA `phase2.203.final_sample_mapping`, provider/primary-study documentation and approved bounded identity metadata; all exact source records versioned.

## Responsibility transferred

Notebook 113 owns **the entire upstream construction, eligibility and proposed freeze of the external cohort**, including:
- **G2 inherited without reinterpretation:** exactly 1,082 simple primary-candidate RNA cases as the principal source universe. Keep 288 multiply represented cases outside primary candidacy (276 multiple samples / 12 multiple aliquots) and 314 ambiguous-ancestry source RNA files with non-disjoint file/case accounting. Preserve the 37 flagged simple cases for a proposed sensitivity, not a silent exclusion.
- **G3 donor provenance/adjudication:** exact cross-resource identities, PDC/TCIA/GDC/original-study cohort links only when identifier semantics and crosswalk are verified, source documentation, classification `DOCUMENTED_INDEPENDENT` / `DOCUMENTED_OVERLAP` / `UNRESOLVED_INDEPENDENCE`. Absence of collision, prospectively recruited cohort names, or publications calling a dataset 'independent' do not automatically satisfy documented patient-level independence.
- **G4 source-to-TCGA lineage crosswalk:** source `project × primary_site × disease_type` distinct from TCGA disease lineage; unresolved/ambiguous mappings retained, with full before/after attrition.
- **G5 sample technical QC admissibility:** provenance, comparability, denominator and missingness; only prereviewed threshold rules, no invented read metrics or retrospectively selected empirical cutoffs.
- **G6 upstream input compatibility and preparation:** gene and workflow compatibility, count representation and deterministic input availability; any projection/reference-scale design that depends on the structural replication estimand is **not** decided by 113 alone.
- **G8 upstream confounder/identifiability feasibility:** source batch, purity, immune/stromal content, proliferation and lineage support and missingness. Statistical adjustment and minimum inferential support remain in the prospective 800 analysis contract.
- Produce a proposed, auditable **one-patient-one-primary-RNA-file** analytic cohort with explicit excluded/not-evaluable statuses and immutable identifiers; freeze only after independent contract review, resolution of hard source gates, and 800-compatible analysis requirements.

Notebook 113 may report **no eligible independent donor cohort** and stop. No opportunistic replacement with multiplicity cases. No expression-program scores, pharmacogenomic evidence, structural replication tests, or confirmatory claims.

## Responsibilities retained by Notebook 800

- Treat executed A–H and already executed preliminary G3 lexical screening as historical diagnostics, not a cohort freeze; do not rerun or extend them as acquisition preflights.
- Consume 113's reviewed SHA-256 verified cohort and eligibility artifacts only, with lineage-aware denominators and explicit unresolved statuses.
- Own G7 replication estimand, matched negative controls, test universe, multiplicity and uncertainty, and G6/G8 **analysis-specific** decisions (normalization/projection, confounder adjustment, lineage support).
- Do **not** rebuild 113's cohort, override G3 identity adjudication or select samples after observing program outcomes. Scientific authorization for inferential use is a separate prospective Phase 8 go/no-go decision; 113 alone cannot authorize scoring.

## Required 113 handoffs (provisional filenames)

1. `113_source_provenance_manifest.json` — SHA-256 of 111/112/TCGA and every external documentary/metadata source, query parameters, snapshot date, versions and dependencies; no silent live updates.
2. `113_donor_identity_and_cohort_links.csv` — complete source identity/evidence, join namespace and method, original cohort membership or explicit UNLINKED status, donor identity class, citation/evidence ID and adjudication status.
3. `113_primary_candidate_case_eligibility.csv` — exact G2 source candidate IDs, multiplicity/ambiguous flags, G3/G4/QC/technical status, all attrition reasons, eligibility and freeze status per donor.
4. `113_source_to_tcga_lineage_crosswalk.csv` — reviewed crosswalk and unresolved groups.
5. `113_cohort_attrition_by_context.csv` — full denominator reconciliation (files, aliquots, samples, cases) by raw source context and, separately, accepted lineage.
6. `113_assay_qc_and_feature_compatibility.csv` — technical and missingness evidence without retrospective optimization.
7. `113_cohort_readiness.json` — blocked/unresolved gates and audited SHA-256 outputs; `cohort_frozen=false` until explicit prospective review and registry transaction.

The returned dataset must distinguish **candidate universe**, **technical/independence evidence**, **proposed eligible membership**, and **approved frozen analytic cohort**. Data in `data/interim/` remain provisional until reviewed; no silent `config/artifact_registry.json` registration.

## Dependencies and gatekeeping

- 111 existing immutable acquired source evidence is sufficient to start a metadata-only evaluation; do not download ~67 GiB again.
- 112 has been developed on separate branches (`notebook-112-cptac3-qc-provenance`, `notebook-112-cptac3-qc-provenance-clean`). Its **merge/accepted handoff has not been verified by this architectural change**; check exact commit, registry and reproducibility before using any 112 outputs.
- External identity metadata acquisition, if necessary, requires a bounded, reviewed source list and frozen retrieval snapshots. No GDC API expansions through 800.
- Before any cohort freeze, validate its compatibility with 800's still-unfrozen G7/G6/G8 inferential requirements. If not demonstrable, report `NOT_EVALUABLE` and stop.
- Preserve existing Phase 2–7 artifacts/representations and G2 selection decision; donor independence and lineage attrition are hard gates. No naive pan-cancer pooling or leakage.

## Implementation status

No Notebook 113 has been implemented or executed through this contract. No G3 class, QC or cohort membership has been changed. The verified Notebook 800 run at `e2269b8` and its outputs remain historical evidence; the documentary review is recorded separately under `docs/audits/phase8/`.

**Next review:** verify 112 dependency and 111 local input interface, approve bounded source-provenance acquisition and one-patient-one-file contract, then implement 113 in its own Phase 1 branch.
