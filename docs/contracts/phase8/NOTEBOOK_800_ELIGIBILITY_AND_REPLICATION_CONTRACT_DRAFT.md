# Notebook 800 — External Bulk Cohort Eligibility and Replication: Consolidated Decision Contract

**Lifecycle:** CONSOLIDATED DRAFT — **G2 CANDIDATE-UNIVERSE POLICY APPROVED 2026-10-23; ANALYSIS CONTRACT AND COHORT NOT FROZEN; NO INFERENTIAL ANALYSIS AUTHORIZED**  
**Created:** 2026-10-23, following PREFLIGHT-A–H and the independently scoped Phase 1 Notebook 112 source-provenance pilot  
**Working branch:** `notebook-800-preflight-a`  
**Baseline Phase 8 checkpoint:** `a78ed5911c984bdb10c26d91fdeb6a04b51c88ff`  
**Existing audit:** `docs/contracts/phase8/NOTEBOOK_800_PREFLIGHT_A_DRAFT.md` (historical evidence and executed preflights, not rewritten into a retrospectively frozen analysis contract)  
**Related Phase 1 audit:** Notebook 111 and Notebook 112, with 112 contained in a separate clean Phase 1 PR (#56, draft at time of drafting)

## 1. Decision to stop expanding Notebook 800's acquisition preflights

**Freeze the A–H evidence *as historical observations*, not as an analytically eligible cohort.** The implementation notebook has already become extensive; it must not be used to conduct open-ended new GDC acquisition or QC-source discovery. Provider metadata provenance, revisions of source manifests and any technically necessary additional acquisition belong in Phase 1 and require a separately defined and reviewed handoff.

The next work in Notebook 800 must be: (i) prospectively commit an explicit patient/file eligibility rule; (ii) audit TCGA–CPTAC donor independence and map genuine comparable lineages; (iii) settle assay-appropriate normalization, quality and confounder gates; (iv) prespecify a meaningful structural replication estimand and negative controls; (v) *only then* execute the analytical evaluation or report non-evaluability.

**Do not add PREFLIGHT-I, rerun 111/112, query GDC from 800, alter frozen Phase 2–7 programs or launch program-scoring cells in the current draft stage.** Historical intermediate outputs remain local and source-fingerprinted. A refactor/auxiliary notebook could be considered later, but it must preserve the executed source and outputs and be reviewed separately from scientific hypothesis testing.

## 2. Exactly what has already been established

These are *observations*, not a selected cohort or claims of external biological replication:

| Evidence | Observed status and scope | Permitted use |
|---|---|---|
| Notebook 111 source acquisition | 2,968 CPTAC-3 STAR Counts files and 2,610 SeSAMe methylation files, all 5,578 locally audited for identity, size and provider MD5 | Reuse technical integrity without rescanning ~67 GiB |
| Sample ancestry from 111 | 314 RNA and 315 methylation files have ambiguous sample ancestry despite direct aliquot identity | Retain unresolved status, no arbitrary sample parent |
| Initial RNA primary candidate inventory | 1,370 provisional primary RNA cases: 1,082 one-file/one-sample/one-aliquot cases and 288 cases with within-case primary RNA multiplicity (649 files) | Descriptive denominators only; **not** a finalized analytic sample |
| Notebook 800 PREFLIGHT-E | 1,082 technically simple primary-candidate STAR Counts files scanned; all 2,389 exact frozen Ensembl genes represented (cached checksum-verified readout) | Structural gene-ID availability only; not read quality, normalization or sample inclusion |
| Notebook 800 PREFLIGHT-G | Source count/STAR-N fields and low-count-tail availability audited | Technical descriptive quantities; do **not** compute pseudo-mapping fractions or retroactively pick a cutoff |
| Notebook 800 PREFLIGHT-H | Twelve selected STAR output files (three each from four GDC source contexts) linked to twelve workflow input-file metadata nodes; six quantitative fields populated for 12/12 | Bounded *availability* result, not population QC rate |
| Notebook 112 Phase 1 pilot | 12/12 direct input-file records matched the exact STAR-output **case + aliquot**; 72/72 GDC-projection field pairs agreed; eight code cells executed without errors | Audited provider *provenance consistency*. Two GDC projections are not independent QC measurement |
| Frozen Phase 4 | Three consensus transcriptomic programs, 2,389 ordered shared genes and three signed loading vectors; Notebook 401 standardized expression and scores **within each biological system** | Fix immutable feature/sign/weight identities. Do not assume numeric tumor scores are a transferable absolute scale |

**112 dependency caveat:** Its pilot is audited on a separate clean Phase 1 branch; PR #56 is still draft pending a reproducibility/merged-dependency resolution. The 112 JSON/CSV outputs are **local, unregistered Phase 1 interim evidence**, and do not automatically become a frozen artifact in 800 or `main`. A future accepted handoff must be SHA-256 verified before consumption.

**Critical evidence distinction:** exact file/aliquot lineage and six populated *provider* fields do not establish comparable independent sequencing quality, the relevant read/fragment denominators, or a QC pass/fail classification. No 1,082-file live GDC QC sweep has been performed, and no expansion is authorized by the successful 12-file pilot.

## 3. Binding safeguards that do not depend on further data

The following constraints are already imposed by the approved project architecture and frozen upstream results, and must survive the eventual 800 freeze:

1. **Independence:** an external cohort must be independent at the biological donor level, not merely have a different GDC UUID or project label. TCGA is the discovery system; it is never external validation.
2. **Analytical unit:** one independent patient/donor contributes at most one primary RNA transcriptome. Repeated STAR files, aliquots and samples cannot be independent replications. Preserve the unselected complete inventory.
3. **Immutable representation:** no relearning program weights, changing sign/orientation, selecting frozen genes anew, score-driven QC, lineage-driven hypothesis rescue, or use of Phase 5–7 evidence to choose which of the three Phase 4 axes can be called replicated.
4. **Role separation:** acquisition QA (111/112) ≠ sample/library technical QC ≠ 800 eligibility ≠ external structural replication. A missing quality field is neither a failed assay nor a license to infer it passed.
5. **Lineage and assay discipline:** preserve source `primary_site × disease_type` labels separately from validated TCGA disease/project crosswalk. No naive pan-cancer pooling, random pan-cancer splits, joint TCGA–CPTAC feature standardization, uncontrolled batch correction, or pooling methylation EPIC and EPIC v2.
6. **No circular success criterion:** nonzero variance, a computable weighted projection or correlation of a program score with its constituent genes **cannot** establish replication, because the score is constructed from those genes.
7. **Negative outcomes are acceptable:** absence of eligible independent donors, insufficient evaluable lineages, inadequate QC comparability, failed structural tests and confounding are reportable conclusions rather than opportunities for post hoc rescue.

## 4. Technical eligibility — candidate policy awaiting freeze

### 4.1 Source-to-patient identity and primary analysis universe

**G2 candidate-universe policy APPROVED on 2026-10-23 (before CPTAC program-scoring or replication analyses).** The **1,082 structurally simple, uniquely mapped provisional-primary RNA cases** from A–H are designated the *initial primary-candidate universe*, **not** an eligible, donor-independent, QC-passed or frozen analysis cohort. This policy uses only audited source metadata, not the biological outcome. All 1,082 still pass through independent donor identity (G3), lineage mapping (G4), technical QC/input compatibility (G5–G6) and the prospectively frozen inferential design (G7–G8). Their final count may decrease; the remaining patients must not be replaced with multiplicity cases post hoc to improve results.

**G2 multiplicity policy APPROVED:** the separate **288 cases with more than one provisional-primary RNA file (649 files)** are **outside the primary-candidate universe**, pending a distinct, preregistered, outcome-blind evaluation for possible *secondary/sensitivity* use. These comprise **276 multiple-sample cases (619 files)** and **12 cases with multiple aliquots of one sample (30 files)**. None has a presently approved preferred file or single-specimen rule. Reproducibility of a secondary use requires independent provenance, a justified file-selection/aggregation rule, a frozen case/file ID list and lineage-stratified attrition *before* examining CPTAC program outcomes. Never treat multiple source files as independent donors, silently select the largest or highest-count file, or rescue a negative primary result using this set. Missing specimen collection chronology, tumor region, assay comparability or source QA remain `UNRESOLVED_MULTIPLICITY` rather than guessed.

**Full source-denominator accounting is compulsory.** Keep the initial **1,370 provisional-primary cases / 1,731 files**, the **1,082 simple cases / 1,082 primary files**, the **288 multiply represented cases / 649 primary files**, and the separate **314 RNA source files with ambiguous sample ancestry** visible in a non-overlapping *file-level* reconciliation. An ambiguous source file can coexist in the same *case* as a uniquely mapped candidate; these file and case counts must **not** be added as disjoint case groups. Do not convert 1,082/1,370 (79.0%) into a QC pass rate or donor-independence rate.

**Same-case additional RNA files are not automatic exclusion evidence.** Among the 1,082 simple primary candidates, **530 cases** have other RNA source files from Notebook 111 (**544 additional files**: 488 resolved normal-tissue, 18 resolved recurrent-tumor and 38 ancestry-ambiguous source files). The additional ambiguous records occur in **37 of the 1,082 cases**; do **not** reinterpret them as additional confirmed primary samples or as a defect of the uniquely linked primary file. These 37 remain **flagged**. A sensitivity *proposed for the final prospective freeze* would repeat the eligible analysis after excluding flagged patients, if relevant; its final inclusion, reference denominator, thresholds and estimand are not approved by the current G2 vote. The sensitivity would not redefine the primary result.

**Outcome-blind G2 source identity gate:** the candidate STAR output must belong to the fixed 111 file universe, match original UUID/name/size/provider MD5, have exactly one direct case+aliquot association, one uniquely resolved sample UUID, and source `sample_type == Primary Tumor`. Case-level sample expansions and agreements of sample-type labels do not rescue ambiguous ancestry. This is *technical identity and sample-type candidacy*, not sequencing QC.

**Mandatory lineage-dependent attrition controls:** preserve the unharmonized GDC `primary_site × disease_type` source strata for initial G2 comparison; later use the explicitly validated G4 lineage crosswalk without pretending the source labels were TCGA lineages. Report each stratum's starting cases/files, simple cases/files, multiplicity subtype/cases/files, simple-case retention with a clear denominator, additional-source-file flags and final losses at each G3–G8 gate. Do not generalize simple-case results to a source stratum with strong multiplicity-dependent attrition. Examples observed in 800-E: `Uterus, NOS × Adenomas and Adenocarcinomas` 56/235 simple cases (23.8%); `Kidney × Adenomas and Adenocarcinomas` 192/232 (82.8%); `Bronchus and lung × Adenomas and Adenocarcinomas` 178/178 (100%); `Pancreas × Ductal and Lobular Neoplasms` 88/100 (88.0%); and `Larynx × Squamous Cell Neoplasms` 18/37 (48.6%). These are **source-label structural retention**, not QC, independent-donor or final lineage-association results.

**G2 closing boundary:** candidate eligibility **policy approved** and retrospective source counts already audited; *no new cohort membership artifact, clinical donor independence, technical-quality eligibility, lineage harmonization, statistical test or score* is frozen by this approval. G3 and G4 remain **HARD BLOCKERS**. Implementing case-level status tables is a later, non-biological metadata handoff after the policy and its G3/G4 linkage fields are reviewed; do not append another unbounded acquisition preflight to the executed 800 notebook.

### 4.2 TCGA–CPTAC donor independence — **HARD BLOCKER**

Use the frozen `phase2.203.final_sample_mapping` from the Phase 4/TCGA reference side and the exact CPTAC-3 case/sample/aliquot/submitter identifiers from 111. Reconcile case UUIDs, submitter identifiers, project-specific source identifiers, clinical project documentation/crosswalks and possible contributions or remapping between CPTAC and TCGA. The completed exact-string collision screen in A is **insufficient** to certify different donors.

Output one explicit identity class **per CPTAC candidate case**: `DOCUMENTED_INDEPENDENT`, `DOCUMENTED_OVERLAP`, or `UNRESOLVED_INDEPENDENCE` with the exact provenance and method of adjudication. Source cohort labels alone do not prove independence. Exclude documented overlaps from an independent-donor primary test. Treat unresolved donor identity as **non-confirmatory** unless a prospectively defended independence standard is met; never call it an independent patient validation set by default.

If no analytically usable donor-independent primary cohort remains, **STOP confirmatory external replication** and publish an auditable non-evaluability finding. Do not use presumed non-overlap as a fallback.

### 4.3 Source lineage crosswalk and confounder feasibility

Create an explicit, auditable mapping from GDC `primary_site × disease_type × project` to the frozen TCGA lineage/project categories. Mapping needs source documentation or unambiguous disease ontology, not lexical similarity or a model trained on validation outcomes. Mark `UNMAPPED`, `AMBIGUOUS` and `CONTRADICTORY` groups rather than assigning them opportunistically.

Report denominator-aware attrition **per source stratum and mapped lineage** through each gate (original 2,968 RNA files; uniquely mapped source files; provisional primary files/cases; 1,082 candidate-simple cases; independent donors; QC-compatible samples; gene-coverage-eligible samples; final analytic set). Maintain distinct `file_id`, `sample_uuid`, `aliquot_uuid` and `case_uuid` counts.

Audit library/STAR workflow/version, batch, RNA input metadata availability, source purity (if available), stromal/immune composition and proliferation confounders. Missing purity/batch/proliferation values must be explicit. Do not infer purity from a program score as a retrospective adjustment, and do not regress out biological lineage when fully confounded with technical batch. If lineage and batch cannot be separated, mark that comparison **technically non-identifiable**.

### 4.4 QC acceptability and coverage — **NOT FROZEN**

111's raw MD5 PASS and E's gene-ID coverage PASS do not certify sequencing or biological sample quality. 112 provides source-provenance support in twelve selected files only. Any candidate use of GDC `total_reads`, `proportion_reads_mapped`, `proportion_reads_duplicated`, `average_base_quality`, `average_read_length`, or `average_insert_size` in sample inclusion requires, **before applying thresholds**, documented calculation software/version, measurement level (read vs pair/fragment), denominator, file/library provenance, applicable data type/workflow, missingness pattern and comparability across mapped lineages.

Do **not** use STAR `N_*` unassigned counters as an independently valid mapping fraction. Do not designate a low-count-tail quantile or project-relative percentile as a quality failure on the basis of observed distribution alone. Missing QC is recorded as **QC_UNASSESSED**, not **QC_PASS** or **QC_FAIL**.

If suitable independently interpretable QC cannot be recovered, a confirmatory claim requiring verified sample quality is **blocked**. It may still be defensible to report a clearly labeled structural technical/feasibility analysis with auditable missingness, provided its narrower claim and eligibility conditions are decided prospectively. That is **not** a permission to declare the initial cohort QC-passed.

A full extraction of new provider QC fields, if later scientifically justified, is a **separate Phase 1 acquisition decision**, not an automatic 800 run. No source-wide API expansion is authorized by this document.

### 4.5 Transcriptome compatibility and normalization — **NOT FROZEN**

PREFLIGHT-E proved that all **2,389 exact frozen feature IDs** are present in the 1,082 inspected STAR files, not that external RNA measurements are normalized comparably. Resolve these questions before any score:

- **Exact feature identity:** require the frozen Phase 4 ordered gene reference and three 2,389-element signed weights; reject ambiguous/non-unique transformations, silent version stripping, unapproved symbol replacement and missing-gene zero imputation.
- **Count identity and processing:** identify the correct GDC unstranded raw count column and audit STAR workflow/annotation versions against the executed Phase 2 RNA path.
- **Normalization:** reproduce the relevant TCGA reference's executed unstranded-count → TMM/logCPM workflow from frozen material where necessary, then specify *separate* CPTAC normalization, library composition strategy and any batch adjustments **without joint fitting on TCGA plus CPTAC**. No tuning to maximize program agreement.
- **Score calibration:** Notebook 401 calculates gene z-scores and then score z-scores *within system*. Hence a directly projected CPTAC score may be useful as an internal descriptive quantity, but published TCGA numeric scores are **not an absolute transferable threshold**. A reference-anchored projection would require a separate technically validated and frozen transformation. Never quietly conflate these.
- **Gene filtering:** the denominator for normalization and decisions about low-count genes must not remove/reweight frozen program features after observing replication behavior. Any feature-universe/zero-variance handling must be defined for the exact input representation before scores.
- **Assessment:** reproducibility tests must distinguish effects of technical normalization, compositional artifacts, batch and actual shared multigene structure. Technical sensitivity options, if any, must be chosen before results.

If compatible preparation of a lineage/assay group cannot be specified, it remains `NOT_EVALUABLE_INPUT_COMPATIBILITY` rather than rescaled by an exploratory rescue.

## 5. Replication question and provisional estimand — **MUST BE FROZEN BEFORE ANY CPTAC PROGRAM TEST**

**Scientific question:** do the *frozen signed Phase 4 transcriptomic programs* exhibit reproducible multigene organization in eligible **biologically independent CPTAC-3 primary tumors**, beyond construction tautologies, generic correlated expression, lineage composition and technical confounding?

### 5.1 Why a projected score alone is insufficient

Each score is a deterministic weighted sum of its constituent genes. A high score, large dynamic range, correlation with the same weighted genes, or exploratory `top genes` enrichment **cannot** validate the same program. A tumor-derived program was constructed using TCGA; a test must ask whether a prespecified part of its structure is independently recoverable in CPTAC-3 *and* exceeds appropriate negative controls, with TCGA acting only as a frozen reference.

### 5.2 Proposed, not yet frozen primary structural analysis

A **candidate design** for review is a *signed gene-disjoint concordance assessment*: partition the frozen nonzero gene-weight vector for each of the **three prespecified programs** into two nonoverlapping gene subsets via a fixed, reference-only strategy balancing sign, weight magnitude and reference detectability (using **TCGA only**, never CPTAC results). Project each subset separately into the same *eligible* external patients under a frozen, non-outcome-tuned normalization rule. Assess cross-patient concordance between independently constructed gene-subset projections **within each harmonized lineage**; compare to the same prespecified reconstruction in the frozen TCGA reference.

Because both subset projections may share lineage, proliferation, purity, compositional and technical drivers, **positive concordance is not intrinsically evidence of unique program replication**. Predefine a matched negative-control family (for example, frozen reference-derived, signed-weight matched assignments with comparable expression level, variability and technical detectability, preserving the same patient and lineage structure) and quantify whether *observed out-of-subset concordance exceeds this null*. Do not use simple random genes that fail to match plausible confounding or signed-weight structure. Internal reference concordance does not by itself establish external independence.

**Open implementation choices requiring prospective freeze:** exact disjoint split construction and number of deterministic repetitions; treatment of near-zero and duplicated loading weights; reference-only matching bins; null-generation algorithm and number of permutations; uncertainty estimator and case-level resampling; correlation vs more robust dependence statistic; covariate adjustment/stratification when identifiable; treatment of sign and direction; primary evidence threshold and multiplicity family. No fabricated numerical cutoff, `n` floor or p-value rule is imposed in this draft.

Possible secondary checks (clearly exploratory unless independently prespecified) include program-score covariance geometry across matched lineages, rank concordance of held-out *independent* gene blocks and robustness to prespecified normalization variants. None may retroactively rescue a negative primary endpoint. Methylation contextual association is **not** a substitute for RNA multigene structural replication.

### 5.3 Lineage-aware evaluation and inferential family

The complete candidate lineage universe, source-to-TCGA crosswalk, eligibility/attrition rule and minimum identifiability requirements must be frozen **before computing CPTAC program projections or inferential test statistics**. Report lineages separately. Any cross-lineage synthesis must use explicitly stated hierarchical/stratified weighting and cannot pool cases naively or hide failures in smaller lineages.

All three frozen programs must enter the prospective primary inferential family, whether their evidence is positive, negative or not evaluable. Multiplicity correction, uncertainty intervals, null family, attempted tests and precommitted `NOT_EVALUABLE` labels must be recorded. If a lineage is underpowered or lacks effective case-level independence, report `INSUFFICIENT_SUPPORT` without post hoc borrowing from other lineages.

**Interpretation ceiling:** a successful analysis could support *cross-dataset recurrence of a candidate transcriptomic program under specified lineages and assumptions*. It cannot demonstrate a causal epigenetic mechanism, longitudinal adaptive resistance, clinical prediction, therapeutic reversibility or independent methylation validation.

## 6. Required outputs and review checkpoints (names provisional)

Keep the execution layer compact. Prefer consuming frozen/handoff tables and a separate vetted implementation helper if this reduces notebook complexity without obscuring decisions. The existing A–H notebook remains an audit record; any migration is a separate preservation-reviewed refactor.

| Proposed artifact | Minimum fields / contract |
|---|---|
| `800_input_provenance_and_decision_manifest.json` | Exact frozen 111, 112, Phase 4 and TCGA source identifiers/hashes; readiness status, policy version, environment, no hidden GDC query |
| `800_case_eligibility_audit.csv` | One row per audited case, all source and final identifiers, missingness, case-level flags, multiplicity reason, independent donor class and evidence |
| `800_eligibility_attrition_by_lineage.csv` | Denominator conservation by source context and TCGA lineage; distinct files/aliquots/samples/cases and reasons for loss |
| `800_gene_feature_compatibility.csv` | Frozen gene IDs, uniqueness, count/workflow compatibility, missing/excluded feature causes |
| `800_normalization_reference_contract.json` | TCGA reference and CPTAC transformation specification, scope of fit, batch conditions, frozen parameters and reproducibility checks |
| `800_external_replication_design.json` | Prospective 3-program × lineage test universe, estimand, gene disjointness, nulls, seeds, confounders, multiplicity and no-rescue decisions |
| `800_external_structural_replication_results.csv` | Only **after authorization**: per-program/per-lineage estimates, null comparisons, uncertainty, FDR/correction, N independent cases, negative/not-evaluable classes |
| `800_external_replication_readiness.json` | Machine-readable gating: `cohort_frozen`, `donor_independence_evidence_adequate`, `normalization_frozen`, `external_analysis_authorized`, method and SHA-256 audit trail |

No output should be registered as external validation/biological replication evidence while any hard gate remains unresolved. Proposal-only outputs remain in `data/interim/`; finalized, reviewed results may move to `data/processed/validation/` and `config/artifact_registry.json` only under the repository's freeze/review policy. Never overwrite registered source data.

## 7. Explicit decision register and readiness matrix

The following are **current statuses, not commitments that all gates will eventually pass**.

| Gate | Required resolution | Current evidence | Status at draft | Authority for next decision |
|---|---|---|---|---|
| G0 | 111 source integrity and frozen Phase 4 identity | Audited PASS | PASS (reuse) | Reverify fingerprints on consumption |
| G1 | 112 technical upstream source identity | 12/12 direct input case+aliquot matches, 72/72 provider values reconciled | PILOT PASS; handoff merge/reproduction unresolved | Phase 1 integration / explicit SHA handoff |
| G2 | One primary-candidate RNA file per CPTAC case, with separate multiplicity sensitivity and explicit source/lineage attrition | 1,082 simple primary-candidate cases; 288 multiplicity cases/649 files; 314 ancestry-ambiguous RNA files (file-level; may coexist in cases) | **CANDIDATE-UNIVERSE POLICY APPROVED 2026-10-23; CASE/COHORT ELIGIBILITY NOT FROZEN** | Implement source identity statuses after G3/G4 metadata decisions; preserve all denominators |
| G3 | Independence from frozen TCGA donor cohort | Lexical identifiers screened, not independently reconciled | **BLOCKED** | Independent provenance and donor crosswalk |
| G4 | GDC source-to-TCGA lineage map, source attrition | Source labels available, no validated mapping | **BLOCKED** | Frozen clinical/disease mapping and audit |
| G5 | Comparable per-sample QC definitions and coverage | 12-file source pilot; no QC threshold/denominator validation | **BLOCKED** | Phase 1 QC applicability / missingness review |
| G6 | Exact-gene input transformation and reference scaling | 2,389/2,389 exact presence in 1,082 files; 401 within-system scaling documented | **BLOCKED** | Freeze count, normalization and projection spec |
| G7 | Program-independent structural estimand, nulls and inference | Candidate disjoint-gene/TCGA-reference strategy only | **BLOCKED** | Freeze test family and controls |
| G8 | Confounders, batch identifiability and lineage support | Source groups described, no completed comprehensive review | **BLOCKED** | Freeze support/exclusion and sensitivity policy |
| G9 | Reproducible artifact/registry and publication boundary | Local preflight snapshots/hashes, registry proposal | OPEN | Reviewed handoff and registry transaction |

**Hard stop:** G3, G4, G5/G6 and G7/G8 must be affirmatively resolved *before* any confirmatory CPTAC program score/test. Data and source fingerprints alone cannot waive these gates. A defensible final outcome may be `NOT_EVALUABLE` if any indispensable source-identity, technical or reference condition cannot be resolved.

**No hidden next preflight:** complete these as a **single consolidated decision review**, not another succession of metadata pilots. Where an independent Phase 1 upstream fix is indispensable, scope and authorize it separately. Once source/eligibility gates pass, freeze a **new version of this contract prospectively** before results are inspected; keep this version as the initial draft. If they cannot pass, document a reproducible non-evaluability closure for 800.

## 8. Immediate work sequence — without running the biological analysis

1. **Preserve** Notebook 800's A–H executed outputs, and verify that the externally isolated Notebook 112 handoff is reproducibly accessible (do not merge PR #56 merely to make the analysis proceed).
2. **G2 policy approved; now resolve G3 and G4 jointly.** Preserve the 1,082-case primary-candidate universe and separate 288-case multiplicity sensitivity boundary, then audit donor independence and exact lineage crosswalk using source/TCGA metadata only. Do not instantiate a final eligibility cohort until donor, lineage and QC conditions have been decided. Retain the 37-case ambiguous-other-file flag for prospectively reviewed sensitivity, not primary exclusion.
3. **Resolve G5–G6** as one normalization/quality admissibility decision. Do not request additional GDC records unless a concrete Phase 1 provenance/measurement blocker and bounded retrieval plan have been authorized.
4. **Freeze G7–G8**—the external structural replication estimand, matched null, test family, lineage support and uncertainty—in a reviewed, prospective final contract. Do not compute outcome statistics during drafting.
5. Execute the external analysis only if the hard gates pass, or record a formal not-evaluable result and closure boundary.

**Current authorization:** `cohort_frozen=false`; `external_analysis_authorized=false`; `biological_validation_authorized=false`. Drafting a contract is not a permission to score programs.
