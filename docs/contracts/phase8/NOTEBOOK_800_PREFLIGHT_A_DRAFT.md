# Notebook 800 — PREFLIGHT-A: external-bulk eligibility and frozen-input readiness

**Document type:** prospective *technical preflight plan* — **DRAFT, NOT FROZEN**  
**Prepared:** 2026-10-22  
**Baseline:** main commit f423d304f6ed3a4187965dcf783879e79abf47b5  
**Primary source candidate:** GDC project CPTAC-3, frozen file universe and acquisition-time metadata from Notebook 111  
**Executable implementation:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb` (PREFLIGHT-A–D executed; PREFLIGHT-E source-count technical inventory implemented, pending local run; no cohort freeze)
**Downstream analysis:** Notebook 800 external replication, not implemented or authorized by this draft

## 1. Scientific scope and non-goals

The objective of this microphase is to determine whether CPTAC-3 contains an auditable, independent and technically compatible external primary-tumor RNA-seq cohort for **external assessment of the three already-frozen Phase 4 transcriptomic consensus representations**. An independent methylation subset may contribute **separate contextual/orthogonal support**, but transcriptomic representation evaluation must not require methylation availability by default.

This is **not** external biological validation, a clinical prediction exercise, an adaptive-resistance study, a new discovery exercise, or an opportunity to change the three frozen consensus programs. No program-score projection, within-CPTAC-3 gene–program correlation, response-related analysis, enrichment, test-statistic inspection, or biological replication analysis is authorized by this preflight document.

The status labels below distinguish **audited technical facts**, **proposed eligibility policy**, and **unresolved prospective analysis decisions**. This document is not a retrospective claim that an unapproved analysis contract has already been frozen.

## 2. Frozen source and program handoffs

### 2.1 CPTAC-3 — technical audit from Notebook 111

Authoritative version-controlled inputs:

- config/manifests/cptac3/gdc_manifest_cptac3_rnaseq.txt
- config/manifests/cptac3/gdc_metadata_cptac3_rnaseq.json
- config/manifests/cptac3/gdc_associated_entities_cptac3_rnaseq.json
- config/manifests/cptac3/gdc_manifest_cptac3_methylation.txt
- config/manifests/cptac3/gdc_metadata_cptac3_methylation.json
- config/manifests/cptac3/gdc_associated_entities_cptac3_methylation.json

Local outputs of Notebook 111, currently **not available through version-controlled GitHub content**, must be reloaded and fingerprint-reconciled, not silently reconstructed:

- data/interim/metadata/111_cptac3_acquisition_audit_summary.json
- data/interim/metadata/111_cptac3_file_index.csv
- data/interim/metadata/111_cptac3_provisional_primary_tumor_files.csv
- data/interim/metadata/111_cptac3_ambiguous_sample_candidates.csv
- data/interim/metadata/111_cptac3_ambiguity_by_lineage.csv
- data/interim/metadata/111_cptac3_aliquot_multiplicity.csv
- data/interim/metadata/111_cptac3_raw_registry_proposal.json

Observed Notebook 111 facts, **not cohort-freeze conclusions**:

| Metric | RNA-seq | Methylation |
|---|---:|---:|
| All files, provider size/MD5 audited | 2,968 | 2,610 |
| Files with unique sample ancestry | 2,654 | 2,295 |
| Files with ambiguous sample ancestry | 314 | 315 |
| Provisional primary-tumor files | 1,731 | 1,450 |
| Provisional primary-tumor sample UUIDs | 1,697 | 1,430 |
| Provisional primary-tumor case UUIDs | 1,370 | 1,336 |

The provisional primary subsets share 1,389 exact sample UUIDs and 1,316 case UUIDs. The all-file sets share **zero exact aliquot UUIDs**. These counts are neither proof of paired biological aliquots nor evidence of external replication. One direct GDC aliquot is associated with multiple candidate sample UUIDs in 629 files; candidate sample-type agreement does **not** resolve that ancestry. Exclusion may differentially affect lineages, notably lung and pancreas. Methylation EPIC (2,371 files) and EPIC v2 (239 files) remain separate platforms.

### 2.2 Immutable Phase 4 representations

Use frozen IDs and checksum-validated files from config/artifact_registry.json:

- phase4.400.cross_system_shared_gene_universe — 2,389 ordered shared genes.
- phase4.401.consensus_transcriptomic_program_catalog — CONSENSUS_TX_01, CONSENSUS_TX_02, CONSENSUS_TX_03.
- phase4.401.consensus_transcriptomic_gene_weights — three complete 2,389-gene signed loading vectors.
- phase4.401.consensus_construction_metadata — identity, tumor-anchored sign and within-system scoring recipe.
- phase4.401.consensus_tumor_scores — reference TCGA tumor-side context, not an external validation cohort.
- phase4.401.consensus_tumor_arm_context — tumor methylation arms as separate context.
- phase4.402.cross_lineage_robustness_summary — internal lineage heterogeneity and limitations.

Notebook 401 standardized expression features *within biological system*, projected onto signed consensus weights, then standardized each projected score *within that same system*. Consequently the published TCGA numeric scores are not a portable absolute scale; CPTAC-3 scoring and inferential replication require distinct, prospectively specified procedures. Phase 4 sign is tumor RNA anchored, **not** intrinsically resistance-like; Phase 7's separate resistance-like orientation must not be imported to redefine Phase 8 representation.

## 3. Technical preflight work packages

### A. Source/registry and audit reproducibility

1. Verify that each local Notebook 111 audit file exists and matches the SHA-256 fingerprint in the 111 summary where available; reconcile source manifests, GDC metadata and direct-associated-entity snapshot IDs.
2. Reuse the observed Notebook 111 provider MD5 PASS, without re-downloading or rehashing all ~67.4 GiB by default. Any changed file or contradictory fingerprint fails the preflight and requires targeted reassessment.
3. Review the locally persisted 111 raw registry proposal and add a separately reviewed registration step for CPTAC-3; config/raw_data_registry.json currently has **no CPTAC-3 entry**. Do not mark a cohort acquired_and_used before downstream scientific eligibility and registry review are completed.
4. Freeze an exact list of source UUIDs and provider metadata versions for 800. A live GDC query must never silently expand or alter the candidate source universe.

### B. Candidate cohort eligibility (technical, not scientific support)

Proposed provisional RNA-seq candidate criteria:

- GDC direct file-to-aliquot association resolves uniquely;
- aliquot links to exactly one sample UUID in the audited provider hierarchy;
- sample_type equals Primary Tumor;
- file belongs to the frozen 111 CPTAC-3 STAR Counts acquisition universe;
- the file has passed the 111 payload-integrity audit.

**Do not** use same-case membership alone as sample matching. Keep the 314 RNA-seq ambiguous sample-ancestry files as explicit **unresolved/excluded-from-primary-candidate** records, even when all proposed sample parents are marked Primary Tumor, until genuine independent biospecimen provenance resolves ancestry. Document the sensitivity of eligible coverage by primary_site × disease_type without relabeling those descriptors as harmonized lineage.

No selected independent observations are frozen yet. Establish an *outcome-blind* one-observation-per-case rule for cases with multiple RNA files, aliquots or samples. Consider provider QC, replicate type, workflow metadata and consistent specimen identity **before** inspecting any program score. Never select the file with the strongest program signal, and never count technical replicates as independent cases.

The primary transcriptomic candidate cohort must not be restricted to samples with DNA methylation. A secondary methylation-compatible candidate inventory requires its own identity, platform, assay and exact-sample pairing policy.

### C. External-cohort independence audit

- Compare exact case UUIDs, specimen UUIDs and submitter identifiers across candidate CPTAC-3 and the *frozen* TCGA primary-tumor mapping from phase2.203.final_sample_mapping.
- Obtain documentation/crosswalk evidence where available for CPTAC project contributions and potential donor overlap. Absence of matching UUIDs alone is insufficient to certify different donors.
- Record separately: documented independent / documented overlap / unresolved identity. Do not assert independent external patient validation for unresolved donors.
- Preserve potential duplicate donor, non-independent sample, and cross-cohort provenance evidence; resolve before a confirmatory claim.

### D. Transcriptomic input-compatibility inventory

Before scoring any program:

1. Load and hash-check the exact 2,389 frozen gene universe and the 7,167 frozen program-gene rows.
2. Verify the STAR Counts source headers, raw count column identity, gene identifiers, annotation/workflow metadata and unexpected duplicated/missing gene mappings. Audit representative technical groups first, then complete required file-level compatibility checks before cohort freeze.
3. Report exact Ensembl-ID match, version-sensitive mismatch, uniquely reconciled ID match and ambiguous/unmapped genes **separately**. Do not silently strip versions or substitute symbols as a rescue rule.
4. Record missingness, count distributions, library sizes and technical QC availability *without looking at gene–program association results*; avoid replacing absent genes with zero weights/zero expression without a justified prespecified policy.
5. Compare source normalization/feature preparation from Phase 2 (unstranded counts, TMM/logCPM) and the projection recipe in 401. Determine whether any TCGA reference gene-level means/SDs need reproducible reconstruction from frozen TCGA inputs, and how GDC workflow differences affect portability.
6. Do not reselect genes, alter signed weights, optimize the reference transformation on CPTAC-3, or jointly fit normalizers using discovery plus external samples.

Define the feature-coverage gate and failed-project treatment only after the preflight technical distributions and provenance are documented and **before** any CPTAC-3 program evidence is inspected.

### E. Context, confounding and compatibility matrix

Produce an inventory by source primary_site × disease_type × modality × platform, with file, aliquot, sample and independent case denominators kept separate. Include:

- ancestry mapping status; fraction of unresolved/excluded records at both file and case levels;
- within-case multiple-sample and within-sample multiple-file structure;
- technical workflow, read/count QC and source batches when available;
- tumor purity, immune/stromal composition and proliferation covariate availability (missing must remain missing, not imputed post hoc for interpretive rescue);
- explicit crosswalk from CPTAC descriptors to TCGA lineage/project definitions, with unmapped or ambiguous categories retained;
- RNA-only and independent methylation coverage by lineage and platform, without pretending two assay modalities are paired merely because cases overlap.

Do not use pooled pan-cancer comparisons as evidence of recurrence.

## 4. Notebook 800 PREFLIGHT-A: technical outputs (executed locally; non-frozen)

The preflight stage is implemented as short, auditable cells inside `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`, following `docs/NOTEBOOK_STYLE_GUIDE.md`, the Notebook 111 acquisition handoff, and frozen Phase 4 registries. It uses existing `Paths`, `calculate_sha256`, `load_artifact_registry`, `get_artifact`, `resolve_artifact_path`, and `load_raw_data_registry` helpers rather than introducing an additional standalone script.

The current implementation reloads/fingerprint-checks the small local Notebook 111 derived audit tables; reuses Notebook 111 file-level source-stratum ambiguity rather than recomputing it; adds a *new case-level* affected-case diagnostic; constructs a case-by-case file/sample/aliquot inventory; **classifies RNA-seq multiplicity by within-case identifier structure and screens cross-file biospecimen ancestry conflicts, without selecting files**; examines exact-string cross-cohort ID collisions without claiming donor independence; and performs one deterministic STAR Counts gene-ID pilot. It **does not** perform full cohort-wide feature compatibility, lineage crosswalk harmonization, donor-provenance review, program scoring, external replication or a frozen cohort selection. These remain subsequent review actions.

Local non-frozen outputs are written under `data/interim/metadata/`:

| Output | Scope |
|---|---|
| `800_preflight_a_candidate_lineage_inventory.csv` | GDC source stratum × modality/platform counts: acquisition files/cases, unresolved files/cases and provisional primary-tumor denominators |
| `800_preflight_a_case_multiplicity.csv` | Exact candidate UUID lists, distinct files/samples/aliquots per provisional primary case, **RNA-specific structural multiplicity class**, cross-file ancestry-contradiction diagnostic, and **NOT_FROZEN** selection flag |
| `800_preflight_a_identifier_collisions.csv` | Exact lexical TCGA/CPTAC case and submitter-string collisions; explicit `UNRESOLVED_WITHOUT_EXTERNAL_PROVENANCE` |
| `800_preflight_a_gene_id_pilot.csv` | Frozen 2,389-gene IDs compared to one deterministic STAR Counts pilot, including version-insensitive **diagnostics only** |
| `800_preflight_a_readiness.json` | Upstream/input fingerprints, RNA-seq case multiplicity class counts, output fingerprints, open gates and explicit no-scoring/no-validation status |

The added case-level classification is deliberately narrower than an adjudication. Its mutually exclusive technical categories are `SINGLE_FILE_SAMPLE_ALIQUOT`, `ONE_ALIQUOT_MULTIPLE_FILES`, `ONE_SAMPLE_MULTIPLE_ALIQUOTS`, `MULTIPLE_SAMPLES_IN_CASE`, and explicit anomaly categories (`INCONSISTENT_BIOSPECIMEN_COUNTS`, `CROSS_FILE_BIOSPECIMEN_CONFLICT`). A single-aliquot/multifile pattern does **not** establish technical replicates, equivalence of counts, or preferred source files. A multiple-sample pattern does **not** establish temporal or spatial sampling provenance. No category is a final inclusion/exclusion decision. The Notebook 111 sample/aliquot/file multiplicity tables are not recomputed; the existing 800 case-level inventory is annotated in place.

These diagnostics are not published to `config/artifact_registry.json` as frozen validation artifacts. No notebook output was executed in GitHub; the GDC source payloads and Notebook 111 interim tables reside on the user's local computer.

## 4B. RNA case/sample/aliquot adjudication **evidence**, not selection

After the first 800 Run All confirmed **1,370 provisional primary RNA cases**, including **1,082 single-file/sample/aliquot cases, 276 cases with multiple sample UUIDs, and 12 cases with multiple aliquots of one sample**, a second outcome-blind stage was added to **the same Notebook 800**. The reported initial counts are frozen observed notebook results, not new eligibility rules.

**PREFLIGHT-B is an evidence sufficiency review of the 288 already flagged cases only.** It consumes `rna_cases` and `candidate_primary` already loaded and classified in Notebook 800; these trace to the exact audited Notebook 111 file index. It does **not** reacquire/revalidate source files, reopen ambiguous ancestry, recheck the original sample/aliquot multiplicity, or reapply the Notebook 111 primary-tumor selection flag.

Inspect only these already audited metadata families:

- exact case/sample/aliquot/file IDs and their submitter counterparts;
- GDC-reported `sample_type`, `tissue_type`, `tumor_descriptor`;
- GDC `primary_site`, `disease_type`, `project_id` to expose source-label conflicts (not to harmonize lineages);
- source `workflow_type` and `platform`; file sizes and hashes retained as provenance **without** interpreting them as quality scores.

Produce one-row-per-case and one-row-per-file evidence inventories **only for the 288 review cases**, including case-class labels, source-descriptor completeness/discordance, cross-file relationship checks, and explicit `INSUFFICIENT_TO_SELECT_WITHOUT_PROSPECTIVE_QC_POLICY` status. Add to the existing notebook-output mapping:

- `data/interim/metadata/800_preflight_b_rna_case_evidence.csv`
- `data/interim/metadata/800_preflight_b_rna_file_evidence.csv`

Extend the existing `800_preflight_a_readiness.json` with B-stage evidence class counts; don't create a second redundant summary or change frozen registries.

**No automatic selection:** even if multiple biospecimens share all reported descriptors, that does not imply same tumor region, same collection time, equivalence or technical replicates. Missing or discordant descriptors must remain visible, not be turned into result-dependent prioritization. Relative RNA-seq quality (e.g., STAR assignment metrics), independent sample provenance, and an outcome-blind file choice/exclusion policy remain **unassessed** in this stage; no arbitrary sorting, larger-file preference, platform preference, sample-ID lexical tiebreaker, case dropping, or scores.

B-stage success means technical metadata evidence was documented reproducibly, **not** that adjudication succeeded or external replication is ready.

## 4C. PREFLIGHT-C — constrained provenance and QC **availability**, not QC adjudication

**Accepted PREFLIGHT-B observation (2026-10-22, GitHub commit `2e3e250`).** The previous 800 Run All examined 288 RNA-seq cases (649 source files): 276 cases/619 files with multiple sample UUIDs and 12 cases/30 files with multiple aliquot UUIDs from one sample. The preserved Notebook 111 descriptors were complete for the B-stage queried fields, with zero cross-file source-descriptor disagreements. This is an *observed technical result*, not proof of biological or technical equivalence. PREFLIGHT-B was accepted for its descriptive sufficiency audit; no case was adjudicated.

**PREFLIGHT-C scope.** Reuse the acquisition-time `config/manifests/cptac3/gdc_metadata_cptac3_rnaseq.json` snapshot, checksum verified against Notebook 111's `source_fingerprints.rnaseq.metadata.sha256`. Restrict all new observations to the exact **649 file UUIDs** in the existing 800-B file evidence inventory, and reach additional biospecimen attributes **only** through the already resolved `case_uuid` → `sample_uuid` → `aliquot_uuid` hierarchy path. The snapshot includes case-scoped expansions; do not infer specimen ancestry from case membership alone, redo the 111 ancestry audit, or rehabilitate the 314 ambiguously mapped RNA files. If an audited case/sample/aliquot path cannot be found, halt for contradiction review rather than guessing.

Measure **field-key availability, informative scalar values, and conflicting scalar values across matching exact paths**. Common placeholders (e.g., `Not Reported`, `Unknown`, `Not Applicable`) are not informative. Store any observed scalar keys *in addition* to explicit probes, so absent predefined probes and unexpected metadata fields are both visible. Distinguish six groups: generic sample descriptors; collection timing; source sampling location detail; sample/portion/analyte processing metadata; administrative identifiers and source file/analysis workflow dates; and quantitative QC metadata probes. Source-file creation times must never be treated as collection times; concentration and `sample_type`/ `tumor_descriptor` labels are not quality measurements or proof of spatial equivalence. Provider hashes and file size remain identity/provenance metadata, never selection criteria.

**Limit of C's technical QC claim:** this is an availability screen of the **preserved JSON snapshot only**. No STAR Counts files, library-level quality profiles, sequencing run reports, alignment logs, or live GDC endpoint expansions are read. A field missing from this acquisition projection is **not proof that the corresponding data are absent elsewhere in GDC**. Even a reported scalar mapping/QC metric would require definition, comparability and prespecified eligibility criteria before use for selection.

Preserve three new *non-frozen* outputs, under `data/interim/metadata/`:

- `800_preflight_c_rna_field_coverage.csv` — explicit probes plus observed scalar fields by nested provenance scope; number of 649 candidate files with key, informative value and within-file disagreement.
- `800_preflight_c_rna_file_availability.csv` — one row per 649 audited RNA files, unchanged file/sample/aliquot/case IDs, matching exact path row count and per-domain availability/discordance.
- `800_preflight_c_rna_case_coverage.csv` — one row per 288 cases, with coverage denominators kept at file and case level; **no candidate selected**.

Extend the existing `800_preflight_a_readiness.json` with C-stage input fingerprint and coverage context (do not write a second readiness summary). Keep `one_record_per_case=PENDING_POLICY`, `biological_validation_authorized=false`, and `cohort_frozen=false`. No registry changes, no scoring, and no inferred donor independence. Outcomes are to be reviewed after **local execution**; these are implementation intentions, not claimed observations.

**Decision boundary after C:** if the snapshot is insufficient to distinguish specimen collection region/timepoint and objective, comparable RNA quality, keep all 288 multiplicity cases explicitly unresolved pending independently sourced provenance/QC. Do not repair that insufficiency using lexical or result-dependent prioritization. Consider later predeclared sensitivity designs using a uniquely unambiguous set, with lineage-dependent attrition documented, only after scientific and technical contracts are reviewed.

## 4D. PREFLIGHT-D — Directed *live GDC* metadata and QC feasibility pilot

**Rationale.** C-stage tests of the 2026 acquisition-time GDC metadata projection yielded no informative field values for the tested precise collection timing, sample location or quantitative QC variables in 649/649 files. This does not demonstrate their absence from the current provider API. The [GDC official API field catalog](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/) documents additional names such as `cases.samples.biospecimen_anatomic_site`, `cases.samples.biospecimen_laterality`, `cases.samples.portions.analytes.rna_integrity_number`, and `analysis.metadata.read_groups.read_group_qcs`. Fields listed in a schema are not necessarily populated for CPTAC-3, nor analytically valid as QC metrics.

**Design and strict scope — staged pilot, not 649-file expansion:**

1. Use only the frozen `rna_adjudication_cases`/`rna_adjudication_files` identities from 800-B, whose inputs and 288-case/649-file counts were verified. Choose **3 cases each** from source-defined `Uterus, NOS`, `Kidney`, `Larynx` (multiple-sample class) and `Pancreas` (multi-aliquot class), sorted by case UUID only to ensure a deterministic **technical diagnostic sample**, not to select a final analysis cohort. If expected source strata are absent or insufficient, stop rather than silently sampling replacement cases.
2. Query `https://api.gdc.cancer.gov/files` by the precise pilot file UUID list with a bounded, fully recorded `fields`, `expand`, `size`, `filters` request. Use the supported file-associated nested biospecimen and analysis/read-group metadata groups; no general GDC queries or acquisition re-download. Capture an immutable-on-rerun, local, non-frozen `800_preflight_d_gdc_targeted_pilot.json` snapshot recording the query, capture time, provider response and SHA of the original Notebook 111 RNA metadata. Cached runs must match the complete request fingerprint.
3. Reconcile the new API file identity (UUID, filename, byte size, MD5) to **Notebook 111's existing authoritative file index**; do not rehash the actual STAR or re-run MD5 of 2,968 files. Retain any absent or contradictory live association as an unresolved provenance signal. Biospecimen fields may be attributed only after matching the **exact previously resolved** case→sample→aliquot triplet and checking the direct file-associated aliquot, never by same-case nested membership alone. The new live snapshot does not resolve the 314 files with ambiguous sample ancestry.
4. Screen source-informed provenance fields (anatomic site, laterality, collection timing and method, preservation), analyte quality candidates (e.g., RIN), and file/read-group QC **availability**. Distinguish scalar informative values, missing/unknown, structured QC reports, and distinct values across candidates within a single case. Field presence is not a quality pass; raw `basic_statistics` objects are not converted into numeric scores. No post-hoc QC threshold, sample promotion, replicate pooling or score-dependent selection.
5. Persist pilot summaries with one-row-per-file identity, long-form file-field evidence and case-field contrasts, plus a 12-case summary. Update existing `800_preflight_a_readiness.json` and record D snapshot SHA, **without** appending new names to `config/raw_data_registry.json` or `config/artifact_registry.json`. The original 111 provider snapshots and frozen acquisition UUID universe remain unchanged.

