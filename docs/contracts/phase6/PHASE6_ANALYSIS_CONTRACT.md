# Phase 6 Analysis Contract

## Lifecycle / execution status

This contract was established prospectively across staged Phase 6 decision
points. Notebook-600 and notebook-601 specifications were frozen before
inspection of the corresponding inferential or predictive-performance results.
The sections below preserve those historical prospective decisions. Notebook
602 attribution and notebook 603 cross-screen replication remain pending
prospective freeze before inspection of their corresponding results.

Notebook `600 — Program–Drug Associations` performed a restricted prerequisite
characterization stage before creation of this contract.

That prerequisite stage was limited to:

- frozen-artifact compatibility;
- deterministic cell-line identity mapping;
- external score transportability;
- pharmacogenomic resource coverage;
- deterministic compound identity mapping;
- PRISM screen structure;
- technically motivated response-metric selection; and
- repeated-experiment structure in CTRP.

No program–drug association coefficient, p-value, or q-value was inspected
before the primary notebook-600 eligibility, model, response-handling, and
multiplicity decisions were frozen.

Additional notebook-600 sensitivity and descriptive characterization rules
that were frozen after execution of the primary GDSC association family are
timestamped explicitly in their corresponding sections. Those later rules
were established before inspection of the results to which they apply.

Notebook-601 predictive-model performance was inspected only after the
predictive specification below had been frozen. No SHAP value, SHAP feature
ranking, or CTRP/PRISM cross-screen replication result has yet been inspected.

The prerequisite characterization must therefore not be represented as having
been preregistered before all Phase 6 data inspection. Its role was narrower:
to define technically valid, outcome-blind analytical objects and to freeze
their handling before inferential result inspection.

Once Phase 6 inferential execution begins, primary eligibility rules,
statistical models, multiplicity families, replication criteria, response
handling, feature spaces, evaluation design, or interpretation thresholds must
not be changed on the basis of whether they produce more favorable results.

The authoritative executable records will be:

- `600 — Program–Drug Associations`;
- `601 — Explainable Predictive Modeling`;
- `602 — SHAP Attribution and Stability Analysis`; and
- `603 — Cross-Screen Replication`.

---

## Status

In progress. Notebook 600 and notebook 601 are complete under their frozen
specifications, with stable downstream-required handoffs persisted, validated,
and registered. Notebook 601 evaluated all 281 frozen GDSC-eligible drugs; 125
satisfy the prospectively frozen predictive-validity gate for subsequent
primary program-level SHAP interpretation. This gate establishes internal
attribution eligibility only.

Notebook 602 attribution has not yet been prospectively frozen or executed, and
no SHAP attribution result has been inspected. Notebook 603 cross-screen
replication remains pending prospective freeze, and CTRP/PRISM replication
outcomes have not been inspected for downstream replication decisions.

## Notebook 601 execution update — 2026-09-17

Notebook 601 has now been executed under the frozen predictive specification
preserved below.

- all 281 frozen eligible GDSC drugs were evaluated;
- median drug-level out-of-fold `R²` was `0.231` for lineage-only models and
  `0.244` for lineage-plus-program models;
- median drug-level incremental performance was `delta_R2 = 0.016`;
- 125 of 281 drugs satisfied all three frozen predictive-validity criteria;
- the secondary unseen-lineage stress test comprised 2,961
  `drug × held-out lineage` evaluations;
- median drug-level unseen-lineage program-model `R²` was `-0.088`;
- median drug-level unseen-lineage `delta_R2` relative to the training-derived
  intercept-only comparator was `0.157`; and
- the median fraction of held-out lineages with positive `delta_R2` was `0.727`.

The unseen-lineage stress test remains secondary and descriptive. Its results
do not rescue or exclude drugs from the primary notebook-602 attribution gate.

The following stable notebook-601 artifacts are registered:

- `phase6.601.primary_cv_partitions`;
- `phase6.601.primary_repeat_performance`;
- `phase6.601.lolo_performance`;
- `phase6.601.drug_level_results`; and
- `phase6.601.analysis_metadata`.

No notebook-601 model family, feature universe, threshold, resampling rule,
compound universe, or predictive-validity gate was changed after
predictive-performance inspection.

This execution update does not freeze any notebook-602 attribution decision.
The notebook-602 section below remains fully pending prospective freeze.

This document defines the analytical decisions governing:

- pharmacogenomic program–drug association analysis;
- explainable predictive modeling;
- SHAP attribution and attribution stability; and
- cross-screen replication.

Some Phase 6 decisions are already frozen below.

Items explicitly marked:

`PENDING FREEZE BEFORE INFERENTIAL EXECUTION`

remain unresolved and must be finalized before inspection of the corresponding
inferential results.

---

## Purpose

Phase 6 characterizes whether the three frozen Phase 4 cross-system consensus
transcriptomic programs are associated with resistance-like pharmacogenomic
contexts across GDSC, CTRP, and PRISM and, where methodologically justified,
whether those frozen program representations provide reproducible predictive
information about pharmacological response.

Phase 6 also contains the project's explicit explainable-modeling layer.

The analysis is designed to distinguish:

- developmental/internal pharmacogenomic association evidence;
- external cross-screen pharmacogenomic replication;
- lineage-aware predictive validity;
- model attribution;
- attribution stability; and
- biological contextualization of model behavior.

These evidence dimensions are not interchangeable.

Positive, negative, heterogeneous, lineage-specific, weakly predictive,
unstable, or non-replicating outcomes are all valid Phase 6 results.

---

## Scientific positioning

Phase 6 addresses the following general questions:

> Are frozen cross-system transcriptomic programs associated with
> resistance-like pharmacogenomic contexts after accounting for major lineage
> structure?

> Do such associations reproduce across pharmacogenomic screens where compound
> and model coverage permit defensible comparison?

> Do frozen program-level representations provide predictive information beyond
> transparent lineage-aware baselines?

> When predictive validity is adequate, which actual model features contribute
> reproducibly to fitted-model behavior?

Phase 6 does not establish:

- clinically acquired drug resistance;
- longitudinal adaptive resistance;
- causal drug-response mechanisms;
- therapeutic efficacy;
- validated biomarkers;
- validated therapeutic targets;
- causal biological regulation;
- clinical predictiveness; or
- therapeutic reversal.

The term `resistance-like` refers to relative baseline pharmacogenomic
insensitivity measured in preclinical cell-line screens.

---

# Frozen upstream inputs

Phase 6 consumes frozen upstream artifacts without reopening their construction
or selection.

## Frozen modeling cohort

The primary developmental/internal model cohort is inherited from:

`phase3.302.integrated_modeling_cohort`

This object contains 713 cell-line models and the frozen GDSC-linked model
identity established upstream.

