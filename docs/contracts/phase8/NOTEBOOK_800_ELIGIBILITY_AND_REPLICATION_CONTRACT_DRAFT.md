# Notebook 800 — CPTAC-3 External Transcriptomic Replication: Consolidated Analysis Contract

**Status (2026-11-02):** 111–113 source audit and proposed handoff executed; 800 source-acceptance and restored full-E gene-compatibility code awaiting first Run All. External structural-replication design remains open; no program scoring or inferential replication authorized.  
**Phase:** 8 — orthogonal external-cohort evaluation.  
**Upstream source of truth:** executed Notebooks 111–113, including `113_source_provenance_manifest.json`, `113_cohort_readiness.json`, `112_cptac3_qc_provenance_handoff.json` and their pinned source/derived SHA-256 evidence on migration branch `refactor/phase1-cptac3-source-audit-order`. The branch has not been merged into `main`.  
**Analysis unit:** one CPTAC-3 primary RNA transcriptome per independent source case.  
**Scope:** structural evaluation of the three fixed Phase 4 transcriptomic programs; not clinical resistance prediction, causal validation, or therapeutic reversal.

## 1. Scientific question and interpretation

Assess whether the **fixed signed multigene structure** of the three TCGA-derived Phase 4 transcriptomic programs is supported in an externally sourced CPTAC-3 primary-tumor cohort, within harmonized cancer lineages, beyond deterministic score construction and plausible technical or biological confounding.

A computable score, nonzero score variance, correlation of a weighted score with its constituent genes, or association with an unvalidated clinical endpoint is **not** structural replication. An observed external association is not causal evidence, clinical prediction, or validation of drug response. The analysis must distinguish within-lineage structural evidence from between-lineage composition.

## 2. Upstream cohort and resolved source decisions (G2–G6)

Notebook 111 established the GDC source inventory (2,968 STAR Counts RNA files and 2,610 SeSAMe methylation files); Notebook 112 examined the provenance of upstream QC-related fields in a bounded, nonrepresentative 12-file RNA pilot. Notebook 113 owns cohort construction and source-level G2–G6/G8 assessment. Notebook 800 **does not rebuild or reselect** the source cohort.

**G2 — case/file structure.** The primary source-candidate universe is 1,082 cases with a single uniquely mapped primary-tumor STAR file, sample and aliquot. The 288 multiply represented cases (276 multiple-sample; 12 multiple-aliquot) are not part of the primary universe; no outcome-driven replacement or selection is allowed. The 37 otherwise simple cases with additional ambiguous RNA ancestry remain flagged for sensitivity, not automatically excluded. File-level ambiguous ancestry must not be counted as a disjoint patient group.

**G3 — external-cohort provenance.** The accepted source classification is `COHORT_SUPPORTED_EXTERNAL`: audited prospective GDC `CPTAC-3` provenance, no flagged exact TCGA identifier collisions in the reviewed candidate universe, and no conflicting source evidence. PDC study linkage may corroborate but is not mandatory for every case. `SOURCE_REVIEW_REQUIRED` provenance exceptions and `DOCUMENTED_OVERLAP` cases are excluded from the proposed primary cohort. This is **cohort-level support**, not verified donor-level genetic independence. A comprehensive TCGA–CPTAC donor crosswalk or genotype-concordance test has not established zero individual overlap; residual undocumented donor reuse cannot be categorically excluded. The uncertainty must accompany any external-replication claim. New affirmative overlap evidence would require a targeted reassessment; the absence of donor-level certification alone is not a reason to restart G3.

**G4 — source-to-lineage harmonization.** Notebook 113 proposes 721 unique source cases/files in seven accepted TCGA lineages: LUAD 178, LUSC 89, STAD 142, SKCM 138, PAAD 82, UCEC 56, HNSC 36. Source context and accepted lineage remain distinct. The other 361 of the 1,082 candidates are not proposed: 351 with unresolved subtype mapping, four with no accepted lineage mapping, and six PAAD source-provenance exceptions. These exclusions describe the proposed source cohort, **not** a final inferentially evaluable set.