**Non-frozen D outputs in `data/interim/metadata/`:** `800_preflight_d_gdc_targeted_pilot.json`, `800_preflight_d_rna_pilot_file_identity.csv`, `800_preflight_d_rna_pilot_field_evidence.csv`, `800_preflight_d_rna_pilot_case_field_comparison.csv`, `800_preflight_d_rna_pilot_case_summary.csv`. Provider live fetch is performed only once when the exact scoped local snapshot is missing. Failure or partial retrieval is an error, not evidence that missing fields do not exist.

**Interpretation decision after local run:** if additional *exact-linked* provenance/QC fields exist, examine their meaning, linkage and within-case differentiation before considering expansion to the remaining 649 files. Otherwise stop the extra-GDC search path, leave 288 cases unresolved and evaluate independent source documentation or a predeclared unambiguous-cohort analysis for PREFLIGHT-E. No automatic move from pilot to 649-file acquisition is authorized.

### 4D.1 Microcorrection after first PREFLIGHT-D execution — **v2 executed and reviewed**

**Observed first pilot (GitHub commit `87d56d3`):** 12 cases, 29 distinct RNA files. All 29 live files matched their 111 file identity and direct linked aliquot, but **0/29** had an exact `case_uuid/sample_uuid/aliquot_uuid` nesting recovered by the queried `/files` response. The availability table consequently reported no informative additional fields. The first run is **technical execution PASS, evidentiary linkage BLOCKED**; the zero field-availability results are not evidence of provider-wide absence. The complete previous raw response is preserved locally in `800_preflight_d_gdc_targeted_pilot.json`.

