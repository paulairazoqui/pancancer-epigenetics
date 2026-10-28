# Notebook 113 → 800 — CPTAC-3 proposed external source cohort handoff

**Date:** 2026-10-28
**Status:** Notebook 113 source-construction work complete; proposed cohort **not frozen**; Notebook 800 inference **not authorized**.
**Source branch:** `notebook-113-cptac3-external-cohort`
**Executed source notebook commit:** `c496e28` (G3–G6 construction and handoff outputs, as inspected on branch).
**Owner:** Notebook 113 (source cohort and case-level provenance); Notebook 800 (independent structural replication design).

## Reviewed, outcome-blind cohort definition

Read the already executed `data/interim/metadata/113_proposed_external_source_cohort.csv`; require its SHA-256 to equal the value recorded in `113_source_provenance_manifest.json` and `113_cohort_readiness.json`. The authoritative digest is **the 64-character value in those generated files**, not a transcription from truncated notebook display.

Per-case inclusion is the intersection of:
- G2: one uniquely linked primary-tumor RNA-seq STAR Counts file/sample/aliquot, frozen 1,082-case source universe.
- G3: `COHORT_SUPPORTED_EXTERNAL`, a proportionate *cohort-level* external provenance assumption (not proof of individual genetic independence).
- G4: `ACCEPTED` source-site/histology → frozen TCGA lineage mapping.
- G6: `COMPATIBLE_RAW_COUNTS`, exact `unstranded` raw count input, unique version-normalized Ensembl IDs, nonnegative integer counts and complete 2,389-gene frozen Phase 4 universe.

**Proposed source cohort: 721 unique cases and 721 files, across seven TCGA lineages.** Executed results:

| TCGA lineage | Cases |
| --- | ---: |
| TCGA-LUAD | 178 |
| TCGA-LUSC | 89 |
| TCGA-STAD | 142 |
| TCGA-SKCM | 138 |
| TCGA-PAAD | 82 |
| TCGA-UCEC | 56 |
| TCGA-HNSC | 36 |
| **Total** | **721** |

The complete 1,082-case G2 inventory is retained. **361 not proposed**: 351 unresolved source subtype (159 brain glioma, 192 kidney adenoma/adenocarcinoma); four other kidney contexts without supported TCGA lineage mapping; and six provenance exceptions in PAAD. These are not automatically recoded or rescued after observing results.

## Mandatory import/checks in Notebook 800

1. Load `113_source_provenance_manifest.json`, `113_cohort_readiness.json`, and the proposed cohort CSV. Independently verify both SHA-256 records, source input fingerprints, the 721-case count, unique case/file IDs, permitted inclusion labels, and the exact seven-lineage denominator **before** reading program scores.
2. Treat case/sample/file identity and source-to-TCGA lineage as immutable. An 800-side mismatch is a STOP, not a reason to reselect G2 cases or amend 113 outputs.
3. Preserve all seven lineages individually and do not pool them naively. Define lineage-aware structural replication estimands, sample-support rules and uncertainty handling prospectively; report any lineage too small as non-evaluable.
4. Predefine count normalization, frozen weight/feature projection, handling of TCGA/CPTAC platform shifts, proliferation and purity limitations, negative controls, multiplicity, and sensitivity analysis, **without using CPTAC replication outcomes to choose preprocessing or eligibility rules**.
5. G5 read-level QC is **not formally assessed**; MD5 integrity and unambiguous sample ancestry are verified, but do not imply QC PASS. G8 purity, sequencing batch, collection center and library preparation are not present in the audited candidate inventory; do not interpret absence of fields as confirmed lack of biological/batch variation. Assess confounder identifiability and any external metadata provenance before claims.
6. Source cohort handoff is **not an analytic cohort freeze**. Do not set `external_analysis_authorized=true` or register the proposed cohort as a frozen artifact until the 800 design and upstream source requirements are separately approved.

## Source evidence / paths

- Notebook: `notebooks/phase1_data_acquisition_and_auditing/113_cptac3_external_cohort_construction.ipynb`
- Contract: `docs/contracts/phase1/NOTEBOOK_113_EXTERNAL_COHORT_CONSTRUCTION_CONTRACT_DRAFT.md`
- Proposed source cohort: `data/interim/metadata/113_proposed_external_source_cohort.csv`
- Per-lineage summary: `data/interim/metadata/113_proposed_source_cohort_lineage_counts.csv`
- Attrition: `data/interim/metadata/113_source_handoff_attrition.csv`
- Complete case ledger: `data/interim/metadata/113_primary_candidate_case_eligibility.csv`
- Local source manifest: `data/interim/metadata/113_source_provenance_manifest.json`
- Readiness: `data/interim/metadata/113_cohort_readiness.json`

The `data/interim` files are generated locally and may not be version-controlled. Their reproducibility and fingerprints—not merely the committed executed notebook outputs—must be verified wherever Notebook 800 runs. No new cohort construction should be attempted inside Notebook 800.
