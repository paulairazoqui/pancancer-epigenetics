# Notebook 112 — CPTAC-3 RNA-seq Source Technical Characterization and Provenance

**Phase:** 1 — Acquisition and source auditing  
**Notebook:** `notebooks/phase1_data_acquisition_and_auditing/112_cptac3_qc_source_provenance.ipynb`  
**Status:** Source-technical characterization executed; independent sequencing QC and downstream analytic eligibility not established.

This contract describes the implemented technical source audit and the interface consumed by Notebook 113. It is not a protocol for sequencing-quality qualification, cohort eligibility, or biological replication. The execution dependency order is **111 → 112 → 113 → 800**.

## 1. Scientific objective and scope

Characterize the available STAR Counts representation of provisionally primary-tumor CPTAC-3 RNA-seq source files, using identities and acquisition evidence produced by Notebook 111.

The analysis:

- Identifies cases represented by exactly one provisional primary-tumor RNA-seq file, sample, and aliquot, without selecting among multiply represented specimens.
- Inspects locally acquired STAR `unstranded` gene counts for structural and numeric consistency.
- Characterizes additional RNA-seq files associated with those cases while preserving unresolved sample ancestry.
- Produces an authenticated technical inventory and provenance handoff for Notebook 113.

The inventory restriction is based on source representation, **not** empirical sequencing-quality thresholds. This notebook neither approves individual specimens for downstream inference nor establishes independent sequencing or library QC.

## 2. Allowed inputs, integrity and dependencies

Notebook 112 consumes only the following Notebook 111 products under `data/interim/metadata/`:

| Input | Purpose |
| --- | --- |
| `111_cptac3_acquisition_audit_summary.json` | Upstream acquisition-integrity declaration and recorded artifact digests |
| `111_cptac3_file_index.csv` | Audited file and specimen associations across the RNA-seq source universe |
| `111_cptac3_provisional_primary_tumor_files.csv` | Provisionally primary-tumor file, case, sample and aliquot identities |

The corresponding local STAR files are read from `data/raw/cptac3/rnaseq_star_counts/<file_id>/<filename>`. Notebook 112 requires each file to exist and its local byte size to equal the recorded `size_bytes` before reading its count table.

Before source characterization, Notebook 112:

1. Requires `full_payload_md5_verified` to be `true` in the Notebook 111 acquisition summary.
2. Recomputes SHA-256 for both upstream CSV inputs and compares them with `audit_artifacts.file_index.sha256` and `audit_artifacts.candidate_primary.sha256` in that summary.
3. Checks primary RNA-seq identifiers, ancestry status and sample type, and reconciles their identities against the audited file index.

The MD5 declaration is evidence inherited from Notebook 111; Notebook 112 does **not** independently recompute provider MD5 checksums for every local STAR file. The acquisition summary itself is included in the downstream input-provenance record with its SHA-256, but is not independently authenticated against a separate expected digest by Notebook 112.

No GDC API queries, downstream notebook artifacts, or supplementary provider metadata files are required for this execution.

## 3. Primary-tumor RNA-seq source and STAR Counts characterization

The executed upstream source scope contains **2,968 audited RNA-seq files**, including **1,731 provisionally primary-tumor files across 1,370 cases**. Structural classification identifies **1,082 cases** with exactly one primary file, sample and aliquot. The remaining **288 cases** have primary-source multiplicity and are not included in the main technical inventory. They are retained for separate downstream adjudication; no alternative primary specimen is chosen here.

For each of the 1,082 locally available STAR Counts files, Notebook 112 reads `gene_id` and `unstranded` and records:

- Source identifiers: `case_uuid`, `file_id`, `sample_uuid` and `aliquot_uuid`.
- Source descriptors: `primary_site` and `disease_type`.
- Gene-row count and version-normalized gene identifier duplication.
- Whether `unstranded` gene counts form a nonnegative integer vector, the number of invalid values, the assigned-gene count total and the number of genes with positive counts.
- The number and `unstranded` counts of the four STAR special categories: `N_unmapped`, `N_multimapping`, `N_noFeature` and `N_ambiguous`.
- Counts of additional same-case RNA-seq files and files with unresolved sample ancestry.

Malformed source representations stop execution; the notebook does not assign sequencing-quality PASS/FAIL status or exclude samples using empirical QC cutoffs.

In the completed execution, all 1,082 files contained **60,660 gene rows**, with valid assessed `unstranded` counts, no duplicated version-normalized gene identifiers and valid representation of the four special categories. These are observations of the available count representation, not independent measures of read-level or library quality. In particular, assigned-gene counts must not be called total sequencing depth.

## 4. Additional RNA-seq files and specimen context

For the 1,082 uniquely represented primary cases, Notebook 112 identifies additional RNA-seq files from the audited Notebook 111 index, excluding each case's designated primary file. It reconciles case-level counts with those already recorded for the primary-source inventory, including zero-count cases.

