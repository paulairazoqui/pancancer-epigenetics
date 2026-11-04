# Notebook 113 → 800 — CPTAC-3 external RNA-seq source cohort handoff

**Source producer:** `notebooks/phase1_data_acquisition_and_auditing/113_cptac3_external_cohort_construction.ipynb`  
**Downstream consumer:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`  
**Status:** Executed, outcome-blind source construction; proposed membership is **not** an approved frozen inferential cohort.

## Source membership and eligibility

Notebook 113 establishes a proposed **727-case / 727-file** GDC `CPTAC-3` primary-tumor RNA-seq source cohort. The source candidate universe contains 1,082 cases with uniquely represented primary STAR Counts RNA-seq file/sample/aliquot identities. Its 355 not-proposed cases are attributable to lineage mapping: 351 ambiguous brain/kidney subtypes and four unsupported kidney source contexts. The 288 multiply represented primary cases are outside the 1,082-case source candidate universe.

| Accepted TCGA lineage | Proposed cases |
| --- | ---: |
| TCGA-HNSC | 36 |
| TCGA-LUAD | 178 |
| TCGA-LUSC | 89 |
| TCGA-PAAD | 88 |
| TCGA-SKCM | 138 |
| TCGA-STAD | 142 |
| TCGA-UCEC | 56 |
| **Total** | **727** |

The source eligibility criteria are: unique primary file/sample/aliquot in the fixed candidate universe; `cohort_provenance_status=COHORT_LEVEL_EXTERNALITY_ASSUMED`; `lineage_mapping_status=ACCEPTED`; validated `unstranded` nonnegative integer raw-count vector; and complete representation of the frozen **2,389** shared Phase 4 Ensembl genes.

Cohort-level externality remains a **qualified study-design assumption**. The status `donor_independence_status=NOT_INDIVIDUALLY_VERIFIED` must be preserved. GDC project provenance and absence of demonstrated overlap do **not** establish genetic donor independence. The ambiguity flag for cases with additional RNA files is preserved for prospective sensitivity analyses; it does not automatically exclude their unique primary-tumor file.

## Four authoritative locally generated source outputs

All four outputs are located under `data/interim/metadata/`:

| Output | Consumer responsibility |
| --- | --- |
| `113_proposed_external_source_cohort.csv` | Exact proposed membership and source file/sample/aliquot/lineage identities |
| `113_primary_candidate_case_eligibility.csv` | Complete 1,082-case candidate ledger, inclusion/non-inclusion reasons, original source context, QC and provenance limitations |
| `113_raw_count_compatibility.csv` | Case/file keyed completed raw-count and 2,389-gene coverage assessment; do not redo source eligibility audit |
| `113_source_provenance_manifest.json` | Input fingerprints, SHA-256 and row/column counts of the three CSVs, per-lineage denominators, source statuses and analysis readiness |

The manifest is generated after the CSVs and has no self-referential checksum. The source files are local generated outputs and are not automatically registered or frozen in Git.

## Mandatory Notebook 800 acceptance

1. Load the four outputs exactly as produced. Verify the SHA-256 of all **three CSVs** against `derived_outputs` in the manifest. Reconcile case/file uniqueness, memberships between eligible ledger rows/cohort/compatibility, source statuses, 727 proposed cases and the seven lineage counts.
2. Verify the frozen TCGA source reference and three immutable Phase 4 programs against their authoritative registry fingerprints. Do not refit program loadings or redefine the 2,389-gene reference based on external outcomes.
3. For the source RNA-seq payloads actually consumed, verify local file availability, `size_bytes` and provider MD5 against the audited identities. This is downstream **file-integrity verification**, not new acquisition or a repeat of 113's matrix-level feature-presence audit.
4. Do not requery GDC for case selection; reconstruct candidate membership; reassess source histology or donor provenance; or select, remove, relabel or replace cases in response to program scores. Producer-output disagreement is a **STOP** requiring correction of the producing source and its fingerprints.
5. Preserve `cohort_frozen=false`, `external_analysis_authorized=false`, `read_level_qc_status=QC_UNASSESSED` and `cross_platform_comparability=NOT_ESTABLISHED` as current readiness limitations. Do not promote source compatibility to read/library-level sequencing QC PASS.
6. Specify and review, before confirmatory testing, normalization and frozen-program projection; a **non-tautological within-lineage structural replication estimand**; negative controls and their matching diagnostics; effect sizes and uncertainty; the primary program-by-lineage multiplicity family; support/evaluability rules; and identifiable sensitivity analyses for purity/composition, proliferation, technical factors and recorded ancestry ambiguity.

If reliable measurement comparability, donor provenance or identifiable adjustment assumptions cannot be established for an intended claim, report the limitation or the relevant `NOT_EVALUABLE` state; do not rescue the analysis by outcome-dependent selection or naïve cross-lineage pooling.

## Governing documents

- `docs/contracts/phase1/NOTEBOOK_113_CPTAC3_EXTERNAL_COHORT_CONTRACT.md`
- `docs/contracts/phase8/NOTEBOOK_800_CPTAC3_EXTERNAL_TRANSCRIPTOMIC_REPLICATION_CONTRACT.md`

Notebook 113 defines and fingerprints the **proposed source cohort**. Notebook 800 owns the prospective analytic readiness decision, lineage-aware structural-replication analysis and its scientifically qualified interpretation. Neither successful 113 execution nor an available program score constitutes inferential authorization.
