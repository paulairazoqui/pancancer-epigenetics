# Phase 7 Analysis Contract

## Lifecycle / execution status

This contract is established prospectively before Phase 7 perturbational
connectivity results are inspected.

Notebook 110 — LINCS/CMap Acquisition and Audit — performed a restricted,
outcome-blind prerequisite characterization stage before creation of this
contract. That prerequisite stage was limited to:

- raw-resource integrity and schema validation;
- dimensional and identifier concordance between the Level 5 GCTX resource and
  LINCS metadata;
- tumor-cell-line and lineage annotation coverage;
- frozen Phase 4 program representation fidelity in landmark, BING, and full
  LINCS gene spaces;
- outcome-blind primary perturbagen coverage;
- replicate and condition hierarchy characterization;
- perturbagen, structure, target, and mechanism-annotation identity audits; and
- publication of stable frozen Phase 7 handoff artifacts.

No program–perturbagen connectivity score, empirical-null p-value, multiplicity
result, compound prioritization result, or mechanism-of-action aggregation
result was inspected during notebook 110.

Notebook 110 therefore serves as a prerequisite acquisition/audit and handoff
stage. It must not be represented as a Phase 7 connectivity analysis or as
having prospectively frozen decisions that were not yet made at that time.

The scientific decisions in this contract were frozen after review of the
outcome-blind notebook-110 handoff and before Phase 7 connectivity execution.

A prospective operational-freeze addendum was established on 2026-09-28,
before inspection of any Phase 7 connectivity result. That addendum freezes the
query-null stratification, permutation coupling, competitive-null role,
sequential Monte Carlo family and exceedance target, random-number generator,
numerical policy, CMap-style sensitivity, perturbational diagnostics, artifact
interfaces, and validation policy described below.

The only primary inferential simulation parameter intentionally left unresolved
after this operational package is the final `Bmax`. Its candidate ladder and
selection rule are frozen, but the final value must be selected prospectively
after an outcome-blind computational benchmark under a resource envelope that
is itself frozen before the benchmark is run.

No observed program–perturbagen connectivity, ranking, p-value, q-value, or
compound result may be inspected before that final `Bmax` freeze.

Once Phase 7 connectivity execution begins, primary program representation,
connectivity definition, analytical hierarchy, empirical-null family,
multiplicity family, sensitivity roles, chemical-identity rules, or
interpretation thresholds must not be changed on the basis of whether they
produce more favorable results.

The authoritative executable records will be:

- `700 — Program Signature Construction`;
- `701 — Connectivity Analysis`;
- `702 — Compound Prioritization`; and
- `703 — Mechanism-of-Action Aggregation`.

---

## Status

Scientific design frozen prospectively.

Phase 7 analytical execution has not begun.

The 2026-09-28 operational package is prospectively frozen. The final primary
Monte Carlo `Bmax` remains pending an outcome-blind benchmark under a
prospectively fixed resource envelope. Notebook 701 primary inferential
execution remains blocked until that final value is recorded.

This contract defines the analytical decisions governing:

- frozen consensus-program query representation;
- primary signed connectivity;
- lineage-aware aggregation;
- empirical-null calibration;
- multiplicity;
- perturbational and representation sensitivities;
- proliferation/stress contextual diagnostics;
- perturbagen and chemical-structure handling;
- compound-level prioritization boundaries; and
- mechanism-of-action aggregation.

---

## Operational freeze addendum — 2026-09-28

This addendum was established before inspection of any Phase 7 connectivity
result.

It prospectively freezes the following operational decisions:

1. gene-level perturbational dispersion is the unscaled median absolute
   deviation (MAD) across the 362,036 frozen primary Level 5 signatures;
2. null strata are defined as LINCS feature space
   (`landmark` versus `best inferred`) × deterministic MAD decile;
3. the primary conditional null has no arbitrary minimum query-gene count per
   stratum;
4. primary-null permutations are coupled across the three frozen consensus
   programs by permuting each gene's complete three-program signed-weight vector
   jointly within stratum;
5. the competitive pseudo-program null is a descriptive robustness analysis
   restricted prospectively to hypotheses with primary
   `q_global <= 0.05`; it uses 10,000 fixed pseudo-program draws and cannot
   create or rescue primary support;
6. primary Monte Carlo inference uses the truncated Besag–Clifford sequential
   procedure with exceedance target `h = 20`;
7. the candidate maximum-draw ladder is
   `500000 -> 250000 -> 100000`; the largest candidate satisfying the frozen
   resource envelope will be selected before observed connectivity is
   inspected;
8. randomization uses NumPy `PCG64DXSM` with
   `SeedSequence(entropy=701, spawn_key=(namespace, replicate_id))`, where
   namespace `1` is the primary conditional null and namespace `2` is the
   competitive-null sensitivity; `replicate_id` is zero-based;
9. source GCTX values may remain stored/read as `float32`, while dot products,
   norms, cosine scores, WTCS calculations, medians, and inferential
   aggregations are evaluated in `float64`;
10. primary null extremeness is defined by
    `null_score <= observed_score` for the one-sided negative tail;
11. primary Monte Carlo outputs are termed
    `conditional randomization p-values` and are interpreted only relative to
    the prospectively specified conditional pseudo-program null;
