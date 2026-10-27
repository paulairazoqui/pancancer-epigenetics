# Notebook 800 — G3 documentary donor-independence audit

**Review date:** 2026-10-27  
**Status:** DOCUMENTARY REVIEW COMPLETED WITH EXPLICIT COVERAGE LIMITS; **G3 NOT PASSED**.  
**Frozen computational checkpoint:** Notebook 800 executed as commit `e2269b8`: 1,082 G2 structurally simple cases; no exact CPTAC–TCGA case UUID or case submitter collisions; 37 simple cases flagged for ancillary ambiguous RNA files. All 1,082 remain `UNRESOLVED_INDEPENDENCE` pending donor-level documentation. No external biological analysis authorized.

## Audit question and decision standard

Is there **positive, applicable evidence** that the 1,082 precise frozen CPTAC-3 RNA candidate donors are disjoint from the frozen TCGA discovery donor cohort (9,965 cases), rather than merely having distinct project names or UUIDs?

The approved G3 protocol requires validated donor crosswalk or explicit applicable non-overlap assurance for `DOCUMENTED_INDEPENDENT`; documented donor match for `DOCUMENTED_OVERLAP`. Prospective tissue collection or lack of exact lexical ID matches cannot suffice. This documentary review does not access controlled donor identifiers.

## Institution-level primary records examined

1. GDC `CPTAC-3`, accession `phs001287`, project page, consulted 2026-10-27: https://portal.gdc.cancer.gov/projects/CPTAC-3 . The **current** displayed GDC scope differs from the frozen 111 snapshot and must not redefine G2.
2. dbGaP `phs001287.v13.p5` and earlier records: https://www.ncbi.nlm.nih.gov/projects/gap/cgi-bin/study.cgi?study_id=phs001287.v13.p5 . Study describes new diagnoses, treatment-naive inclusion, tissue source sites, consent and prospectively acquired material; does **not** state a verified TCGA donor-exclusion crosswalk.
3. GDC consortium description: https://gdc.cancer.gov/about-gdc/contributed-genomic-data-cancer-research/clinical-proteomic-tumor-analysis-consortium-cptac . CPTAC-3 `phs001287` must not be conflated with CPTAC-2 `phs000892`.
4. NCI TCGA historical sample requirements: https://www.cancer.gov/ccg/research/genome-sequencing/tcga/studied-cancers . Similar primary untreated specimen criteria are **not** evidence of biological disjointness.

## Original-study context evidence

| CPTAC-3 context | Primary original document (methods) | Source provenance actually supported | TCGA donor non-overlap explicitly certified? |
|---|---|---|---|
| Lung adenocarcinoma | https://pmc.ncbi.nlm.nih.gov/articles/PMC7373300/ | 111 participants, 13 tissue source sites; prospective collection | Not found |
| Lung squamous carcinoma | https://pmc.ncbi.nlm.nih.gov/articles/PMC8475722/ | Prospective treatment-naive surgical specimens | Not found |
| Clear-cell kidney carcinoma | https://pmc.ncbi.nlm.nih.gov/articles/PMC7331093/ | Prospectively collected CPTAC specimens | Not found |
| Uterine/endometrial carcinoma | https://pmc.ncbi.nlm.nih.gov/articles/PMC10631452/ | Prospective collection May 2016–May 2019; five countries | Not found |
| Pancreatic ductal carcinoma | https://pmc.ncbi.nlm.nih.gov/articles/PMC8654574/ | Prospectively collected treatment-naive surgical cases | Not found |
| Head and neck squamous carcinoma | https://pmc.ncbi.nlm.nih.gov/articles/PMC7946781/ | 110 prospectively collected primary tumors | Not found |
| Glioblastoma original proteogenomic cohort | https://pmc.ncbi.nlm.nih.gov/articles/PMC8044053/ | 99 cases collected from ten tissue source sites per CPTAC-3 protocol | Not found |

**Important counterexample to blanket prospective characterization:** TCIA CPTAC-GBM collection https://www.cancerimagingarchive.net/collection/cptac-gbm/ states that a GBM *confirmatory* cohort was supplemented by retrospective CHOP–UPenn specimens. Retrospective origin does not establish TCGA overlap, but invalidates any unqualified assertion that every material in the later aggregated CPTAC-3 context must have been newly prospectively collected.

This is a context-level *documentation* matrix, not a verified join between each publication's subject list and the exact 1,082 G2 cases. In particular, source-label contexts in Notebook 111 may extend beyond the specific named histologies in original papers. Do not treat the papers' n as frozen G2 counts or assume complete row-level mapping. A full source-stratum applicability mapping must use the local 111 G2 identity inventory and G4 crosswalk rather than guessed TCGA lineages.

## Evidence evaluation

- **Supported:** institutionally distinct program, prospectively recruited discovery cohorts in several major CPTAC-3 cancer contexts; audited zero exact case identifier collisions against frozen TCGA mapping.
- **Not established:** explicit, study- and case-applicable TCGA non-overlap certification; validated cross-cohort donor-level matching; absence of overlap specifically within retrospectively supplemented/confirmatory cases; positive independence status for any given one of the 1,082 candidates.
- **No documented overlap demonstrated:** zero validated donor matches found in the checked public records; this is not equivalent to proven disjointness.
- **Evidence ceiling:** the sources are sufficient to describe CPTAC-3 as *prospectively sourced in documented discovery cohorts* and *operationally external at the study level*, with exceptions to universal prospective origin. They are insufficient to label the precise G2 set donor-independent under the frozen standard.

