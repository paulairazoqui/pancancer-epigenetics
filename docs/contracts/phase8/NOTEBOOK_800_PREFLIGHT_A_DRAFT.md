# Notebook 800 — PREFLIGHT-A: external-bulk eligibility and frozen-input readiness

**Document type:** prospective *technical preflight plan* — **DRAFT, NOT FROZEN**  
**Prepared:** 2026-10-22  
**Baseline:** main commit f423d304f6ed3a4187965dcf783879e79abf47b5  
**Primary source candidate:** GDC project CPTAC-3, frozen file universe and acquisition-time metadata from Notebook 111  
**Executable implementation:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb` (PREFLIGHT-A section only)
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

## 4. Notebook 800 PREFLIGHT-A: technical outputs (NOT YET EXECUTED LOCALLY)

The preflight stage is implemented as short, auditable cells inside `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`, following `docs/NOTEBOOK_STYLE_GUIDE.md`, the Notebook 111 acquisition handoff, and frozen Phase 4 registries. It uses existing `Paths`, `calculate_sha256`, `load_artifact_registry`, `get_artifact`, `resolve_artifact_path`, and `load_raw_data_registry` helpers rather than introducing an additional standalone script.

The current implementation reloads/fingerprint-checks the small local Notebook 111 derived audit tables; reports acquisition-file/stratum-level ancestry ambiguity and provisional primary-tumor coverage; leaves a case-by-case file/sample/aliquot inventory without selection; examines exact-string cross-cohort ID collisions without claiming donor independence; and performs one deterministic STAR Counts gene-ID pilot. It **does not** perform full cohort-wide feature compatibility, lineage crosswalk harmonization, donor-provenance review, program scoring, external replication or a frozen cohort selection. These remain subsequent review actions.

Local non-frozen outputs are written under `data/interim/metadata/`:

| Output | Scope |
|---|---|
| `800_preflight_a_candidate_lineage_inventory.csv` | GDC source stratum × modality/platform counts: acquisition files/cases, unresolved files/cases and provisional primary-tumor denominators |
| `800_preflight_a_case_multiplicity.csv` | Exact candidate UUID lists, distinct files/samples/aliquots per provisional primary case and **NOT_FROZEN** selection flag |
| `800_preflight_a_identifier_collisions.csv` | Exact lexical TCGA/CPTAC case and submitter-string collisions; explicit `UNRESOLVED_WITHOUT_EXTERNAL_PROVENANCE` |
| `800_preflight_a_gene_id_pilot.csv` | Frozen 2,389-gene IDs compared to one deterministic STAR Counts pilot, including version-insensitive **diagnostics only** |
| `800_preflight_a_readiness.json` | Upstream/input fingerprints, local candidate counts, output fingerprints, open gates and explicit no-scoring/no-validation status |

These diagnostics are not published to `config/artifact_registry.json` as frozen validation artifacts. No notebook output was executed in GitHub; the GDC source payloads and Notebook 111 interim tables reside on the user's local computer.

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

Next action: execute the **PREFLIGHT-A section of Notebook 800 locally** in the already established Jupyter kernel; review its observed lineage, multiplicity and pilot mapping inventories, then complete donor provenance, lineage mapping and full technical compatibility before freezing the separate Notebook 800 replication contract. No standalone preflight script is part of the approved execution path. Do not merge this draft into a claim of completed preflight/validation merely because the document exists.
