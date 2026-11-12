# Notebook 800 — External Transcriptomic Program Replication in CPTAC-3

**Phase:** 8 — Orthogonal validation  
**Notebook:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`  
**Scientific status:** Proposed 727-case CPTAC-3 source cohort; independent normalization and frozen program projection are specified. The three structural estimands, descriptive two-cohort tumor bootstrap, and technical evaluability rules are prospectively specified below. This is a **descriptive external-assessment design**, not a calibrated hypothesis test, binary replication rule or permission to override Notebook 113 readiness flags. No external structural result is established by this contract.

## 1. Scientific objective and scope

Evaluate whether the three fixed, TCGA-derived Phase 4 transcriptomic candidate programs exhibit reproducible multigene structure in an externally sourced CPTAC-3 primary-tumor RNA-seq cohort, accounting for tumor lineage, analytical representation and plausible technical or biological confounding.

The scientific target is **external structural support for previously defined transcriptomic programs**. Neither a calculable program score nor nonzero between-sample variation constitutes replication. Agreement with genes used to construct a score is mechanically dependent and is not independent evidence of the underlying multigene structure. The analysis must specify which non-tautological property of each frozen program it tests, how statistical uncertainty is handled and which technical or biological alternative explanations remain plausible.

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


### 5.2. Primary descriptive structural statistic

For each lineage `l` and frozen program `k`, compute gene–gene Pearson correlations separately from the eligible TCGA and CPTAC-3 tumors of that lineage, using the same 2,389 ordered genes. For each distinct pair `i<j`, let `r^TCGA_ij,l` and `r^CPTAC3_ij,l` be their respective sample correlations, and `q_ij,k=abs(w_i,k*w_j,k)` the frozen nonnegative pair weight.

```text
T(k,l) = weighted_Pearson_corr(
    {r^TCGA_ij,l : i<j},
    {r^CPTAC3_ij,l : i<j},
    weights={q_ij,k : i<j}
)
```

`T` is the **primary descriptive measure of relative edge-pattern concordance**, not a confirmatory network-replication test. A positive affine transformation of all comparison edges can yield `T=1` despite changed magnitudes. `T` does not use the frozen loading signs, require absolute edge-level agreement, or establish regulatory causality or program specificity. All three programs apply different weight kernels to the **same 2,852,466 gene pairs** and the same two cohort-specific correlation matrices; the pairs and programs are not independent biological replicates.

Use **untransformed Pearson correlations**, not Fisher-`atanh` correlations, as the primary definition. Do not apply an observed-`T` threshold or label a program–lineage combination positive/negative for replication. Degenerate or nonfinite inputs are governed by Section 6.

### 5.3. Prespecified complementary descriptive measures

**Signed multigene coherence within each cohort.** Set `s_ij,k=sign(w_i,k*w_j,k)`, `z_ij=s_ij,k*r_ij`, and `q_ij,k=abs(w_i,k*w_j,k)`. Report the **weighted median** of `z_ij` as the central signed-coherence description; its definition is the smallest value whose cumulative normalized weight reaches 0.5. Report `C_mean=sum(q_ij,k*z_ij)/sum(q_ij,k)` as secondary magnitude-sensitive characterization. Both summaries retain their signs. For a linear score built from the same weights and within-lineage standardized genes, `C_mean` is algebraically linked to the score variance, and must not be treated as independent score evidence. The weighted median lacks that exact variance identity but is also statistically dependent on the reference correlations, weights and samples. Cohort-specific measures and their CPTAC-3-minus-TCGA descriptive differences may be reported, without using them as a second success criterion.

**Weighted mean absolute-correlation change.** Define the complementary effect:

```text
Delta_M(k,l) =
    sum_{i<j} q_ij,k * (abs(r^CPTAC3_ij,l) - abs(r^TCGA_ij,l))
    / sum_{i<j} q_ij,k