Notebook 600 does not redefine membership in this cohort in order to improve
pharmacogenomic associations.

---

## Frozen consensus transcriptomic programs

The Phase 6 program universe is restricted to the three frozen Phase 4
cross-system consensus transcriptomic representations:

- `CONSENSUS_TX_01`;
- `CONSENSUS_TX_02`; and
- `CONSENSUS_TX_03`.

The corresponding frozen cell-line scores are inherited from:

`phase4.401.consensus_cellline_scores`

The frozen consensus gene weights are inherited from:

`phase4.401.consensus_transcriptomic_gene_weights`

Phase 6 must not:

- discover additional consensus programs;
- remove a frozen program because of unfavorable pharmacogenomic results;
- alter program orientation;
- refit program weights;
- rename programs according to downstream pharmacogenomic behavior; or
- use Phase 5 or later evidence to redefine the Phase 4 program universe.

---

## Developmental non-independence of GDSC

GDSC is not treated as an independent external replication resource in Phase 6.

The frozen Phase 3 modeling cohort was constructed using GDSC-linked
pharmacological information, and Phase 4 cross-system construction inherited a
cell-line candidate universe that had already been characterized relative to
the Phase 3 resistance-like pharmacogenomic phenotype.

Therefore:

- GDSC serves a developmental/internal role in Phase 6;
- GDSC association results must not be described as independent validation;
- CTRP and PRISM provide the primary cross-screen external replication
  resources; and
- agreement between GDSC and an external screen must retain this asymmetry in
  interpretation.

---

# Phase 6 score universe

## Frozen anchor scores

The 713-model Phase 4 consensus-score matrix remains the authoritative score
representation for models already present in the frozen Phase 4 cohort.

These models receive:

`score_origin = frozen_phase4`

No score is recomputed for those models in order to change their Phase 6
values.

---

## External score projection

Additional pharmacogenomic models may receive Phase 6 program scores only when
their required DepMap expression features are available and they can be mapped
deterministically to the relevant pharmacogenomic resource.

External program scores are generated using the frozen Phase 4 representation.

The transformation is defined by parameters estimated exclusively from the
original 713-model Phase 4 reference cohort:

1. gene means from the frozen 713-model reference;
2. gene standard deviations from the frozen 713-model reference;
3. frozen Phase 4 consensus gene weights;
4. projected-score means from the frozen 713-model reference; and
5. projected-score standard deviations from the frozen 713-model reference.

External models receive this frozen transformation.

They do not contribute to estimation of the transformation parameters.

No joint re-standardization across the combined anchor-plus-external cohort is
permitted.

This prevents external/test-cohort composition from determining feature scale.

External scores receive:

`score_origin = projected_from_frozen_phase4`

They are Phase 6-derived projected scores and must not be described as original
frozen Phase 4 scores.

---

## Score-transport verification

Before external projection was used, the frozen transformation was reproduced
on the original 713 models.

The reconstructed and serialized frozen Phase 4 scores agreed to numerical
precision for all three programs.

This check is a local transportability verification.

It does not reopen or revalidate the scientific conclusions of notebook 401.

---

## External scoreable model universe

Outcome-blind deterministic mapping and expression eligibility identified:

- 256 expression-scoreable CTRP models outside the frozen anchor cohort;
- 136 expression-scoreable PRISM models outside the frozen anchor cohort;
- 124 external models shared between CTRP and PRISM; and
- 268 unique external scoreable models across the two external resources.

The resulting Phase 6 score universe contains:

- 713 frozen Phase 4 anchor models; and
- 268 externally projected models;

for a total of:

`981 models`

The 981-model score universe must not be redefined according to drug-response
association strength, predictive performance, or downstream replication.

---

# Cell-line identity harmonization

## GDSC model identity

GDSC developmental/internal analyses use the frozen Sanger-to-DepMap model
mapping inherited through the Phase 3 modeling cohort.

All 713 frozen anchor models have GDSC response coverage.

No additional fuzzy cell-line matching is introduced for GDSC.

---

## PRISM model identity

PRISM model identity uses the provider-supplied:

`depmap_id`

as the stable primary model identifier.

Screen-specific response rows without a defensible DepMap model identity are
not rescued through cell-line-name matching.

No fuzzy or manual model-name rescue is permitted in the primary Phase 6 PRISM
mapping.

---

## CTRP model identity

CTRP does not provide a stable DepMap model identifier in its native cell-line
metadata.

The Phase 6 CTRP-to-DepMap mapping therefore uses deterministic normalized
cell-line names.

Normalization is restricted to:

- uppercase conversion; and
- removal of non-alphanumeric characters.

A CTRP-to-DepMap match is accepted only when the normalized name key is
one-to-one across the full relevant DepMap model universe.

Anchor membership must not be used to resolve a globally ambiguous mapping.

No:

- fuzzy matching;
- manual alias rescue;
- lineage-based rescue;
- histology-based rescue; or
- downstream response-based rescue

is permitted.

---

## Globally ambiguous CTRP identity

One CTRP cell line is excluded from the primary Phase 6 crosswalk because its
normalized name is not globally unique:

`KMH2`

The normalized key maps to both:

- `ACH-000815` — `KM-H2`; and
- `ACH-002397` — `KMH-2`.

Because CTRP does not provide an additional stable identifier sufficient to
resolve this ambiguity, the mapping remains unresolved.

The final globally unambiguous CTRP Phase 6 crosswalk contains:

`821 scoreable models`

comprising:

- 565 frozen-anchor models; and
- 256 externally projected models.

The ambiguous `KMH2` mapping must not be reinstated on the basis of downstream
results.

---

# Pharmacogenomic resource roles

The Phase 6 pharmacogenomic resources have the following frozen roles:

| Resource | Primary Phase 6 role |
| --- | --- |
| GDSC | developmental / internal |
| CTRP | external cross-screen replication |
| PRISM | external cross-screen replication |

Cross-screen agreement involving overlapping cell lines is not automatically
interpreted as independent cell-level replication.

Cell-line overlap must remain explicit in notebook 603.

---

# Compound identity harmonization

## Native identifiers

Native compound identifiers remain authoritative within each resource:

- GDSC: `DRUG_ID`;
- CTRP: `master_cpd_id`;
- PRISM: `broad_id`.

Native identifiers are retained even when a cross-resource match is available.

---

## Exact cross-resource compound identity

The primary cross-resource compound crosswalk uses normalized compound names
only when the normalized key is unambiguous within every participating
resource.

The normalization rule is restricted to:

- leading/trailing whitespace removal;
- uppercase conversion; and
- removal of non-alphanumeric characters.