The completed execution observed **544 additional RNA-seq files across 530 cases**. Source annotations classify these files as:

| Source context | Additional files | Distinct cases |
| --- | ---: | ---: |
| Resolved normal tissue | 488 | 486 |
| Resolved recurrent tumor | 18 | 16 |
| Ambiguous sample ancestry; no sample attribution | 38 | 37 |

Distinct-case counts in this table are **not additive** because a case may have more than one additional specimen context. A further 552 of the 1,082 primary cases have no additional RNA-seq file in the audited source index.

The analysis checks whether each additional file shares an **exact resolved sample or aliquot UUID** with the designated primary source, and verifies that unresolved ancestry is never assigned an exact relationship. No additional file was found to share the exact primary sample or aliquot identifier in the completed execution.

An association at the case level does not establish an exact specimen relationship. Additional normal, recurrent or ambiguous-ancestry records are not substituted for the designated primary files or treated as validated technical replicates.

## 5. Persisted outputs and Notebook 113 interface

Exactly two generated artifacts are persisted under `data/interim/metadata/`:

| Output | Required content |
| --- | --- |
| `112_cptac3_rna_simple_primary_technical_inventory.csv` | One row per uniquely represented primary case/file, with source identities, STAR count diagnostics and additional same-case RNA indicators |
| `112_cptac3_qc_provenance_handoff.json` | Notebook 111 input paths and SHA-256 values, source-scope counts, technical-characterization boundary, scientific limitations and technical-inventory receipt |

The CSV **must retain** these fields consumed or validated by Notebook 113:

- `case_uuid`, `file_id`, `sample_uuid`, `aliquot_uuid`
- `n_gene_rows`, `n_duplicate_versionless_ids`
- `unstranded_nonnegative_integer_vector`, `n_invalid_unstranded_gene_values`
- `unstranded_gene_count_total`, `n_detected_star_genes`

The other source descriptors, STAR special-category counts and additional-RNA indicators remain part of the implemented technical inventory; they do not independently authorize sample eligibility.

The JSON must contain `outputs.technical_inventory` with:

- `path`: repository-relative POSIX path to the generated CSV.
- `rows`: number of generated technical-inventory records.
- `sha256`: SHA-256 of the persisted CSV bytes.

Notebook 113 checks that these receipt fields match the expected output path, its own candidate-ledger row count and the actual CSV digest. It also reconciles source identities and required technical diagnostics. The observed 1,082-row scope describes this completed source execution; the number must not be interpreted as a biological or sequencing-QC acceptance threshold.

The manifest records `schema_version=1`, `notebook=112`, the source inputs and their fingerprints, the technical-characterization scope and the actual output receipt. Its scientific boundary fields include:

- `technical_characterization.independent_sequencing_qc_performed=false`
- `technical_characterization.empirical_qc_thresholds_applied=false`
- `technical_characterization.qc_based_exclusions_applied=false`
- `QC_eligibility_authorized=false`
- `cohort_frozen=false`
- `program_scores_computed=false`
- `biological_replication_performed=false`

`source_technical_audit_complete=true` refers **only** to the bounded technical characterization performed here; it is not a statement of sequencing-QC qualification or external-cohort readiness.

The two outputs are regenerated from the specified local source inputs and are not Git-tracked deliverables. No additional intermediate CSV or JSON artifact is required by Notebook 113.

## 6. Validation requirements and scientific limitations

Successful execution requires:

1. The Notebook 111 integrity declaration and both recorded upstream CSV SHA-256 comparisons to succeed.
2. Primary-source identifiers to be unique and consistent with the audited source index; the uniquely represented primary cases must have exactly one file, sample and aliquot.
3. All included STAR count files to be present, pass the recorded-size check, and have valid gene identifiers, version-normalized uniqueness, nonnegative integer `unstranded` counts and valid STAR special-category representations.
4. Additional same-case RNA records to reconcile with the source index, without assigning exact sample or aliquot relationships to unresolved ancestry.
5. The persisted CSV to have the expected schema, row count and source identities; its SHA-256 must be captured in the JSON receipt. The persisted JSON must survive read-back comparison with the generated manifest.
6. No dependency on Notebook 113, Notebook 800, or outputs from later phases.

These conditions establish **technical representation and source-provenance consistency**, not read-level sequencing-quality acceptance. The notebook does not independently assess RNA integrity, library complexity, alignment-quality denominators, batch comparability, tumor purity, proliferation, cancer-lineage harmonization or TCGA–CPTAC donor independence. Nor does it normalize expression, score transcriptomic programs, adjudicate multiple primary specimens or evaluate external biological replication.

**Readiness boundary:** The generated inventory and manifest are eligible for **technical handoff to Notebook 113 only**. Their existence does not establish sample-level QC eligibility, frozen cohort membership, cross-dataset biological comparability, clinical prediction, causal mechanisms or external replication.
