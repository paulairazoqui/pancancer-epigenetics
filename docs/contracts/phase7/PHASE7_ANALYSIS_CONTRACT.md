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

Some implementation parameters remain explicitly marked:

`PENDING FREEZE BEFORE CONNECTIVITY EXECUTION`

Those parameters must be finalized prospectively, without inspection of Phase 7
connectivity results, before the corresponding inferential execution begins.

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

Operational parameters explicitly marked `PENDING FREEZE BEFORE CONNECTIVITY
EXECUTION` remain unresolved and must be finalized before the corresponding
connectivity or inferential results are inspected.

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

The exact perturbational-dispersion statistic, binning rule, tie handling,
minimum stratum-size handling, and any cross-program coupling of permutation
indices are:

`PENDING FREEZE BEFORE CONNECTIVITY EXECUTION`

These rules must be frozen before any primary connectivity result is inspected.

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

The competitive sensitivity must preserve, prospectively and as closely as
defined before execution:

- query size;
- signed-weight distribution;
- landmark / best-inferred composition; and
- perturbational-dispersion matching.

Its exact matching, resampling, and Monte Carlo specification is:

`PENDING FREEZE BEFORE CONNECTIVITY EXECUTION`

The competitive null cannot replace, redefine, or rescue the primary
conditional-null inference.

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

The exact sequential algorithm parameters, including exceedance target,
maximum null draws, batch size, seed schedule, and implementation details are:

`PENDING FREEZE BEFORE CONNECTIVITY EXECUTION`

These parameters must be selected through an outcome-blind computational
benchmark and frozen before connectivity-result inspection.

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

The exact rank-based enrichment formula and deterministic tie handling are:

`PENDING FREEZE BEFORE CONNECTIVITY EXECUTION`

Only one prospectively frozen implementation will be used.

Multiple gene-count cutoffs or alternate enrichment statistics must not be
screened and then selected according to favorable results.

---

# Perturbational amplitude, proliferation, and stress diagnostics

Phase 7 will prospectively characterize broad perturbational context without
using those diagnostics as primary exclusion gates.

## Perturbational amplitude

Available LINCS activity-related quantities such as:

- `tas`; and
- `ss_ngene`

may be reported together with a prospectively defined transcriptomic-amplitude
summary.

These measures must be described as perturbational activity/amplitude
diagnostics.

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

Exact artifact identifiers and schemas are:

`PENDING FREEZE BEFORE CONNECTIVITY EXECUTION`

They should be finalized before implementation creates the corresponding stable
downstream interfaces.

At minimum, stable Phase 7 handoffs are expected to cover:

- query definitions and query metadata;
- null-stratification metadata;
- primary perturbagen-level connectivity results;
- lineage-level connectivity summaries;
- empirical-null inference metadata;
- prespecified sensitivity summaries;
- proliferation/stress/amplitude diagnostic summaries;
- exact-structure reconciliation;
- compound/structure-level perturbational summaries;
- target/MoA mappings and mechanism summaries; and
- analysis metadata/provenance.

Intermediate matrices or null-draw batches need not be registered merely
because they were computed.

---

# Operational freeze required before notebook 701 inference

Before the first primary connectivity result is inspected, a prospective
operational addendum to this contract must freeze at minimum:

1. exact perturbational-dispersion statistic used for null stratification;
2. dispersion-bin construction and tie handling;
3. minimum-stratum handling;
4. whether primary-null permutations are coupled across programs;
5. competitive-null gene-matching and replacement rules;
6. exact sequential Monte Carlo procedure;
7. exceedance/stopping parameter;
8. maximum null draws;
9. deterministic seed schedule;
10. batch and numerical-precision policy where analytically relevant;
11. empirical p-value estimator;
12. exact CMap-style rank-enrichment statistic and tie handling;
13. any transcriptomic-amplitude summary beyond frozen LINCS metadata fields;
14. exact diagnostic-score implementation;
15. stable artifact identifiers and required schemas; and
16. local validation tolerances needed to confirm deterministic
    implementation.

These decisions must be made without inspection of Phase 7 connectivity
results.

If a technical benchmark demonstrates that a proposed implementation is
infeasible, the replacement rule must be selected and documented before result
inspection.

---

# Analytical closure criteria

Phase 7 will be considered analytically complete when:

1. all items marked `PENDING FREEZE BEFORE CONNECTIVITY EXECUTION` have been
   prospectively resolved;
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