A normalized-name key is eligible for exact-name cross-resource matching only
when it maps to exactly one native compound identifier in each participating
resource.

No ambiguous within-resource key is promoted to an exact compound match.

---

## Ambiguous compound-name keys

Within-resource normalized-name collisions were observed in:

- GDSC; and
- PRISM.

Those ambiguous keys are excluded from exact-name replication mapping unless a
separate, prospectively frozen identity authority is introduced before
inferential execution.

CTRP contained no normalized-name collisions under the frozen rule.

No fuzzy matching, target-based rescue, mechanism-of-action rescue, or manual
synonym selection is part of the primary exact-compound definition.

---

## Cross-resource exact-name universe

The frozen exact-name mapping identified:

- 68 unambiguous GDSC–CTRP matches;
- 87 unambiguous GDSC–PRISM matches;
- 151 unambiguous CTRP–PRISM matches; and
- 39 compounds represented unambiguously in all three resources.

After deduplication of three-way membership, the cross-resource exact-name
catalog contains:

`228 compounds`

represented in at least two resources.

Of these:

- 39 occur in all three resources; and
- 189 occur in exactly two resources.

These counts characterize the available replication universe.

They do not themselves define inferential eligibility.

---

## Exact replication versus pharmacological analogy

A cross-resource normalized-name match satisfying the frozen one-to-one rule may
be used as a candidate exact-compound replication link.

Related compounds, compounds sharing a target, compounds from the same
mechanistic class, or compounds from the same drug family are not considered
exact compound replication merely because of that relationship.

Drug-family or mechanism-level concordance, if evaluated later, must remain
separate contextual evidence.

---

# PRISM screen handling

## Screen preservation

PRISM screen identity is retained explicitly.

The following screens represented cross-resource compounds during prerequisite
characterization:

- `HTS002`;
- `MTS006`;
- `MTS010`.

`MTS005` did not contribute coverage to the cross-resource exact-compound
universe characterized for primary replication.

Screens must not be pooled naïvely.

---

## Primary PRISM screen rule

The primary PRISM screen for a compound is assigned prospectively using the
following hierarchy.

### 1. MTS010 priority

When `MTS010` is available for a compound, `MTS010` is used as the primary
PRISM screen.

This follows the provider documentation identifying `MTS010` as a technical
redo and recommending the redo when available.

### 2. Single available non-redo screen

When `MTS010` is unavailable and the compound occurs in exactly one other
eligible PRISM screen, that unique screen is used.

### 3. Multiple non-redo screens without MTS010

When `MTS010` is unavailable and more than one non-redo screen is available,
no screen is selected ad hoc.

The compound receives:

`AMBIGUOUS_NONREDO`

for the primary PRISM screen assignment.

Such compounds may be retained for explicitly labeled screen-specific
sensitivity analysis but do not receive an arbitrarily selected primary screen.

---

## Realized primary-screen assignment before inference

Among 199 cross-resource exact-name compounds represented in PRISM:

- 156 receive `HTS002`;
- 37 receive `MTS010`;
- 4 receive `MTS006`; and
- 2 receive `AMBIGUOUS_NONREDO`.

Thus:

`197`

cross-resource compounds have a unique prospectively assigned primary PRISM
screen.

The 2 `AMBIGUOUS_NONREDO` compounds remain outside the primary unique-screen
PRISM representation unless a later sensitivity analysis explicitly preserves
their screen-specific identities.

Their status must not be resolved according to association strength.

---

# Pharmacogenomic response representations

## General direction convention

The primary response variables are oriented so that larger values represent a
more resistance-like / less-sensitive baseline pharmacogenomic context within
the corresponding screen.

This common directional interpretation does not imply that response values are
numerically exchangeable across resources.

Raw response values from GDSC, CTRP, and PRISM must not be naively pooled into
one shared quantitative scale.

---

## GDSC primary response

The primary GDSC response metric is:

`LN_IC50`

with:

`higher value = more resistance-like`

This representation was selected upstream in Phase 3 on methodological grounds
before the current Phase 6 program–drug analysis.

Phase 6 preserves that frozen choice rather than reselecting a GDSC metric
according to downstream association behavior.

GDSC remains developmental/internal evidence.

---

## CTRP primary response

The primary CTRP response metric is:

`area_under_curve`

from the provider post-QC fitted-curve resource.

Direction:

`higher value = more resistance-like`

CTRP EC50 is not selected as the primary metric because the audited resource
contains substantial fitted-value extrapolation beyond tested concentration
ranges.

The choice of AUC is technical and precedes program–drug association
inspection.

---

## PRISM primary response

The primary PRISM response metric is:

`auc`

from the provider dose-response curve-parameter resource.

Direction:

`higher value = more resistance-like`

PRISM IC50 is not selected as the primary metric because finite IC50 coverage is
substantially incomplete in the audited resource.

The choice of AUC is technical and precedes program–drug association
inspection.

---

# CTRP repeated-experiment handling

## Analytical unit

The primary CTRP pharmacogenomic response unit is:

`ModelID × master_cpd_id`

rather than:

`experiment_id × master_cpd_id`

Repeated experiments for the same model–compound pair are therefore not treated
as independent biological observations.

---

## Prerequisite repeated-experiment characterization

Within the Phase 6 scoreable CTRP universe, there are:

`357,460`

unique model–compound pairs.

Of these:

- 349,752 are represented by one experiment; and
- 7,708 are represented by more than one experiment.

Repeated pairs therefore represent:

`2.16%`

of the Phase 6 CTRP model–compound universe.

The maximum number of experiments per model–compound pair is:

`3`

No primary pair is excluded according to observed inter-experiment AUC
discordance.

No post hoc AUC-difference threshold is introduced.

---

## Primary CTRP aggregation rule

When a CTRP model–compound pair is represented by more than one experiment, the
primary response is:

`median(area_under_curve)`

across retained post-QC experiments for that pair.

The resulting primary object contains one response value per:

`ModelID × master_cpd_id`

and retains:

`n_experiments`

as technical metadata.

The median was selected as a transparent model-level aggregation rule that does
not allow repeated experimental measurements to create pseudo-replication and
provides robustness when three experiments are available.

No pair is preferentially retained or removed because its experiments are more
or less concordant.

The realized primary CTRP response object contains:

`357,460 model–compound observations`

with:

`0 missing primary response values`

---

## CTRP repeated-experiment sensitivity

A prespecified CTRP sensitivity analysis will restrict the response object to:

`n_experiments == 1`

when evaluating the stability of primary CTRP findings for which such a
sensitivity is scientifically relevant.

This sensitivity evaluates whether repeated-experiment aggregation materially
affects conclusions.

It must not:

- replace the primary median-aggregated response according to favorable results;
- define an alternative significance route;
- rescue a primary association; or
- generate a preferred post hoc compound set.

