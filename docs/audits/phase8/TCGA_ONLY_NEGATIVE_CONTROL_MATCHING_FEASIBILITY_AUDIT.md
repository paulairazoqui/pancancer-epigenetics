# Phase 8 TCGA-only negative-control matching feasibility audit

**Status:** exploratory methodological audit; not an external-replication
analysis and not a control-based inferential result.  Executed 2026-11-10.

## Scope and firewall

This audit used the Phase 2.205 TMM/logCPM TCGA matrix, the immutable Phase 4
gene membership and weights, and the CPTAC-3 *protein-coding identifier list*
only.  It read neither CPTAC-3 expression nor a TCGA--CPTAC-3 coexpression
statistic, score, edge, or replication outcome.  It did not alter the 2,389
frozen genes, signs, or weights.

The local checkout was at `660c270` on `main` before creating
`codex/phase8-negative-control-feasibility`.  Tracked changes were empty by
`git diff`; `git status` could not complete its untracked-file scan in this
OneDrive checkout.  GitHub PR #63 was verified separately as merged (merge
commit `1cb1a665...`); its merged §6.5 fixes the uncalipered pilot used here,
but that commit was not assumed to be present locally and this audit does not
edit the contract or Notebook 800.

## Frozen inputs and calculations

The shared technical universe has 18,123 TCGA genes, with 2,389 frozen genes
and 15,734 distinct alternatives.  For each of the seven pre-specified
lineages, candidates were characterised from TCGA samples only by mean
logCPM, sample SD of logCPM, and prevalence(logCPM > 0).  Percentile ranks use
the full 18,123-gene lineage universe and average ties, exactly as in Notebook
800's executed cells.

SMD is `(frozen weighted mean - alternative weighted mean) / SD(all genes in
the lineage)`.  The four required profiles are unweighted and absolute frozen
weights for each consensus program; acceptance is absolute SMD <= 0.10 for
each feature and profile.  This is a diagnostic gate, not a p-value.

## Results

### Strict-caliper feasibility: mathematical impossibility under the stated constraints

`maximum_bipartite_matching` finds the maximum possible cardinality of the
exact eligibility graph.  Consequently every nonzero entry below is a proof
that a 2,389-gene, distinct, within-caliper matching does not exist for that
caliper--not a greedy-assignment or solver failure.

| Lineage | Unmatched at 0.10 | Unmatched at 0.14 | Targets with no 0.10 candidate |
| --- | ---: | ---: | ---: |
| HNSC | 102 | 43 | 6 |
| LUAD | 56 | 22 | 4 |
| LUSC | 81 | 47 | 1 |
| PAAD | 114 | 49 | 1 |
| SKCM | 15 | 6 | 0 |
| STAD | 119 | 64 | 10 |
| UCEC | 78 | 30 | 0 |

Candidate availability was nevertheless broad for most targets (0.10-caliper
median candidate counts: 360--622; 90th percentiles: 1,007--1,139).  Thus the
failure is also caused by collisions among targets for the same alternatives,
not just isolated targets.  The full tables are in `tables/`.

### Unconditional balance bounds

For each feature/profile, the audit computes the attainable lower and upper
alternative mean after relaxing *all pairwise-distance constraints*.  It uses
the rearrangement inequality: for the lower extreme, it pairs the largest
absolute weights with the smallest selected alternative feature values; for the
upper extreme, it pairs the largest weights with the largest values.  The resulting minimum
absolute SMD is an optimistic mathematical lower bound.  No single
feature/profile bound exceeded 0.10 in any lineage.

This means that the observed SD deficit is **not proven impossible from the
candidate marginal distribution alone**.  It does not establish feasibility:
the bounds allow arbitrary pairings, ignore the other two features, and ignore
the individual-distance criteria.  They distinguish this from a demonstrated
global shortage of high-SD genes.

### Exploratory §6.5 full-cardinality assignment

The one prospectively specified alternative is rectangular, no-replacement
assignment over all 15,734 candidates, minimizing the sum of three-feature
Euclidean percentile-rank distances, with no hard caliper.  STAD was run first
and then the unchanged procedure was extended to the other six lineages.  It
gave full coverage and uniqueness everywhere, but failed the joint SMD gate in
every lineage, principally due to `sd_logcpm`.

