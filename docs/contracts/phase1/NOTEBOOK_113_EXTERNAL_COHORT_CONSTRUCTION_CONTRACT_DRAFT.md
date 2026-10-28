# Notebook 113 — CPTAC-3 External Cohort Construction and Source-Provenance Contract

**Lifecycle:** ARCHITECTURAL RESPONSIBILITY TRANSFER APPROVED 2026-10-27; NOTEBOOK 113 IMPLEMENTED AS A CONSERVATIVE, UNEXECUTED METADATA LEDGER; G3 PROTOCOL APPROVAL, COHORT FREEZE AND BIOLOGICAL INFERENCE PENDING.
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

Notebook 113 has been implemented in `notebooks/phase1_data_acquisition_and_auditing/113_cptac3_external_cohort_construction.ipynb` (commit `be7500b`), but not yet executed or locally validated. It reconstructs the approved G2 universe and emits conservative unresolved G3/G4/QC evidence ledgers, with optional separately reviewed external evidence. It does not freeze a cohort, assign sample eligibility from program outcomes or authorize inference. No G3 scientific approval is implied. The verified Notebook 800 run at `e2269b8` and its outputs remain historical evidence; the documentary review is recorded separately under `docs/audits/phase8/`.

**Next execution:** run the implemented 113 notebook locally against 111 CSV artifacts and the frozen TCGA mapping; audit exact G2 reconciliation and emitted interim ledgers. Then adjudicate documented donor/cohort linkage, lineage, QC, G6 and G8 evidence before any freeze. Notebook 112 remains a separate, not-yet-accepted QC provenance input.


---

## Normative addendum — transferred G2/G3 rules and source cohort construction

**Status (2026-10-27):** Architectural transfer approved; **G2 candidate-universe policy APPROVED (2026-10-23)**; **G3 protocol PROSPECTIVE DRAFT, NOT APPROVED**; G4–G8 criteria and final cohort freeze pending review. This is an operational transfer of responsibilities, not retroactive scientific approval.

**Traceable original sources (branch `notebook-800-preflight-a`, transfer HEAD `b7ccc7e`):**
- `docs/contracts/phase8/NOTEBOOK_800_ELIGIBILITY_AND_REPLICATION_CONTRACT_DRAFT.md` (G2 policy §4.1, identity §4.2, other gate safeguards §3–7, architectural amendment §9).
- `docs/contracts/phase8/NOTEBOOK_800_G3_DONOR_INDEPENDENCE_PROTOCOL_DRAFT.md` (prospective G3 evidence hierarchy and adjudication specification).
- `docs/audits/phase8/NOTEBOOK_800_G3_DONOR_INDEPENDENCE_DOCUMENTARY_AUDIT.md` (historical exploratory evidence, not prospective donor adjudication).
These original files need not be merged to `main` for this Phase 1 contract to be operationally self-contained; their exact Git source revisions remain auditable.

### G2 — approved, inherited unchanged

From the audited provisional-primary inventory of **1,370 cases / 1,731 primary RNA files**, the initial **primary candidate universe is exactly 1,082 cases / 1,082 files** with one uniquely resolved primary-tumor STAR file, sample, and aliquot each. Source identity must match the Notebook 111 immutable file inventory (UUID, filename, size, provider MD5, direct case/aliquot association, unique sample UUID, `sample_type == Primary Tumor`). File/case/sample/aliquot identifiers must never be conflated.

The **288 multiply represented cases / 649 primary files** are outside this candidate universe: **276 multiple-sample cases / 619 files** and **12 multiple-aliquot cases / 30 files**. No preferred-file, selection, or secondary sensitivity policy is approved. A separately preregistered, outcome-blind selection and identity reconciliation are prerequisites for any secondary use; never rescue insufficient primary numbers post hoc.

