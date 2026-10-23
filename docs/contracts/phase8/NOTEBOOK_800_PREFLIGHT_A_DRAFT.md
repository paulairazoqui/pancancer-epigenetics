# Notebook 800 — PREFLIGHT-A: external-bulk eligibility and frozen-input readiness

**Document type:** prospective *technical preflight plan* — **DRAFT, NOT FROZEN**  
**Prepared:** 2026-10-22  
**Baseline:** main commit f423d304f6ed3a4187965dcf783879e79abf47b5  
**Primary source candidate:** GDC project CPTAC-3, frozen file universe and acquisition-time metadata from Notebook 111  
**Executable implementation:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb` (PREFLIGHT-A–F executed; PREFLIGHT-G QC feasibility implemented, awaiting local run; no cohort freeze)
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

### 4E.1 Observed PREFLIGHT-E outcome — 2026-10-23

The first local Run All completed **47/47 executable code cells**, no errors, committed as `2e1642174447f1806759c528c5c1f5ce74f2908b`. No cell sources were changed from the prepared version. The 1,082 provisionally single-primary-file samples were processed with only `gene_id` and `unstranded` from each already acquired STAR Counts file.

**Compatibility evidence:** **1,082/1,082** files had **60,660 STAR gene rows** and exactly **2,389/2,389 frozen tumor gene IDs**. No file was missing a frozen exact ID or required version-insensitive rescue. No file had invalid non-integer, negative or nonfinite unstranded count values; this is a count-vector parsability result, not complete sample sequencing QC. Per-file total unstranded gene counts: median **38,347,562**, min **1,074,810**, max **84,641,397**. Positive-count genes: median **42,264**, min **20,953**, max **46,782**. A low-count tail merits follow-up using the existing E CSV; empirical thresholds **must not** be tuned to achieve favorable sample or lineage retention.

**Source-case multiplicity that survived the simple-primary structural screen:** **530/1,082** have at least one other GDC RNA file attached to their case outside the uniquely mapped provisional-primary universe, including **37** with an additional ambiguous-sample-ancestry RNA record. These figures cannot determine that a second file is another primary tumor, a normal, a technical replicate, or the same biopsy. Distinguish its tissue/mapping status from the already fingerprinted Notebook 111 index before selecting whole-patient or unique-specimen policies. This is not justification for discarding all 530.

**Highly unequal attrition by *source* context:** uterine adenocarcinoma **56 single/235 provisional cases** (179 multiplicity cases), kidney adenocarcinoma **192/232**, laryngeal squamous tumors **18/37**, other tongue squamous **7/19**, floor-of-mouth squamous **6/17**, pancreatic ductal/lobular **88/100**. This is **raw primary-site/disease-type stratification**, not harmonized TCGA lineage. Discarding the 288 multiplicity cases would disproportionately change the uterine and parts of head-and-neck representation; case counts are not an independent-donor validation denominator until overlap and lineage controls are settled.

The following E outputs were generated locally (not automatically committed as external validated evidence):
`800_preflight_e_rna_single_primary_file_technical.csv` (1,082 rows),
`800_preflight_e_frozen_gene_id_coverage.csv` (2,389 rows),
`800_preflight_e_source_context_case_attrition.csv` (22 rows).
The readiness record reports `DESCRIPTIVE_COMPLETE_NOT_ELIGIBILITY`, no E sample selection, no frozen cohort and `biological_validation_authorized=false`.

**Verdict:** **PASS for E's bounded technical readout and source-context attrition inventory**, **NOT PASS for RNA sample QC, donor independence or prospective analytic eligibility**. Before any biological projection, review the low-count tail, explain other same-case RNA files, obtain or define independent source-aware QC evidence, assess lineage-aware feasibility and document a prespecified policy for the 288 unresolved multiplicity cases. Do not repeat the full 1,082-file scan solely to explore a different threshold. Phase 8 replication is still **unauthorized**.

## 4F. PREFLIGHT-F — Non-rescanning additional-RNA provenance and low-count QC triage (pending execution)

**Accepted E result (2026-10-23):** of **1,082** cases with exactly one uniquely mapped provisional primary-tumor RNA file, **530** also had other same-case RNA records in Notebook 111's *full-source* file inventory; **37** had at least one additional RNA file with ambiguous sample ancestry. The 1,082-file STAR technical scan verified all 2,389 frozen gene IDs in every file, with zero nonnumeric/negative/noninteger count vectors. None of these results proves donor independence, adequate RNA sequencing QC, or eligibility.

**Performance and input-integrity contract:** The preceding `p800-e-003` cell previously reparsed all 1,082 STAR files and took a long time on local OneDrive-backed storage. Its default has been replaced with a **verified E-output cache**: it loads `800_preflight_e_rna_single_primary_file_technical.csv` and `800_preflight_e_frozen_gene_id_coverage.csv` only after matching their complete SHA-256 values against the **previously executed** `800_preflight_a_readiness.json`, checking Notebook 111 source fingerprints, the frozen gene universe fingerprint, exact case/file/sample/aliquot tuples, source filename/provider MD5/byte-size metadata, gene ID identity and coverage conservation. This avoids rereading 1,082 payloads on subsequent Run All executions. If any cache requirement fails or an input changes, execution **fails closed**; it does not silently re-read all files, reconstruct another version of the audit, or substitute new input rows. `RUN_E_FULL_STAR_RESCAN=True` is an **explicit, separately reviewable opt-in** to repeat the original full scan when technically justified. The default is `False`. It is not an exemption from audit: the initial full E scan was executed and the persisted outputs' fingerprints are already recorded.

**F tasks using existing small metadata only:**

1. Revisit `111_cptac3_file_index.csv` already fingerprint-verified in Notebook 800. Join the exact 1,082 structurally simple provisional-primary case IDs to **all** available RNA source file IDs, subtracting only the single already nominated provisional-primary file in each case. Preserve the raw 111 `mapping_status`, `sample_type`, sample/aliquot IDs, file IDs, site/disease descriptors. Classify the other files as: ambiguous sample ancestry, other unresolved association, independently resolved primary tumor (unexpected and worthy of review), resolved normal, resolved recurrent, resolved metastatic, or remaining resolved/unspecified sample type. **Never** infer file–sample ancestry from same-case membership.
2. Compute other-file counts by sample type and mapping status, plus one row per source file and one row per each of 1,082 cases. Check that the already observed **530 cases with any other RNA** and **37 cases with any ambiguous-ancestry RNA** reconcile exactly; otherwise stop. Report how often additional records share the resolved primary sample/aliquot UUID **only** for files whose own unique mapping was already audited. The actual categories are to be interpreted *after* local Run All.
3. Summarize case-level additional-file burden by unharmonized GDC `primary_site` × `disease_type`, keeping case denominators separate from file denominators. This is not a completed TCGA lineage crosswalk and must not be presented as replicated cross-cancer signal.
4. Using the **cached** E file diagnostics, list a reproducible **fixed 20 lowest total-unstranded-count records** (ascending count, file UUID tie-break). Include exact gene coverage, detected gene counts and existing STAR `N_` summary fields for review. This rank is descriptive; **there is no bottom-20 exclusion, QC failure label or data-tuned count cutoff**. Low library counts are not necessarily failed sample sequencing QC in isolation.

**Four new non-frozen F outputs:**

- `data/interim/metadata/800_preflight_f_other_same_case_rna_files.csv` — full extra-file identities with original source mapping and typed descriptors; no promotion/exclusion.
- `data/interim/metadata/800_preflight_f_single_primary_case_context.csv` — **1,082 case rows**, including the zero-extra-file cases and audited extra-file categories.
- `data/interim/metadata/800_preflight_f_source_context_additional_rna_summary.csv` — descriptive provider source-site/disease case and file denominators.
- `data/interim/metadata/800_preflight_f_low_count_tail_descriptive.csv` — **20 descriptive records**, no QC cutoff or exclusion.

Persist these alongside existing E outputs in the existing readiness JSON with observed record counts and SHA-256 fingerprints. Do not modify 111 source, the frozen Phase 4 weights, registries or the previously captured D snapshots. Explicit eligibility, a truly independent QC source, donor-overlap evidence, within-lineage comparability, a one-observation-per-case protocol and an external replication estimand remain unresolved and **biological validation remains unauthorized**.

**Review gate after execution:** assess the kinds of other RNA records (especially normal versus independent tumor samples versus ambiguous ancestry) and the evidence in low-count-tail diagnostics *without retrofitting QC thresholds*. Then specify the prospective inclusion and source QC strategy, lineage-aware case attrition, and donor-independence evidence needed for the scientific cohort freeze. No automatic promotion to eligible or confirmatory analysis is allowed.

### 4F.1 Observed PREFLIGHT-F findings — 2026-10-23

The local execution (`39883d7367aaa12d3ab54e2969e13833e637d270`) recorded **zero Python exceptions** and no source changes to the prepared notebook. Of 52 code cells, **51 retain execution counts**; one persistence-check cell has `execution_count=null` but a saved success message, followed by a numbered readiness-write execution. This anomalous notebook metadata does not imply a failed persistence check but should not be hidden behind a literal 52/52 count claim. The SHA-256-attested E data cache was successfully reloaded, with **zero rereads of 1,082 original STAR payloads**.

**Additional RNA records in the 1,082 structurally simple *primary-candidate* cases:** **544 other source files across 530 cases**, reconciled exactly with E's per-case counts. The frozen 111 file-index sample-type/mapping attributes classify these 544 files as follows:

| Additional RNA source class | Source files | Distinct cases |
|---|---:|---:|
| Resolved normal-tissue sample type | 488 | 486 |
| Resolved recurrent-tumor sample type | 18 | 16 |
| Ambiguous sample ancestry — no sample attribution | 38 | 37 |
| **File total** | **544** | **530 distinct cases in union** |

Category-level distinct-case counts **overlap**, so their sum is not a patient denominator. There were **zero additional resolved primary-tumor records** and zero same-exact-sample/aliquot comparisons relative to the nominated provisional primary in the reused source mapping. The labels are **GDC original sample-type classes**, not evidence that a normal specimen is adjacent normal, that a recurrent specimen comes from the same collection episode, or that an ambiguous file has a valid sample assignment. The existence of any other RNA record does **not** disqualify the primary candidate automatically. The **37** cases with ancillary ancestry ambiguity require explicit sensitivity/provenance interpretation; they do not convert the primary file's uniquely mapped identity into an ambiguous identity or rescue the ambiguous file.

**Lowest-count descriptive diagnostics from existing E cache:** the smallest two unstranded gene-count totals were **1,074,810** and **1,324,757**, both source-classified as uterine adenocarcinoma. **8/20** files in the prespecified lowest-count rank list had the same raw source context, and all 20 retained all 2,389 exact frozen gene IDs (presence not necessarily positive expression). The STAR `N_` special counts are available in these records but should not be presented as independently calibrated read-quality fractions. This file ranking is **not** a threshold or an exclusion set; distributional and lineage sensitivity must be assessed under prospective QC rules, without selecting thresholds based on favored biological findings.

**New persisted (non-frozen) metadata outputs:** `800_preflight_f_other_same_case_rna_files.csv` (**544** rows), `800_preflight_f_single_primary_case_context.csv` (**1,082** rows), `800_preflight_f_source_context_additional_rna_summary.csv` (**18** rows), and `800_preflight_f_low_count_tail_descriptive.csv` (**20** rows). These remain local outputs with paths and fingerprints recorded in `800_preflight_a_readiness.json`; not all source CSVs are committed to GitHub, so full independent payload reinspection requires the locally preserved handoff.

**Verdict: PASS for bounded F metadata/source diagnostics and cost-efficient reproducibility; NO analytic eligibility PASS, no QC-based file exclusion, no donor independence finding.** The remaining scientific gates should be addressed prospectively and separately: independent source/technical RNA-seq QC and normalization; lineage-aware crosswalk and attrition; documented donor overlap; treatment of 288 multi-primary-candidate cases; and a predeclared independent replication estimand and matched null. There is no permission for score projection, sample promotion, program refit, or validation claim at this stage.

## 4G. PREFLIGHT-G — Prospective RNA-seq QC evidence feasibility, WITHOUT QC thresholds

**Entry boundary (F accepted, 2026-10-23):** F reconciled 544 RNA files occurring in 530 cases with one uniquely mapped provisional primary file (488 resolved normal-tissue files, 18 resolved recurrent-tumor files, 38 with ambiguous sample ancestry). Full original E coverage for 2,389/2,389 frozen Ensembl IDs was observed in all 1,082 simple primary candidates, but very low `unstranded` assigned-gene-count totals were present in a small source-context-dependent tail. These observations justify a **technical QC source review**, not empirical cutoff selection or a biological comparison.

**Prospective G question:** what technical RNA-seq measurements can we reproducibly obtain from the existing Notebook 111 + E/F evidence, what do they actually measure, and what independent, comparable library-/alignment-level QC and sample-provenance inputs are needed before any sample-eligibility policy?

Scientific evidence distinctions:

1. **Identity/byte integrity:** Notebook 111 independently checked provider MD5 of the downloaded files and the exact source UUID associations. Evidence: acquired payload identity, *not* RNA sequencing quality or tumor suitability.
2. **Expression-table parseability/feature support:** full E scan found 2,389 exact frozen genes per file, no invalid negative/noninteger/nonfinite `unstranded` count vectors in the 1,082 simple-primary candidate subset. Evidence: schema and count integrity, not confirmation of comparable RNA integrity, fragment distribution, alignment quality or biological score scaling. G reuses the **SHA-256-confirmed E cache** and does **not** repeat 1,082 file reads; the already implemented default `RUN_E_FULL_STAR_RESCAN = False` remains in force.
3. **Assigned gene counts and positive-count gene numbers:** descriptive technical indicators available from E, but their distributions reflect gene assignment, sequencing depth, assay type and biological sample composition. Do not equate `sum(unstranded gene counts)` with input sequencing read depth. G reports min/Q1/median/Q3/max by *source* `primary_site × disease_type` and counts representation in the fixed F lowest-20 descriptive list, without labels of PASS/FAIL, universal technical thresholds, inferential p values or selection of favored lineages.
4. **STAR `N_` special-row tallies:** `N_unmapped`, `N_multimapping`, `N_noFeature`, `N_ambiguous` are preserved as **unstranded-source counts**. They are *not* recombined with assigned-gene counts as a new alignment-rate, deduplication-rate or mapping-rate denominator. The GDC harmonized RNA-seq workflow produces STAR unstranded/stranded raw counts, with separate normalization; GDC does not automatically batch-correct study-specific expression. [GDC mRNA pipeline](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/), [GDC FAQ](https://gdc.cancer.gov/about-gdc/gdc-faqs).
5. **Independent library quality and biological confounding:** uniquely aligned read/fragment mapping, duplication/library complexity, RNA integrity (RIN), gene-body 5′/3′ coverage, rRNA/mitochondrial burden, strand/preparation/batch effects and tumor purity are **not established by the audited E/F source inputs**. The previous D pilot tested source metadata for only 29 of the 649 files with primary multiplicity; absent D fields cannot be generalized to the whole 1,082-file cohort or to all provider endpoints. Mapping/coverage QC require independent documented technical reports or aligned reads, e.g. [RSeQC](https://academic.oup.com/bioinformatics/article/28/16/2184/325191) and [RNA-SeQC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3356847/). Tumor purity and proliferation remain *analysis confounders*, not automatic sample exclusion thresholds.

**Implementation — bounded, read-only G diagnostics:**

- Define an explicit *metric evidence catalogue* with `metric_id`, source, unit/definition, verified scope, evidence class and interpretation limitation. Do not mark any metric as an analytic quality PASS or freeze a threshold.
- Reuse precisely the 1,082 file identities and cached `unstranded` count diagnostics. Cross-check case/sample/aliquot identity and the F case-context handoff. Store a file-level technical feasibility table with count summaries, source context, previously observed other-RNA-file flags and `analytic_eligibility=NOT_FROZEN`.
- Produce source-stratified descriptive distributions and existing fixed lowest-20 membership, with no data-derived cutoff or pan-cancer pooling.
- Inspect `N_` columns solely for availability, valid numeric tallies and observed ranges; explicitly record `rate_denominator_defined=false`, `mapping_rate_estimated=false` and `quality_pass_assigned=false`.
- Construct a prospective list of **required, independently sourced prevalidation gates** (QC provenance and denominators, externally motivated QC criteria, normalization/batch strategy, lineage harmonization, the 288-case multiple-primary policy, CPTAC–TCGA donor independence, and frozen matched-null replication estimand). No `pass_authorized` or sample exclusion status may be set.

**Five new *non-frozen* outputs under `data/interim/metadata/`:**

- `800_preflight_g_qc_metric_evidence.csv` — expected versus actually source-backed RNA QC dimensions.
- `800_preflight_g_rna_file_qc_feasibility.csv` — one row per 1,082 previously scanned provisional simple-primary files; no exclusion or score.
- `800_preflight_g_source_context_qc_distribution.csv` — source-context-level descriptive count distributions and fixed-lowest-20 membership.
- `800_preflight_g_star_n_tally_availability.csv` — raw special-row tally availability and ranges, no denominator-based rates.
- `800_preflight_g_prevalidation_qc_gates.csv` — prospective evidence requirements and current unresolved status.

Persist all five and their hashes in the **existing** `800_preflight_a_readiness.json` alongside the accepted earlier evidence, and preserve `cohort_frozen=false`, `rna_one_record_per_case_selection=NOT_FROZEN`, `biological_validation_authorized=false`, and **zero empirically chosen QC thresholds**.

**Decision gate after local Run All:** determine whether available local evidence suffices for **a technical QC policy** (not merely a valid STAR schema), and which independently sourced QC reports can be obtained efficiently *without reopening all source acquisition*. A decision to acquire missing QC sources must be prospective, evidence-linked and lineage-aware. No biological projection, regression, program refit, or cohort freeze is authorized by G. A provider-wide or 1,082-file QC absence must not be asserted based on the 29-file D pilot.

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
