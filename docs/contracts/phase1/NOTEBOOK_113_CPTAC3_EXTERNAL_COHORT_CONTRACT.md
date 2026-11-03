# Notebook 113 — CPTAC-3 External Cohort Construction and Eligibility

**Phase:** 1 — Data acquisition and source auditing  
**Notebook:** `notebooks/phase1_data_acquisition_and_auditing/113_cptac3_external_cohort_construction.ipynb`  
**Scientific status:** Source-cohort construction executed; a 721-case source cohort is proposed and auditable, but not frozen as an inferential cohort. Independent read-level sequencing QC and downstream analysis authorization are not established.

## 1. Scientific objective and scope

Construct an auditable, outcome-blind CPTAC-3 primary-tumor RNA-seq source cohort for external, lineage-aware assessment of previously fixed transcriptomic programs. The construction must preserve source provenance; distinguish patients, samples, aliquots and files; identify a uniquely represented primary-tumor expression file per candidate case; assess source-cohort externality and lineage comparability; and verify raw-count compatibility with the frozen program feature universe.

This notebook establishes **source membership and technical feasibility**, not reproducibility of biological programs. It does not compute program scores, infer drug resistance, assess perturbational reversal, select patients on the basis of expression-program outcomes, or claim causal or clinical validity. A technically compatible source cohort is not, by itself, an approved inferential validation cohort.

## 2. Data sources, reference objects and provenance

The principal source is the GDC `CPTAC-3` project, using its audited STAR Counts RNA-seq files and associated case, sample and aliquot metadata. The source inventory established by Notebook 111 contains 2,968 RNA-seq STAR Counts files and 2,610 SeSAMe DNA-methylation files. **This cohort-construction analysis uses RNA-seq**; availability of methylation data does not establish a matched methylation cohort.

Use the existing, fingerprinted acquisition and identity outputs from Notebook 111, including `data/interim/metadata/111_cptac3_file_index.csv` and `111_cptac3_acquisition_audit_summary.json`. The frozen TCGA primary-tumor reference is `phase2.203.final_sample_mapping`, with 9,965 discovery cases. The downstream feature-compatibility target comprises the three immutable Phase 4 programs and their 2,389 ordered shared genes. No program genes, signs or weights may be relearned in this notebook.

Where source provenance requires corroboration, retain separately identified, dated evidence from GDC, PDC, original CPTAC studies or other applicable primary sources. Evidence records must identify the original namespace, source URL or identifier, applicable case/cohort scope, retrieval date, and exact provenance snapshot. A PDC match can corroborate study membership but must not be invented or required for every valid GDC case.

The 12-file upstream QC-metadata investigation in Notebook 112 verifies limited source-field linkage and agreement, not population-wide read-quality acceptability. All source files, evidence snapshots, execution inputs and produced tables must be traceable through recorded hashes; do not silently replace an input with live provider metadata.

## 3. Primary-tumor source candidate definition

Start from the audited primary-tumor source inventory with 1,370 cases and 1,731 uniquely resolved primary RNA files. Retain the **1,082 cases with exactly one eligible primary-tumor STAR Count file, one uniquely resolved sample and one aliquot** as the primary candidate universe. Preserve exact GDC case, sample, aliquot and file identifiers, including file UUID, filename, size, provider MD5 and direct source associations. Sample and aliquot identities are not interchangeable with donor identities.

The other **288 cases / 649 primary files** are not primary candidates: 276 cases / 619 files have multiple primary samples, and 12 cases / 30 files have multiple primary aliquots. Do not choose a preferred file or reintroduce these cases to improve statistical power. Their potential secondary use would require an independent, outcome-blind and prospectively specified selection rule.

Preserve the **314 source RNA files with ambiguous sample ancestry** in file-level accounting; they are not a disjoint set of patients and may belong to cases already represented elsewhere. Among the 1,082 simple primary candidates, 530 cases have additional RNA files (544 in total: 488 resolved normal, 18 resolved recurrent and 38 ambiguous). The **37 simple cases with additional ambiguous RNA ancestry** remain in the candidate universe and carry an explicit sensitivity flag; the flag is not an automatic exclusion.

At every selection step, report separate denominators for files, aliquots, samples and cases; account for each file once; and retain the original `project × primary_site × disease_type` context and all non-inclusion reasons.

## 4. External cohort provenance and donor-overlap uncertainty

Classify cohort externality using documented GDC `CPTAC-3` source provenance, the prospective CPTAC-3 acquisition context, source/study linkage where available, and outcome-blind exact identifier screening against the frozen TCGA reference. Identifier comparison is valid only when namespace and entity semantics are compatible. A zero-collision screen alone is **not** genetic proof that no patient appears in both resources.

Use distinct, explicit provenance statuses:

- `COHORT_SUPPORTED_EXTERNAL`: source membership is supported by the audited GDC `CPTAC-3` project, no relevant exact TCGA identifier collision is flagged and no contradictory source evidence is present. This is a **cohort-level externality assumption**, not demonstrated donor-level independence.
- `SOURCE_REVIEW_REQUIRED`: source membership, subproject linkage, PDC corroboration, identifier collision or other documentary evidence is contradictory or uncertain. Withhold these cases from the proposed primary cohort pending targeted source review.
- `DOCUMENTED_OVERLAP`: verified common-donor provenance or a namespace-valid link to an already used TCGA donor. Exclude these cases.

Do not infer independent patients from different UUID namespaces, recruitment labels, clinical similarity/difference, or the absence of apparent collisions. Conversely, do not require genetic identity testing for every case to use a clearly qualified cohort-level externality assumption. Record residual uncertainty and re-examine specific cases if affirmative contrary evidence becomes available.

## 5. Cancer lineage harmonization

Map the original GDC source-site and broad-disease descriptions to a TCGA lineage **only where source metadata support an unambiguous correspondence**. Keep original and harmonized labels side by side. The supported mappings cover LUAD, LUSC, PAAD, SKCM, STAD, UCEC and HNSC; HNSC may originate from several documented anatomic source sites.

A broad `Brain/Gliomas` label does not distinguish TCGA-GBM from TCGA-LGG, and `Kidney/Adenomas and Adenocarcinomas` does not resolve KIRC, KIRP or KICH. Such cases remain ambiguous rather than being assigned by organ name or expression profile. Other unsupported source groups remain unmapped. PDC study labels alone must not replace case-level histology.

Retain `ACCEPTED`, `AMBIGUOUS`, `UNMAPPED` or `CONTRADICTORY` mappings as appropriate. Report attrition by original source context as well as accepted TCGA lineage. Neither donor eligibility nor lineage labels may be revised after inspecting external program results.

## 6. Sequencing quality, source integrity and missing evidence

Verify source-file identity, payload integrity, sample ancestry and deterministic counts availability separately from sequencing-quality evidence. Provider MD5 agreement, unambiguous primary-sample ancestry and complete gene presence establish important **integrity and compatibility** properties; they do **not** establish independent library/read-level sequencing QC.

Comparable provider mapping, duplication, read-quality and related measures would require verified provenance, metric definitions, denominator, assay/workflow version, applicability and missingness before use as acceptance criteria. The limited Notebook 112 pilot cannot establish such criteria for the complete source cohort. Do not derive mapping fractions from STAR `N_*` rows, invent numerical QC thresholds, interpret missing metrics as either QC PASS or QC FAIL, or retrospectively exclude low-count files to improve program replication.

Record the resulting limitation as **read-level QC not independently assessed** (`QC_UNASSESSED` where a row-level label is needed). Any documented source-specific technical failure must remain traceable for explicit review; no unverified QC status may silently change cohort membership.

## 7. Transcriptomic input and feature compatibility

For each proposed source file, verify that the designated GDC STAR Counts data provide the **`unstranded` raw-count** representation, uniquely version-normalized Ensembl gene identifiers, nonnegative integer count values, and complete presence of the 2,389 fixed program genes. Preserve file-level compatibility status and exact failures; do not impute absent genes as zero or substitute symbols for source IDs.

The executed input audit reports `COMPATIBLE_RAW_COUNTS` for all 721 cases meeting the source-provenance and lineage criteria. This confirms availability of usable source count representations, **not cross-platform numerical calibration** with TCGA. Normalization, between-cohort comparability, fixed-program projection, confounder adjustment and structural-replication inference are distinct downstream analytical decisions. They must not be optimized during source-cohort construction.

## 8. Cohort eligibility and exclusion rules

A case enters the **proposed source cohort** only when all of the following are simultaneously documented: (i) exactly one uniquely mapped primary-tumor RNA-seq file/sample/aliquot in the fixed 1,082-case universe; (ii) `COHORT_SUPPORTED_EXTERNAL`; (iii) an `ACCEPTED` TCGA lineage mapping; and (iv) `COMPATIBLE_RAW_COUNTS`.

Use stable identifiers, explicit reason codes, deterministic ordering, unique-case and unique-file checks, and full source-to-proposed attrition reconciliation. Preserve rejected, unresolved and not-evaluable cases in the complete audit rather than deleting their records. No expression-program scores, replication statistics or pharmacogenomic outcomes may determine source eligibility.

**Proposed source eligibility is not inferential authorization.** A final analysis cohort can be frozen only after its fingerprinted source membership and the prospective statistical, normalization, confounding and lineage-support requirements of the intended external analysis have been reviewed. If an essential requirement cannot be established, report the non-evaluable state; do not silently rescue cases.

## 9. Executed source-cohort characteristics and attrition

The audited source construction yields **721 unique cases / 721 primary RNA files** meeting the proposed source criteria:

| Harmonized TCGA lineage | Cases |
| --- | ---: |
| TCGA-LUAD | 178 |
| TCGA-LUSC | 89 |
| TCGA-STAD | 142 |
| TCGA-SKCM | 138 |
| TCGA-PAAD | 82 |
| TCGA-UCEC | 56 |
| TCGA-HNSC | 36 |
| **Total** | **721** |