---

# Lineage representation

The primary cell-line lineage variable is inherited from the deterministic
DepMap model metadata and represented by:

`OncotreeLineage`

All currently scoreable Phase 6 models have a lineage annotation.

Lineage is treated as a major biological structure and potential confounder.

Random pan-cancer splitting or interpretation of pooled effects without
lineage-aware evaluation is prohibited.

---

# Current resource coverage

After deterministic model identity mapping and score eligibility, the Phase 6
resources contain:

| Resource | Scoreable models | Represented lineages |
| --- | ---: | ---: |
| GDSC | 713 | 27 |
| CTRP | 821 | 25 |
| PRISM | 477 | 22 |

Coverage is not uniform across lineages or screens.

Absence of coverage must not be interpreted as biological absence of an
association.

Coverage characterization is used to define what can be estimated.

It is not evidence for or against a program–drug relationship.

---

# Notebook 600 frozen inferential specification

The following notebook-600 rules were frozen before inspection of program–drug
association estimates, p-values, q-values, rankings, or favorable drug/program
patterns.

## Drug-level estimability and lineage-support rule

Primary drug eligibility is defined prospectively from response coverage and
lineage support before inspection of any program–drug association estimate,
p-value, q-value, effect direction, or drug/program ranking.

The same rule is applied across pharmacogenomic resources.

### Supported lineage

For a given drug, a lineage is considered:

`supported`

when at least:

`20 models`

from that lineage have an available primary response value for the drug.

Lineages with fewer than 20 response-covered models for that drug do not
contribute to the corresponding primary pooled association model.

This threshold is an operational estimability requirement rather than a claim
that 20 observations constitute a universal statistical minimum.

It is intended to prevent sparsely represented lineages from contributing
unstable drug-specific information to the primary cross-lineage analysis.

---

### Primary drug eligibility

A drug enters the notebook-600 primary inferential family only when all of the
following conditions are satisfied:

1. at least 3 lineages are `supported`;
2. each supported lineage contains at least 20 response-covered models; and
3. at least 100 models are available in total across the supported lineages.

Therefore, primary eligibility is defined as:

`>=20 models per supported lineage`

and:

`>=3 supported lineages`

and:

`>=100 models across supported lineages`

Only models belonging to supported lineages contribute to the primary
drug-specific association model.

Models from lineages below the 20-model support threshold are not added merely
to increase the global sample size.

---

### Rationale

The rule combines two distinct requirements:

- lineage breadth, to prevent a nominally pan-cancer association from being
  estimated almost entirely from one or two cancer contexts; and
- total effective sample size, to avoid admitting drug-level models that meet
  the lineage criterion only marginally.

A criterion based only on total sample size was rejected because a large
global `N` can remain dominated by a single lineage.

A criterion based only on the number of represented lineages was rejected
because lineages with very sparse response coverage could otherwise contribute
equally to the eligibility count.

No additional maximum-lineage-fraction threshold is imposed.

Potential dominance by individual lineages is evaluated subsequently through
the prespecified lineage-heterogeneity and leave-one-lineage-out
characterization rather than through an additional arbitrary eligibility gate.

---

### Outcome-blind feasibility characterization

Before this rule was frozen, its feasibility was evaluated using only
drug-response availability and lineage membership.

No program score, association coefficient, p-value, q-value, effect direction,
or predictive result was used.

Under the frozen `20 / 3 / 100` rule:

- GDSC: 281 of 295 drugs satisfy primary eligibility;
- CTRP: 499 of 545 compounds satisfy primary eligibility; and
- among the 197 PRISM exact cross-resource compounds with a unique primary
  screen assignment, 194 satisfy primary eligibility.

The PRISM count above characterizes the exact cross-resource replication
universe only. It does not define the complete native PRISM drug universe.

The high retention under the rule indicates that the lineage-aware
estimability requirements do not materially collapse the available
pharmacogenomic search space.

These coverage results are technical feasibility information only.

They are not evidence for or against any program–drug association.

---

### Cross-resource consistency

The eligibility thresholds must not be relaxed or tightened separately for
GDSC, CTRP, or PRISM according to downstream association or replication
results.

A compound that fails the frozen support rule in a resource is considered
insufficiently supported for the corresponding primary analysis in that
resource.

Failure of eligibility reflects insufficient analyzable coverage and must not
be interpreted as evidence of biological absence.

No drug may be rescued into the primary inferential family because it has a
favorable association in another screen, belongs to an interesting
pharmacological class, or is biologically attractive.

---

## Primary notebook-600 association model

The primary inferential family in notebook 600 is restricted to GDSC.

GDSC is treated as developmental/internal pharmacogenomic evidence because
upstream construction of the frozen cell-line program framework is not
independent of GDSC-derived information.

CTRP and PRISM are therefore not included in the notebook-600 primary
multiplicity family and remain reserved for cross-screen replication analyses.

For each eligible GDSC drug and each frozen consensus transcriptomic program,
the primary association model is:

`LN_IC50 ~ program_score + C(OncotreeLineage)`

The model is fitted by ordinary least squares using HC3
heteroskedasticity-robust standard errors.

The executable implementation uses two-sided t-based inference with residual
degrees of freedom (`use_t=True`) for HC3 coefficient tests and reports 95%
confidence intervals. This implementation detail was fixed before inspection
of the primary association results.

Only models belonging to drug-specific supported lineages under the frozen
`20 / 3 / 100` eligibility rule contribute to the corresponding model.

The three program scores are entered separately rather than jointly.

No interaction terms, nonlinear transformations, feature selection, or
data-driven covariate additions are included in the primary model.

The primary GDSC response remains raw `LN_IC50`.

Frozen Phase 4 consensus program scores remain on their existing reference
scale and are not re-standardized within individual drug subsets.

Accordingly:

- positive program coefficients indicate association with higher `LN_IC50`
  and therefore a more resistance-like baseline pharmacogenomic context;
- negative coefficients indicate association with lower `LN_IC50` and
  therefore a more sensitivity-like baseline pharmacogenomic context.

Coefficient magnitude is interpreted on the native GDSC response scale and
must not be compared naively with effect magnitudes from CTRP or PRISM.

Before inferential execution, all candidate drug-program design matrices were
checked for algebraic estimability.

The resulting primary family contains:

`281 eligible drugs × 3 frozen programs = 843 tests`

All 843 candidate models have full-rank design matrices, non-constant response,
and non-constant program scores.

No association coefficient, direction, p-value, or q-value was inspected
before this specification was frozen.

## Primary multiplicity control

The complete notebook-600 primary family consists of the 843 GDSC
drug-program association tests.

