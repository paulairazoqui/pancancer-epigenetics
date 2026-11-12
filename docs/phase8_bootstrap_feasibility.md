# Phase 8 bootstrap feasibility — temporary technical note

Run `python scripts/phase8/bootstrap_feasibility.py --output-dir audit_outputs/phase8_bootstrap_feasibility` from the repository root. The utility validates registered frozen TCGA inputs and uses only the contractual CPTAC-3 counts; it never reads CPTAC-3 expression.

Recommendation for Notebook 800: use a tumour/case-level, within-lineage paired bootstrap with 1,000 retained attempts. Resample TCGA and CPTAC-3 independently to their original cohort sizes; reuse each cohort's resample indices and its correlation matrix across all three frozen programs. Report 2.5th–97.5th percentile descriptive intervals for `T`, `Delta_M`, and cohort-specific signed coherence (weighted median primary; weighted mean sensitivity). Orient coherence edges by `sign(w_i w_j)`. For a between-cohort coherence contrast, take the contrast inside each joint bootstrap draw. These are uncertainty summaries, not tests or replication decisions.

Before running a lineage, preflight both frozen expression matrices: exact ordered 2,389-gene identity, one weight per gene/program in that order, sample/metadata column correspondence, one independent tumour per case, finite expression, nonzero gene variance, and positive finite edge-weight total. A bootstrap attempt is invalid only for an explicit computational/math condition (zero/nonfinite gene variance, nonfinite correlations, nonpositive weighted-Pearson denominator, or nonfinite statistic). Record its reason and attempt number; do not replace values, delete genes, or silently drop it. Redraw until 1,000 valid draws or a cap of 1,100 attempts. Mark a lineage technically non-evaluable if preflight fails or if the cap cannot yield 1,000 valid draws. A wide interval or an extreme result is imprecision, not non-evaluability.

The script performs the limited required checks: frozen-artifact integrity and TCGA contract counts; synthetic percentile stability at budgets 200/500/1,000; and TCGA-only correlation timings at `n=36`, `56`, and `103`. For a conservative serial estimate, multiply the benchmarked paired-draw cost (two correlations plus the three-program summaries for both cohorts) by 7,000 (seven lineages × 1,000). Matrix peak storage is roughly two 2,389-square double matrices plus edge vectors, ordinarily below 250 MiB if matrices are released per draw. The actual runtime is reported by the local benchmark rather than inferred from CPTAC-3 expression.

The common procedure is feasible in principle for all seven contractual lineages. HNSC (CPTAC-3 `n=36`) and UCEC (`n=56`) have the greatest sampling uncertainty; SKCM (`n=103` TCGA) is the smallest TCGA cohort. LUAD, LUSC, PAAD, STAD have larger smallest cohorts. None of these sizes is automatically a technical failure. `Delta_M` remains sample-size-sensitive even with percentile intervals; retain it as descriptive only.

| Lineage | n TCGA | n CPTAC-3 | Feasibility | Technical risk | Recommendation |
| --- | ---: | ---: | --- | --- | --- |
| HNSC | 520 | 36 | Candidate | Largest sampling uncertainty | Run common preflight/bootstrap; label imprecision. |
| LUAD | 512 | 178 | Candidate | None beyond standard preflight | Run common procedure. |
| LUSC | 500 | 89 | Candidate | Moderate CPTAC-3 sampling uncertainty | Run common procedure. |
| PAAD | 178 | 88 | Candidate | Moderate two-cohort sampling uncertainty | Run common procedure. |
| SKCM | 103 | 138 | Candidate | Smallest TCGA cohort | Run common procedure; label imprecision. |
| STAD | 412 | 142 | Candidate | None beyond standard preflight | Run common procedure. |
| UCEC | 543 | 56 | Candidate | High CPTAC-3 sampling uncertainty | Run common procedure; label imprecision. |

The bounded run completed its `n=36`, `56`, and `103` TCGA resamples without a degeneracy. In the synthetic `n=36` cohort, some valid draws contained only 17 unique tumours, confirming that low uniqueness is not itself a failure. Synthetic `T` percentile widths were 0.302, 0.300 and 0.298 at 200, 500 and 1,000 draws respectively; the 2.5th/97.5th endpoints changed by 0.004/0.007 from 200 to 500 and by 0.0001/0.002 from 500 to 1,000. On this workstation, a 2,389-gene correlation used 0.03–0.13 seconds and about 43.5 MiB; calculating all three programs' summaries for one cohort used 2.5–3.2 seconds, mostly because exact weighted medians require ordering 2.85 million edges. Thus 1,000 joint draws for all lineages are approximately 9–13 serial CPU-hours (two cohorts per draw), readily reducible by independent lineage-level workers subject to memory availability.

Document, rather than automatically adjust, purity, cellular composition, proliferation, within-lineage subtype mix, platform/technical effects, and TCGA/CPTAC-3 selection differences. They limit biological interpretation, not computation. No external expression result, p-value, threshold, or success/failure criterion is produced here.