**G5 — QC evidence boundary.** Source file integrity, identity and gene coverage are established to the extent documented in 111–113; independent, comparable read/library-level sequencing QC is **not** established across the proposed cohort. The 112 pilot supports source-field linkage and metadata agreement, not general QC PASS. Missing or incomparable QC must be described as `QC_UNASSESSED`, not silently converted to PASS or FAIL. Do not invent read-quality thresholds, infer mapping rates from STAR `N_*` fields, or claim a QC-screened external cohort.

**G6 — source count compatibility.** For the 721 proposed files, Notebook 113 reports compatible raw unstranded counts, unique version-normalized Ensembl IDs, nonnegative integer counts and presence of all 2,389 frozen Phase 4 genes. This is input availability, not proof of cross-platform numeric calibration. Three program loading vectors, ordered gene identities and signs remain fixed. **Distinct original E full-source scope:** 800 additionally reconstructs exact *versioned* gene-ID presence and detection across *all 1,082* G2 simple-source files against the 2,389 frozen reference genes. A 721-file versionless G6 result must never be substituted for this full-source E audit.

**Source status:** 721 is a **proposed** cohort, not a registered/frozen inferential sample. No biological analysis is authorized by the upstream source handoff alone.

## 3. Required 113 → 800 acceptance check

Before any program projection, verify the actual local `113_source_provenance_manifest.json`, `113_cohort_readiness.json`, and proposed membership file against their recorded SHA-256 values; reconcile exact unique case/file identities, all 721 rows, seven lineage counts, exclusion/status labels and one-case-one-primary-file constraint. Verify frozen Phase 4 feature order and loading identities against the authoritative registry. Missing local files, fingerprint mismatch, duplicate case/file identities or contradictory eligibility states mean `HANDOFF_NOT_ACCEPTED` until corrected at source. Do not substitute reconstructed or newly fetched 800 membership.

Report cohort attrition from 1,082 to 721 by source context and harmonized lineage, including the 37-case sensitivity flag and the separate 288-case multiplicity boundary. Acceptance is a reproducibility/identity check, not a claim of donor-level certification or QC PASS.

## 4. G6 — analytical normalization and projection specification (decision pending)

The primary input is the GDC STAR Counts **unstranded raw-count** representation selected by 113, with the exact frozen ordered 2,389-gene intersection and signed Phase 4 loadings. No gene-symbol substitution, missing-gene zero imputation, feature reselection, sign inversion, loading refit or joint TCGA–CPTAC standardization.

The analytical implementation must document and verify the TCGA reference's executed normalization and program-scoring definitions (including TMM/logCPM and within-system standardization in Notebook 401) against frozen artifacts. For CPTAC-3, use a separately fitted, deterministic normalization based on its raw counts, without using TCGA+CPTAC jointly to estimate scale parameters and without tuning choices to improve concordance. Keep normalization feature-universe and zero-count handling explicit and compatible with the frozen feature set. Absolute TCGA score thresholds are **not transferable by assumption**.

**Before scoring, choose and document**: (a) the exact normalization universe, filtering and TMM/logCPM implementation; (b) how each frozen loading vector is projected after within-cohort gene scaling or a justified reference-anchored alternative; (c) treatment of zero-variance features; (d) a bounded, non-outcome-tuned normalization sensitivity. These choices must be evaluated for technical validity, not optimized for a positive G7 result. If a required transformation cannot be justified, mark the relevant comparison `NOT_EVALUABLE_INPUT_COMPATIBILITY`.

## 5. G7 — structural replication design (proposed; inferential specification not yet frozen)

**Primary estimand.** Within each eligible harmonized lineage and each of the **three** fixed programs, estimate concordance between projections derived from two **disjoint sets of frozen program genes**, relative to a prespecified matched negative-control distribution. The target is external cross-patient coherence of nonoverlapping gene blocks, **not** correlation between a full score and its own genes.