**Correction:** document the prior snapshot's observed nested identifier structure locally, without re-querying it. Obtain two **bounded, separately hashed query projections**, restricted to exactly the original 29 file UUIDs and 12 case UUIDs:

- `/files`: request `cases.case_id`, `cases.samples.sample_id`, `cases.samples.portions.portion_id`, `cases.samples.portions.analytes.analyte_id`, `cases.samples.portions.analytes.aliquots.aliquot_id` explicitly alongside the original direct-associated-entity and analysis/read-group expansions.
- `/cases`: use an exact 12-case UUID filter with `samples.sample_id`, `samples.portions.portion_id`, `samples.portions.analytes.analyte_id`, `samples.portions.analytes.aliquots.aliquot_id`, plus relevant sampled collection/spatial/analyte fields and fully nested sample hierarchy expansions.

This dual-source approach is **not** permission to resolve file ancestry by case membership. Additional specimen attributes can be attributed to a file only if: (1) the returned file UUID, filename, size and MD5 agree with Notebook 111; (2) the new /files direct associated aliquot and case agree with the 111 pre-resolved link; (3) the /cases or /files hierarchy contains the exact *same* previously mapped case/sample/aliquot triplet. If these conditions fail, mark the record **`BLOCKED_NO_EXACT_TRIPLET`** or the corresponding direct-link conflict; never claim that a sample is uniquely assigned by a case-scoped expansion. Prioritization of /cases-linked attribute completeness over /files is explicitly documented, and the provenance path is written for every file.