Benjamini-Hochberg false-discovery-rate correction is applied jointly across
all 843 tests.

`q < 0.05` defines the FDR-controlled developmental association set eligible
for subsequent characterization and cross-screen replication.

Nominal p-values, biological interest, drug class, target annotation, or
results from other screens must not be used to rescue tests that do not meet
the frozen multiplicity criterion.

No additional hard effect-size threshold is imposed.

Failure to meet the FDR threshold is retained as a valid negative result and
must not be interpreted as evidence of biological absence.

## Lineage robustness and heterogeneity

Lineage robustness is evaluated after the primary model using prespecified
leave-one-supported-lineage-out refits.

These analyses are sensitivity and heterogeneity characterizations.

They do not modify primary coefficients, p-values, q-values, or membership in
the primary FDR-controlled association set.

No lineage-specific result may rescue an association that fails the primary
multiplicity criterion.

Conversely, heterogeneous or lineage-sensitive results that pass the primary
FDR criterion must be reported transparently rather than silently removed.

---

## Additional lineage-heterogeneity characterization

The primary lineage-robustness procedure is frozen as
leave-one-supported-lineage-out refitting.

The exact descriptive summaries were frozen after the primary GDSC association
family had been executed, but before any leave-one-lineage-out refit result was
inspected.

This timing does not alter the already frozen primary model, multiplicity
family, coefficients, p-values, q-values, or FDR-controlled association set.

For every primary GDSC drug-program association, one refit is performed after
omitting each supported lineage in turn.

The leave-one-lineage-out analysis is descriptive and does not define a second
inferential family.

For each primary association, the following summaries are retained:

- number of leave-one-lineage-out refits;
- minimum leave-one-lineage-out coefficient;
- maximum leave-one-lineage-out coefficient;
- median leave-one-lineage-out coefficient;
- fraction of refits retaining the same coefficient sign as the primary model;
- whether any leave-one-lineage-out refit reverses coefficient sign;
- maximum absolute coefficient change relative to the primary estimate; and
- identity of the omitted lineage producing the largest absolute coefficient
  change.

No leave-one-lineage-out p-value or q-value is used as an alternative
significance criterion.

No minimum sign-concordance fraction or maximum coefficient-change threshold is
used to rescue, reject, or reclassify the primary FDR-controlled association.

These summaries characterize sensitivity to lineage composition only.

---

## Proliferation handling

Proliferation remains a recognized potential cell-line confounder.

Before primary notebook-600 inference, the available frozen upstream Phase 3
artifact set was reviewed for a previously defined proliferation
representation with defensible coverage of the relevant Phase 6 model
universe.

No such frozen cell-line proliferation covariate was identified.

Therefore, no proliferation covariate is added to the primary notebook-600
association model.

A new proliferation representation will not be constructed post hoc merely to
reduce this limitation after the analytical universe and primary model have
been defined.

Potential residual proliferation confounding therefore remains an explicit
limitation of the Phase 6 pharmacogenomic association analysis.

This limitation must not be interpreted as evidence that proliferation is
irrelevant to the observed associations.

---

# Frozen notebook 601 predictive-modeling specification

The following notebook-601 decisions are:

**FROZEN BEFORE NOTEBOOK 601 MODEL-PERFORMANCE INSPECTION**

These rules were finalized after completion of notebook 600 and before inspection of any notebook-601 predictive-performance result.

Notebook 601 evaluates whether the three frozen Phase 4 consensus transcriptomic program scores provide reproducible predictive information about GDSC drug response beyond transparent lineage-aware baselines.

The objective is not to maximize predictive performance.

The primary question is:

> For a known GDSC drug and a previously unseen cell-line model belonging to a lineage already represented for that drug, do the three frozen consensus transcriptomic program scores provide incremental predictive information about `LN_IC50` beyond lineage alone?

The primary evaluation therefore concerns within-supported-lineage generalization to previously unseen cell-line models.

It does not establish:

- prediction for clinically treated patients;
- prediction of acquired or longitudinal drug resistance;
- prediction for previously unseen drugs;
- prediction for previously unseen drug families;
- generalization to completely unseen lineages as the primary estimand;
- therapeutic efficacy;
- causal drug-response mechanisms; or
- clinical predictiveness.

---

## Developmental resource and prediction target

Notebook 601 uses GDSC exclusively for model development and internal predictive evaluation.

The prediction target is the frozen notebook-600 GDSC primary response:

`LN_IC50`

with:

`higher value = more resistance-like`

The response remains continuous and is modeled on its frozen native GDSC scale.

Notebook 601 must not:

- dichotomize `LN_IC50` into resistant versus sensitive classes;
- redefine the response according to notebook-600 association results;
- select an alternative GDSC response metric according to predictive performance; or
- transform the target using CTRP or PRISM information.

GDSC remains developmental/internal evidence and must not be described as independent validation.

---

## Primary compound universe

The primary notebook-601 compound universe consists of the:

`281`

GDSC drugs already declared eligible in notebook 600 under the frozen `20 / 3 / 100` coverage and lineage-support rule.

Eligibility is therefore inherited from the frozen notebook-600 technical universe and is not redefined according to predictive performance.

Notebook 601 must not restrict the primary modeling universe according to:

- notebook-600 association p-values;
- notebook-600 q-values;
- membership in the notebook-600 FDR-controlled association set;
- effect direction or magnitude;
- leave-one-lineage-out behavior from notebook 600;
- drug target;
- pathway annotation;
- pharmacological attractiveness;
- Phase 5 functional-vulnerability evidence;
- CTRP or PRISM coverage; or
- external-screen behavior.

In particular, the 222 GDSC drugs with at least one notebook-600 FDR association do not define the notebook-601 primary modeling universe.

The frozen notebook-600 GDSC association-result artifact must not be used to select notebook-601 compounds, features, models, thresholds, or resampling rules.

---

## Predictive-model architecture

Notebook 601 uses one independent predictive analysis per eligible GDSC drug.

No primary model pools different drugs into a shared drug-by-cell-line prediction model.

No model parameter, fitted response relationship, or learned drug representation is shared across drugs.

This architecture is chosen because the primary scientific question concerns whether the frozen transcriptomic programs add predictive information for a known drug, rather than whether a model can learn transferable representations across compounds.

The primary architecture therefore does not claim generalization to previously unseen drugs.

---

## Frozen feature universe

The primary predictive feature universe is restricted to the three frozen Phase 4 consensus transcriptomic program scores:

- `CONSENSUS_TX_01`;
- `CONSENSUS_TX_02`; and
- `CONSENSUS_TX_03`.

All three program scores enter the primary predictive model jointly.

No program may be:

- removed because it performs poorly;
- selected because it performed favorably in notebook 600;
- reweighted according to GDSC response;
- reoriented;
- re-standardized within a drug-specific subset; or
- replaced by a downstream-derived representation.

No genome-wide or transcriptome-wide feature space is part of the primary notebook-601 analysis.

Gene-level expression features are not introduced merely to obtain gene-level SHAP attribution.

If notebook 602 later attributes the frozen primary model, the resulting SHAP attribution is therefore program-level.

Frozen gene weights and biological annotations may subsequently provide hierarchical biological contextualization, but they do not become gene-level model attribution.

---

## Primary baseline model

For each eligible GDSC drug, the primary transparent baseline is:

`LN_IC50 ~ C(OncotreeLineage)`

using only the drug-specific supported lineages inherited from notebook 600.

This baseline represents predictable drug-response structure attributable to lineage membership without using the frozen consensus program scores.

An intercept-only predictor may be retained as a descriptive no-information reference but is not the primary scientific comparator.

---

## Primary predictive model

For each eligible GDSC drug, the primary predictive model is:

`LN_IC50 ~ C(OncotreeLineage) + CONSENSUS_TX_01 + CONSENSUS_TX_02 + CONSENSUS_TX_03`

The model is linear and contains:

- one intercept;
- lineage representation;
- the three frozen consensus program scores; and
- no interaction terms.

No nonlinear transformation, interaction search, automated feature selection, Random Forest, gradient boosting, XGBoost, neural network, or other higher-complexity model family is part of the primary notebook-601 analysis.

The primary model family is fixed prospectively and is not selected according to observed cross-validation performance.

---

## Primary generalization target

The primary evaluation target is:

> prediction for a previously unseen cell-line model from a lineage already represented in the training data for the same known drug.

This estimand must remain explicit when interpreting notebook-601 performance.

The primary evaluation does not establish performance for a completely unseen lineage.

Generalization to an unseen lineage is assessed separately only as a secondary stress test defined below.

---

## Primary lineage-aware resampling

Primary model evaluation uses:

`5-fold lineage-stratified cross-validation × 5 repeats`

independently for each eligible GDSC drug.

For each drug:

- only models belonging to the frozen drug-specific supported lineages contribute;
- fold assignment is stratified by `OncotreeLineage`;
- every supported lineage is represented across the five folds;
- each `ModelID` belongs to exactly one test fold per repeat;
- the same `ModelID` cannot occur in both training and test partitions within a fold;
- baseline and program models use exactly the same folds;
- response values are not used to define fold membership; and
- no random pan-cancer train/test split is permitted.

The notebook-600 requirement of at least 20 response-covered models per supported lineage ensures that the five-fold primary design is technically feasible for every retained lineage.

Performance is calculated from the complete set of out-of-fold predictions generated within each repeat.

Fold-specific `R²` values are not averaged to define the primary repeat-level `R²`.

Instead, all held-out predictions from the five folds of one repeat are concatenated and evaluated jointly against their corresponding observed values.

The five resulting repeat-level performance estimates are then summarized prospectively as defined below.

---

## Randomness and reproducibility

The fixed notebook-601 random seed is:

`601`

The five repeated lineage-stratified partitions are generated deterministically from this frozen seed.

The seed must not be changed according to whether particular partitions produce more favorable predictive performance.

Input ordering must be deterministic before resampling.

---

## Preprocessing boundaries

Notebook 601 preserves the frozen consensus-program score scale.

The primary analysis performs no:

- external or combined re-standardization;
- drug-specific program-score re-standardization;
- outcome-informed scaling;
- imputation;
- PCA;
- feature selection;
- feature screening; or
- response-informed transformation.

Any categorical encoding required for lineage is fitted within the corresponding training partition.

No transformation estimated from a held-out fold may contribute to the fitted training model.

Unexpected missing program scores, duplicate analytical units, or incompatible frozen handoff structure must trigger diagnostic review rather than an improvised imputation, deduplication, or replacement rule.

---

## Hyperparameter tuning

The primary notebook-601 model has no tuned hyperparameters.

No nested hyperparameter search is therefore required for the primary analysis.

The absence of tuning is intentional and preserves a low-dimensional, transparent model directly aligned with the frozen scientific question.

Alternative model families must not be introduced after inspecting primary predictive performance in order to improve notebook-601 results.

Any later alternative-model analysis would require separate prospective definition and explicit exploratory or sensitivity labeling.

---

## Primary predictive-performance metric

The primary metric is incremental out-of-fold explained variance relative to the lineage-only baseline:

`delta_R2 = R2_program_model - R2_lineage_baseline`

For each repeat:

- `R2_lineage_baseline` is calculated from the concatenated out-of-fold lineage-baseline predictions;
- `R2_program_model` is calculated from the concatenated out-of-fold primary-model predictions; and
- `delta_R2` is their difference.

The primary drug-level incremental-performance summary is:

`median(delta_R2 across 5 repeats)`

This metric directly addresses whether the frozen consensus programs add predictive information beyond lineage.

---

## Supporting predictive-performance metrics

The following supporting out-of-fold metrics are reported for both the lineage baseline and the full program model:

- `R²`;
- root mean squared error (`RMSE`); and
- mean absolute error (`MAE`).

Relative RMSE reduction may also be reported descriptively.

The primary model is not selected according to whichever supporting metric appears most favorable.

Performance differences across drugs must not be treated as biologically equivalent solely because their numerical values are similar.

---

## Model-selection rule

There is no post-performance model-family selection in the primary notebook-601 analysis.

The lineage-only baseline and the lineage-plus-three-program primary model are fixed before performance inspection.

No drug-specific choice between multiple model families is permitted.

No drug is promoted merely because it ranks highly relative to other drugs.

Notebook 601 uses absolute prospectively defined predictive-validity criteria rather than selecting the best-performing fixed number or percentile of compounds.

---

## Drug-family leakage control

The primary notebook-601 architecture prevents cross-drug parameter sharing by fitting every eligible drug independently.

Therefore:

- response measurements from one drug do not train the predictive model for another drug;
- related compounds do not share fitted parameters;
- `PUTATIVE_TARGET` and `PATHWAY_NAME` do not define leakage groups for the primary model;
- pharmacological family annotations do not enter the prediction model; and
- no drug-family grouping is used to rescue or prioritize predictive results.

Because drug-specific performance estimates may nevertheless be correlated across related compounds or shared cell-line populations, the 281 drug-level analyses must not be interpreted as 281 independent biological replications.

Any future explicit drug-family analysis would require a separately frozen family-identity authority and prospective analytical rule.

---

## Cell-line-overlap control

The same cell-line model may have GDSC response measurements for multiple drugs.