**Gene-block construction.** Construct the partition from frozen TCGA reference information and fixed loadings only, without inspecting CPTAC program outcomes. Maintain disjointness; balance signed loading contributions and reference expression/detectability as feasible. If repeated partitions are used, their deterministic seeds, number and aggregation rule must be fixed before external analysis. Do not discard unfavorable partitions after inspection.

**Statistic and null.** For each program × lineage, compute a declared rank-based or otherwise robust concordance statistic between independently projected blocks across unique cases. Compare it with a **matched** control family that preserves relevant gene-level reference expression/detectability, loading-sign and weight-magnitude characteristics and the same patient/lineage structure. Unmatched random-gene controls alone are insufficient. Null construction must avoid leakage from CPTAC outcomes and avoid reusing program genes in ways that make the control tautological. Specify the exact statistic, control matching algorithm, number of draws, test tail and effect-size definition before calculation.

**Confounding caveat.** Disjoint-gene concordance can reflect proliferation, purity, immune/stromal admixture, lineage composition or shared technical factors. Exceeding a matched null is **supportive structural evidence**, not proof of a unique epigenetic program or biological mechanism. Require within-lineage analysis; report whether relevant adjustments/sensitivities are identifiable.

**Uncertainty and multiplicity.** Treat cases as independent units only to the extent supported by source evidence; use a declared case-level uncertainty estimator. The primary inferential family covers all three programs across all lineages deemed evaluable by outcome-blind criteria. Fix multiplicity correction and the decision rule before examining CPTAC statistics. Report all attempted tests, effect sizes, uncertainty and negative results; do not select only successful programs or lineages. Any cross-lineage synthesis must be explicitly stratified/hierarchical and cannot replace lineage-specific results.

**Remaining decisions required to freeze G7:** exact partition algorithm and repetitions; primary statistic; matched-null algorithm and draw count; uncertainty method; multiplicity procedure and evidence threshold; definition of insufficient support; whether and how a TCGA-reference comparison is used. These are **open design choices**, not assumed historical obligations. Final choices require a brief methodological justification and should not be chosen from observed CPTAC replication performance.

## 6. G8 — confounding, identifiability and support (decision pending)

Notebook 113 documents limited source availability of collection center, library-preparation, batch and tumor-purity metadata. Do not imply that these variables are available or that their absence is innocuous.

For each proposed lineage, record: unique-case sample size; input missingness; source technical/workflow homogeneity where verifiable; available purity, immune/stromal and proliferation proxies; and whether any planned adjustment is statistically identifiable. Prefer within-lineage estimates. If batch and lineage are inseparable, do not fit an unidentifiable batch correction or interpret pooled differences as program-specific biology.

**Before analysis, define**: minimum evaluability based on effective sample size and variance/identifiability (with justification rather than arbitrary universal cutoffs); the set of feasible adjustment or sensitivity covariates; handling of unavailable purity/batch variables; and explicit `NOT_EVALUABLE` criteria. Proliferation and composition effects must be discussed even where measured covariates are unavailable. No outcome-driven lineage exclusion, covariate selection or normalization rescue.

## 7. Analysis boundary and reporting

The primary analysis is **lineage-aware external structural assessment** of fixed transcriptomic programs. The following are distinct and not substitutes for G7: source eligibility; file integrity; QC-field availability; gene presence; within-cohort score distributions; methylation context; perturbational signatures; and clinical drug resistance.

The final report must include: verified input/registry identifiers; cohort denominators and attrition; G3 cohort-level externality with residual donor uncertainty; G5 QC limitation; G6 exact transformation; G7 complete test family and matched controls; G8 confounder feasibility; lineage-specific positive, negative and non-evaluable findings; and clearly separated exploratory analyses. Do not claim clinical prediction, donor-certified independence, causality or therapeutic reversal.