Write the entire new raw-provider response and both complete query definitions under a **new, non-overwriting** `800_preflight_d_gdc_targeted_pilot_v2.json`, including source/capture timestamps, original 111 metadata SHA, prior v1 SHA when present and a deterministic SHA of the combined two-query contract. Exact file and case UUID sets must reconcile. All subsequent D-stage diagnostics/readiness must refer to the v2 source SHA while preserving the prior v1 snapshot. A v2 run with fewer than 29 exact-linked files is explicitly `BLOCKED_INCOMPLETE_EXACT_TRIPLET`, not an audit PASS for specimen provenance; the field table must not attribute case-scoped descriptors to unlinked files.

**Next decision:** evaluate the v2 pilot results *before* considering expansion to all 649 files. No automatic case adjudication, external validation, frozen cohort, registry mutation or program scoring is authorized.

### 4D.2 Observed v2 pilot outcome and evidence boundary — 2026-10-23

The revised notebook completed **41/41 code cells** without error (GitHub execution commit `fd0ea57f`). Only notebook output payloads were modified during that local execution; the code cell sources remained unchanged. A separate snapshot was captured as `data/interim/metadata/800_preflight_d_gdc_targeted_pilot_v2.json`, SHA-256 `297c48c0b6be7979b56e12fb67853cbc32ee75017d79eafb28b4cba307d25c31` (local non-frozen source evidence; not a Git-tracked CSV).