Keep the **314 RNA source files with ambiguous sample ancestry** visible in separate **file-level** accounting; these can coexist with unique candidates in the *same case* and must not be added as disjoint patient groups. **530** of the 1,082 simple cases have additional RNA files (**544** extra files: 488 resolved normal, 18 resolved recurrent, 38 ambiguous). **37 simple cases** have additional ambiguous RNA files: retain their primary-candidate membership, flag them, and consider exclusion **only as a prespecified sensitivity**, never by default. These are structural—not QC or donor-independence—observations.

Preserve at every step (a) raw GDC `project × primary_site × disease_type` contexts, (b) files/aliquots/samples/cases as separate denominators, (c) non-overlapping file accounting, (d) exact per-case eligibility status and attrition reasons. The 1,082 cases are **candidates**, not a frozen external analytic cohort.

### G3 — transferred prospective adjudication policy (NOT YET APPROVED)

**Evidence priority:**
1. Existing audited Notebook 111 acquisition-time GDC direct entity relationships, source identities, and fingerprinted manifests (verify checksums, never fill absent fields).
2. Exact frozen TCGA `phase2.203.final_sample_mapping` for **9,965 discovery cases**, verified against its authoritative registry SHA-256 before use.
3. Versioned, specific original CPTAC-3, TCGA, dbGaP, PDC, TCIA or institutional donor provenance, validated identity crosswalk or **explicit applicable non-overlap/exclusion statement**. Retain document URL, source title, date accessed, wording/claim, precise subset to which it applies and evidence ID.
4. Unknown identities remain unknown. Do not infer personal matches from clinical attributes, disease, sex, dates, or cohort size; do not fabricate a crosswalk.

**Outcome-blind exact namespace-aware screening:** compare CPTAC `case_uuid` with TCGA `rna_case_uuid`; CPTAC `case_submitter_id` with TCGA `case_submitter_id`; only compare other identifiers where both their namespace and donor-level semantics have been documented. Preserve originals, missingness, join cardinalities, flagged collisions and source evidence. A collision is a **review flag**, not automatically a demonstrated donor overlap when identifier namespaces differ; zero collisions **does not prove independence**.

**Exactly one per-case identity classification:**
- `DOCUMENTED_OVERLAP`: positive donor-level linkage via verified common identifier namespace, provenance or validated crosswalk.
- `DOCUMENTED_INDEPENDENT`: a credible, explicit, applicable institutional/study non-overlap assurance or independently verifiable donor-level evidence that excludes overlap with the frozen TCGA discovery patients. An assurance at cohort level applies **only after verified linkage of each candidate case to its covered cohort**.
- `UNRESOLVED_INDEPENDENCE`: neither criterion established; includes incompatible namespaces, unavailable source records, unknown cohort membership, absent non-overlap assurance or credible conflict.

**Hard rule:** prospectively recruited study ≠ proven donor-independent study; different project UUIDs ≠ proven independent donors. Conflicting credible evidence remains unresolved for independent review; never settle by favorable expression patterns. The previous 800 lexical screen reported **zero exact collisions / all 1,082 unresolved**: this is *historical screening only*, not an outcome for 113 and not grounds to label independent.

Until review and explicit approval of this G3 protocol, implementations may populate *evidence ledgers* but must not designate classes as frozen eligibility decisions. Unresolved cases cannot contribute to confirmatory independent-donor replication by default. If no sufficient independent donor set is documented, return `NOT_EVALUABLE_DONOR_INDEPENDENCE` and stop without replacing G2 candidates.

### G4 — lineage construction

Document a crosswalk of original GDC `project × primary_site × disease_type` to supported, frozen TCGA lineage/project designations using ontology or documented study records. Retain unmapped source labels; classify `UNMAPPED`, `AMBIGUOUS`, `CONTRADICTORY`. No guess from a label, no outcome-guided rescue. Attribute losses by **source context** and **accepted harmonized lineage** separately, preserving all source denominators.

### G5 — technical QC admissibility

