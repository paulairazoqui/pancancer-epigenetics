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

A second prospective methodological amendment was established on 2026-09-28
after an independent adversarial audit and before inspection of any Phase 7
connectivity result. It clarifies the resistance-like orientation used for
Phase 7 inference, the conditional-null assumption and interpretation,
direction/evaluability handling, dependence-robust multiplicity control,
sequential Monte Carlo boundary behavior, deterministic RNG consumption,
chemical-identity edge cases, MoA deduplication, scientific result states, and
benchmark requirements. Historical wording from the earlier addendum is
retained for chronology where practical; the later amendment governs wherever
the two differ.

The final primary inferential simulation budget was resolved prospectively on
2026-09-29 after the outcome-blind Notebook 700 benchmark and before inspection
of any observed program–perturbagen connectivity, ranking, p-value, q-value, or
compound result. The governing final value is `Bmax = 5,058,108`, selected by
the statistical-resolution rule documented in the third amendment below.

The original 24-hour projected-runtime ceiling and the historical
`500000 -> 250000 -> 100000` candidate ladder are retained as audit history
but no longer govern the final simulation budget.

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

The 2026-09-28 operational package and post-audit methodological amendment are
prospectively frozen. The 2026-09-29 outcome-blind computational amendment
prospectively freezes the final primary Monte Carlo budget at
`Bmax = 5,058,108` before inspection of observed connectivity. Notebook 701
primary inferential execution becomes authorized only after Notebook 700 has
persisted, registered, and passed QA for its four stable handoff artifacts.

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
   `q_BY_global <= 0.05`; it uses 10,000 fixed pseudo-program draws and cannot
   create or rescue primary support;
6. primary Monte Carlo inference uses the truncated Besag–Clifford sequential
   procedure with exceedance target `h = 20`;
7. the historical candidate maximum-draw ladder was
   `500000 -> 250000 -> 100000`; this operational rule is superseded by the
   2026-09-29 prospective computational amendment, which fixes
   `Bmax = 5,058,108` using a statistical-resolution criterion before observed
   connectivity is inspected;
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

Specific clauses concerning multiplicity, RNG consumption, direction, and
interpretation are superseded by the later post-audit amendment below.

---

## Post-audit methodological amendment — 2026-09-28

This amendment was established after an independent adversarial review of the
frozen Phase 7 contract and before inspection of any Phase 7 perturbational
connectivity result.

It does not reopen the frozen Phase 4 program weights or the notebook-110
perturbational universe. It prospectively resolves additional inferential and
operational ambiguities identified during review.

The governing changes are:

1. Phase 7 preserves the frozen Phase 4 program orientation but separately
   derives a fixed `resistance_like_orientation_multiplier` from frozen
   upstream Phase 3/4 evidence before LINCS connectivity is inspected;
2. primary inferential direction is defined on the resulting
   resistance-like-oriented connectivity, not on the arbitrary positive pole of
   the Phase 4 consensus representation;
3. the conditional randomization test is explicitly interpreted under a
   working within-stratum exchangeability assumption for gene-to-weight-vector
   assignment; MAD matching does not prove that assumption;
4. non-inverse and not-evaluable hypotheses remain in the complete 23,742-test
   family with multiplicity input equal to 1;
5. global Benjamini–Yekutieli adjustment at `q_BY <= 0.05` is the primary
   inferential gate; global BH is retained as nominal exploratory context;
6. the Besag–Clifford branch `p = h/L` applies whenever the twentieth
   exceedance is reached, including exactly at `L = Bmax`; the
   `(g + 1)/(Bmax + 1)` branch applies only when `g < h`;
7. permutation draws are sampled with replacement from the allowed permutation
   space; repeated and identity permutations are permitted;
8. random streams are assigned at namespace × replicate × stratum level so that
   batching, parallelism, or the current active-hypothesis set cannot alter a
   pseudo-program replicate;
9. chemical reconciliation cannot bridge incompatible full InChIKeys through a
   fallback SMILES and unknown structures cannot collapse into one shared
   chemical entity;
