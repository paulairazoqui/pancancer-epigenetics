# Notebook 800 — External Transcriptomic Program Replication in CPTAC-3

**Phase:** 8 — Orthogonal validation  
**Notebook:** `notebooks/phase8_orthogonal_validation/800_external_bulk_cohorts.ipynb`  
**Scientific status:** External RNA-seq source cohort proposed and source compatibility assessed; the analytical normalization, primary replication estimand and inferential decision rules require prospective specification before confirmatory analysis. No external program-replication result is established by this contract.

## 1. Scientific objective and scope

Evaluate whether the three fixed, TCGA-derived Phase 4 transcriptomic candidate programs exhibit reproducible multigene structure in an externally sourced CPTAC-3 primary-tumor RNA-seq cohort, accounting for tumor lineage, analytical representation and plausible technical or biological confounding.

The scientific target is **external structural support for previously defined transcriptomic programs**. Neither a calculable program score nor nonzero between-sample variation constitutes replication. Agreement with genes used to construct a score is mechanically dependent and is not independent evidence of the underlying multigene structure. The analysis must specify which non-tautological property of each frozen program it tests and which alternative explanations its controls address.

This notebook does not discover or refit programs, reconstruct the CPTAC-3 source cohort, predict clinical drug resistance, estimate treatment effects, validate drug response, infer causal epigenetic mechanisms or demonstrate perturbational reversal. An external transcriptomic pattern, if supported, remains a computational association subject to validation.

## 2. Reference programs and external study population

The reference objects are the **three immutable Phase 4 consensus transcriptomic programs**, with their frozen gene identities, ordering, signs, loadings and associated reference metadata. The exact authoritative program artifacts and registry fingerprints must be resolved before calculations; no replacement from a similarly named working file is acceptable. The relevant feature universe contains **2,389 shared ordered genes**. Reference transformations and score definitions must be reconstructed from their executed Phase 4 specification, including the role of TMM/logCPM and gene standardization where applicable, without assuming that arbitrary alternative scaling preserves program interpretation.

The external source is the GDC `CPTAC-3` primary-tumor STAR Counts RNA-seq inventory constructed and audited under **Notebook 113 — CPTAC-3 External Cohort Construction and Eligibility**. Its proposed source membership contains **721 unique cases and 721 primary RNA files**:

| Harmonized TCGA lineage | Proposed cases |
| --- | ---: |
| TCGA-LUAD | 178 |
| TCGA-LUSC | 89 |
| TCGA-STAD | 142 |
| TCGA-SKCM | 138 |
| TCGA-PAAD | 82 |
| TCGA-UCEC | 56 |
| TCGA-HNSC | 36 |
| **Total** | **721** |

These are **source candidates**, not an automatically frozen inferential cohort. The corresponding 1,082-case primary-source universe, 361 non-proposed cases, separately tracked multiplicity and ambiguous-ancestry records, and precise inclusion reasons remain defined by the Notebook 113 contract. Do not rebuild, reselect, relabel or replace cases after examining external expression or program outcomes.

Externality is supported at the **cohort provenance** level; complete donor-level non-overlap with TCGA has not been genetically established. Missing independently comparable read-level sequencing QC is an explicit uncertainty, not a sample-level QC PASS or automatic rejection. These limitations accompany the interpretation of any external result.

## 3. Input acceptance and reproducibility checks

Before expression projection or inferential computations, read the exact locally generated `113_source_provenance_manifest.json`, `113_proposed_external_source_cohort.csv`, `113_primary_candidate_case_eligibility.csv` and `113_raw_count_compatibility.csv`. Recompute and compare the three recorded CSV SHA-256 fingerprints against the manifest; verify source identities, stable file and case IDs, permitted inclusion statuses, one source primary RNA file per case, all 721 proposed rows and the seven lineage totals. Read cohort-readiness and source-limitations statuses from the manifest rather than expecting a separate readiness file. Use the complete eligibility and attrition tables for denominator reconciliation rather than deriving a new cohort from filenames or clinical characteristics.

Verify the immutable Phase 4 loading vectors, ordered gene identities, reference representations and registry fingerprints independently. A missing input, checksum mismatch, unexpected duplicated case/file, contradictory status or incompatible program version **halts the affected analysis** pending source or reference correction. An integrity failure must not be bypassed by reconstructing membership inside Notebook 800.

Maintain a deterministic, versioned execution environment and recorded input hashes. Separate checks of file identity and raw-count compatibility from checks of biological analytical validity: passing the former is necessary but not sufficient for the latter.

## 4. Transcriptomic data preparation and program projection

The audited external input representation is the GDC STAR Counts **`unstranded` raw-count column**, with uniquely version-normalized Ensembl gene IDs, nonnegative integer values and all 2,389 required reference genes present in the 721 proposed files. The presence of all required identifiers does not itself establish numerical equivalence between platforms, library preparations or pipelines.