**Readiness decision:** `SOURCE_COHORT_PROPOSED`; `G3_COHORT_SUPPORTED_WITH_RESIDUAL_UNCERTAINTY`; `G4_SOURCE_MAPPING_AVAILABLE`; `G5_QC_NOT_CERTIFIED`; `G6_SOURCE_COUNTS_COMPATIBLE_ANALYTICAL_TRANSFORM_OPEN`; `G7_DESIGN_OPEN`; `G8_ANALYTICAL_POLICY_OPEN`; `EXTERNAL_INFERENCE_NOT_AUTHORIZED`.

**Next step:** complete the bounded G6/G7/G8 design decisions and verify the local 113 handoff. Only then approve or decline a clearly scoped analysis; do not extend acquisition preflights or reconstruct Notebook 113.


## Addendum — 2026-11-02 full-source historical PREFLIGHT-E preservation

The original Notebook 800, prior to the 111→112→113→800 reorganization, included a feature-compatibility audit over **1,082 structurally simple provisional-primary STAR Count files** (not only the 721 proposed downstream sources). The executed October 2026 baseline was: **2,389/2,389 exact frozen Ensembl IDs present in each of 1,082/1,082 files**; zero exact missing IDs, zero versionless-only rescue events, zero invalid unstranded vectors; complete feature presence across 1,082/1,082 files for every frozen feature. This result was an **input-compatibility observation, not independent sequencing QC**.

The prior E/F source-only case structure, 1,082 STAR count diagnostics and provider-origin QC metadata now live in Notebook 112; the B/C/D multiplicity investigations live in Notebook 113. The restored 800 E block therefore consumes the fingerprinted **112 full source technical inventory**, the **113 1,082-case G2 ledger and handoff manifest**, and the **Phase 4 frozen exact gene universe**. It verifies sample/file/aliquot identities before evaluating the original version-sensitive gene-set intersection, versionless-only diagnostic and frozen-gene detection per case, plus per-gene exact presence across all 1,082 files. It checks those results against the 112 source-count readouts and the original E baseline, with no new eligibility decision or reclassification.

**First-run acquisition:** Unlike the 18-cell metadata-only baseline of Notebook 800, the restored E logic scans the local 1,082 STAR Count files once if the new cache is absent. This is local regeneration of a derived dataset, **not** a GDC/PDC re-download. It reads only `gene_id` and `unstranded`, verifies file size against 113's frozen source identity, does not repeat provider MD5 nor create independent sequencing QC. There is **no dependency on the obsolete `800_preflight_a_readiness.json` or archived E CSVs**. On successful source-count/identity reconciliation, 800 stores the regenerated per-file exact-feature diagnostics, per-gene exact coverage and a SHA-256 manifest under gitignored `data/interim/metadata/` (the filenames start `800_cptac3_e_exact_`). Those derived files are **not Git evidence snapshots**. Subsequent runs reuse the cache only if the SHA-256 fingerprints of 112 technical input/handoff, 113 manifest/ledger, original 111 primary source index and Phase 4 reference still agree. Missing partial or modified cached outputs must stop, not silently produce favorable results. Explicit opt-in (`E_REBUILD_FULL_STAR_AUDIT = True`) allows re-evaluation.

**Acceptance:** reproduce the 1,082/1,082 × 2,389/2,389 exact-ID coverage and all original 112 readout agreements; preserve the 721 proposed case/file/lineage membership and seven source lineages without modifying 113; retain `cohort_frozen=False`, `external_analysis_authorized=False`, no normalization/scoring, no inferential statistics and no clinical/causal conclusions. The 800 acceptance JSON must fingerprint the full-source E manifest and distinguish source feature compatibility from the 721-file G6 intersection. All 800 results must be produced by a local `Run All` before this addendum can be marked executed.

**Caveat:** the exact 2,389-gene presence does not establish transcriptome-wide completeness, cross-platform calibration, cohort biological independence, read quality or stable program behavior. E result coverage is only one prerequisite for later predeclared G6 normalization and G7 structural tests.