10. MoA summaries receive one descriptive contribution per exact structure,
    after preserving within-structure `pert_id` heterogeneity; and
11. scientific statuses, inferential fields, benchmark outputs, and provenance
    requirements are frozen before connectivity inspection.

The amendment narrows interpretation where needed. It does not convert
conditional randomization support into evidence of a universal biological null,
causal mechanism, therapeutic efficacy, or therapeutic reversal.

---

## Purpose

Phase 7 evaluates whether perturbational signatures in the audited LINCS/CMap
resource show computational opposition to the prospectively oriented
resistance-like-associated poles of the three frozen Phase 4 cross-system
consensus transcriptomic programs.

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

> Do perturbational signatures show computational opposition to the
> prospectively oriented resistance-like-associated pole of a frozen
> cross-system consensus transcriptomic program?

> Are those resistance-like-oriented oppositions more extreme than expected
> under a prospectively specified conditional pseudo-program null?

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

A negative resistance-like-oriented primary connectivity score may be
described as computational opposition to the upstream
resistance-like-associated pole.

It must not be described as therapeutic reversal, causal reversal, or evidence
that the frozen positive Phase 4 pole itself encoded resistance.

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

The 1,495-gene BING representation is the primary query representation. It
contains 90 landmark genes and 1,405 best-inferred genes per frozen program.

Outcome-blind algebraic fidelity of this projection supports representation
choice but does not biologically validate each inferred gene or eliminate
platform-specific limitations.

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

## Resistance-like orientation for Phase 7 inference

Notebook 401 explicitly states that consensus score direction is anchored to
the tumor RNA component and does not itself encode a resistance-like
direction.

Phase 7 therefore preserves the frozen Phase 4 weights exactly but defines one
additional program-level orientation multiplier from frozen upstream evidence,
before any LINCS connectivity result is inspected.

For consensus program `p`:

```text
resistance_like_orientation_multiplier[p]
    = sign(
        phase4_orientation_multiplier[p]
        * phase3_311_lineage_adjusted_rho[source_cell_line_program[p]]
      )
```

The authoritative frozen source is
`phase3.311.program_robustness_summary`, together with the Phase 4
`orientation_multiplier` used to align the cell-line program to the tumor RNA
axis.

The resulting multipliers are:

| Consensus program | Phase 3 source | Phase 4 orientation multiplier | Frozen lineage-adjusted rho | Phase 3 robustness context | resistance-like multiplier |
|---|---|---:|---:|---|---:|
| `CONSENSUS_TX_01` | `ICA_PROGRAM_09` | +1 | -0.038606 | `CONTEXT_SENSITIVE_CANDIDATE` | -1 |
| `CONSENSUS_TX_02` | `ICA_PROGRAM_29` | -1 | -0.097379 | `ROBUSTNESS_SUPPORTED_CANDIDATE` | +1 |
| `CONSENSUS_TX_03` | `ICA_PROGRAM_13` | -1 | -0.136528 | `ROBUSTNESS_SUPPORTED_CANDIDATE` | +1 |

These values orient Phase 7 inference only. They do not alter, overwrite, or
re-publish the frozen Phase 4 gene weights.

The TX01 resistance-like association is explicitly context-sensitive and
attenuated after lineage adjustment. That limitation must propagate to any
Phase 7 interpretation involving TX01.

The resistance-like orientation is derived from internal post-selection Phase 3
association evidence. It is not independent validation and does not convert the
program into a clinical resistance biomarker.

---

# Primary connectivity definition

For perturbational signature `s` and frozen program `p`, the raw
connectivity score is the signed cosine similarity over the program's frozen
BING support `G_p`:

```text
C_raw[s,p] =
    sum_g(w[p,g] * z[s,g])
    / (sqrt(sum_g(w[p,g]^2)) * sqrt(sum_g(z[s,g]^2)))
```

where:

- `w[p,g]` is the frozen Phase 4 signed program weight; and
- `z[s,g]` is the Level 5 perturbational signature value.

Genes outside the frozen program support do not enter the cosine denominator.

