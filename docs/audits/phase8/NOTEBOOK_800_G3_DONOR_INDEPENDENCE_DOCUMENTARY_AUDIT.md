# Notebook 800 — G3 documentary donor-independence audit

**Status:** EVIDENCE REVIEW IN PROGRESS — NOT A G3 PASS  
**Review date:** 2026-10-27  
**Scope:** fixed G2 simple-case candidate universe (1,082 CPTAC-3 primary RNA cases) against the frozen TCGA reference (9,965 cases).  
**Implementation:** Notebook 800 G3 execution committed as `e2269b8`; 0 exact case UUID/submitter collisions; all 1,082 conservatively `UNRESOLVED_INDEPENDENCE`. This is a source-label collision screen, not donor certification.  
**Source-of-truth contract:** `docs/contracts/phase8/NOTEBOOK_800_ELIGIBILITY_AND_REPLICATION_CONTRACT_DRAFT.md` section 4.2; separate G3 prospective protocol.

## Public primary-source evidence inventory (initial pass)

| Source | Locator | Observation directly supported | What it does NOT prove |
|---|---|---|---|
| GDC CPTAC-3 project | https://portal.gdc.cancer.gov/projects/CPTAC-3 | Project CPTAC-3 is associated with dbGaP `phs001287`; current GDC aggregate includes multiple disease contexts | That every frozen 111 file corresponds to a donor not present in TCGA; current portal counts are not the frozen 111 candidate denominators |
| dbGaP CPTAC-3 | https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001287.v23.p7 | Inclusion includes newly diagnosed untreated primary cases, consent, and source eligibility; prospective case-set framing | Explicit TCGA donor exclusion or a case-level TCGA↔CPTAC crosswalk |
| NCI CPTAC consortium / tissue source sites | https://dctd.cancer.gov/research/networks/cptac/consortium | CPTAC tissue source sites prospectively collect clinically annotated specimens under quality protocols | That every CPTAC-3 donor is absent from TCGA |
| NCI TCGA sample material policy | https://www.cancer.gov/ccg/research/genome-sequencing/tcga/using-tcga-data | NCI states TCGA cannot provide analytes/tissues outside that program and that consent limits redistribution | Absence of an independently recruited person being included in both programs, or absence of data reuse; cannot equate material-transfer restriction with donor-level non-overlap |

Sources consulted 2026-10-27; exact referenced study versions should be preserved when extending the audit.

## Adjudication discipline

`DOCUMENTED_INDEPENDENT` requires an explicitly applicable exclusion/non-overlap assurance or validated donor-level crosswalk. `DOCUMENTED_OVERLAP` requires positive validated donor linkage. Differing GDC IDs, study codes, chronological recruitment and tissue source design are not sufficient. `UNRESOLVED_INDEPENDENCE` is the default if neither standard is met.

This document must next be extended to a *source-stratum-specific applicability matrix* using the frozen 111 G2 strata, with a reference for each relevant CPTAC-3 disease study and a recorded direct statement (or explicit absence of one) addressing overlap. Do not label a lineage solely from name similarity before G4. The version-controlled G3 protocol prohibits unbounded GDC acquisition in Notebook 800.

## Current preliminary evaluation

**G3 BLOCKED.** The documents above support prospectively acquired CPTAC specimens and describe the TCGA sample-distribution policy, but currently do not establish donor-level disjointness for the 1,082 exact G2 cases. No patient class changes and no confirmatory external replication authorized.

**Not a final documentary audit:** disease/context coverage and study-specific TCGA overlap statements still require verification. If no adequate source exists after a bounded review, close as `NOT_EVALUABLE_DONOR_INDEPENDENCE` for confirmatory claims, rather than assuming independence or escalating automatically into a new acquisition notebook.

## Handoff after documentary review

Document verified references and per-stratum applicability; peer-review documentary interpretation; update the G3 protocol/contract gate status as a separate versioned decision. Only if authoritative new identity data are found should Phase 1 acquire them in a bounded source-fingerprinted handoff and G3 cases be readjudicated. Preserve the executed G3 csv/json SHA-256 fingerprints; never overwrite the frozen TCGA mapping or historical A–H snapshots.