12. the CMap-style sensitivity uses fixed 150-gene up and 150-gene down sets
    selected by frozen Phase 4 BING weights, then treats membership as
    directional but unweighted and reports raw WTCS only;
13. perturbational amplitude/reproducibility context uses the provider-defined
    LINCS `tas`, `ss_ngene`, and `cc_q75` fields; no project-defined BING
    RMS metric is added;
14. proliferation/stress diagnostics use only the five prospectively frozen
    Hallmark sets and a transparent mean signed Level 5 z-score over available
    BING genes;
15. stable Phase 7 artifact namespaces and roles are frozen below, while
    transient null batches and matrix chunks are not registry artifacts; and
16. structural identities are validated exactly, whereas floating-point
    algorithms are validated against small independent `float64` reference
    implementations using method-specific tolerances.

This addendum does not change the scientific estimand or reopen any frozen
upstream object.

---

## Purpose

Phase 7 evaluates whether perturbational signatures in the audited LINCS/CMap
resource show inverse computational association with the three frozen Phase 4
cross-system consensus transcriptomic programs.

The phase is designed to generate conservative perturbational hypotheses while
preserving:

- the frozen Phase 4 program definitions;
- the outcome-blind LINCS analytical universe established in notebook 110;
- provider-defined Level 5 signature structure;
- experimental hierarchy;
- lineage balance;
- explicit empirical-null calibration;
- global multiplicity control;
- chemical-identity uncertainty; and
- separation from Phase 5 and Phase 6 evidence.

Positive, negative, heterogeneous, lineage-restricted, technically limited, or
not-evaluable results are all valid Phase 7 outcomes.

---

## Scientific positioning

Phase 7 addresses the following general questions:

> Do perturbational signatures show inverse computational association with a
> frozen cross-system consensus transcriptomic program?

> Are those inverse associations more extreme than expected under a
> prospectively specified conditional pseudo-program null?

> Are the primary results stable to prespecified perturbational,
> representation, lineage-composition, and competitive-null sensitivities?

> Do chemically distinct perturbagens annotated to related mechanisms show
> descriptively concordant perturbational patterns?

Phase 7 does not establish:

- therapeutic efficacy;
- therapeutic reversal;
- causal reversal of a biological state;
- validated drug targets;
- validated mechanisms of action;
- clinical drug sensitivity;
- clinical resistance prediction;
- longitudinal adaptive resistance;
- pharmacological independence merely because several LINCS perturbagen
  identifiers are present; or
- external validation from subsets of the same LINCS/CMap perturbational
  ecosystem.

A negative primary connectivity score may be described as an
`inverse computational association`.

It must not be described as therapeutic reversal.

---

# Frozen upstream inputs

Phase 7 consumes frozen upstream artifacts without reopening their construction,
selection, orientation, or eligibility.

## Frozen consensus transcriptomic programs

The Phase 7 program universe is restricted to:

- `CONSENSUS_TX_01`;
- `CONSENSUS_TX_02`; and
- `CONSENSUS_TX_03`.

Their frozen signed gene weights are inherited from:

`phase4.401.consensus_transcriptomic_gene_weights`

Program orientation, sign, weight magnitude, membership, and identity must not
be changed according to Phase 7 perturbational results.

Phase 7 must not:

- discover replacement programs;
- rotate program orientation;
- re-estimate weights from LINCS;
- remove a frozen program because its perturbational result is weak;
- rename a program according to a favorable perturbagen;
- use Phase 5 or Phase 6 evidence to alter program representation; or
- use downstream mechanism annotations to redefine the query.

---

## Frozen LINCS/CMap handoff

Notebook 110 publishes the authoritative Phase 7 LINCS/CMap handoff artifacts:

- `phase1.110.raw_input_inventory`;
- `phase1.110.program_representation_fidelity`;
- `phase1.110.bing_gene_handoff`;
- `phase1.110.landmark_gene_handoff`;
- `phase1.110.primary_signature_handoff`;
- `phase1.110.primary_perturbagen_coverage`; and
- `phase1.110.primary_compound_annotation`.

These artifacts are frozen upstream inputs.

Phase 7 must consume them rather than silently reconstructing the notebook-110
eligibility universe.

---

# Primary perturbational universe

The primary Phase 7 perturbational universe is the frozen notebook-110
Level 5 `trt_cp` universe satisfying all of the following:

- `qc_pass == 1`;
- tumor cell line;
- explicitly annotated non-unknown lineage;
- complete dose metadata;
- complete time metadata;
- at least 5 unique tumor cell lines per perturbagen; and
- at least 4 unique annotated lineages per perturbagen.

The authoritative frozen primary universe contains:

- 362,036 Level 5 perturbational signatures; and
- 7,914 perturbagens.

No perturbagen may be added to or removed from this primary universe according
to observed Phase 7 connectivity.

The `is_hiq` field is not a primary inclusion criterion.

A stricter `is_hiq` analysis is a prespecified sensitivity and must
independently satisfy the same 5-cell-line / 4-lineage perturbagen support rule.

Normal-cell, pool, and tumor unknown-lineage contexts are outside the primary
universe. They must not be introduced as primary evidence or used to rescue a
failed primary result.

---

# Primary gene space and query representation

## BING as the primary query space