The Phase 7 primary inferential score is:

```text
C_RL[s,p] =
    resistance_like_orientation_multiplier[p] * C_raw[s,p]
```

The same fixed multiplier is propagated to condition-, cell-line-, lineage-,
and perturbagen-level summaries.

A more-negative `C_RL` indicates stronger computational opposition to the
upstream resistance-like-associated pole.

For `CONSENSUS_TX_01`, because its multiplier is -1, a positive raw cosine
corresponds to negative resistance-like-oriented connectivity. For
`CONSENSUS_TX_02` and `CONSENSUS_TX_03`, raw and resistance-like-oriented
signs are the same.

Both `C_raw` and `C_RL` must be retained in stable outputs.

Neither score establishes therapeutic reversal, efficacy, causal reversal, or
clinical resistance modification.

No post hoc transformation, reorientation, recentering, rank selection, or
alternate normalization may replace these prospectively frozen definitions
according to observed LINCS results.

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

This equal-lineage aggregation balances represented lineages within a
perturbagen. It does not force every perturbagen to share the same set of
lineages and does not eliminate upstream lineage dependence of the frozen
programs.

Primary outputs must preserve at minimum:

- the lineage-specific scores;
- the number of evaluable lineages;
- the number of evaluable cell lines;
- inter-lineage dispersion; and
- the fraction of evaluable lineages with negative resistance-like-oriented
  connectivity.

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

The purpose of the primary null is to test whether, conditional on the frozen
gene support, strata, observed perturbational matrix, and signed-weight-vector
multiset, the observed gene-to-weight assignment produces a more extreme
negative resistance-like-oriented connectivity than assignments allowed by the
prospectively specified randomization mechanism.

The working null assumption is within-stratum exchangeability of the assignment
of complete three-program signed-weight vectors to genes.

The `feature_space × MAD_decile` matching improves comparability but does not
prove this exchangeability assumption and does not control every possible
coexpression, pathway, or perturbational-covariance property.

Keeping the LINCS matrix fixed preserves its observed gene-gene covariance
matrix, but permutation generally changes the relationship between program
weights and that covariance structure. The contract must not claim otherwise.

Accordingly, this is a conditional assignment-specificity null.

It is not a universal null of "no biological relationship."

A conditional randomization p-value therefore quantifies extremeness under this
specific assignment model. It must not be interpreted as the probability that
no biological association exists.

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
by at most one. If the feature-space gene count is not divisible by 10, the
earliest deciles in ascending decile order receive one additional gene until
the remainder is exhausted. These groups are the MAD deciles used for null
stratification.

MAD must be computed over the complete frozen primary signature universe as
specified above. A median of independently computed chunk-level MAD values is
not equivalent and is prohibited.

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
- the observed perturbational matrix.

It does not generally preserve the relationship between program weights and the
matrix covariance structure.

Notebook 700 must report, for each program and stratum:

- total BING genes;
- query genes;
- effectively permutable query genes;
- degenerate one-gene strata, if any; and
- the number of distinct positions available to the permutation generator.

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
`q_BY_global <= 0.05`.

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
lower-numbered bin is selected.

After every merge, both the required query-gene demand and eligible background
pool are recomputed on the union before any further merge decision. Merging is
repeated only until sufficient background genes exist.

Within each final matched block, background genes are sampled without
replacement inside a pseudo-program. Signed-weight vectors are assigned
one-to-one using the deterministic query-gene order followed by the
pseudo-program RNG draw order. Merged blocks and their sizes must be persisted
in sensitivity metadata.

Exactly 10,000 competitive pseudo-program draws are generated.

For an observed negative resistance-like-oriented score, the descriptive
competitive-null quantity is:

```text
competitive_null_tail_fraction = (g + 1) / 10001
```

where `g` is the number of competitive-null resistance-like-oriented scores
less than or equal to the observed resistance-like-oriented score.

This quantity is not named a p-value, receives no BH/BY correction, has no
PASS/FAIL threshold, and cannot create, replace, redefine, or rescue primary
support.

---

# Primary evaluability and directional gate