The analytical procedure must preserve the original programs: no gene-symbol substitution, arbitrary feature selection, absent-gene zero imputation, re-estimation of loadings, sign reversal or outcome-dependent normalization. Treat the expression normalization and gene-scaling choices as part of the measurement model, not as an opportunity to maximize replication.

**Required prospective specifications before projection:**

1. The exact input gene universe used for library normalization, filtering, offsets and any zero-count handling; the algorithm and package implementation, including version and parameters.
2. The relationship between the executed TCGA reference transformation and the external transformation, including whether scale parameters are estimated independently within CPTAC-3 or externally anchored to frozen TCGA reference quantities.
3. The projection formula for each frozen signed loading vector, the scaling domain, treatment of constant genes and handling of missing or nonfinite measurements.
4. A bounded normalization/projection sensitivity justified by technical comparability rather than by observed replication results.

Do not combine TCGA and CPTAC-3 to estimate normalization or standardization parameters in a manner that leaks external outcomes into the reference. Do not assume that an absolute score threshold learned in TCGA transfers to CPTAC-3. No external program scores should be computed for inferential purposes until the transformation and projection are approved and reproducible. Mark a comparison **not evaluable for input compatibility** if an essential measurement assumption cannot be supported.

## 5. Structural replication target and analysis design

The primary inferential target must be the **within-lineage external reproducibility of a clearly defined non-tautological property of each frozen signed multigene program**. The chosen property should distinguish coherent program structure from mere ability to calculate a fixed weighted sum.

An analysis design is not fully specified merely by naming a correlation, projection or score. Before examining CPTAC-3 replication statistics, define the target population, estimand, unit of analysis, test statistic, negative-control reference, uncertainty estimator and decision rule. Methods that compare independent or disjoint gene contributions, preservation of a reference multigene relationship, or other structural criteria may be evaluated for suitability, but **no single method is approved by this contract merely because it was proposed previously**.

Any chosen structural criterion must address:

- **Non-tautology:** do not treat a score–constituent-gene correlation, or a statistic algebraically implied by the score, as independent replication.
- **Frozen representation:** no learning or reweighting of program components using CPTAC-3 responses to the replication analysis.
- **Lineage awareness:** estimate evidence separately within each eligible lineage; between-lineage composition may not substitute for within-lineage structure.
- **Technical and biological alternatives:** clarify what the statistic can and cannot distinguish from shared library, proliferation, immune/stromal or purity effects.
- **Negative outcomes:** a failed or inconclusive test is reportable; do not alter the structure, membership or statistic to recover support.

A formal confirmatory structural claim requires the design details and justification to be frozen prospectively. Descriptive score summaries, visualization, exploratory correlations and technical feasibility summaries must be clearly labeled and must not be substituted for the structural test.

## 6. Negative controls and statistical inference

Negative controls must be chosen to challenge the property measured by the primary statistic, not merely to produce a favorable contrast. Their construction must preserve relevant gene-level and sample-level properties **to the extent necessary for the chosen estimand**—potentially reference expression abundance, detectability, signed loading distribution, program size, lineage or technical characteristics—without importing CPTAC program-replication results into selection or tuning. Unmatched random-gene controls alone should not be presumed sufficient. A null that reuses the tested signal or encodes the desired result is unacceptable.

Specify before inferential execution: the exact control-generation algorithm and eligibility universe; matching variables and tolerances; treatment of overlap with frozen program genes; deterministic seed(s); number of draws; target statistic; test direction; effect-size definition; uncertainty method; and any failure-to-match handling. Control validity and attainable matching quality must be reported even when results are unfavorable.

The primary multiplicity family must be defined over the **three programs and all lineages passing outcome-blind evaluability criteria**, without selecting comparisons on observed effect size. Prespecify the family-wise or false-discovery-rate procedure, the evidence threshold and the uncertainty reporting convention. The case, not a gene or technical replicate, is the independent observational unit to the extent supported by source provenance. Account for dependence among program tests and avoid treating repeated resampling draws as independent biological samples.

Report every planned program-by-lineage test, including negative, uncertain, unmatched-control and non-evaluable outcomes. Any cross-lineage synthesis requires an explicit stratified or hierarchical estimand and cannot replace the lineage-level findings.

**Statistical choices not yet approved:** primary structural estimand and statistic; control-matching and null procedure; resampling/uncertainty scheme; multiplicity method and threshold; and the role, if any, of direct TCGA-reference comparisons. These require scientific approval before confirmatory calculations.

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

**Readiness:** The 721-case cohort is proposed and raw-count feature compatibility has been assessed at source level. Its final inferential membership and the primary normalization/projection, structural estimand, controls, statistical decision rules and identifiable sensitivity analyses are **not yet frozen**. These decisions must be scientifically reviewed and documented before confirmatory execution; until then, no external structural-replication claim is warranted.