Notebook 110 established BING as the primary Phase 7 representation space using
outcome-blind fidelity to the frozen Phase 4 program weights.

For each frozen program:

- 2,389 Phase 4 genes are present in the original frozen representation;
- 1,769 have exact LINCS representation;
- 1,495 are represented in BING; and
- 90 are landmark genes.

The 1,495-gene BING representation is the primary query representation.

The landmark-only representation is a prespecified sensitivity and must not
replace or rescue the BING primary analysis.

The lower negative-arm retention observed for `CONSENSUS_TX_03` in BING is a
frozen representation limitation and must remain visible in interpretation.

---

## Continuous signed weighted representation

The primary program query is continuous, signed, and weighted.

For each program, the authoritative Phase 4 weights are restricted to its
frozen 1,495-gene BING support.

Phase 7 must not:

- binarize the primary query;
- reweight genes according to LINCS behavior;
- re-estimate weights from perturbational signatures;
- select genes according to connectivity;
- alter positive/negative-arm balance after result inspection; or
- use the CMap-style discrete sensitivity to redefine the primary query.

---

# Primary connectivity definition

For perturbational signature `s` and frozen program `p`, the primary
connectivity score is the signed cosine similarity over the program's frozen
BING support `G_p`:

```text
C[s,p] =
    sum_g(w[p,g] * z[s,g])
    / (sqrt(sum_g(w[p,g]^2)) * sqrt(sum_g(z[s,g]^2)))
```

where:

- (w_{p,g}) is the frozen Phase 4 signed program weight; and
- (z_{s,g}) is the Level 5 perturbational signature value.

Genes outside the frozen program support do not enter the primary cosine
denominator.

The primary inferential direction is negative.

More-negative scores indicate stronger inverse computational association.

Positive scores remain valid observed data but do not support the primary
inverse-association hypothesis.

No post hoc transformation, recentering, rank selection, or alternate
normalization may replace the primary cosine according to observed results.

---

# Experimental hierarchy and pseudoreplication control

Notebook 110 established that Level 5 signatures are provider-defined
replicate-collapsed units and that multiple Level 5 signatures may still share
the same nominal perturbagen, cell line, dose, and time.

Phase 7 therefore preserves the frozen hierarchy:

1. score individual Level 5 signatures;
2. summarize signatures sharing
   `pert_id × cell line × dose × time` by median;
3. summarize dose-level condition scores by median within each time point;
4. summarize time-point scores by median to one
   `pert_id × cell line` score.

No:

- best signature;
- best dose;
- best time point;
- best cell line; or
- best lineage

may be selected according to favorable connectivity.

---

# Lineage-aware primary aggregation

After the frozen notebook-110 hierarchy produces one score per
`pert_id × cell line`, the primary cross-cell aggregation is lineage-aware.

For perturbagen `j` and lineage `l`:

```text
C[j,l] = median over cell lines c in lineage l of C[j,c]
```

The final primary perturbagen score is:

```text
C[j] = median over evaluable lineages l of C[j,l]
```

Each evaluable lineage therefore contributes one lineage-level summary,
regardless of the number of represented cell lines.

Primary outputs must preserve at minimum:

- the lineage-specific scores;
- the number of evaluable lineages;
- the number of evaluable cell lines;
- inter-lineage dispersion; and
- the fraction of evaluable lineages with negative connectivity.

These quantities provide breadth and heterogeneity context.

They do not constitute alternate significance gates.

A direct pooled-cell-line aggregation that does not equalize lineages is a
prespecified composition sensitivity only.

It cannot rescue a failed primary result.

---

# Primary empirical null

## Conditional fixed-support null

Primary empirical calibration uses a conditional pseudo-program null.

For each frozen program, the primary null:

- retains the exact 1,495-gene BING support;
- retains the observed LINCS perturbational data for those genes;
- retains the complete set of frozen signed program weights;
- retains the number of positive and negative weights;
- retains the weight-magnitude distribution and associated L1/L2 norms; and
- randomizes the correspondence between genes and signed weights within
  prospectively defined gene strata.

The purpose of the primary null is to test whether the observed signed/weighted
configuration of the independently frozen program shows a more extreme inverse
association than comparable configurations on the same gene support.

This is a conditional null.

It is not a universal null of "no biological relationship."

The resulting empirical p-value must be interpreted only relative to the
prospectively specified randomization mechanism.

---

## Primary-null stratification

The primary null must stratify weight reassignment using technical and
perturbational gene properties determined without inspecting connectivity
results.

At minimum the stratification must preserve:

- LINCS feature space, distinguishing landmark from best-inferred genes; and
- a prospectively frozen measure of gene-level perturbational dispersion.

Perturbational dispersion is defined for every BING gene as the unscaled
median absolute deviation across the 362,036 frozen primary Level 5 signatures:

```text
MAD[g] = median_s( abs(z[s,g] - median_s(z[s,g])) )
```

MAD is used only as an outcome-blind nuisance-matching quantity.

Genes are first separated by LINCS feature space:

- landmark; and
- best inferred.

Within each feature space, all BING genes are ordered deterministically by:

1. ascending MAD; then
2. ascending `gene_id`.

