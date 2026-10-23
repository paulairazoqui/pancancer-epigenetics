# Notebook 800 — G3 donor-independence adjudication protocol (draft)

**Status:** PROSPECTIVE DRAFT; not approved or frozen; no G3 donor class assigned by this document.
**Scope:** CPTAC-3 RNA primary-candidate universe defined in G2 (1,082 simple cases); 288 multiply represented cases retained outside primary analysis.
**Repository source of authority:** `docs/contracts/phase8/NOTEBOOK_800_ELIGIBILITY_AND_REPLICATION_CONTRACT_DRAFT.md`, section 4.2.
**No biology or inferential analysis authorized.**

## 1. Evidence hierarchy
1. Audited direct entity and identity evidence: Notebook 111 file index, original acquisition-time GDC metadata, direct associated-entities snapshot; verify pre-existing fingerprint records before consuming. Preserve source UUID and submitter fields without filling missing values.
2. TCGA reference: exact registered `phase2.203.final_sample_mapping` (9,965 rows, frozen SHA-256 from `config/artifact_registry.json`); check fingerprint before reading.
3. Documentary provenance: versioned, specific CPTAC-3 and TCGA source/cohort documentation, donor crosswalks or explicit cohort-exclusion statements. Preserve source URL, title, access date, exact claim and applicability to each case/study segment.
4. Evidence unavailable in these sources stays unavailable. No inferred person identity from disease, sex, dates, tissue or clinical similarity. No speculative matching; no live GDC fetch within 800.

## 2. Outcome-blind screening and adjudication
- Verify the 1,082 G2 simple-case universe is recovered exactly from 111/800-A metadata; do not select replacements from 288 multiplicity cases.
- Run separate exact namespace-aware joins: CPTAC `case_uuid` vs TCGA `rna_case_uuid`; CPTAC `case_submitter_id` vs TCGA `case_submitter_id`; and only additional comparable identifiers whose semantics are explicitly documented. Preserve raw values, nonmissingness, multiplicity and evidence per join. Avoid cross-namespace comparisons and arbitrary string transformations.
- Exact collision is a **review flag**, not automatically a donor overlap without proof the IDs share a donor namespace or a validated crosswalk. No collision is **not** proof of independence.
- `DOCUMENTED_OVERLAP`: positive donor-level linkage from shared donor identifier with established namespace, or independently validated crosswalk/provenance.
- `DOCUMENTED_INDEPENDENT`: explicit, applicable documentary assurance or donor-level identity verification ruling out overlap with the frozen TCGA donor cohort. Merely distinct project IDs, collection prospective design, absence of collision or different UUIDs do not qualify.
- `UNRESOLVED_INDEPENDENCE`: neither of the above standards met. Record reason(s): insufficient source coverage; incomparable ID namespaces; source provenance only at study level; conflicting evidence; unresolved crosswalk.
- Conflicting credible evidence must remain unresolved for adjudication and be escalated; never resolve with score/lineage behavior. No bulk assignment of `DOCUMENTED_INDEPENDENT` from cohort-level prospective design without an explicit cohort non-overlap guarantee applicable to the cases being classified.
- Any adjudication decision is reviewed and versioned independently of replication results.

## 3. Required non-inferential outputs
- `800_g3_donor_identity_evidence.csv`: exactly one row per G2 simple case, case UUID, case submitter, file/sample/aliquot identifiers; source counts/flags, tested namespace joins, match counts and matched reference IDs (when appropriate), evidence provenance IDs, adjudication class, justification, reviewer status.
- `800_g3_identity_source_inventory.csv`: source/handoff location, hash, field schema, coverage, data vintage, whether original case identifier information is present; documentary URL/DOI and applicability.
- `800_g3_donor_independence_summary.json`: G2 input/reconciliation counts; independent/overlap/unresolved counts (not assumed), collision results and review status; hard gate `G3=BLOCKED` unless reviewed independence suffices; `external_analysis_authorized=false`.
- Denominators: one record per case, report source context `primary_site × disease_type` without treating this as a harmonized TCGA lineage. Preserve the 37-case additional ambiguous-RNA-file flag and distinct 288-case secondary boundary.
- Persist SHA-256 of inputs and outputs, code version, protocol version, and exact source documents. The outputs are interim only until review; do not register them as validation evidence.

## 4. Implementation boundary
The G3 adjudication belongs scientifically in Phase 8. Prefer a small, independently testable helper under `src/` and a compact Notebook 800 consumption/reporting stage. Preserve executed A–H history; **do not append PREFLIGHT-I** or re-run full A–H. Existing lexical collision screen in Notebook 800 is descriptive historical evidence only.
If the available sources lack a required donor crosswalk or provenance statement, formulate a **bounded Phase 1 acquisition/handoff request**, with precise missing fields and source, rather than querying GDC directly from 800.

## 5. Gate and falsification criteria
G3 cannot PASS because of zero collisions. It cannot PASS from prospective-study origin alone. Confirmatory independent-donor replication cannot use `UNRESOLVED_INDEPENDENCE` cases by default. If no sufficiently documented independent cohort is identifiable, conclude `NOT_EVALUABLE_DONOR_INDEPENDENCE`, preserving exploratory potential separately, without changing G2 or the Phase 4 programs. G4 and G5–G8 remain blocked independently.