Program-level frozen query weights must be finite and have non-zero norm.
Failure of either condition is an implementation/input error that halts the
analysis rather than creating a scientific not-evaluable result.

A Level 5 signature score is evaluable only when all values required for the
program support are finite and the perturbational-vector norm over that support
is strictly greater than zero.

No silent `nanmedian`, imputation, or denominator shrinkage is permitted.

If individual signature scores are non-evaluable, the frozen aggregation
hierarchy may proceed using only explicitly evaluable units, while retaining
counts of every loss.

A `program × pert_id` primary hypothesis remains scientifically evaluable only
if, after these losses and after the frozen hierarchy is applied, it still has
at least:

- 5 unique evaluable tumor cell lines; and
- 4 unique evaluable annotated lineages.

If either coverage requirement is no longer satisfied:

- `evaluability_status = NOT_EVALUABLE`;
- the raw conditional p-value is absent;
- `p_for_multiplicity = 1`; and
- the hypothesis remains one of the 23,742 members of the global family.

For an otherwise evaluable hypothesis with final
`C_RL >= 0`, the observed direction does not support the prespecified inverse
alternative. In that case:

- `directional_status = NON_INVERSE`;
- no Monte Carlo sampling is required;
- `p_conditional = 1`; and
- `p_for_multiplicity = 1`.

Only evaluable hypotheses with `C_RL < 0` enter sequential Monte Carlo
sampling.

This directional gate is prospectively fixed and must not be changed according
to the number of discoveries it produces.

---

# Monte Carlo inference

Primary conditional randomization p-values are one-sided for the negative
resistance-like-oriented tail.

Monte Carlo inference uses the truncated Besag–Clifford sequential procedure
with exceedance target:

`h = 20`

For each evaluable inverse hypothesis, a null replicate is counted as at least
as extreme when:

```text
C_RL_null <= C_RL_observed
```

Let `L` be the exact number of completed null replicates at stopping and
`g` the number of exceedances among those `L` replicates.

If the twentieth exceedance is reached at any `L <= Bmax`, including exactly
at `L = Bmax`:

```text
p_conditional = 20 / L
```

If `Bmax` is reached with `g < 20`:

```text
p_conditional = (g + 1) / (Bmax + 1)
```

The `(g + 1)/(Bmax + 1)` branch must not be used when `g = 20`.

A p-value of zero is not permitted.

Permutation replicates are sampled independently with replacement from the
allowed within-stratum permutation space. Repeated permutations and identity
permutations are permitted.

A pseudo-program replicate is defined globally before any hypothesis-specific
stopping decision. The same replicate must be used for every still-active
hypothesis to which it applies.

Batching is computational only. If the twentieth exceedance occurs inside a
batch, `L` is the exact replicate index of that exceedance. The end of the
batch must never replace that stopping position.

No stopping criterion based on provisional BY values, BH values, rankings,
compound identities, or result favorability is permitted.

The final prospectively frozen simulation budget is:

```text
Bmax = 5,058,108
```

This value is governed by the 2026-09-29 computational-resolution amendment.
The earlier `500000 -> 250000 -> 100000` ladder is retained only as historical
benchmark context and no longer governs execution.

Randomization uses NumPy `PCG64DXSM` with independent deterministic
substreams:

```text
SeedSequence(
    entropy=701,
    spawn_key=(namespace, replicate_id, stratum_id)
)
```

where:

- namespace `1` = primary conditional null;
- namespace `2` = competitive-null sensitivity;
- namespace `3` = outcome-blind computational benchmark;
- `replicate_id` is zero-based; and
- `stratum_id` is the deterministic integer ID assigned after sorting first by
  feature space and then by MAD decile.

Gene order, feature-space order, stratum order, program order, replicate order,
and the mapping from random integers to permutations must be frozen in Notebook
700 metadata before observed connectivity is computed.

Random streams must not depend on:

- batch size;
- thread count;
- parallel execution order;
- the number of hypotheses that remain active; or
- observed scientific results.

The exact NumPy/environment versions used for execution must be persisted in
analysis metadata.

