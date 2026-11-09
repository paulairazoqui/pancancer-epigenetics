# Notebook 800 — External Transcriptomic Program Replication in CPTAC-3

**Phase:** 8 — Orthogonal validation  
**Notebook:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`  
**Scientific status:** External RNA-seq source cohort proposed and source compatibility assessed. The normalization and fixed-program projection approach, the primary scientific replication property, and two negative-control families have been selected. A weighted reference-network concordance statistic is a **candidate**, not a frozen confirmatory test; control algorithms, uncertainty, and decision rules remain to be specified before confirmatory analysis. No external program-replication result is established by this contract.

## 1. Scientific objective and scope

Evaluate whether the three fixed, TCGA-derived Phase 4 transcriptomic candidate programs exhibit reproducible multigene structure in an externally sourced CPTAC-3 primary-tumor RNA-seq cohort, accounting for tumor lineage, analytical representation and plausible technical or biological confounding.

The scientific target is **external structural support for previously defined transcriptomic programs**. Neither a calculable program score nor nonzero between-sample variation constitutes replication. Agreement with genes used to construct a score is mechanically dependent and is not independent evidence of the underlying multigene structure. The analysis must specify which non-tautological property of each frozen program it tests and which alternative explanations its controls address.

This notebook does not discover or refit programs, reconstruct the CPTAC-3 source cohort, predict clinical drug resistance, estimate treatment effects, validate drug response, infer causal epigenetic mechanisms or demonstrate perturbational reversal. An external transcriptomic pattern, if supported, remains a computational association subject to validation.

## 2. Reference programs and external study population

The reference objects are the **three immutable Phase 4 consensus transcriptomic programs**, with their frozen gene identities, ordering, signs, loadings and associated reference metadata. The exact authoritative program artifacts and registry fingerprints must be resolved before calculations; no replacement from a similarly named working file is acceptable. The relevant feature universe contains **2,389 shared ordered genes**. Reference transformations and score definitions must be reconstructed from their executed Phase 4 specification, including the role of TMM/logCPM and gene standardization where applicable, without assuming that arbitrary alternative scaling preserves program interpretation.

The external source is the GDC `CPTAC-3` primary-tumor STAR Counts RNA-seq inventory constructed and audited under **Notebook 113 — CPTAC-3 External Cohort Construction and Eligibility**. Its proposed source membership contains **727 unique cases and 727 primary RNA files**:

| Harmonized TCGA lineage | Proposed cases |
| --- | ---: |
| TCGA-LUAD | 178 |
| TCGA-LUSC | 89 |
| TCGA-STAD | 142 |
| TCGA-SKCM | 138 |
| TCGA-PAAD | 88 |
| TCGA-UCEC | 56 |
| TCGA-HNSC | 36 |
| **Total** | **727** |

These are **source candidates**, not an automatically frozen inferential cohort. The corresponding 1,082-case primary-source universe, 355 non-proposed cases, separately tracked multiplicity and ambiguous-ancestry records, and precise inclusion reasons remain defined by the Notebook 113 contract. Do not rebuild, reselect, relabel or replace cases after examining external expression or program outcomes.

Externality is supported at the **cohort provenance** level; complete donor-level non-overlap with TCGA has not been genetically established. Missing independently comparable read-level sequencing QC is an explicit uncertainty, not a sample-level QC PASS or automatic rejection. These limitations accompany the interpretation of any external result.

## 3. Input acceptance and reproducibility checks

Before expression projection or inferential computations, read the exact locally generated `113_source_provenance_manifest.json`, `113_proposed_external_source_cohort.csv`, `113_primary_candidate_case_eligibility.csv` and `113_raw_count_compatibility.csv`. Recompute and compare the three recorded CSV SHA-256 fingerprints against the manifest; verify source identities, stable file and case IDs, permitted inclusion statuses, one source primary RNA file per case, all 727 proposed rows and the seven lineage totals. Read cohort-readiness and source-limitations statuses from the manifest rather than expecting a separate readiness file. The expected source classifications are `COHORT_LEVEL_EXTERNALITY_ASSUMED` and `NOT_INDIVIDUALLY_VERIFIED`; the readiness fields are `cohort_frozen=false`, `external_analysis_authorized=false`, `read_level_qc_status=QC_UNASSESSED` and `cross_platform_comparability=NOT_ESTABLISHED`. None of these flags is an outcome of the Notebook 800 inferential tests, nor may they be silently overridden. Use the complete eligibility and attrition tables for denominator reconciliation rather than deriving a new cohort from filenames or clinical characteristics.

Verify the immutable Phase 4 loading vectors, ordered gene identities, reference representations and registry fingerprints independently. A missing input, checksum mismatch, unexpected duplicated case/file, contradictory status or incompatible program version **halts the affected analysis** pending source or reference correction. An integrity failure must not be bypassed by reconstructing membership inside Notebook 800. Do not derive new source eligibility, tumor-lineage mappings or raw-count feature-coverage status within Notebook 800. If integrity or membership checks fail, stop and correct the originating producer rather than reconstructing a more favorable downstream cohort.

Maintain a deterministic, versioned execution environment and recorded input hashes. Separate checks of file identity and raw-count compatibility from checks of biological analytical validity: passing the former is necessary but not sufficient for the latter.

## 4. Transcriptomic data preparation and program projection

The audited external input representation is the GDC STAR Counts **`unstranded` raw-count column**, with uniquely version-normalized Ensembl gene IDs, nonnegative integer values and all **2,389** frozen reference genes present in the **727** proposed files. Identifier coverage does not establish numerical comparability across sequencing workflows.

### 4.1. Agreed primary normalization

- Normalize the CPTAC-3 counts **independently of TCGA** using `edgeR` in R: trimmed mean of M values (**TMM**) library normalization followed by **log2 counts per million (logCPM)**, with the executed TCGA Notebook 205 procedure as the technical reference.
- Estimate TMM normalization factors from the **broad protein-coding count universe**, not only the 2,389 program genes. Apply `edgeR::filterByExpr` for the genes informing normalization, using the **seven accepted lineages as groups**. The agreed primary specification uses its conventional defaults (`min.count=10`, `min.total.count=15`, `large.n=10`, `min.prop=0.7`), subject to checking the installed `edgeR` version and actual function call at implementation.
- Calculate logCPM for **all 2,389 frozen genes**, including those that do not pass `filterByExpr`, using the TMM factors and effective library sizes estimated from the broader reference. Expression filtering must **not** redefine the frozen scoring features.
- Retain the logCPM convention from Notebook 205 (`edgeR::cpm(..., log=TRUE, prior.count=2, normalized.lib.sizes=TRUE)`) unless an explicit implementation-compatibility issue is identified and resolved before projection. Notebook 205 used a CPM >= 1 gene-presence criterion instead of `filterByExpr`; this difference must be recorded, not described as an identical transformation.
- The Notebook 800 Python workflow may invoke a small, versioned R script via `Rscript`, following the existing repository pattern. **RStudio is not an execution requirement.** Avoid redundant persisted intermediate matrices unless reproducibility requires them.

### 4.2. Agreed immutable program projection

- Use the frozen `phase4.400.cross_system_shared_gene_universe` and `phase4.401.consensus_transcriptomic_gene_weights` artifacts (3 programs × 2,389 ordered genes) with exact identities, signs, magnitudes, and SHA-256 verification.
- Following executed Notebook 401, within **CPTAC-3 as one cohort**, standardize each gene independently using its CPTAC-3 mean and sample standard deviation (`ddof=1`) after normalization. Do **not** reuse TCGA means/standard deviations, join cohorts for scaling, or standardize genes separately within each lineage for the primary projection.
- For each sample and program, compute the dot product of the standardized 2,389-gene expression vector and the **unchanged** signed consensus-weight vector. Standardize each resulting program score to mean zero and sample SD one **within CPTAC-3**, following Notebook 401.
- Analyze structural evidence **within lineage**. Global within-CPTAC-3 standardization can depend on the relative composition of the seven lineages; it must not be interpreted as cross-platform absolute-score calibration. A score's computability or dispersion is **not** itself replication.
- Diagnose zero-variance genes, nonfinite values, absent identifiers, and the fraction of 2,389 frozen genes passing `filterByExpr`. **Do not silently delete genes, zero-fill missing genes, replace SD=0 by an arbitrary constant, or alter frozen weights.** If standardization is undefined, record the problem and its scope before any affected projection proceeds.

### 4.3. Technical sensitivity and reproducibility

- Agreed technical sensitivity: compare the expression-filtering behavior with the executed TCGA Notebook 205 **CPM >= 1** rule. This does not redefine the primary normalization or remove frozen genes.
- An optional diagnostic may examine TMM factors estimated from only the 2,389 fixed genes; because such factors may be program-biased, this **cannot replace the broad-gene primary normalization** and must not be chosen based on favorable replication outcomes.
- Before executing the workflow, pin and record relevant R/`edgeR` and Python dependency versions, precise counting/normalization settings, sample order, gene alignment, and numerical tolerances.

Do not re-estimate loadings, reorient programs, replace features by symbols, perform de novo ICA in CPTAC-3, or use external replication results to optimize transformations. Essential measurement incompatibility remains a reason to classify an analysis as non-evaluable rather than repairing the frozen program after seeing outcomes.

## 5. Structural replication target and analysis design

### 5.1. Approved scientific target

The **approved primary scientific property** is **within-lineage preservation in CPTAC-3 of the TCGA reference gene–gene coexpression structure** for each of the three frozen signed consensus programs. A favorable projection score alone cannot establish this property. The **approved complementary property** is within-CPTAC-3 signed multigene coherence, evaluated without treating score–constituent-gene association as independent evidence.

TCGA and CPTAC-3 must be evaluated separately for each of the seven accepted matching lineages. The TCGA reference is estimated from its observed tumors, not assumed to be an error-free true network. A result for one lineage does not automatically generalize to other cancer types.

### 5.2. Candidate primary statistic — not yet frozen

The leading **candidate** is the weighted Pearson correlation between corresponding **untransformed gene–gene Pearson correlations** in lineage-matched TCGA and CPTAC-3, using only distinct gene pairs:

```text
T(program k, lineage l) =
    weighted_Pearson_corr(
        { r_TCGA(i,j,l) : i < j },
        { r_CPTAC3(i,j,l) : i < j },
        pair_weights = { abs(w_i,k * w_j,k) : i < j }
    )