For the same deterministic **12 cases and 29 file UUIDs**, identity and exact pre-resolved case/sample/aliquot hierarchy reconstruction succeeded **29/29**. Both new /files and /cases projections contained the exact link; the specimen-field provenance table used **CASES_ENDPOINT_EXACT_TRIPLET**, conditional on direct file–aliquot association and 111 ancestry. The earlier v1 result of 0/29 nested links was a source-projection omission rather than an unresolved contradiction in the frozen association mapping.

In the v2 pilot, **29/29** files had informative general anatomical and at least one collection/procurement descriptor (e.g., `biospecimen_anatomic_site`, `days_to_sample_procurement`, `method_of_sample_procurement`, `preservation_method`). Other location or processing fields were only partly present. Across the **300** case × probed-field combinations, **no pair of candidate files within a case** had differing informative field values. **0/29** pilot files carried informative queried quantitative file-level QC fields or read-group QC records. No subset was selected or excluded.

**Decision:** PREFLIGHT-D v2 has **PASS for the limited source-linkage and metadata-availability pilot**. It provides no observed, prospectively defensible within-case specimen preference, and the sampled metadata fields alone do not justify an automatic 649-file expansion. The zeros are specific to the **29-file pilot** and those response fields; they cannot establish provider-wide QC absence or absence of differentiated provenance in all 649 files. The **288 multiplicity cases remain pending**, and the 1,082 structurally simple cases remain provisional pending technical QC, lineage-aware attrition, compatibility and donor-independence review. No validation cohort or biological replication contract is frozen.