Source GCTX values may remain stored/read as `float32`. Dot products, norms,
cosines, WTCS calculations, medians, empirical-null aggregations, and p-value
calculations must use `float64`.

Batch size remains an engineering parameter only if deterministic validation
confirms identical replicate identities, exceedance indicators, stopping
positions, and final outputs.

Computational inconvenience is not a valid reason to alter the null or stopping
rule after observed results are inspected.

---

# Primary hypothesis family and multiplicity

The primary hypothesis family contains:

```text
3 programs × 7,914 perturbagens = 23,742 hypotheses
```

Every frozen `program × pert_id` pair remains in this family regardless of
direction or evaluability.

The multiplicity input is:

```text
p_for_multiplicity =
    p_conditional, if evaluable and C_RL < 0
    1,             otherwise
```

The primary inferential multiplicity procedure is global
Benjamini–Yekutieli adjustment across all 23,742
`p_for_multiplicity` values.

The primary support criterion is:

```text
q_BY_global <= 0.05
```

BY is used because the dependence structure among the 23,742 hypotheses is
complex and no independence or PRDS condition is claimed for these p-values.

The dependence-robust FDR interpretation remains conditional on the marginal
validity of the conditional randomization p-values under the explicitly stated
working exchangeability null.

Global Benjamini–Hochberg adjusted values are retained as nominal exploratory
context:

`q_BH_global`

BH values do not define primary support and cannot rescue a hypothesis that
fails the BY gate.

Program-specific BH or BY summaries may be reported descriptively. They do not
replace the global family.

The analysis must not claim that BY repairs an invalid scientific null. It only
addresses multiple-testing dependence conditional on valid marginal p-values.

The finite Monte Carlo resolution associated with the final `Bmax` must be
reported together with the BY procedure. A lack of primary support caused in
part by discrete p-value resolution remains a valid negative/limited outcome
and must not trigger a post hoc change of multiplicity method.

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
- global BH nominal exploratory summaries; and
- program-specific BH/BY descriptive summaries.

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

The exact-structure reconciliation hierarchy is:

1. when a usable full InChIKey exists, exact full InChIKey defines the primary
   exact-structure group;
2. when full InChIKey is unavailable but canonical SMILES is usable, exact
   canonical SMILES may provide fallback grouping;
3. a SMILES-only entity may be attached to an existing full-InChIKey group only
   when that canonical SMILES maps unambiguously to exactly one full-InChIKey
   group in the frozen primary annotation universe;
4. a canonical SMILES must never bridge two incompatible full InChIKeys into one
   exact-structure group;
5. if one SMILES corresponds to multiple full InChIKeys, SMILES-only rows remain
   explicitly unresolved rather than forcing a merge;
6. literal `restricted` is unavailable identity information;
7. `cmap_name` is never used to merge chemical entities; and
8. entities lacking both usable full InChIKey and usable canonical SMILES are
   not collapsed together. Each remains an explicitly unknown structure tied to
   its own `pert_id`.

If a frozen `pert_id` unexpectedly maps to more than one usable full InChIKey,
Notebook 702 must halt reconciliation for that `pert_id` and emit an identity
conflict rather than choosing one identifier.

When a full InChIKey and canonical SMILES disagree with mappings elsewhere, the
full InChIKey remains authoritative for primary exact-structure identity and the
conflict is preserved as metadata.

The first 14-character InChIKey connectivity block may be retained as a
`shared_connectivity` diagnostic flag.

It is not the primary exact-structure identity and must not automatically
collapse stereochemically or otherwise distinct full InChIKeys.

For each exact structure and program, the descriptive structure-level
connectivity is the median of the contributing `pert_id` resistance-like-
oriented connectivity values.

The structure summary must also retain:

- all contributing `pert_id` values;
- number of contributing `pert_id` values;
- minimum and maximum perturbagen-level connectivity;
- IQR when estimable;
- direction concordance; and
- all contributing primary inferential statuses.

No best `pert_id` may be selected.

Multiple `pert_id` values representing the same exact structure must not be
described as independent pharmacological replications.