```

This is an imperfect finite-sample estimate of the analogous population difference in weighted **mean absolute** gene–gene correlations. The use of `abs(r)` introduces sample-size- and distribution-dependent bias, especially with weak correlations and small tumor counts. A positive/negative estimate denotes greater/smaller *estimated* average absolute correlation, not a proven biological strengthening/attenuation. A near-zero effect can mask compensation, rewiring or sign inversions and **does not demonstrate preservation of individual edge magnitudes**. The mandatory matched-`n` sensitivity is specified in Section 6.4.

**Context.** TCGA reference-reliability characterization and disjoint-gene score-construction diagnostics, where applied as already specified, describe internal reference stability or score construction rather than independent external evidence. The three structural summaries are related and must not be counted as separate independent tests.

### 5.4. Interpretation boundary

All primary effect sizes are program-by-lineage; do not pool cancers naïvely, treat millions of dependent gene pairs as independent samples, or choose lineages after observing their external values. Similar edge patterns may reflect proliferation, immune/stromal composition, tumor purity, platform or batch effects rather than a specific epigenetic program. An external structural association is not clinical resistance prediction, causal validation or therapeutic reversal.


## 6. Reference reliability, tumor-level uncertainty and evaluability

### 6.1. Estimation units and inferential scope

Analyze the seven accepted lineages separately, using one tumor/case as the independent observational and resampling unit within each cohort. Compute the original full-cohort `T`, `Delta_M` and cohort-specific signed median/mean per program and lineage. TCGA is an estimated source reference, not a true, error-free network.

The planned family includes **21 program–lineage comparisons** on dependent data. No no-replication null, p-value, equivalence margin, multiplicity correction, binary replication decision or confirmatory claim is approved. 'Primary' denotes priority of descriptive interpretation for `T`, not inferential significance. Observed results cannot retroactively change case selection, program definitions or methodological choices.

### 6.2. Joint independent-cohort tumor bootstrap

For each lineage, obtain **1,000 fully valid joint bootstrap draws** within a cap of **1,100 attempts**. In each attempt, independently resample TCGA cases and CPTAC-3 cases **with replacement**, retaining the respective original lineage sample counts. Recompute one correlation matrix per cohort from the resampled tumors and reuse each matrix and the same tumor-index draws for all three programs and all approved summaries. Between-cohort contrasts must be calculated **within the same joint draw**. Never resample gene pairs as independent units or create separate program-specific tumor draws.

Use base RNG seed `20261112` with reproducible, independently derived streams for each lineage and analysis component, e.g. `numpy.random.SeedSequence` with fixed lineage indices. Record all seed inputs, implementations and software versions. A failed attempt is **atomic**: if any required metric for any of the three programs is invalid, discard all of that attempt's metrics, record the attempt number and exact failure cause, and redraw **both** cohorts. Do not retain partial program results from invalid attempts.

For each estimand report the full-cohort value and empirical **2.5th and 97.5th percentile values** across the 1,000 valid joint draws (95% *descriptive* percentile interval, standard linear quantile interpolation). Signed coherence also receives cohort-specific intervals; any signed-coherence difference must use joint paired-draw contrasts. Bootstrap attempts are not biological replicates. These percentile intervals are approximate uncertainty summaries: coverage has not been demonstrated for every statistic and lineage, and they do **not** remove finite-sample bias in `abs(r)`, platform effects or biological confounding.

### 6.3. Preflight, numerical failures and no evaluability

Before external structural computation, verify exact ordered identity of all 2,389 genes in **both** frozen expression matrices, unmodified gene/program weights and signs, sample-to-column correspondence, one independently represented tumor per case, original accepted lineage counts, finite expression, nonzero finite within-lineage gene variance and positive finite edge-weight totals. Check that cohort-specific correlation vectors and the weighted-Pearson denominator are mathematically defined. Reuse the validated source and registry evidence; do not rerun acquisition/QC of Notebooks 111–113 or silently rescue samples or genes. Reuse independently computed CPTAC-3 normalization without joint TCGA/CPTAC-3 scaling.

A bootstrap attempt is invalid only for a documented mathematical/computational failure: gene variance or norm zero/nonfinite, correlation nonfinite, nonpositive/nonfinite weighted-Pearson denominator, or a nonfinite required statistic. Use and record the numerical tolerance applied to degenerate denominators; no silent clipping, zero filling, gene removal or replacement of undefined values is permitted. Few unique tumors in a with-replacement draw, an extreme finite statistic and broad uncertainty are **not** invalidity conditions.

A lineage is **technically non-evaluable** only when its required preflight fails or 1,000 fully valid joint draws cannot be obtained within 1,100 attempts. A failure in any mandatory program/statistic invalidates that joint draw; report the specific affected program, failure reason and all original denominators. Do not promote partial successful programs to a selected subset. A broad interval, an interval spanning zero or an unfavorable result indicates limited precision/interpretability, **not** non-evaluability. HNSC (CPTAC-3 n=36), UCEC (n=56) and SKCM (TCGA n=103) are retained under the common policy with appropriate small-sample cautions.

### 6.4. Mandatory matched-n sensitivity for absolute magnitude

For `Delta_M`, conduct **32** outcome-blind, without-replacement subsamples per lineage using `n_common=min(n_TCGA,n_CPTAC3)` in **each** cohort and reproducible RNG streams distinct from the bootstrap (same documented base seed `20261112`). For every paired subset, recompute cohort correlations and all three program-specific `Delta_M` values using shared subset indices across programs. Summarize each program's 32 estimates by **median and range**, alongside full-cohort `Delta_M`. This range is **not** a confidence interval; repeated subsamples do not create independent tumors. A cohort already at `n_common` contributes all of its tumors to every draw.

Matched-`n` analysis diagnoses sensitivity to unequal precision but sacrifices information and leaves finite-sample `abs(r)` bias and other cohort differences. It must not replace the full-cohort effect automatically, be tuned after observing external effects or serve as a replication threshold. Any substantive discordance is reported descriptively, without choosing the more favorable result.

### 6.5. TCGA reference characterization and further inference

For internal reference characterization, use eight deterministic TCGA tumor split repetitions with seed `20261111`; each disjoint half has `min(floor(n_TCGA/2),n_CPTAC3)` tumors. These internal comparisons are descriptive stability diagnostics, not a calibrated null or automatic external cutoff, and their precision differs from that of the full TCGA reference.

No weight reassignment/permutation, additional edge statistic or Fisher-`atanh` sensitivity is required or approved as a no-replication null. Any later hypothesis test, null calibration, FDR/FWER family or novel sensitivity would require a separate prospective specification; the present contract does **not** authorize it.


## 7. Lineage-aware evaluability and interpretation

Retain the seven accepted CPTAC-3 source denominators (HNSC 36, LUAD 178, LUSC 89, PAAD 88, SKCM 138, STAD 142, UCEC 56) and the frozen, lineage-matched TCGA denominators. Apply the same preflight, bootstrap and matched-`n` rules to all lineages. Distinguish **technical evaluability**, **statistical precision** and **biological interpretability**. A technically evaluable lineage may have substantial uncertainty or an inconclusive effect; it remains reportable. Never pool cancer types to rescue small sample groups or select lineages after viewing their external effects.

Cross-cancer recurrence may be discussed only as a qualitative, descriptive synthesis of lineage-specific estimates and limitations. No pooled pan-cancer statistic or cross-lineage hypothesis test is specified.

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
4. Prespecified descriptive structural estimands and internal TCGA reference characterization.
5. Lineage-specific descriptive structural assessment with two-cohort bootstrap uncertainty and matched-n magnitude sensitivity, gated by source readiness and technical preflight.
6. Confounding limitations and only independently justifiable sensitivities.
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
| Descriptive structural assessment | Per-program/lineage `T`, `Delta_M`, cohort signed-coherence estimates, two-cohort bootstrap percentile intervals and matched-n magnitude sensitivity |
| Specificity sensitivity (if implemented) | Exact weight-reassignment scheme, preserved quantities, diagnostic comparisons and interpretation limits |
| Confounding and sensitivity | Available covariates, identifiability, sensitivity estimates and residual uncertainties |
| Scientific reporting | Descriptive, unfavorable, inconclusive and non-evaluable findings, without uncalibrated p-values or binary labels |

Exact output filenames, whether artifacts must persist, and registry updates **are not predetermined here**. Define them from scientific reproducibility requirements before creation, rather than generating multiple intermediate files by default. Do not register an inferential cohort or claim a frozen replication artifact merely because a notebook runs to completion.

## 11. Limitations, interpretation and readiness

The current proposed CPTAC-3 population supports source-level externality rather than confirmed zero patient-level overlap with TCGA. Read/library-level QC is not independently certified cohort-wide. Cross-platform normalization and scaling can change score distributions or distort structural comparisons. Broad source histology excludes some potentially relevant lineages, and covariate availability may leave purity, proliferation or batch effects incompletely identified. Cross-sectional external transcriptomes cannot establish adaptive treatment-resistance trajectories or causal epigenetic regulation.

Permissible conclusions must be limited to the specific external transcriptomic structure actually tested and the lineages in which the design is evaluable. Evidence that a structure recurs does not imply resistance-like phenotype replication, a validated target, clinical prediction or therapeutic reversal; such outcomes require separate data and validation.

**Readiness:** The scientific estimands and planned descriptive bootstrap/evaluability procedure are now specified (Sections 5–7); they are ready for implementation and review, not yet for a confirmatory replication claim. The 727-case CPTAC-3 set remains a **proposed source cohort** and the original Notebook 113 manifest retains `cohort_frozen=false`, `external_analysis_authorized=false`, `read_level_qc_status=QC_UNASSESSED` and `cross_platform_comparability=NOT_ESTABLISHED`. These are **recorded upstream provenance/readiness facts**, not fields to be silently rewritten, overridden or treated as passed by completion of this contract. Before the first external **structural comparison**, record an explicit Phase 8 descriptive-analysis authorization after authenticating the 113 handoff and accepted cohort and passing the relevant expression/preflight gates; halt if the required transition cannot be justified. Normalization and immutable program projection may proceed under Section 4 independently of this final structural-comparison gate. No null-based confirmatory inference, donor-level independence, causal mechanism, clinical resistance prediction or therapeutic reversal is authorized.