## 4E. PREFLIGHT-E — Single-primary RNA-seq technical readout and context attrition (pending local execution)

**Entry gate.** PREFLIGHT-D v2 recovered the exact case/sample/aliquot provenance of its 29-file pilot; none of the newly informative provider attributes discriminated between candidates within a case and no queried quantitative QC field was populated. The 288 multiplicity cases therefore remain **unadjudicated**. Do **not** automatically expand the D metadata API query to 649 files or choose candidates using either program signal or administrative IDs.

**Prospective E boundary: technical diagnostics, not cohort freeze.** Use the 800-A structural class `SINGLE_FILE_SAMPLE_ALIQUOT` to create exactly **1,082 cases with one provisional primary RNA-seq file each**. The phrase *single-file* refers to the **already audited provisional primary subset**, not necessarily to every source file associated with the patient. Reconcile their existing case/file IDs to the fixed Notebook 111 `candidate_primary` inventory and compute the number of *other same-case RNA files*, including records with unresolved sample ancestry, from `111_cptac3_file_index.csv` (already fingerprinted). Source context attributes are retained as `primary_site` and `disease_type`, **not** harmonized TCGA lineages.

**Read-only STAR Counts technical inventory of the 1,082 files:**

- Reuse the **provider MD5 PASS of Notebook 111** and frozen source UUID/file name/byte size; *do not rehash ~67 GiB, redownload, or rescan other modalities*. Missing or wrong-sized source payload is an error. Read `gene_id` and `unstranded` only, with comment lines excluded.
- Parse the STAR `N_` special non-gene rows separately (e.g. `N_unmapped`, `N_multimapping`, `N_noFeature`, `N_ambiguous`). Record availability and descriptive counts but do **not** relabel them as alignment QC, sample-mapping rates or externally comparable RIN/FASTQ quality.
- Detect duplicated exact gene IDs and malformed/negative/non-integer/nonfinite count values. Report file-level gene rows, total unstranded gene counts, number of detected genes, exact presence of the **frozen 2,389 tumor Ensembl IDs**, and versionless matching **diagnostics only**. Do not strip annotation versions to create mappings, replace absent genes by zeros, recalculate consensus weights or compute program scores.
- Produce a compact **gene-ID coverage table** (2,389 frozen genes × count of simple-case files with exact ID) and **one technical-record row per file**. The small tables contain diagnostics and source IDs, **not** an external expression matrix.
- Stratify the 1,370 provisional RNA primary cases by source `primary_site` × `disease_type`, separating **1,082 simple** and **288 multiplicity** cases, with indicators for other RNA records, ambiguously mapped same-case files, exact gene-ID compatibility and count-vector parsability. This is **structural attrition** rather than a proof of independent cases or valid source-to-TCGA lineage mapping.

