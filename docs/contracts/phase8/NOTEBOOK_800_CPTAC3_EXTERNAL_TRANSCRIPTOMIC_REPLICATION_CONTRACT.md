# Notebook 800 — External Transcriptomic Program Replication in CPTAC-3

**Phase:** 8 — Orthogonal validation  
**Notebook:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`  
**Scientific status:** Notebook 800 completed a descriptive TCGA–CPTAC-3 structural assessment of three frozen transcriptomic programs across seven matched lineages. The 727 CPTAC-3 tumors are the proposed source cohort defined by Notebook 113.

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

### 4.1. Primary normalization

- The independently normalized CPTAC-3 matrix is generated by [`scripts/r/800_cptac3_tmm_logcpm.R`](../../../scripts/r/800_cptac3_tmm_logcpm.R) using `edgeR` and `rhdf5`.
- `filterByExpr` uses the seven matched lineages as groups on the broad protein-coding count matrix. The call uses the installed `edgeR` defaults. Subsetting with `keep.lib.sizes = FALSE` recomputes library sizes on retained genes. `normLibSizes(method = "TMM")` estimates the normalization factors on the filtered matrix.
- For all 2,389 frozen genes, the script calculates log2-CPM from their raw counts via `cpm(log = TRUE, prior.count = 2)` with explicit effective library sizes (filtered library size multiplied by its TMM factor). The filter determines the TMM reference and the full frozen feature set is used in projection and structural analysis.

### 4.2. Agreed immutable program projection

- Use the frozen `phase4.400.cross_system_shared_gene_universe` and `phase4.401.consensus_transcriptomic_gene_weights` artifacts (3 programs × 2,389 ordered genes) with exact identities, signs, magnitudes, and SHA-256 verification.
- Following executed Notebook 401, within **CPTAC-3 as one cohort**, standardize each gene independently using its CPTAC-3 mean and sample standard deviation (`ddof=1`) after normalization. Do **not** reuse TCGA means/standard deviations, join cohorts for scaling, or standardize genes separately within each lineage for the primary projection.
- For each sample and program, compute the dot product of the standardized 2,389-gene expression vector and the **unchanged** signed consensus-weight vector. Standardize each resulting program score to mean zero and sample SD one **within CPTAC-3**, following Notebook 401.
- Analyze structural evidence **within lineage**. Global within-CPTAC-3 standardization can depend on the relative composition of the seven lineages; it must not be interpreted as cross-platform absolute-score calibration. A score's computability or dispersion is **not** itself replication.
- Diagnose zero-variance genes, nonfinite values, absent identifiers, and the fraction of 2,389 frozen genes passing `filterByExpr`. **Do not silently delete genes, zero-fill missing genes, replace SD=0 by an arbitrary constant, or alter frozen weights.** If standardization is undefined, record the problem and its scope before any affected projection proceeds.

### 4.3. Expression filtering and technical comparability

The script reports the number of protein-coding genes retained for TMM and the number of frozen genes passing `filterByExpr`. Notebook 205 used a `CPM >= 1` gene-presence criterion. The R script prints the CPTAC-3 filter diagnostic. The reported assessment does not include a numerical comparison of the two filtering rules.

Both cohorts use GDC STAR Counts. CPTAC-3 records the Illumina platform for 726 tumors and has one missing platform label in SKCM. Library preparation, read-level sequencing quality and batch comparability remain unresolved. See Section 10 for the execution inputs and session information.

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

The analysis includes **21 program–lineage comparisons** on dependent data. No no-replication null, p-value, equivalence margin, multiplicity correction, binary replication decision or confirmatory claim is approved. 'Primary' denotes priority of descriptive interpretation for `T`, not inferential significance. Observed results cannot retroactively change case selection, program definitions or methodological choices.

### 6.2. Joint independent-cohort tumor bootstrap

For each lineage, obtain **1,000 fully valid joint bootstrap draws** within a cap of **1,100 attempts**. In each attempt, independently resample TCGA cases and CPTAC-3 cases **with replacement**, retaining the respective original lineage sample counts. Recompute one correlation matrix per cohort from the resampled tumors and reuse each matrix and the same tumor-index draws for all three programs and all approved summaries. Between-cohort contrasts must be calculated **within the same joint draw**. Never resample gene pairs as independent units or create separate program-specific tumor draws.

The bootstrap uses NumPy's `default_rng` with `SeedSequence([20261112, lineage_index, 0])`, where `lineage_index` is the zero-based index of the sorted TCGA lineage labels. A failed attempt discards all its metrics, records the attempt number and failure message, and redraws both cohorts.

For each estimand report the full-cohort value and empirical **2.5th and 97.5th percentile values** across the 1,000 valid joint draws (95% *descriptive* percentile interval, standard linear quantile interpolation). Signed coherence also receives cohort-specific intervals; any signed-coherence difference must use joint paired-draw contrasts. Bootstrap attempts are not biological replicates. These percentile intervals are approximate uncertainty summaries: coverage has not been demonstrated for every statistic and lineage, and they do **not** remove finite-sample bias in `abs(r)`, platform effects or biological confounding.

### 6.3. Preflight, numerical failures and no evaluability

Before external structural computation, verify exact ordered identity of all 2,389 genes in **both** frozen expression matrices, unmodified gene/program weights and signs, sample-to-column correspondence, one independently represented tumor per case, original accepted lineage counts, finite expression, nonzero finite within-lineage gene variance and positive finite edge-weight totals. Check that cohort-specific correlation vectors and the weighted-Pearson denominator are mathematically defined. Reuse the validated source and registry evidence; do not rerun acquisition/QC of Notebooks 111–113 or silently rescue samples or genes. Reuse independently computed CPTAC-3 normalization without joint TCGA/CPTAC-3 scaling.

A bootstrap attempt is invalid only for a documented mathematical/computational failure: gene variance or norm zero/nonfinite, correlation nonfinite, nonpositive/nonfinite weighted-Pearson denominator, or a nonfinite required statistic. Use and record the numerical tolerance applied to degenerate denominators; no silent clipping, zero filling, gene removal or replacement of undefined values is permitted. Few unique tumors in a with-replacement draw, an extreme finite statistic and broad uncertainty are **not** invalidity conditions.

A lineage is **technically non-evaluable** only when its required preflight fails or 1,000 fully valid joint draws cannot be obtained within 1,100 attempts. A failure in any mandatory program/statistic invalidates that joint draw; report the specific affected program, failure reason and all original denominators. Do not promote partial successful programs to a selected subset. A broad interval, an interval spanning zero or an unfavorable result indicates limited precision/interpretability, **not** non-evaluability. HNSC (CPTAC-3 n=36), UCEC (n=56) and SKCM (TCGA n=103) are retained under the common policy with appropriate small-sample cautions.

### 6.4. Mandatory matched-n sensitivity for absolute magnitude

For `Delta_M`, the notebook evaluates 32 paired comparisons per lineage at `n_common = min(n_TCGA, n_CPTAC3)`. It draws without replacement from the larger cohort and uses the full smaller cohort in each draw. The same subset is used across programs within a draw. The notebook traverses sorted lineage labels with a dedicated NumPy random stream initialized using `SeedSequence(20261112, spawn_key=(800, 1))`. The median and observed range of the 32 estimates accompany the full-cohort `Delta_M`. The range describes variation across overlapping subsets.

Matched-`n` analysis diagnoses sensitivity to unequal precision but sacrifices information and leaves finite-sample `abs(r)` bias and other cohort differences. It must not replace the full-cohort effect automatically, be tuned after observing external effects or serve as a replication threshold. Any substantive discordance is reported descriptively, without choosing the more favorable result.

### 6.5. TCGA reference characterization and further inference

For internal reference characterization, use eight deterministic TCGA tumor split repetitions with seed `20261111`; each disjoint half has `min(floor(n_TCGA/2),n_CPTAC3)` tumors. These internal comparisons are descriptive stability diagnostics, not a calibrated null or automatic external cutoff, and their precision differs from that of the full TCGA reference.

No weight reassignment/permutation, additional edge statistic or Fisher-`atanh` sensitivity is required or approved as a no-replication null. Any later hypothesis test, null calibration, FDR/FWER family or novel sensitivity would require a separate prospective specification; the present contract does **not** authorize it.


## 7. Lineage-aware evaluability and interpretation

Retain the seven accepted CPTAC-3 source denominators (HNSC 36, LUAD 178, LUSC 89, PAAD 88, SKCM 138, STAD 142, UCEC 56) and the frozen, lineage-matched TCGA denominators. Apply the same preflight, bootstrap and matched-`n` rules to all lineages. Distinguish **technical evaluability**, **statistical precision** and **biological interpretability**. A technically evaluable lineage may have substantial uncertainty or an inconclusive effect; it remains reportable. Never pool cancer types to rescue small sample groups or select lineages after viewing their external effects.

Cross-cancer recurrence may be discussed only as a qualitative, descriptive synthesis of lineage-specific estimates and limitations. No pooled pan-cancer statistic or cross-lineage hypothesis test is specified.

## 8. Confounding, identifiability and sensitivity analyses

The source-ancestry sensitivity recomputes the structural summaries in the four affected lineages after excluding 35 CPTAC-3 cases flagged in Notebook 113 for additional RNA-seq files of ambiguous ancestry. The comparison uses the full TCGA reference and captures the combined effect of cohort composition and reduced CPTAC-3 sample size.

The notebook summarizes TCGA covariate coverage and CPTAC-3 workflow and platform metadata. The CPTAC-3 inputs lack measures comparable to the TCGA tumor purity, leukocyte fraction, and proliferation covariates, so the cross-cohort estimates are unadjusted for these factors. Residual differences in tissue composition, clinical mix, collection center, library preparation and batch remain plausible contributors to lineage-specific differences. A covariate-adjusted comparison requires comparable measurements with documented provenance, sufficient within-lineage support, and scrutiny of overlap between any expression-derived covariate and the frozen program genes.

## 9. Analysis workflow and reporting requirements

Notebook 800 verifies the source and frozen-program identities, prepares CPTAC-3 expression and projections, assesses internal TCGA reference stability, and reports lineage-specific structural estimates with tumor bootstrap percentiles and matched-size sensitivity. The source-ancestry sensitivity, metadata coverage and source provenance support the interpretation of the main comparison.

## 10. Reproducibility and outputs

1. Use the Notebook 113 cohort, eligibility and count-compatibility files with their provenance manifest. The dependencies are Notebooks 111 → 112 → 113 for the external cohort, Notebook 205 for the frozen TCGA expression and sample and gene metadata, and Notebooks 400–401 for the frozen genes and programs.
2. Run [Notebook 800](../../../notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb) through **Export CPTAC-3 raw counts for R normalization**. This writes `800_cptac3_protein_coding_raw_counts.h5`, `800_cptac3_protein_coding_gene_metadata.csv`, and `800_cptac3_sample_metadata.csv` under `data/interim/expression/`.
3. From the repository root, run `Rscript scripts/r/800_cptac3_tmm_logcpm.R`. The script writes `800_cptac3_frozen_genes_tmm_logcpm.h5`, `800_cptac3_tmm_factors.csv`, and `800_cptac3_tmm_session_info.txt` to the same directory. The session file records the actual versions of R, `edgeR`, and `rhdf5`.
4. Resume Notebook 800 at **Load TMM-normalized CPTAC-3 expression**. The notebook saves lineage bootstrap draws and failure logs under `data/interim/phase8/bootstrap/`. Reuse existing checkpoints for the same inputs, settings, and implementation. For an independent run with changed inputs or settings, use fresh checkpoints. The notebook validates the checkpoint table structure, replicate identities, and numeric values before reuse.

The executed notebook reports the 21 program–lineage comparisons, uncertainty and sensitivity summaries, and source and covariate limitations. The local normalization artifacts and bootstrap checkpoints support execution. The notebook results constitute a descriptive evidence layer.

## 11. Limitations, interpretation and readiness

The current proposed CPTAC-3 population supports source-level externality rather than confirmed zero patient-level overlap with TCGA. Read/library-level QC is not independently certified cohort-wide. Cross-platform normalization and scaling can change score distributions or distort structural comparisons. Broad source histology excludes some potentially relevant lineages, and covariate availability may leave purity, proliferation or batch effects incompletely identified. Cross-sectional external transcriptomes cannot establish adaptive treatment-resistance trajectories or causal epigenetic regulation.

Permissible conclusions must be limited to the specific external transcriptomic structure actually tested and the lineages in which the design is evaluable. Evidence that a structure recurs does not imply resistance-like phenotype replication, a validated target, clinical prediction or therapeutic reversal; such outcomes require separate data and validation.

**Execution and readiness.** The project owner agreed to run Notebook 800 on 2026-11-12. The descriptive comparison followed source verification and expression preflight. This execution record is retrospective. A separate post-preflight authorization was not recorded before the comparison. The Notebook 113 source manifest retains `cohort_frozen=false`, `external_analysis_authorized=false`, `read_level_qc_status=QC_UNASSESSED`, and `cross_platform_comparability=NOT_ESTABLISHED`. The scope of this execution was descriptive.