| Lineage | SD SMD (unweighted) | TX01 | TX02 | TX03 | Pair gaps >0.10 / >0.14 | Max coordinate gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| HNSC | 0.141 | 0.166 | 0.204 | 0.192 | 276 / 186 | 0.368 |
| LUAD | 0.216 | 0.222 | 0.244 | 0.215 | 258 / 150 | 0.349 |
| LUSC | 0.251 | 0.284 | 0.383 | 0.283 | 385 / 238 | 0.467 |
| PAAD | 0.160 | 0.198 | 0.180 | 0.195 | 308 / 215 | 0.393 |
| SKCM | 0.170 | 0.193 | 0.290 | 0.176 | 88 / 44 | 0.312 |
| STAD | 0.193 | 0.209 | 0.236 | 0.211 | 324 / 235 | 0.390 |
| UCEC | 0.166 | 0.162 | 0.194 | 0.172 | 301 / 185 | 0.358 |

All 28 variability SMDs exceed 0.10.  Additional mean-logCPM failures occur
for TX02/HNSC and TX01--03/LUSC.  Therefore full cardinality is coverage only;
it is not a scientifically acceptable matched control under the currently
stated diagnostic.

## Comparison and recommendation

| Strategy | Optimises / preserves | Result | Interpretation |
| --- | --- | --- | --- |
| Strict maximum-cardinality, 0.10 | Exact three-rank eligibility, uniqueness | Incomplete in 7/7 | Demonstrated infeasibility under contractual caliper |
| Strict maximum-cardinality, 0.14 | Same, relaxed fixed caliper | Incomplete in 7/7 | Demonstrated infeasibility under this exploratory relaxation |
| Uncalipered minimum Euclidean assignment (§6.5) | Coverage, uniqueness, total individual distance | 2,389 unique genes in 7/7; fails balance in 7/7 | Valid coverage diagnostic, invalid matched-control construction |
| Explicit global balance-constrained optimisation | Could enforce SMD jointly with distances | Not run | Exploratory alternative, not a rescue: needs a frozen multiobjective and acceptance rule before inspection |

An optimisation with explicit unweighted and three weighted global balance
constraints could improve on individual-distance minimisation.  It would be a
different exploratory design, however, and would need to specify all four
profiles, all three features, a fixed distance trade-off, and a single solver
formulation prospectively.  Searching penalty weights after these failures
would be outcome-driven method selection.  It is computationally more demanding
than the 2,389 x 15,734 assignment and, even if it finds a solution, would
need its own diversity and exchangeability assessment.

**Recommendation:** it is not scientifically defensible to construct the
proposed complete matched controls under the current requirements.  Complete
sets are computationally viable, but neither evaluated valid construction
satisfies coverage plus individual comparability plus all required balance.
Do not use the current full assignments as negative controls or interpret any
control rank as a p-value.

Defensible next options require approval: (1) prospectively replace this
matched-gene null with a control matched to the eventual structural estimand
rather than gene marginals; (2) approve one explicit constrained global
optimisation as an exploratory feasibility test, with failure retained as a
result; or (3) accept that no complete gene-matched null is available and use
only clearly labelled descriptive/sensitivity comparisons.  None authorizes
TCGA--CPTAC-3 comparison.

## Reproducibility

Run the script once per lineage in constrained environments (as done here),
or without `--lineage` where sufficient time is available:

```powershell
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-STAD
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-HNSC --extend-uncalipered-all
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-LUAD --extend-uncalipered-all
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-LUSC --extend-uncalipered-all
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-PAAD --extend-uncalipered-all
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-SKCM --extend-uncalipered-all
python scripts/phase8_audit_negative_control_feasibility.py --lineage TCGA-UCEC --extend-uncalipered-all
python scripts/phase8_audit_negative_control_feasibility.py --bounds-only --skip-uncalipered-stad-pilot --lineage TCGA-STAD
python scripts/phase8_audit_negative_control_feasibility.py --consolidate-lineage-outputs
```

The bounds-only command is the targeted post-review regeneration route; repeat
it across the seven lineages before consolidation. The provenance JSON records
Python and package versions. No seed is needed: all methods are deterministic.
Five compact output tables retain caliper feasibility, availability,
unconditional bounds, full-assignment balance diagnostics, and provenance; no
expression matrices, pairwise correlations, or gene-level maps are stored.

## Approval required before continuing

1. Whether to accept the negative feasibility conclusion and abandon complete
   gene-matched controls under the current gate.
2. If an additional exploratory constrained optimisation is desired, its exact
   objective/constraints and a precommitted decision rule.
3. The primary structural estimand and a statistically calibrated null before
   any external TCGA--CPTAC-3 analysis.