**New non-frozen outputs in `data/interim/metadata/`:**

- `800_preflight_e_rna_single_primary_file_technical.csv` — exact case/file/sample/aliquot identifiers plus technical diagnostics and same-case other source-file flags; no selected/eligible label.
- `800_preflight_e_frozen_gene_id_coverage.csv` — exact frozen gene presence across the 1,082 file records; no gene weights or scores.
- `800_preflight_e_source_context_case_attrition.csv` — distinct case-count denominators and structurally simple/multiple proportions by **unharmonized source context**.

Append these outputs and their hashes to the existing `800_preflight_a_readiness.json`. This is a **new local read-only count/feature diagnostic**, not re-execution of Notebook 111 file identity, provider checksums or provenance mapping.

**What E does NOT establish:** library fragment metrics, usable read alignment/duplication, RNA quality scores such as RIN, platform batch comparability, tumor purity, lineage crosswalk, donor independence from TCGA, one-record-per-case selection for the 288 cases, preservation of relative program-score scale, and a frozen external replication estimand. Read count distribution and exact identifier presence do **not** define prospective QC exclusion thresholds. Every source stratum remains *not evaluable for confirmatory inference* until those requirements are reviewed and the explicit cohort and null model are frozen.

**Decision after first Run All:** inspect exact 2,389-gene coverage across files, any malformed count-vector evidence, how many of the 1,082 nominally simple cases have additional/unresolved source RNA records, and which source strata lose disproportionate numbers of cases. Based on those observed **technical** results, separately propose (not implement silently) phenotype-agnostic QC criteria, independent donor-provenance checks, a lineage crosswalk and sensitivity analyses. The descriptive E output is not permission to score, normalize or freeze a CPTAC-3 validation cohort.