This does not create within-model train/test leakage in the primary architecture because each drug is fitted independently and no parameters are shared across drugs.

Within every drug and every repeat:

- each `ModelID` appears in exactly one held-out fold;
- no `ModelID` appears simultaneously in the training and test set for the same fitted model; and
- baseline and full models use the same cell-line partitions.

Cross-drug dependence created by repeated use of the same biological models remains an explicit limitation when summarizing the collection of drug-level results.

---

## External-screen isolation

CTRP and PRISM remain sealed external pharmacogenomic resources during notebook 601 model development and internal evaluation.

Notebook 601 must not inspect CTRP or PRISM association or predictive-performance outcomes in order to choose:

- compounds;
- features;
- model family;
- hyperparameters;
- performance metrics;
- predictive-validity thresholds;
- resampling structure; or
- interpretation rules.

CTRP and PRISM outcomes are reserved for notebook 603 cross-screen replication under separately frozen rules.

Their notebook-600 technical interfaces may remain registered and available for provenance, but their response outcomes must not inform notebook-601 modeling decisions.

---

## Phase 5 isolation

Phase 5 functional-vulnerability results do not enter notebook 601 as:

- features;
- drug-selection criteria;
- model-selection criteria;
- predictive-validity thresholds; or
- rescue evidence.

Notebook 601 therefore remains analytically separated from downstream vulnerability-based therapeutic prioritization.

---

## Secondary unseen-lineage stress test

Generalization to a completely unseen lineage is not the primary notebook-601 estimand.

A prospectively defined secondary stress test uses leave-one-supported-lineage-out evaluation.

For each eligible drug and each supported lineage:

1. all models from one lineage are held out;
2. models from all remaining supported lineages form the training set;
3. the held-out lineage is never represented during fitting.

Because a lineage-specific categorical effect cannot be estimated for a lineage absent from training, the secondary stress-test comparator is:

`LN_IC50 ~ 1`

and the corresponding program model is:

`LN_IC50 ~ CONSENSUS_TX_01 + CONSENSUS_TX_02 + CONSENSUS_TX_03`

No lineage indicator is included in either secondary stress-test model.

This analysis asks whether the frozen transcriptomic programs retain any predictive transportability to a lineage absent from training.

It is a secondary robustness characterization only.

It must not:

- replace the primary lineage-stratified evaluation;
- determine primary model selection;
- rescue a model that fails the primary predictive-validity criteria;
- redefine the primary generalization target; or
- be used to select favorable drugs for subsequent analysis.

---

## Predictive-validity gate for subsequent SHAP interpretation

Notebook 602 model attribution is not justified solely because a model can be fitted.

For a GDSC drug to have adequate internal predictive validity for primary program-level SHAP interpretation, all of the following prospectively frozen criteria must be satisfied:

1. median out-of-fold full-model performance across the five repeats:

   `median R2_program >= 0.05`

2. median incremental out-of-fold performance across the five repeats:

   `median delta_R2 >= 0.02`

3. positive incremental performance in at least four of the five repeats:

   `delta_R2 > 0 in >= 4 of 5 repeats`

These thresholds are operational predictive-validity criteria.

They are not universal statistical or biological significance thresholds.

The first criterion requires the complete fitted model to demonstrate non-trivial out-of-fold predictive validity.

The second requires the frozen consensus programs to provide non-trivial incremental predictive information beyond lineage.

The third requires that the incremental improvement not depend on a single favorable repeated partition.

The five repeats are not treated as statistically independent observations, and the `4 of 5` requirement is not interpreted as a formal hypothesis test.

No p-value or multiplicity-adjusted significance test is used as the primary predictive-validity gate.

---

## Predictive-validity outcome categories

Failure of the SHAP-eligibility gate is retained as a valid notebook-601 result.

Where useful for transparent interpretation, failure may be characterized descriptively according to its reason, including:

- inadequate overall predictive validity;
- inadequate incremental program contribution;
- unstable incremental predictive improvement; or
- combinations of these conditions.

These categories must not be used to create alternative post hoc promotion routes.

A drug failing the frozen gate must not be rescued because of:

- notebook-600 FDR association;
- biological interest;
- drug target or pathway;
- Phase 5 evidence;
- external literature;
- CTRP or PRISM behavior; or
- favorable SHAP appearance.

Passing the gate does not establish biological importance, mechanism, causality, external reproducibility, clinical predictiveness, or therapeutic relevance.

It establishes only sufficient internal predictive validity to justify primary interpretation of fitted-model behavior in notebook 602.

The exact notebook-602 attribution procedure, background/reference handling, attribution aggregation, stability analysis, and lineage-consistency rules remain subject to their own prospective freeze before SHAP results are inspected.

---

## Proliferation and unresolved confounding

Notebook 601 inherits the notebook-600 conclusion that no previously frozen and methodologically defensible proliferation representation with appropriate coverage is available for this Phase 6 model universe.

No new proliferation proxy is constructed post hoc solely to improve predictive robustness or reduce this limitation.

Residual proliferation confounding therefore remains explicit.

Other unresolved cell-line biological or technical confounders must likewise be reported rather than improvised after predictive results are known.

---

## Negative-result policy for notebook 601

Notebook 601 remains scientifically complete if:

- most or all drugs have low out-of-fold predictive performance;
- lineage alone explains most predictable response structure;
- the three frozen programs add little incremental information;
- incremental improvement is unstable across repeated lineage-aware partitions;
- unseen-lineage transportability is weak;
- few or no drugs satisfy the predictive-validity gate for notebook 602; or
- no primary program-level SHAP interpretation is ultimately justified.

No feature space, model family, threshold, resampling rule, or compound universe may be relaxed after predictive-performance inspection in order to ensure that notebook 602 produces favorable attribution results.

---

# Decisions pending before notebook 602 SHAP analysis

The following items are:

**PENDING FREEZE BEFORE NOTEBOOK 602 ATTRIBUTION INSPECTION**

SHAP analysis may proceed only after the corresponding predictive model has a
frozen target, feature space, evaluation structure, and adequately reported
predictive validity.

The attribution contract must define:

- which fitted models are eligible for attribution;
- whether attribution is calculated on held-out, out-of-fold, or other
  leakage-safe predictions;
- SHAP background/reference handling;
- attribution aggregation;
- attribution-stability analysis;
- lineage-consistency characterization; and
- model-class sensitivity where applicable.

If the fitted model uses the three consensus-program scores as features, SHAP
attribution is program-level.

Frozen gene weights may be used for downstream biological contextualization.

They must not be transformed into gene-level SHAP values unless genes were
actual fitted-model features.

SHAP explains fitted-model behavior.

It does not establish causality or mechanism.

---

# Decisions pending before notebook 603 cross-screen replication