Provider MD5 PASS, unambiguous sample ancestry and 2,389/2,389 Ensembl gene availability do **not** imply independent sequencing QC PASS. GDC source read/map/duplicate/base quality/insert-size fields may support QC only after verified measurement definition, software version, denominator (read vs pair/fragment), data-generation workflow, provenance and cross-lineage comparability. STAR `N_*` unassigned counts are not valid standalone mapping fractions. No retrospective empirical read-count or low-count percentile thresholds. Missing = `QC_UNASSESSED`, never automatic PASS/FAIL. The 112 twelve-file pilot supports GDC source-field provenance, **not population-wide QC**, and 112 handoff is not considered accepted until its exact branch/PR/reproducibility and output SHA-256 are verified.

### G6 — source assay/input compatibility

Audit deterministic availability and exact gene identifiers, STAR/count workflow provenance, count representation, measurement comparability and missingness. Preserve Phase 4's **three immutable programs**, 2,389 shared ordered features and signed loadings; do not relearn weights, change their orientation, standardize TCGA/CPTAC jointly or derive QC thresholds from program scores. Normalization/projection decisions affecting 800's replication estimand require a **prospective, outcome-blind alignment with 800 before any 113 cohort freeze**. No biological scores in 113.

### G8 — source confounder and design feasibility

Record batch/workflow/site, tumor purity (if validly sourced), immune/stromal and proliferation covariate availability, data missingness and batch-lineage identifiability. Do not assume missing covariates are normal. If lineage and batch are fully confounded, flag `NON_IDENTIFIABLE`; do not force an adjustment. Notebook 800 retains inferential covariate decisions, negative controls and minimum lineage support; 113 documents feasibility and cohort-level status without inspecting program outcomes.

### Artifact-level handoff and scientific authorization

Notebook 113 must produce immutable, SHA-256-verified case-level evidence and provenance tables, complete G2-to-final attrition, accepted lineage crosswalk, QC/feature audit, confounder feasibility and explicit blockers consistent with the seven prospective outputs specified above. Separate **source candidate**, **documentary/technical adjudication**, **proposed eligible**, and **independently approved frozen** status. Every join must preserve donor uniqueness; state denominators before and after each gate. No registry write or `cohort_frozen=true` merely because an analysis ran.

Notebook 113 owns upstream cohort construction and the **proposed freeze**, conditional on signed-off identity/QC/lineage criteria and upstream/downstream compatibility. Notebook 800 owns G7 inferential test specification, structural replication and the independent go/no-go for consuming the proposed cohort; 800 must not select or replace patients after viewing scores.

**Current stop state:** `G2_POLICY_APPROVED`; `G3_PROTOCOL_DRAFT`; `G3_BLOCKED`; `G4_G5_G6_G8_NOT_ADJUDICATED`; `cohort_frozen=false`; `external_analysis_authorized=false`. No new G3 class, no finalized cohort and no biological inference are created by this document.


---

## Superseding G3 amendment — proportional cohort-level standard (2026-10-28)

**This amendment supersedes the earlier G3 individual-donor documentary requirement and all conflicting G3 stop-state wording above.** The previous per-case assurance standard was an overly stringent assistant-proposed criterion, not a user-approved scientific necessity. G2, G4–G8, no-leakage safeguards, and cohort-freeze responsibilities remain unchanged.

**Objective.** Establish a defensible *external cohort* for structural replication relative to TCGA, not certify absence of every conceivable shared donor with genetic identity testing. The primary cohort is the audited GDC `CPTAC-3` prospective acquisition. Published uses of CPTAC-3 for external validation and the distinction from retrospective `CPTAC-TCGA` sources provide cohort-level context. Exact GDC/TCGA case-ID screening (zero flags in the executed candidate universe) is complementary, **not** definitive donor-identity proof.