The ordered genes are divided into 10 deterministic groups whose sizes differ
by at most one. These groups are the MAD deciles used for null stratification.
This rank-based construction avoids data-dependent handling of duplicated
quantile boundaries.

The primary conditional null imposes no arbitrary minimum number of query genes
per stratum. If a stratum contains only one query gene, that gene's weight
vector remains fixed for that stratum in that null replicate.

The three frozen program weights associated with one gene are treated as one
three-component signed-weight vector. Within each
`feature_space × MAD_decile` stratum, the same permutation of gene rows is
applied jointly to all three programs.

Thus the primary null preserves:

- exact query gene membership;
- exact feature-space composition;
- exact per-program signed-weight multisets;
- cross-program weight geometry;
- stratum-level perturbational-dispersion composition; and
- the observed perturbational data and their gene-gene correlation structure.

No stratum definition may be tuned according to p-values, compound rankings,
or favorable connectivity.

---

## Competitive pseudo-program null sensitivity

A secondary competitive-null sensitivity will compare the observed program
against pseudo-programs constructed from the broader BING space using matched
gene resampling.

This sensitivity is intended to address a different question from the primary
conditional null:

> Is the observed inverse association also unusual relative to technically
> comparable pseudo-programs with different gene membership?

The competitive sensitivity is restricted prospectively to
`program × pert_id` hypotheses satisfying the primary global criterion
`q_global <= 0.05`.

For each program, pseudo-program membership is sampled from the broader BING
space after excluding the program's real 1,495-gene BING support.

Replacement genes must match the query requirement within the same:

`feature_space × MAD_decile`

and are sampled without replacement within each pseudo-program.

The competitive sensitivity preserves:

- query size;
- the complete signed-weight multiset;
- landmark / best-inferred composition; and
- MAD-decile composition.

If a stratum has fewer eligible background genes than required replacements,
it is merged deterministically with the adjacent MAD decile in the same feature
space whose median MAD is closest. If both adjacent bins are equally close, the
lower-numbered bin is selected. Merging is repeated only until sufficient
background genes exist.

Exactly 10,000 competitive pseudo-program draws are generated.

For an observed negative-tail score, the descriptive competitive-null quantity
is:

```text
competitive_null_tail_fraction = (g + 1) / 10001
```

where `g` is the number of competitive-null scores less than or equal to the
observed score.

This quantity is not named a p-value, receives no BH/BY correction, has no
PASS/FAIL threshold, and cannot create, replace, redefine, or rescue primary
support.

---

# Monte Carlo inference

Primary empirical p-values are one-sided for the negative tail.

Monte Carlo inference must use a formal prospectively specified sequential
procedure rather than informal early stopping.

The procedure must satisfy all of the following:

- random-number generation is deterministic and reproducible;
- seeds are frozen before execution;
- stopping rules are frozen before execution;
- p-values are never reported as zero solely because no sampled null replicate
  exceeded the observed statistic;
- the same analytical hierarchy and lineage aggregation are applied to observed
  and null program scores;
- stopping must not depend on observed BH/q-value outcomes; and
- no tail extrapolation or alternate parametric approximation may be introduced
  after result inspection.

Primary inference uses the truncated Besag–Clifford sequential Monte Carlo
procedure with exceedance target:

`h = 20`

For each primary hypothesis, a null draw is counted as at least as extreme when:

```text
null_score <= observed_score
```

If the twentieth exceedance is reached after `L` null draws before
`Bmax`, the conditional randomization p-value is:

```text
p_conditional = 20 / L
```

If `Bmax` is reached with `g < 20` exceedances:

```text
p_conditional = (g + 1) / (Bmax + 1)
```

A p-value of zero is not permitted.

The candidate `Bmax` ladder is frozen as:

```text
500000 -> 250000 -> 100000
```

Notebook 700 must run an outcome-blind computational benchmark using the same
matrix access pattern and null-scoring operations but synthetic/permuted query
weights that do not reveal observed program–perturbagen connectivity.

Before that benchmark is run, the execution resource envelope must itself be
frozen. The final `Bmax` is the largest candidate in the frozen ladder that
satisfies that resource envelope. The selected value must be recorded in this
contract before any observed primary connectivity result is inspected.

Randomization uses NumPy `PCG64DXSM` with:

```text
SeedSequence(entropy=701, spawn_key=(namespace, replicate_id))
```

where:

- namespace `1` = primary conditional null;
- namespace `2` = competitive-null sensitivity; and
- `replicate_id` is zero-based.

The generator stream for a replicate must therefore be independent of batch
size or execution partitioning.

The exact NumPy/environment versions used for execution must be persisted in
analysis metadata.

Source GCTX values may remain stored/read as `float32`. Dot products, norms,
cosines, WTCS calculations, medians, empirical-null aggregations, and p-value
calculations must use `float64`.

Batch size is an engineering parameter and may change to fit memory provided
that it does not change random streams, analytical membership, or validated
numeric outputs.

Computational inconvenience is not a valid reason to alter the null after
results are observed.

---

# Primary hypothesis family and multiplicity

The primary hypothesis family contains:

```text
3 programs × 7,914 perturbagens = 23,742 hypotheses
```

Each hypothesis tests the prespecified negative-tail inverse-association
question for one frozen program and one frozen primary perturbagen.