## Final documentary verdict as of 2026-10-27

**G3 = UNRESOLVED / HARD BLOCKER for confirmatory independent-donor replication** under current evidence. This is a completed bounded documentary review with a negative sufficiency outcome, not a claim that overlap exists.

No `DOCUMENTED_INDEPENDENT` or `DOCUMENTED_OVERLAP` per-case assignments are justified by the reviewed documents; retain the executed 1,082 `UNRESOLVED_INDEPENDENCE` G3 labels. No changes to G2 or frozen Phase 4 representations. Do not declare G3 PASS, release G4 as confirmatory eligibility, perform program scoring, or merge 800 as independently validated.

**Ways to resolve the hard gate without lowering the criterion:** obtain written study-wide and subcohort-specific non-overlap assurance from CPTAC/GDC/BCR applicable to frozen G2 donors, or an authorized validated donor-level crosswalk / matching audit with privacy-safe attestation. If these are unavailable, the contract permits `NOT_EVALUABLE_DONOR_INDEPENDENCE` for the confirmatory track; exploratory structural study-level assessment, if ever authorized, needs a separately prospective narrowed estimand and cannot be misreported as independent patient replication.

## Audit and reproducibility limitations

- Literature review does not prove a negative: absence of published crosswalk is not proof no crosswalk exists.
- The audited GitHub snapshot contains code and outputs, but the local 111 G2 case-by-document-source matrix was not available to this document review. No claim of full per-case publication coverage is made.
- Public institutional GDC counts change with releases and cannot replace immutable manifest/source fingerprints.
- Controlled germline or direct patient identity inference was neither attempted nor authorized.
- Phase 1 acquisition remains unopened pending a specifically justified, bounded source request.

**Recommended decision log entry:** documentary search complete; G3 not met; decision pending on seeking an authoritative non-overlap attestation versus explicitly closing confirmatory independent-donor replication as non-evaluable. G4 lineage mapping can be documented separately only if it does not imply G3 PASS or authorize biological results.


## Published TCGA–CPTAC external-validation precedents (reviewed 2026-10-27)

The following articles establish **precedent for cross-resource evaluation**, not per-donor evidence for the frozen G2 subset.

| Publication | TCGA role | CPTAC role | Explicit donor independence basis and limitation |
|---|---|---|---|
| *Deep contrastive learning for predicting cancer prognosis using gene expression values*, Brief Bioinform (2024), https://academic.oup.com/bib/article/25/6/bbae544/7848896 | LUAD/LUSC model development | CPTAC-3 lung independent-cohort evaluation | Labels cohort independent; inspected material does not substantiate donor-level matching/certification |
| *Multiomics-Based Feature Extraction and Selection for the Prediction of Lung Cancer Survival*, IJMS (2024), https://pmc.ncbi.nlm.nih.gov/articles/PMC11011391/ | 267 LUAD discovery cases | 96 CPTAC-3 LUAD hold-out cases | Uses distinct cohorts and separately transfers feature selection; no matched donor crosswalk identified in retrieved text |
| *Cross-cancer homologous recombination deficiency prediction from whole slide images using transfer learning*, Sci Rep (2026), https://www.nature.com/articles/s41598-026-52094-6 | 4,147 cases across eight cancers | 214 CPTAC LUAD/LUSC external evaluation | Describes CPTAC cohorts as independent; does not supply G2-specific identity proof |
| *A pan-cancer multi-omic SuperLearner for regulated cell death survival topologies*, Front Artif Intell (2026), https://pmc.ncbi.nlm.nih.gov/articles/PMC13538856/ | TCGA model development | 1,039 CPTAC cases across ten cancers | Explicitly states no patient overlap; inspected text does not establish the method used to verify this or exact correspondence to frozen G2 cases |
| *Pan-cancer molecular subtypes revealed by mass-spectrometry-based proteomic characterization of more than 500 human cancers*, Nat Commun (2019), https://www.nature.com/articles/s41467-019-13528-0 | Independent TCGA reference and TCGA-derived CPTAC component | 532 non-TCGA CPTAC Confirmatory/Discovery cases contrasted with CPTAC–TCGA samples | Most directly states a distinction between TCGA-excluded CPTAC and TCGA-overlapping CPTAC, **but its specific 532-case cohort cannot automatically be identified with the present GDC CPTAC-3 G2 1,082-case universe** |

### Review consequence

Cross-publication precedent supports the use of distinct CPTAC collections as external resources, **not G3 donor-level adjudication automatically**. The 2019 Nat Commun study is particularly informative because it separates explicitly non-TCGA CPTAC cases from TCGA-origin CPTAC profiles. The study cohort labels, acquisition versions, source IDs and case inclusion criteria must be reconciled to the frozen 111 G2 cases *before* transferring its independence assurance. Similarly, the categorical 2026 no-overlap statement is supporting secondary literature but its underlying identity-verification method requires review.

**G3 status remains UNRESOLVED/BLOCKED.** The search strengthens operational study-level plausibility and establishes standard practice; it does not warrant relabelling the 1,082 `UNRESOLVED_INDEPENDENCE` records. Proposed bounded next question: can primary study documentation and exact subcohort labels from the frozen 111 snapshots demonstrate that particular G2 case strata belong to CPTAC collections documented as excluding TCGA participants? If not, require source-program attestation or maintain non-evaluability for confirmatory independent-donor replication.