Notebook 702 may summarize chemical context, but it must not create a post hoc
significance route that rescues failed perturbagen-level primary inference.

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

Notebook 702 must emit a complete catalog rather than select only visually or
scientifically "interesting" hits.

The catalog's primary scientific status is inherited from notebook 701
(`q_BY_global <= 0.05` versus not primary-supported). Any display ordering must
be deterministic and declared in metadata; ordering does not create an
additional evidence tier.

Final cross-evidence therapeutic prioritization belongs to Phase 9.

---

# Notebook 703 mechanism-of-action aggregation

Mechanism-of-action aggregation must preserve the many-to-many mapping between
perturbagens, exact structures, targets, and MoA annotations.

Annotation relations must be deduplicated before summary construction.

A target × MoA Cartesian product generated by table joins must not be
interpreted as evidence that every target is causally linked to every MoA.

Mechanism-level descriptive summaries are constructed in two stages:

1. summarize each exact structure once per program using the frozen
   structure-level summary from notebook 702; then
2. allow each unique exact structure to contribute at most once to a given MoA
   summary for that program.

Multiple `pert_id` values representing one exact structure therefore cannot
inflate mechanism-level chemical support.

Mechanism summaries must retain at minimum:

- `n_unique_structures`;
- `n_pert_ids`;
- contributing exact structures;
- contributing perturbagen identifiers;
- structure-level median connectivity distribution;
- median across unique structures;
- dispersion/heterogeneity across structures;
- direction concordance across structures; and
- within-structure heterogeneity metadata inherited from notebook 702.

Entities with unresolved/unknown exact structure may retain MoA annotations as
perturbagen-level descriptive metadata but must not be counted automatically as
chemically independent support.

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
- change frozen Phase 4 program weights or the prospectively frozen
  resistance-like orientation according to perturbational direction;
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
- global BY primary inference retains few or no findings even when nominal
  global BH context is less conservative;
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

- a perturbagen shows computational opposition to the prospectively oriented
  resistance-like-associated pole of a frozen consensus program;
- that opposition is or is not extreme under the prespecified conditional
  assignment-specific randomization null;
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

Conditional-randomization extremeness remains distinct from therapeutic
efficacy and from proof of a universal biological null.

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
- `phase7.700.null_stratification_manifest`;
- `phase7.700.benchmark_report`; and
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

Physical column order and storage dtypes may be finalized locally before first
persistence, but scientific fields and states that affect interpretation are
already frozen by this contract and must not be invented after connectivity is
observed.

At minimum, `phase7.700.program_query_definitions` must retain program ID,
source cell-line program, Phase 4 orientation multiplier, frozen Phase 3
lineage-adjusted rho, Phase 3 robustness category,
`resistance_like_orientation_multiplier`, query gene identity, and frozen
weight.

At minimum, `phase7.701.primary_perturbagen_connectivity` must retain:

- `program_id` and `pert_id`;
- `C_raw` and `C_RL`;
- `resistance_like_orientation_multiplier`;
- signature, condition, cell-line, and lineage evaluability counts;
- `evaluability_status` and `directional_status`;
- lineage dispersion and fraction of negative `C_RL`;
- `p_conditional`;
- `p_for_multiplicity`;
- `mc_L`, `mc_g`, `mc_stop_reason`, and final `Bmax`;
- `q_BY_global` and `q_BH_global`; and
- `primary_support_status`.

Required primary support states are:

- `PRIMARY_BY_SUPPORTED`;
- `INVERSE_NOT_BY_SUPPORTED`;
- `NON_INVERSE`; and
- `NOT_EVALUABLE`.

Notebook-701 analysis metadata must retain RNG entropy, namespace/stratum
mapping, software/environment versions, input artifact hashes, benchmark/final
`Bmax` provenance, and the exact null/multiplicity specification version.

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

Notebook 700 is authorized to begin outcome-blind preparatory work.

Notebook 701 observed primary connectivity remains blocked until the final
simulation budget is prospectively resolved.