Primary multiplicity control is global Benjamini–Hochberg FDR across all
23,742 primary empirical p-values.

The primary significance threshold is:

`q_global <= 0.05`

Program-specific BH-adjusted values may be reported as descriptive/sensitivity
context.

They do not rescue a hypothesis that fails the global primary family.

A global Benjamini–Yekutieli correction may be reported as a conservative
dependence sensitivity.

It does not replace the primary BH family and cannot create additional primary
support.

The analysis must not claim that BH guarantees exact 5% FDR under arbitrary
dependence.

---

# Prespecified sensitivities

The following sensitivities are prospectively defined and must remain separate
from primary inference:

- landmark-only program representation;
- stricter `is_hiq` perturbational signatures with independent preservation
  of the frozen 5-cell-line / 4-lineage support rule;
- pooled-cell-line aggregation without equal-lineage weighting;
- fixed CMap-style up/down query;
- competitive matched pseudo-program null;
- program-specific BH summaries; and
- global BY multiplicity sensitivity.

Sensitivity analyses may evaluate:

- effect-size correlation;
- direction concordance;
- ranking stability;
- lineage-composition dependence;
- representation dependence; and
- stability of primary FDR-supported findings.

A sensitivity result must not be used to declare primary support when the
primary analysis fails.

No favorable sensitivity may be selected post hoc as the preferred analysis.

---

# CMap-style up/down sensitivity

The conventional discrete-query sensitivity uses:

- the 150 largest positive frozen BING weights; and
- the 150 largest-magnitude negative frozen BING weights

for each program.

This is a fixed CMap-style rank-based sensitivity.

It is not the primary program representation.

It must not be described as a reproduction of the complete CLUE/CMap
normalization or tau pipeline unless that full procedure is explicitly
implemented and validated.

Frozen Phase 4 weights are used only to select membership in the two query
arms.

For each program:

- the 150 genes with the largest positive frozen BING weights form the up arm;
- the 150 genes with the most negative frozen BING weights form the down arm;
- ties at the selection boundary are resolved by ascending `gene_id`; and
- after selection, query membership is directional but unweighted.

Each Level 5 signature is ranked across all 10,174 BING genes by:

1. descending signature z-score; then
2. ascending `gene_id`.

For one query arm `S`, the raw enrichment score is the signed maximum
absolute deviation of a weighted running-sum statistic. A hit contributes
`abs(z)` normalized by the total `abs(z)` over genes in `S`; a miss
contributes `1 / (N - |S|)`. If multiple positions share the same maximum
absolute deviation, the earliest rank position is used.

Let the resulting arm scores be `ES_up` and `ES_down`. Raw WTCS is:

```text
WTCS = (ES_up - ES_down) / 2
       if ES_up and ES_down have opposite signs
WTCS = 0
       otherwise
```

If the hit-weight denominator for an arm is exactly zero, that signature's
CMap-style sensitivity score is marked not evaluable rather than rescued by an
alternate statistic.

Only raw WTCS is used.

No normalized connectivity score (NCS), tau transformation, alternate
gene-count cutoff, or alternate enrichment statistic may be introduced as a
result-dependent replacement.

---

# Perturbational amplitude, proliferation, and stress diagnostics

Phase 7 will prospectively characterize broad perturbational context without
using those diagnostics as primary exclusion gates.

## Perturbational amplitude

Perturbational activity/reproducibility context is restricted to the
provider-defined LINCS quantities:

- `tas`;
- `ss_ngene`; and
- `cc_q75`.

No project-defined BING RMS or other ad hoc global-amplitude metric is added.

These fields are summarized through the same condition → dose/time → cell-line
→ lineage hierarchy when perturbagen-level context is required.

They must be described as perturbational activity/reproducibility diagnostics.

They are not direct cytotoxicity measurements.

## Proliferation-related context

The frozen MSigDB Hallmark resource may be used prospectively to summarize:

- `HALLMARK_E2F_TARGETS`; and
- `HALLMARK_G2M_CHECKPOINT`.

## Stress/apoptosis-related context

The prospectively defined stress-context panel is limited to:

- `HALLMARK_P53_PATHWAY`;
- `HALLMARK_APOPTOSIS`; and
- `HALLMARK_UNFOLDED_PROTEIN_RESPONSE`.

For each Hallmark diagnostic and Level 5 signature, the diagnostic score is the
mean signed Level 5 z-score across Hallmark genes represented in BING.

The implementation must retain:

- total Hallmark gene count;
- BING-represented Hallmark gene count;
- BING coverage fraction; and
- overlap with each frozen consensus-program support.

Diagnostic scores are summarized through the same experimental and
lineage-aware hierarchy used for perturbagen context.

No Hallmark p-value, enrichment FDR, or diagnostic PASS/FAIL threshold is part
of Phase 7.

No additional stress pathway may be introduced because it explains a favorable
or unfavorable observed compound.

The overlap between each diagnostic gene set and each frozen consensus program
must be quantified so that mathematical overlap is not presented as independent
biological evidence.

These diagnostics:

- do not exclude perturbagens from the primary universe;
- do not modify p-values or q-values;
- do not rescue primary results; and
- do not establish direct cytotoxicity.

A strong inverse association accompanied by a broad stress-like transcriptional
response must remain in the analysis with correspondingly cautious
interpretation.