The following items are:

**PENDING FREEZE BEFORE NOTEBOOK 603 REPLICATION-RESULT INSPECTION**

The final cross-screen replication framework must define:

- exact-compound replication eligibility;
- resource-specific primary response representation;
- same-model overlap handling;
- non-overlapping-model analysis;
- treatment of insufficient non-overlap coverage;
- direction-concordance rule;
- effect-size comparison;
- screen-specific multiplicity;
- exact versus drug-family replication terminology; and
- handling of failed, heterogeneous, or unavailable replication.

Exact cross-screen replication must use the frozen exact-compound identity
framework unless an additional identity authority is prospectively introduced
before replication results are inspected.

Related compounds from the same drug family are contextual pharmacological
analogues, not exact replication.

Because CTRP and PRISM may share cell lines with GDSC and with each other,
cross-screen agreement on overlapping models must not automatically be
presented as independent cell-level replication.

---

# General prohibited analyses and interpretations

Phase 6 must not:

- redefine frozen Phase 4 programs using pharmacogenomic results;
- select program weights according to drug-response associations;
- select exact compound mappings according to favorable replication;
- use fuzzy compound matching as an unreported rescue route;
- resolve ambiguous cell-line mappings according to response behavior;
- pool GDSC, CTRP, and PRISM response values naïvely;
- pool PRISM screens naïvely;
- treat repeated CTRP experiments as independent biological observations;
- select response metrics according to favorable association results;
- use random pan-cancer train/test splitting;
- fit preprocessing or feature-selection steps on held-out evaluation data;
- use external replication screens to tune a model that will later be evaluated
  on those screens;
- interpret SHAP as causal biological evidence;
- report downstream gene annotation as gene-level SHAP when genes were not
  model features;
- describe cross-screen agreement as clinical validation;
- infer therapeutic efficacy;
- infer validated targets;
- infer therapeutic reversal; or
- reconstruct longitudinal adaptive resistance from cross-sectional screens.

---

# Negative-result policy

Phase 6 remains scientifically complete if:

- no program–drug association survives multiplicity correction;
- associations are lineage-restricted or heterogeneous;
- GDSC developmental findings do not reproduce in CTRP or PRISM;
- exact-compound overlap proves too sparse for some hypotheses;
- non-overlapping-model replication has limited power;
- predictive models do not outperform transparent baselines;
- predictive performance is unstable across lineage-aware partitions;
- SHAP attribution is unstable;
- different model classes produce inconsistent attribution;
- external-screen performance is poor;
- cross-screen effect directions disagree; or
- pharmacogenomic evidence does not strengthen a frozen consensus program.

No eligibility rule, statistical family, mapping rule, response metric,
resampling design, or interpretation threshold may be relaxed after result
inspection to manufacture positive findings.

Null, failed, and heterogeneous results remain valid Phase 6 outputs.

---

# Downstream-use boundary

Phase 6 outputs may contribute to Phase 9 integrated evidence synthesis as
separately traceable pharmacogenomic and explainable-model evidence.

Downstream integration must preserve the distinction between:

- developmental/internal association evidence;
- external cross-screen replication;
- predictive-model validity;
- model attribution;
- attribution stability;
- exact-compound replication;
- pharmacological family/context evidence; and
- unresolved lineage or cell-line-overlap limitations.

Phase 6 results must not be used retrospectively to:

- remove a frozen Phase 4 program;
- promote or redefine a frozen Phase 4 program;
- convert a Phase 5 putative vulnerability into a validated target;
- establish therapeutic causality; or
- claim clinical drug resistance prediction.

---

# Scientific interpretation boundary

Phase 6 may support statements such as:

- a frozen consensus program is associated with a resistance-like
  pharmacogenomic context for a compound;
- an association is lineage-aware, heterogeneous, or lineage-restricted;
- a developmental/internal GDSC association shows or fails to show concordant
  external cross-screen evidence;
- a frozen program representation contributes predictive information under a
  leakage-aware evaluation design;
- a fitted model displays stable or unstable program-level attribution; or
- cross-screen evidence is limited by compound coverage, lineage coverage,
  overlapping cell lines, or platform differences.

Phase 6 does not support statements that:

- a program causes drug resistance;
- a compound clinically overcomes resistance;
- a program is a validated biomarker;
- a gene or program is a validated therapeutic target;
- SHAP identifies a causal regulator;
- pharmacogenomic association proves mechanism;
- cross-screen agreement establishes therapeutic efficacy; or
- baseline cell-line response reconstructs acquired adaptive resistance.

Association remains distinct from causality.

Predictive attribution remains distinct from biological mechanism.

Cross-screen computational replication remains distinct from experimental or
clinical validation.

---

# Planned provenance and artifact registration

Stable Phase 6 outputs required downstream should be persisted, validated,
provenance-recorded, and registered in:

`config/artifact_registry.json`

using the Phase 6 namespace:

`phase6.*`

Registration should include, where applicable:

- stable artifact identifier;
- exact repository path;
- producer notebook;
- analytical role;
- shape;
- byte size;
- SHA256 identity;
- explicit upstream artifact lineage;
- response-resource identity;
- applicable mapping rules;
- score origin;
- primary/sensitivity status; and
- relevant interpretation limitations.

Derived score projections, crosswalks, eligibility tables, primary association
outputs, predictive-model outputs, attribution outputs, and replication outputs
should be persisted only when they constitute stable downstream interfaces.

Intermediate diagnostic objects need not be registered merely because they were
computed.

---

# Analytical closure criteria

Phase 6 will be considered analytically complete when:

1. all Phase 6 inferential and evaluation rules marked `PENDING FREEZE` have
   been resolved before inspection of their corresponding results;
2. the Phase 6 score universe and score provenance are frozen;
3. model and compound identity mappings are frozen;
4. primary pharmacogenomic response handling is frozen;
5. the complete notebook-600 primary inferential family is generated and
   analyzed under the frozen rules;
6. multiplicity correction is applied exactly as prespecified;
7. required lineage and sensitivity characterizations are completed;
8. notebook-601 predictive models are evaluated using the frozen leakage-aware
   design;
9. SHAP is calculated only for models meeting the frozen attribution
   preconditions;
10. attribution stability is reported without exceeding the actual fitted
    feature resolution;
11. notebook-603 replication is evaluated under the frozen exact-compound and
    overlap-aware rules;
12. negative, heterogeneous, non-replicating, and weakly predictive findings
    remain explicitly represented;
13. stable downstream-required outputs are persisted and validated;
14. analysis metadata and provenance are finalized; and
15. downstream-required artifacts are registered with frozen identity.

Analytical completion does not require a positive association, successful
prediction, stable attribution, or successful cross-screen replication.