Before any benchmark timing is measured, Notebook 700 must persist the
benchmark resource envelope containing at minimum:

- execution-host identifier;
- CPU model and logical/physical core count;
- GPU model and usable VRAM, if used;
- physical RAM and maximum RAM allowed for the benchmark;
- BLAS/threading configuration;
- maximum benchmark/projection wall-clock budget;
- temporary-storage allowance;
- checkpoint/restart policy; and
- exact software/environment versions.

Those values may reflect the available execution host, but they must be written
before timing results are produced.

The benchmark must use namespace `3` and must not compute or expose observed
program–perturbagen connectivity for the real frozen programs.

It must measure or conservatively project the actual execution path, including:

- GCTX access and I/O;
- null permutation generation;
- score calculation;
- signature → condition → dose/time → cell-line → lineage → perturbagen
  aggregation;
- exceedance counting;
- active-hypothesis bookkeeping;
- checkpoint I/O; and
- peak memory.

At minimum, benchmark cases must include:

1. a maximum-active-set case in which all 23,742 hypotheses remain active over
   the measured benchmark block;
2. prespecified reduced-active-set cases to verify expected scaling; and
3. restart/checkpoint validation.

The historical benchmark initially evaluated the frozen operational ladder
`500000 -> 250000 -> 100000` against the pre-written resource envelope.
Those projections remain part of the benchmark record.

Before observed connectivity was inspected, the 2026-09-29 prospective
computational-resolution amendment superseded the runtime-based selection rule.
The governing final value is `Bmax = 5,058,108`, chosen by the BY rank-1
Monte Carlo resolution criterion specified above.

The original 24-hour ceiling is therefore retained as an operational planning
target rather than an inferential eligibility gate. Computational
implementation may be optimized, batched, checkpointed, resumed, or moved to a
different execution host only if the frozen scientific procedure and
deterministic RNG mapping remain unchanged.

The benchmark report must retain the historical candidate-specific projected
runtime, peak memory, I/O assumptions, and corresponding Monte Carlo resolution,
together with the superseding final statistical-resolution decision.

The finite resolution of `Bmax = 5,058,108`, including its relationship to
the global BY rank-1 threshold, must be explicitly recorded before Notebook 701
begins.

## Deterministic implementation validation

Structural objects must match exactly, including:

- program and perturbagen identifiers;
- resistance-like orientation multipliers;
- query membership;
- gene ordering keys;
- MAD-decile assignments;
- deterministic remainder allocation to deciles;
- permutation replicate identifiers;
- RNG entropy, namespace, replicate and stratum spawn keys;
- lineage membership;
- chemical mappings; and
- expected row counts.

Reference tests must verify not only approximate score agreement but exact
exceedance indicators, exact `g`, exact `L`, and exact stop reason for
constructed boundary cases, including the twentieth exceedance occurring
exactly at `Bmax`.

For small independent `float64` reference calculations, cosine, WTCS, and
hierarchical aggregation implementations must reproduce reference values using:

```text
rtol = 1e-10
atol = 1e-12
```

These tolerances apply to score reference checks and do not permit ambiguity in
discrete exceedance/stopping decisions.

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

1. the resource envelope, benchmark report, and final primary `Bmax` have
   been prospectively frozen before observed connectivity inspection;
2. all required Phase 7 inputs are consumed from frozen registered upstream
   artifacts rather than silently reconstructed;
3. the continuous signed weighted BING query representations are persisted and
   validated;
4. landmark and fixed CMap-style sensitivity queries are frozen before
   connectivity-result inspection;
5. raw and resistance-like-oriented connectivity are calculated exactly as
   specified;
6. the frozen signature → condition → dose/time → cell-line hierarchy is
   preserved;
7. the equal-lineage primary aggregation is applied exactly as specified;
8. the conditional fixed-support empirical null is executed under frozen
   stratification and Monte Carlo rules;
9. all 23,742 primary hypotheses are represented, including null and
   not-evaluable states where applicable;
10. global BY FDR is applied as the primary inferential multiplicity procedure
    and global BH is retained only as nominal exploratory context;
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