**Prospective outcome-blind rule.**
- `COHORT_SUPPORTED_EXTERNAL`: audited `CPTAC-3` GDC source, no flagged TCGA ID collision, and no conflicting source evidence. PDC `CPTAC3 Discovery and Confirmatory` is corroborating evidence. A missing PDC match does not invalidate the GDC project provenance. This class is a *cohort-level assumption*, not `DOCUMENTED_INDEPENDENT` at patient level.
- `SOURCE_REVIEW_REQUIRED`: contradictory/ambiguous PDC linkage, subprojects outside the prospective Discovery/Confirmatory label (including `CPTAC3-Other`), ID collision or other provenance uncertainty. These cases are withheld from a proposed external analytic cohort pending narrowly scoped source review; no individual genetic testing required.
- `DOCUMENTED_OVERLAP`: affirmative, namespace-verified donor reuse or verified `CPTAC-TCGA` origin. Exclude.
- Case-level reviewed exception evidence may override default only with traceable source, applicability and review. No expression-program outcomes may enter the decision.

**Interpretation and scope.** G3 can be provisionally closed at the *cohort-provenance* level using these rules, provided all exceptions remain excluded/pending and source references are recorded. Do not claim zero donor-level overlap. Do not confuse a G3 PASS with G4/G5/G6/G8, which remain blocked until evaluated. Notebook 113 must retain all 1,082 G2 candidates with explicit G3 statuses; it cannot freeze the final cohort or authorize Notebook 800 inference by itself.

**Foundational source context (not proof of each donor's identity):** NCI CPTAC program and CPTAC-3 prospective acquisition; dbGaP `phs001287`; original CPTAC-3 cancer-cohort studies linked in Notebook 113; PDC project and study identity snapshots with locally verified SHA-256. Exact source URLs and evidence must be preserved in the phase handoff; `G3_CPTAC3_PROSPECTIVE_COHORT` is the named cohort-level evidence identifier. This rule was set without looking at external program replication outcomes.


---

## G4 source-context harmonization implementation — 2026-10-28

G4 uses a predefined, **source site × GDC broad histology** crosswalk targeting only project IDs present in the frozen TCGA reference. It does not equate broad GDC histology to histopathological subtyping, nor does it impute subtype from organ alone. Seven disease groups are provisionally comparable: LUAD, LUSC, PAAD, SKCM, STAD, UCEC and HNSC (multiple anatomic sites). Source `Brain/Gliomas` and `Kidney/Adenomas and Adenocarcinomas` remain `AMBIGUOUS` because GBM/LGG and KIRC/KIRP/KICH cannot be safely distinguished from the GDC fields alone. Remaining kidney histologies are `UNMAPPED`. Linked PDC study labels remain traceable but cannot by themselves establish a patient's histology. No donor will be reassigned based on program scores or to rescue sample size.

The crosswalk in Notebook 113 is G4 exploratory source-harmonization eligibility, distinct from later analysis-specific comparability, case-mix and platform validity. The case table and a source-stratum crosswalk include explicit statuses and reasons; exact G2 and G3 inventories stay unchanged. G4 acceptance is conditional on support in the frozen TCGA lineage universe; G5, G6 and G8 remain independent pending gates. This amendment supersedes any earlier generic `UNMAPPED` G4 stop-state descriptions only for the implemented deterministic source mapping.


---

## Proportionate G5–G8 evidence boundary (2026-10-28)

The Notebook 111 full-payload provider MD5 and exact primary-sample ancestry checks constitute completed **source-integrity** evidence, not a read-level sequencing QC assessment. Missing read-level QC metrics are reported as limitations, not scored as failure or imputed pass. Explicit independently reviewed file-level QC failures, if available, remain exclusions.

G6 records source STAR-count workflow coverage and retains a separate pending decision for real count-column/gene-feature identity and fixed-program projection compatibility. These tests are performed on actual matrices before inference, never inferred from metadata alone.

G8 records availability of source covariates and outcome-blind source-context/workflow/lineage support. Missing tumor purity or batch data are not invented; confounding and identifiability are evaluated in the analysis design before confirmatory replication. No covariate adjustment, program scores, or lineage-aware inference are run in Notebook 113.

The remaining `BLOCKED` readiness state means **the full analytic cohort is not frozen**, not that all 1,082 RNA files have failed sequencing QC. G3/G4 candidate counts remain untouched; the readouts above permit proceeding to focused matrix-level compatibility and study design without a new general-purpose sequencing QC research phase.