---

# Isolation from Phase 5 and Phase 6 evidence

Phase 5 functional-vulnerability evidence and Phase 6 pharmacogenomic/XAI
evidence must not define, filter, rescue, or reorder the Phase 7 primary
perturbagen universe.

They must not determine:

- which perturbagens are scored;
- which programs are retained;
- which p-values enter the primary family;
- empirical-null construction;
- connectivity thresholds;
- sensitivity selection; or
- compound-level primary significance.

Cross-evidence integration belongs to Phase 9.

Phase 7 results may later be joined to Phase 5 and Phase 6 evidence only after
the Phase 7 primary analysis and status fields are frozen.

---

# Perturbagen identity

The primary experimental perturbagen unit is the LINCS:

`pert_id`

`cmap_name` is descriptive metadata and is not an analytical identity key.

Target and mechanism-of-action annotations are many-to-many and incomplete.

Missing annotation must not be interpreted as biological absence.

Distinct `pert_id` values remain distinct experimental units during notebook
701 even when they share a usable chemical structure identifier.

Structure-aware reconciliation occurs only after primary perturbagen-level
connectivity inference.

---

# Notebook 702 chemical-structure reconciliation

Notebook 702 must preserve the primary notebook-701 `pert_id` results and
reconcile chemical redundancy without selecting the most favorable
experimental representation.

The primary exact-structure grouping rule is:

1. exact full usable InChIKey when available;
2. exact canonical SMILES as fallback when a usable InChIKey is unavailable;
3. literal `restricted` is treated as unavailable identity information; and
4. `cmap_name` is never used to merge chemical entities.

The first 14-character InChIKey connectivity block may be retained as a
`shared_connectivity` diagnostic flag.

It is not the primary exact-structure identity and must not automatically
collapse stereochemically or otherwise distinct full InChIKeys.

When several `pert_id` values map to one exact structure:

- all perturbagen-level results remain visible;
- no best `pert_id` is selected;
- within-structure heterogeneity remains explicit; and
- those `pert_id` values must not be described as independent pharmacological
  replications.

Notebook 702 may summarize compound/structure-level context, but it must not
create a post hoc significance route that rescues failed perturbagen-level
primary inference.

---

# Compound prioritization boundary

Phase 7 compound prioritization is a perturbational-hypothesis organization
step.

It may use prospectively defined primary connectivity evidence, chemical
redundancy, lineage breadth/heterogeneity, and prespecified diagnostic context
to organize results transparently.

It must not:

- incorporate Phase 5 or Phase 6 evidence into the primary Phase 7 ordering;
- create an opaque composite score;
- prefer a compound because a later mechanism annotation appears favorable;
- select one experimental `pert_id` representation and discard unfavorable
  representations of the same exact structure; or
- describe a prioritized compound as therapeutically validated.

Final cross-evidence therapeutic prioritization belongs to Phase 9.

---

# Notebook 703 mechanism-of-action aggregation

Mechanism-of-action aggregation must preserve the many-to-many mapping between
perturbagens, structures, targets, and MoA annotations.

Within an MoA summary, repeated rows or multiple `pert_id` values representing
the same exact chemical structure must not inflate the number of independent
chemical entities.

Mechanism summaries should retain at minimum:

- `n_unique_structures`;
- `n_pert_ids`;
- contributing exact structures;
- contributing perturbagen identifiers;
- connectivity distribution;
- median connectivity;
- dispersion/heterogeneity; and
- direction concordance.

A singleton mechanism annotation remains a valid descriptive annotation but is
not equivalent to a pattern observed across multiple chemically distinct
structures.

No arbitrary threshold such as `n >= 3` may be used to label a mechanism as
strong, validated, or confirmed.

No formal MoA-level significance family is part of the primary Phase 7
inferential design.

MoA aggregation cannot rescue a failed perturbagen- or structure-level primary
result.

---

# Notebook responsibilities

## Notebook 700 — Program Signature Construction

Notebook 700 is responsible for constructing and validating the frozen Phase 7
query representations and the outcome-blind quantities required by the
prespecified null and sensitivity designs.

Notebook 700 must not inspect compound connectivity results.

Its role includes, as applicable:

- consuming frozen Phase 4 and notebook-110 handoffs;
- materializing continuous BING query vectors;
- materializing landmark sensitivity vectors;
- materializing fixed 150/150 CMap-style sensitivity queries;
- constructing outcome-blind gene-level statistics needed for frozen
  null-stratification;
- finalizing the prospectively frozen null strata after the operational
  specification is approved; and
- persisting stable query-definition and metadata handoffs.

Notebook 700 must not rank compounds.

## Notebook 701 — Connectivity Analysis

Notebook 701 is responsible for:

- primary signature-level cosine scoring;
- frozen hierarchical aggregation;
- lineage-aware perturbagen summaries;
- primary conditional empirical-null inference;
- global multiplicity control;
- prespecified sensitivities;
- proliferation/stress/amplitude diagnostics; and
- persistence of perturbagen-level connectivity and inferential results.

Notebook 701 must not use Phase 5 or Phase 6 evidence to redefine its primary
results.

## Notebook 702 — Compound Prioritization

Notebook 702 is responsible for:

- preserving notebook-701 perturbagen-level status;
- exact-structure reconciliation;
- chemical redundancy diagnostics;
- structure-level descriptive consolidation; and
- transparent perturbational-hypothesis organization.

It must not redefine notebook-701 primary significance.

## Notebook 703 — Mechanism-of-Action Aggregation

Notebook 703 is responsible for:

- many-to-many target/MoA propagation;
- unique-structure-aware mechanism summaries;
- descriptive recurrence and heterogeneity characterization; and
- explicit preservation of singleton, sparse, discordant, and heterogeneous
  mechanism contexts.

It must not create a mechanism-level rescue route.

---

# General prohibited analyses and interpretations

Phase 7 must not:

- redefine frozen Phase 4 programs using LINCS results;
- change program orientation according to perturbational direction;
- select genes according to favorable connectivity;
- select best signatures, doses, times, cell lines, or lineages;
- pool lineages naïvely as though LINCS cell-line composition were biologically
  representative;
- tune null strata according to observed p-values;
- change Monte Carlo stopping rules after result inspection;
- report Monte Carlo p-values of zero merely because no sampled null replicate
  was more extreme;
- change the multiplicity family to obtain significance;
- use sensitivity analyses to rescue the primary analysis;
- use Phase 5 or Phase 6 evidence to select the primary perturbagen universe;
- collapse chemical entities by name;
- count shared exact structures as independent pharmacological confirmation;
- treat target/MoA annotations as one-to-one;
- treat missing target/MoA annotation as biological absence;
- interpret stress/apoptosis transcription as direct cytotoxicity;
- describe LINCS internal subsets as external validation;
- claim therapeutic reversal;
- infer therapeutic efficacy;
- infer causal mechanism;
- claim validated targets;
- claim clinical predictiveness; or
- reconstruct longitudinal adaptive resistance from cross-sectional
  perturbational signatures.

---

# Negative-result policy

Phase 7 remains scientifically complete if:

- no perturbagen survives global primary FDR;
- one or more frozen programs show no credible inverse perturbational
  associations;
- results are heterogeneous across lineages;
- primary results weaken in the `is_hiq` subset;
- landmark-only representation is poorly concordant with BING;
- pooled-cell and equal-lineage summaries differ;
- the CMap-style sensitivity is discordant with continuous weighted cosine;
- the competitive-null sensitivity is less favorable than the primary
  conditional null;
- global BY sensitivity retains few or no findings;
- strong inverse associations occur in broad stress-like transcriptional
  contexts;
- exact chemical structures show heterogeneous results across `pert_id`
  representations;
- mechanism annotations are sparse or discordant; or
- no multi-structure MoA pattern emerges.

No query representation, eligibility rule, lineage aggregation, null family,
Monte Carlo rule, multiplicity correction, chemical grouping rule, or
interpretation threshold may be relaxed after result inspection to manufacture
positive perturbational evidence.

Null, weak, heterogeneous, discordant, and not-evaluable results remain valid
Phase 7 outputs.

---

# Downstream-use boundary

Phase 7 outputs may contribute to Phase 9 integrated evidence synthesis as a
separately traceable perturbational evidence layer.

Downstream integration must preserve distinctions between:

- primary weighted connectivity;
- empirical-null calibration;
- global multiplicity status;
- lineage breadth and heterogeneity;
- representation sensitivities;
- perturbational amplitude/stress/proliferation context;
- perturbagen identity;
- exact chemical structure;
- related-structure flags;
- target annotation; and
- MoA annotation.

Phase 7 results must not be used retrospectively to:

- redefine a frozen Phase 4 program;
- convert a Phase 5 putative vulnerability into a validated target;
- upgrade a Phase 6 pharmacogenomic association into therapeutic evidence;
- establish therapeutic efficacy; or
- claim clinical drug resistance prediction.

Phase 8 provides orthogonal/external validation where suitable independent
resources exist.

LINCS/CMap internal subsets are not Phase 8 external validation.

---

# Scientific interpretation boundary

Phase 7 may support statements such as:

- a perturbagen shows a negative computational connectivity with a frozen
  consensus program;
- that inverse association is or is not extreme under the prespecified
  conditional empirical null;
- an association is broad or heterogeneous across represented lineages;
- a primary result is stable or unstable to prespecified representation or
  perturbational sensitivities;
- several LINCS perturbagen identifiers correspond to one exact chemical
  structure;
- chemically distinct structures sharing an MoA annotation show concordant or
  discordant descriptive perturbational patterns; or
- a perturbational hypothesis is accompanied by broad proliferation- or
  stress-related transcriptional context.

Phase 7 does not support statements that:

- a compound therapeutically reverses a cancer state;
- a compound will overcome clinical resistance;
- a perturbagen is an effective treatment;
- an MoA is causally responsible for the observed connectivity;
- a target is validated;
- a perturbational signature proves drug efficacy; or
- internal LINCS consistency constitutes external biological validation.

Perturbational association remains distinct from causal mechanism.

Empirical-null extremeness remains distinct from therapeutic efficacy.

Mechanism annotation remains distinct from mechanism validation.

---

# Planned provenance and artifact registration

Stable Phase 7 outputs required downstream must be persisted, validated,
provenance-recorded, and registered in:

`config/artifact_registry.json`

using the namespace:

`phase7.*`

From Phase 6 onward, the preferred notebook-closure sequence applies:

persist outputs → validate outputs → finalize provenance → register artifacts →
validate registry.

The stable Phase 7 artifact identifiers are frozen as follows.

Notebook 700:

- `phase7.700.program_query_definitions`;
- `phase7.700.null_stratification_manifest`; and
- `phase7.700.analysis_metadata`.

Notebook 701:

- `phase7.701.lineage_connectivity`;
- `phase7.701.primary_perturbagen_connectivity`;
- `phase7.701.sensitivity_connectivity`;
- `phase7.701.perturbational_context_diagnostics`; and
- `phase7.701.analysis_metadata`.

Notebook 702:

- `phase7.702.perturbagen_structure_map`;
- `phase7.702.structure_connectivity_summary`;
- `phase7.702.perturbational_hypothesis_catalog`; and
- `phase7.702.analysis_metadata`.

Notebook 703:

- `phase7.703.mechanism_annotation_map`;
- `phase7.703.mechanism_summary`; and
- `phase7.703.analysis_metadata`.

Their exact column-level schemas and data types must be frozen locally before
each notebook first persists the corresponding stable interface. Schema
finalization may clarify representation but must not alter analytical
membership, inferential status, eligibility, null construction, or rescue
rules.

At minimum, these stable handoffs must preserve:

- query definitions and query metadata;
- null-stratification metadata;
- lineage-level and perturbagen-level connectivity;
- conditional-randomization inference metadata;
- prespecified sensitivity results;
- provider-defined activity/reproducibility and Hallmark diagnostic context;
- exact-structure reconciliation;
- compound/structure-level perturbational summaries;
- target/MoA mappings and mechanism summaries; and
- analysis metadata/provenance.

Intermediate matrices or null-draw batches need not be registered merely
because they were computed.

---

# Remaining operational freeze before notebook 701 inference

The 2026-09-28 addendum resolves the operational package required for query
construction, null stratification, sensitivity definition, randomization
family, diagnostics, artifact naming, and deterministic validation.

Notebook 701 primary inferential execution remains blocked until the following
final simulation item is prospectively resolved:

1. freeze the computational resource envelope before benchmarking;
2. execute the outcome-blind benchmark under that envelope;
3. select the largest feasible `Bmax` from
   `{500000, 250000, 100000}`; and
4. record the selected `Bmax`, benchmark environment, and resource envelope in
   this contract before observed connectivity is inspected.

No candidate outside that frozen ladder may be substituted after result
inspection.

## Deterministic implementation validation

Structural objects must match exactly, including:

- program and perturbagen identifiers;
- query membership;
- gene ordering keys;
- MAD-decile assignments;
- permutation replicate identifiers;
- RNG entropy, namespace, and spawn keys;
- lineage membership;
- chemical mappings; and
- expected row counts.

For small independent `float64` reference calculations, cosine, WTCS, and
hierarchical aggregation implementations must reproduce reference values using:

```text
rtol = 1e-10
atol = 1e-12
```

These tolerances apply to the reference checks rather than serving as a
universal tolerance for every persisted object.

Primary cosine scores must remain within their theoretical interval
`[-1, 1]` up to numerical tolerance.

WTCS query membership and ranking order must be exact after the frozen
tie-breaking rules are applied.

A failed deterministic or numerical validation must halt the relevant
execution path and trigger diagnosis. Validation tolerances must not be relaxed
after observing favorable or unfavorable scientific results.

---

# Analytical closure criteria

Phase 7 will be considered analytically complete when:

1. the resource envelope and final primary `Bmax` have been prospectively
   frozen before observed connectivity inspection;
2. all required Phase 7 inputs are consumed from frozen registered upstream
   artifacts rather than silently reconstructed;
3. the continuous signed weighted BING query representations are persisted and
   validated;
4. landmark and fixed CMap-style sensitivity queries are frozen before
   connectivity-result inspection;
5. primary signature-level cosine connectivity is calculated exactly as
   specified;
6. the frozen signature → condition → dose/time → cell-line hierarchy is
   preserved;
7. the equal-lineage primary aggregation is applied exactly as specified;
8. the conditional fixed-support empirical null is executed under frozen
   stratification and Monte Carlo rules;
9. all 23,742 primary hypotheses are represented, including null and
   not-evaluable states where applicable;
10. global BH FDR is applied exactly as prespecified;
11. sensitivities remain separate and do not rescue primary inference;
12. proliferation/stress/amplitude diagnostics remain contextual and do not
    redefine eligibility;
13. perturbagen-level results remain primary through notebook 701;
14. exact-structure reconciliation preserves all contributing `pert_id`
    results and chemical heterogeneity;
15. target/MoA aggregation preserves many-to-many structure and unique-chemical
    support;
16. weak, null, discordant, heterogeneous, and technically limited outcomes
    remain explicit;
17. stable downstream-required outputs are persisted and validated;
18. provenance and analysis metadata are finalized; and
19. downstream-required artifacts are registered with frozen identity.

Analytical completion does not require a significant perturbagen, a favorable
compound, a recurrent mechanism, or a perturbational hypothesis suitable for
experimental follow-up.