Of the original 1,082 simple primary candidates, **361 are not proposed**: 351 have unresolved brain/kidney subtype assignment (159 brain glioma; 192 kidney adenoma/adenocarcinoma), four belong to other unsupported kidney mappings and six PAAD candidates require source-provenance review. These counts describe source eligibility and must not be misrepresented as sequencing-QC failures or inferential test exclusions.

The 288 multiply represented primary cases remain outside the starting candidate denominator, and ambiguous-ancestry files remain in a separate, non-disjoint file-level ledger. The 37-case ambiguity sensitivity flag is preserved without changing primary membership.

## 10. Reproducibility and analytical inputs

The notebook persists **only results with a defined downstream consumer**. Its four derived outputs under `data/interim/metadata/` are:

| Artifact | Downstream use |
| --- | --- |
| `113_proposed_external_source_cohort.csv` | Exact proposed 721-case membership, unique primary RNA file/sample/aliquot identities, source labels, accepted TCGA lineage, provenance and eligibility flags used by Notebook 800 |
| `113_primary_candidate_case_eligibility.csv` | Full 1,082-case, outcome-blind candidate ledger, including source identifiers, reviewed PDC/source evidence where relevant, provenance and lineage adjudications, QC limitations, selection status and non-inclusion reasons needed for Notebook 800 checks |
| `113_raw_count_compatibility.csv` | Persisted case/file-level STAR count-schema and frozen-gene coverage assessment consumed by Notebook 800 without repeating the source matrix audit |
| `113_source_provenance_manifest.json` | Input and source-evidence identities, verified SHA-256 values of the three CSVs, cohort-level readiness/limitations and the exact provenance needed by Notebook 800 to accept its inputs |

The manifest must record the exact hashes, row counts, versions and source identities required to authenticate these artifacts. It must also convey `cohort_frozen=false`, `external_analysis_authorized=false`, the unresolved read-level QC limitation and the qualified cohort-level externality assumption. No second readiness JSON is needed. The manifest is written **after** the three CSVs have been finalized and fingerprinted; avoid self-referential checksums.

The candidate ledger is the authoritative persisted record of source provenance, lineage decisions, ambiguous or excluded cases and their reasons. Its column names and status codes must be scientifically self-explanatory, not internal preflight labels. The raw-count compatibility file records the completed matrix-level assessment with case and file keys, rather than requiring downstream notebooks to repeat that assessment. Only the proposed cohort file defines the exact downstream source membership; the ledger documents the selection and excluded alternatives.

The following remain **in-notebook results**, not separate exported artifacts: lineage counts, attrition tables, source-context/workflow summaries, field-availability reports, PDC study catalogs and linkage diagnostics, source lineage crosswalk summaries, and other intermediate adjudication views. Preserve their underlying source evidence and any decision-bearing case-level conclusions needed downstream in the retained input snapshots, candidate ledger and manifest. Do not export duplicate CSV representations solely because the analysis computed or displayed them.

Immutable provider metadata, PDC/source snapshots, the frozen TCGA reference and other fingerprinted **inputs** are distinct from these four derived outputs. Required source snapshots must remain available with traceable hashes; the four-output rule does not authorize deletion of source inputs.

A downstream notebook must verify the three produced CSVs against the manifest, their case/file uniqueness and the expected source-lineage denominator before using them. It must not redo source eligibility, donor/cohort adjudication, histology harmonization or raw-count matrix compatibility. A hash mismatch or inconsistent membership is a stop condition requiring correction at the producing notebook.

No artifact is created for speculative future use. If a specific additional analytical result is later required downstream, add its export to Notebook 113, execute and verify that producer, update its manifest, then consume the persisted result. Do not repeat the underlying source analysis in the consumer. Generated local outputs are not automatically frozen or registered solely because the notebook executed.

## 11. Limitations and interpretation

The proposed CPTAC-3 cohort has credible **cohort-level external provenance**, but no comprehensive genotype-based donor crosswalk proves absence of every possible TCGA patient overlap. Broad source histology leaves some tumor types non-comparable; source mapping does not validate histopathological subtype equivalence. Read-level sequencing QC lacks cohort-wide independently justified acceptance criteria. Tumor purity, collection center, sequencing batch and library-preparation covariates are not established in the audited candidate inventory; unknown values must not be treated as absent biological or technical effects.

Compatibility of raw counts and frozen genes does not guarantee comparability of normalized expression or program scores across TCGA and CPTAC-3. The 721 cases therefore constitute an **auditable proposed external source cohort**, not a validated independent-donor cohort, a QC-certified sample set, or a frozen inferential cohort.

The notebook's permissible conclusion is that source-level case selection, provenance, lineage assignment and raw-count input compatibility have been documented with explicit unresolved uncertainties. Any eventual structural replication of candidate programs requires a separately specified, lineage-aware analysis with negative controls, multiplicity management, sensitivity assessment and conservative interpretation.