## 5. Pre-confirmatory analysis contract — OPEN items only

Before observing CPTAC-3 program scores or representation-replication statistics, separately review and freeze:

1. Biological unit, selected one-per-case hierarchy, independent-donor status, lineage mapping and handling of ambiguous ancestry.
2. Transcriptomic QC criteria, full frozen-gene coverage policy, normalization/reference scaling, missing-gene handling, and complete preplanned technical exclusions.
3. **Independent replication estimand**: what property beyond the mere existence of a projected score constitutes recovery of program structure, with an internal TCGA reference and an appropriately matched null/negative control. A score correlated with its own constituent expression genes is circular evidence and not an acceptable primary replication endpoint.
4. Gene-disjoint or other genuinely held-out structural checks if used; data partitioning, gene-set construction, weight-sign balance and random seeds frozen before looking at outcomes. No post hoc threshold or gene-list rescue.
5. Lineage-aware primary comparisons and handling of technical, purity, stromal/immune and proliferation confounding. Set the primary family, planned effect sizes, uncertainty intervals, multiplicity correction, evaluation gates and power/coverage limitation categories.
6. A primary RNA-seq replication analysis distinct from any secondary methylation contextual association; EPIC and EPIC v2 platform harmonization and exact-matched sample criteria only for the latter.
7. Reporting of positive, negative, heterogeneous, not-evaluable and identity-unresolved outcomes without post-selection or undisclosed rescue.
8. Source provenance, complete source and environment fingerprints, expected output schema, deterministic re-execution and role of Phase 9. The endpoint must not become a clinical predictor, mechanistic claim or therapeutic validation.

## 6. Scientific and operational risk register

| Risk | Present evidence | Required gate |
|---|---|---|
| Sample-ancestry misassignment | 629 files across modalities have multiple candidate sample UUIDs | Exclude unresolved from primary candidate or resolve through independent provenance |
| Lineage-dependent attrition | Notebook 111 documents heterogeneous ambiguity (including pancreas and lung) | Quantify retained-case fractions by stratum; report selection limitation |
| Technical-replicate pseudo-replication | Multiple RNA files per sample/case, particularly in uterine and kidney strata | One independent selected unit per case after outcome-blind rule |
| Different molecular preprocessing | GDC STAR Counts vs frozen TCGA TMM/logCPM; Notebook 401 within-system standardization | Technical compatibility and primary projection rule prior to scoring |
| Outcome-circular validation | Same genes both construct and assess a score | Independent structural estimand and prespecified negative controls |
| Non-independent donor sets | Exact cross-project donor mapping not audited | Document overlap or retain unresolved independence status |
| Pan-cancer lineage leakage | Dominant and heterogeneous source lineages | Lineage-aware evaluation and no naive pooled support claim |
| Multi-omic/platform leakage | EPIC and EPIC v2; case overlap not aliquot equivalence | Independent modality assessment and exact-source provenance |

## 7. Current gate and next action

**SOURCE TECHNICAL INTEGRITY: PASS** (Notebook 111, 2026-10-21).  
**PROVISIONAL RNA-PRIMARY INVENTORY: AVAILABLE, NOT COHORT-FROZEN.**  
**DONOR INDEPENDENCE: NOT FULLY VERIFIED.**  
**EXTERNAL FEATURE COMPATIBILITY: NOT ASSESSED.**  
**PHASE 8 REPLICATION CONTRACT: NOT FROZEN.**  
**BIOLOGICAL VALIDATION AUTHORIZED: NO.**

Next action: run the revised Notebook 800 locally to execute D's bounded 12-case *live-GDC exact-file* pilot; review whether new fields are actually populated, correspond to the already audited case/sample/aliquot triplets, and differentiate within-case files. If field-value coverage is insufficient, identify the specific missing provenance/QC sources prospectively rather than choosing files arbitrarily. Cohort selection, lineage mapping, donor independence and full technical QC still require separately reviewed decisions; no external program replication is authorized.