```

Here `w_i,k` is the unchanged consensus weight for gene `i` in program `k`. This is **relative edge-pattern concordance**: it does **not** demonstrate equal coexpression magnitudes, preservation of causal or regulatory edges, or independence from shared latent factors. No universal observed-`T` cutoff has been adopted. Fisher `atanh` transformation of individual correlations is **not primary**; its possible sensitivity role remains to be justified.

The candidate is not a prevalidated ICA network-preservation test. Its suitability, stability and inferential calibration must be assessed prospectively before confirmatory CPTAC-3 evaluation. A high score with weakened correlation magnitudes must not be described as full structural preservation.

### 5.3. Approved supporting analyses and reference characterization

- **Secondary:** within-lineage signed coexpression coherence, with pairwise correlations oriented by `sign(w_i * w_j)` and summarized using a **weighted median** with pair weights `abs(w_i * w_j)`. This characterizes internal coherence but is not an independent confirmation of reference-network preservation.
- **Complementary interpretation:** inspect attenuation or shifts in coexpression strength compared with TCGA using a prespecified, weighted effect-size summary; its exact formula is **pending**. Do not promote this automatically to a second independent success test.
- **Construction diagnostic:** concordance of scores from prespecified **disjoint-gene** partitions balanced for frozen weight sign and magnitude; not a substitute for network preservation.
- **Reference stability:** assess whether TCGA gene–gene patterns are reproducible within each lineage using tumor-level partitions/resampling; comparability with the smaller external sample sizes must be considered. This has **not yet been executed as an inferential reference-calibration study**.

The completed **TCGA-only descriptive audit** used verified frozen files, did not access CPTAC-3, and did not amend registered artifacts. It established materially different weight concentration across programs:

| Program | Positive / negative / zero weights | Energy in highest 10% `abs(w)` genes | Effective number of genes, inverse squared-energy concentration |
| --- | ---: | ---: | ---: |
| `CONSENSUS_TX_01` | 819 / 1,570 / 0 | 75.3% | 138.3 |
| `CONSENSUS_TX_02` | 1,348 / 1,041 / 0 | 55.0% | 503.9 |
| `CONSENSUS_TX_03` | 1,024 / 1,365 / 0 | 53.5% | 489.6 |

In seven reference TCGA lineages, the unweighted median signed correlations across all 2,389 genes were generally small (0.007–0.030), whereas medians among pairs of the top 10% `abs(w)` genes ranged from 0.067 to 0.281 (program/lineage dependent). Weighted median signed correlations across lineages ranged 0.032–0.062 (TX_01), 0.028–0.070 (TX_02), and 0.017–0.053 (TX_03). These are **descriptive source-reference observations, not external replication results or pairwise-independent statistical tests**. The concentration of TX_01 weighs against unweighted all-gene median coherence as a primary estimand.

The TCGA-only audit reported disjoint-partition score correlations of 0.980–0.988 (TX_01), 0.943–0.990 (TX_02) and 0.959–0.987 (TX_03); these do not independently establish biological specificity. The audit figures were reported in the development review and are **not yet a newly frozen registered artifact**; any figures used in a manuscript or confirmatory calibration must be reproducibly regenerated and recorded from the SHA-verified source inputs.

### 5.4. Interpretation boundary

All primary effect sizes are program-by-lineage; do not pool cancers naïvely, treat millions of dependent gene pairs as independent samples, or choose lineages after observing their external values. Similar edge patterns may reflect proliferation, immune/stromal composition, tumor purity, platform or batch effects rather than a specific epigenetic program. An external structural association is not clinical resistance prediction, causal validation or therapeutic reversal.

## 6. Negative controls and statistical inference

### 6.1. Approved conceptual negative-control families

Two control families have been **approved in principle**, but their exact algorithms and valid roles remain to be specified against the candidate statistic:

1. **Primary negative reference: matched alternative gene sets.** Compare the tested program with alternative gene sets of matching cardinality and relevant expression characteristics, accounting for detectability, abundance and variability using prospective TCGA-side or otherwise outcome-blind information. Preserve a defensible signed/magnitude weight distribution. An eligible alternative-gene universe must be shown to exist and to have comparably available expression in both cohorts; **the 2,389 frozen scoring genes are not automatically a sufficient alternative pool**. Construct corresponding TCGA and CPTAC-3 references for the *same* alternative genes. Specify allowed overlap and failure-to-match handling.
2. **Complementary negative reference: reassignment/permutation of frozen weights and signs.** Evaluate whether the original assignment has distinctive performance relative to alternatives on the same genes. In the candidate primary statistic, pair weights use **absolute magnitudes**; a **global sign inversion** changes nothing, while permuting sign labels alone does not change its absolute pair weights and is therefore **not a meaningful primary-statistic null**. Reassigning magnitudes can alter primary-statistic weights. Signed permutations can instead be useful for the **signed-coherence secondary analysis** with an explicitly defined null.

Unmatched random genes alone are not a sufficient primary control. Neither a null that retains the tested signal trivially nor a null designed to favor the observed result is acceptable. Control distributions must not be tuned using CPTAC-3 replication outcomes.

### 6.2. Reference reliability and tumor-level uncertainty

Before confirmatory use, characterize **within-lineage TCGA reference stability** by deterministic repeated, disjoint tumor splits or suitable tumor-level resampling. Specify sample counts and acknowledge that TCGA split-half precision differs from full-TCGA-versus-CPTAC-3 precision. A TCGA internal-reference reproducibility score is **not an automatic external replication threshold**.

Uncertainty for the primary statistic should be estimated at the **tumor/case level**, considering uncertainty in **both** TCGA reference edges and CPTAC-3 edges. Bootstrap or related tumor-resampling design remains to be specified, with stratification by lineage and attention to small external sample counts (notably CPTAC-3 HNSC, n=36) and smaller reference counts (notably TCGA-SKCM, n=103). Neither dependent gene pairs nor permutations/splits are independent biological replicates.

### 6.3. Inferential specifications still open

Before viewing confirmatory CPTAC-3 coexpression preservation statistics, define and record the following:

- Exact matched-control source universe, matching variables, tolerances, set construction, sample-level handling, permitted overlap, seeds, number of controls and null interpretation.
- Exact weight-reassignment control (if informative for the chosen test), number of permutations, and handling of invariant sign operations.
- TCGA reference stability design, treatment of estimated reference-network uncertainty, and primary-statistic degeneracy (e.g., nearly constant edge vectors).
- Tumor-level uncertainty estimator, test direction, effect-size comparison to controls, and rules for non-evaluability.
- Primary multiplicity family over **3 programs × 7 accepted lineages** (21 planned comparisons), with an explicit missing/non-evaluable policy and selected FDR or FWER method and thresholds.
- If used, the exact formula for coexpression-magnitude attenuation and any technical sensitivity of the `atanh` correlation transform.

A scientifically defensible no-effect/negative conclusion and an inconclusive result must remain reportable; do not reselect genes, tumors, controls, or statistics to recover a positive result. No confirmatory structural comparison is authorized by the conceptual approvals alone.

## 7. Lineage-aware evaluability and interpretation

Begin with the seven accepted source lineages and their fixed proposed case counts. Define **outcome-blind** minimum statistical support, effective case counts, data completeness, usable variance, identifiable adjustment structure and any other necessary conditions before evaluating program replication. A universal minimum sample-size cutoff is not justified merely by convenience; support criteria must reflect the chosen statistic, anticipated precision and control feasibility.

Preserve all original lineage denominators and distinguish a failure to meet an evaluability condition from a tested negative result. If a lineage or program cannot be evaluated, report the precise technical, sample-support or identifiability reason. Never pool tumor types naïvely to rescue small strata or choose lineages because they show larger program effects.

Evaluate cross-lineage recurrence only after acknowledging differing lineage composition, technical support and uncertainty. Consistency across several evaluable lineages is descriptive evidence unless a cross-lineage statistical synthesis has itself been prespecified.

## 8. Confounding, identifiability and sensitivity analyses

Assess plausible influences of tumor purity, immune/stromal admixture, proliferative activity, collection center, sequencing/library workflow, batch and source-context heterogeneity. Notebook 113 does not establish complete per-case metadata for several of these variables. Missing variables must remain **unmeasured**, not silently assumed absent or constant.

Before inferential use, identify which covariates or proxies are available with valid provenance, which are estimable independently of the tested program signal, and whether adjustments are identifiable within each lineage. Any expression-derived proxy requires scrutiny for overlap or circularity with the frozen program genes. If batch and lineage are aliased, an across-lineage batch adjustment is not identifiable; if a covariate is absent or unreliable, acknowledge residual confounding rather than inventing a substitute.

Prespecify feasible sensitivity analyses and their interpretation. At minimum, review the already recorded ambiguity flag among simple source cases, normalization/projection dependence and source technical comparability; evaluate purity/composition/proliferation effects only to the extent supported by valid data and an identifiable design. Sensitivity analysis must not become a post hoc selection filter for the primary result.

Disjoint-gene or otherwise controlled coherence, even if statistically supported, may reflect shared biological axes or technical factors. It is **support for an observed transcriptomic structure**, not proof of a specific epigenetic mechanism.

## 9. Analysis workflow and reporting requirements

Keep the executable notebook scientifically organized rather than narrating project development. Each analysis section should explain the biological/statistical question, exact input, operation, interpretable output and limitations. Use readable, Black-compatible Python and the repository's established notebook conventions. Avoid redundant source QC, live acquisition or undocumented persistent files.

The notebook should proceed through these logically separate analytical responsibilities:

1. Source and frozen-program identity checks with explicit stop conditions.
2. Outcome-blind cohort and lineage accounting, metadata coverage and analysis feasibility.
3. Technically justified count normalization and fixed-program projection.
4. Prospective structural test and matched negative-control evaluation.
5. Complete lineage-specific inference, uncertainty and multiplicity.
6. Prespecified confounding and sensitivity assessments.
7. An integrated, conservative interpretation of supported, unsupported and non-evaluable findings.

Execution of later analytical stages is conditional on the relevant design and readiness decisions being approved; the presence of a section in this contract does not authorize running an otherwise unspecified statistical procedure.

## 10. Reproducibility and outputs

Inputs must refer to the exact 113 membership and source-manifest files, frozen Phase 4 program artifacts, and authoritative registries. Record file fingerprints, software/library versions, transformation parameters, random seeds and numerical tolerances sufficient to reproduce projections and tests without live source replacement.

The intended scientific output classes are:

| Output class | Required contents |
| --- | --- |
| Input and cohort verification | Checked artifact IDs/hashes, unique case and file identities, cohort status, original and analytic denominators |
| Lineage feasibility | Per-lineage support, input missingness, usable measurements and non-evaluable reasons |
| Projection specification | Gene universe, count transformation, fixed loading identity, scaling rule, technical diagnostics and exact parameters |
| Structural replication | Complete program-by-lineage effect sizes, test statistics, reference/null comparisons and uncertainty |
| Control diagnostics | Matching quality, null construction, failure cases and dependence limitations |
| Confounding and sensitivity | Available covariates, identifiability, sensitivity estimates and residual uncertainties |
| Scientific reporting | Clearly separated confirmatory and exploratory findings, including negative and non-evaluable results |

Exact output filenames, whether artifacts must persist, and registry updates **are not predetermined here**. Define them from scientific reproducibility requirements before creation, rather than generating multiple intermediate files by default. Do not register an inferential cohort or claim a frozen replication artifact merely because a notebook runs to completion.

## 11. Limitations, interpretation and readiness

The current proposed CPTAC-3 population supports source-level externality rather than confirmed zero patient-level overlap with TCGA. Read/library-level QC is not independently certified cohort-wide. Cross-platform normalization and scaling can change score distributions or distort structural comparisons. Broad source histology excludes some potentially relevant lineages, and covariate availability may leave purity, proliferation or batch effects incompletely identified. Cross-sectional external transcriptomes cannot establish adaptive treatment-resistance trajectories or causal epigenetic regulation.

Permissible conclusions must be limited to the specific external transcriptomic structure actually tested and the lineages in which the design is evaluable. Evidence that a structure recurs does not imply resistance-like phenotype replication, a validated target, clinical prediction or therapeutic reversal; such outcomes require separate data and validation.

**Readiness:** The 727-case source cohort remains proposed, with feature compatibility assessed at source level. The primary normalization and immutable program-projection **approaches are approved** (Section 4), the reference-network preservation property is **approved** (Section 5), and matched-gene and weight/sign-reassignment **control families are approved conceptually** (Section 6). The weighted edge-pattern Pearson statistic is a **candidate, not a frozen inferential specification**. Final inferential membership, implemented normalization details and versioning, TCGA reference reliability, exact null generation, uncertainty, multiplicity, outcome-blind evaluability and feasible confounding sensitivities remain **open**. The Notebook 800 may be developed incrementally for authenticated inputs, normalization and fixed projection; a confirmatory external structural-replication claim requires the remaining design decisions before its inferential computation.
