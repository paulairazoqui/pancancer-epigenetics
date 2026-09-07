# Notebook 450 Analysis Contract

## Status

Implemented.

This document consolidates the analytical decisions used by notebook
`450 — Secondary Genomic Context Characterization`.

It is a documentation refactor of decisions that were explicitly established
within the notebook before the corresponding result-inspection stages. It does
not constitute retrospective preregistration, introduce new analytical gates,
change the completed analysis, or promote exploratory diagnostics into primary
criteria.

The authoritative executable record remains:

`notebooks/phase4b_secondary_molecular_characterization/450_secondary_genomic_context_characterization.ipynb`

---

## Purpose

Notebook 450 characterizes somatic genomic context associated with the three
frozen Phase 4 cross-system consensus transcriptomic programs in the TCGA
primary-tumor cohort.

Somatic mutation information is used strictly as a downstream contextual layer.
It does not contribute to consensus-program discovery, construction,
orientation, weighting, eligibility, or naming.

The analysis is designed to distinguish:

- primary gene-level mutation–program associations;
- lineage-aware recurrence across eligible TCGA projects;
- stability under prespecified sensitivity analyses; and
- exploratory evidence that apparent gene-level associations may be entangled
  with broader observed mutational-load context.

All reported relationships remain computational associations. They do not
establish causal mechanisms, driver status, biological necessity, clinical
prediction, therapeutic relevance, or validated targets.

---

## Frozen upstream inputs

Notebook 450 consumes frozen upstream information without reopening the
corresponding analyses.

### Somatic mutation resource

The mutation layer is inherited from:

`108 — TCGA Somatic Mutation Acquisition and Audit`

The authoritative frozen handoffs are:

- `phase1.108.primary_file_handoff`;
- `phase1.108.case_eligibility`;
- `phase1.108.download_validation`; and
- `phase1.108.case_payload_status`.

Notebook 450 does not reselect the mutation resource, remap tumor samples, or
redefine mutation-resource eligibility.

### Consensus tumor programs

The outcome space is inherited from:

`401 — Consensus Program Construction`

The primary program universe is restricted to:

- `CONSENSUS_TX_01`;
- `CONSENSUS_TX_02`; and
- `CONSENSUS_TX_03`.

The frozen tumor scores are consumed exactly as produced by Phase 4.

Notebook 450 does not introduce the broader Phase 2 candidate-program space
into the primary genomic-context analysis.

### Confounder covariates

Where used in sensitivity analyses, tumor-side covariates are taken from the
frozen Phase 2 confounder artifact rather than reconstructed locally.

---

## Mutation-resource representation

### Exact-sample analytical unit

Mutation-resource eligibility is defined at the frozen TCGA tumor-sample level.

Only MAF files mapped exactly to the frozen tumor sample selected upstream are
eligible for case-level mutation-state construction.

Cases without a mutation resource or without an exact match to the frozen tumor
sample remain unavailable for primary mutation-state analysis.

They are not assigned a negative mutation state.

---

## Multi-MAF cases

Some frozen tumor samples are represented by more than one exact-sample MAF.

No arbitrary single-file selection is permitted.

For the primary analysis, all retained exact-sample MAFs for a case are combined
by:

1. taking the union of observed variants across retained files; and
2. removing duplicate observations using the frozen genomic variant key.

This preserves all available exact-sample information without allowing file
multiplicity to create duplicate variant observations.

A separate single-MAF sensitivity analysis is used to evaluate whether
multi-file representation materially affects the primary associations.

---

## Genomic variant identity

A somatic variant is identified by the following genomic key:

- `NCBI_Build`;
- `Chromosome`;
- `Start_Position`;
- `End_Position`;
- `Reference_Allele`; and
- `Tumor_Seq_Allele2`.

The audited mutation resource uses GRCh38 coordinates.

Within the frozen resource, `Tumor_Seq_Allele2` provides the non-reference tumor
allele and is therefore used as the alternate allele in the genomic key.

Variant identity is genomic rather than file-specific.

`Hugo_Symbol` and `Variant_Classification` are retained as annotations but are
not part of the genomic identity key.

---

## Structurally empty MAFs

A structurally empty MAF is not interpreted as evidence that a tumor is
mutation-free.

Cases for which every retained exact-sample MAF is structurally empty are
classified as indeterminate for primary binary gene-level mutation analysis.

They are excluded from primary mutation-state construction rather than being
assigned to the non-mutated group.

For cases containing both empty and non-empty retained MAFs:

- the non-empty MAFs remain informative;
- empty files contribute no variant observations; and
- an empty file does not negate a variant observed in another retained MAF for
  the same case.

---

## Gene-level mutation-state terminology

For informative mutation-resource cases, binary gene state is described as:

- `qualifying_somatic_variant_observed`; or
- `no_qualifying_somatic_variant_observed`.

The second category means only that no qualifying variant was observed in the
retained informative mutation resource under the frozen variant definition.

It must not be described as definitive wild type.

---

## Primary qualifying somatic-variant definition

The primary mutation representation is based on an outcome-blind set of
protein-altering or canonical splice-site classifications.

A variant qualifies for the primary gene-level mutation state when
`Variant_Classification` is one of:

- `Missense_Mutation`;
- `Nonsense_Mutation`;
- `Frame_Shift_Del`;
- `Frame_Shift_Ins`;
- `Splice_Site`;
- `In_Frame_Del`;
- `In_Frame_Ins`;
- `Translation_Start_Site`; or
- `Nonstop_Mutation`.

This definition was fixed before mutation–program associations were inspected.

---

## Non-qualifying classifications

The following observed classifications do not contribute to the primary binary
gene-level mutation state:

- `Silent`;
- `Intron`;
- `Splice_Region`;
- `RNA`;
- `3'UTR`;
- `5'UTR`;
- `5'Flank`;
- `3'Flank`; and
- `IGR`.

`Splice_Region` is kept separate from canonical `Splice_Site` in the primary
definition because the broader annotation does not by itself imply an
equivalent functional consequence.

---

## Extended splice-region sensitivity

A prespecified sensitivity analysis extends the qualifying definition by adding:

- `Splice_Region`.

This sensitivity is used only to characterize stability of primary
associations.

It cannot replace the primary qualifying-variant definition because it produces
more favorable results.

---

## Variant filters not introduced

The primary mutation definition does not introduce additional thresholds based
on:

- variant allele fraction;
- sequencing depth;
- mutation count;
- predicted pathogenicity;
- cancer-driver annotation;
- external functional scores; or
- gene-specific biological prior knowledge.

`Variant_Type` is not used as an additional independent eligibility filter once
the frozen `Variant_Classification` rule has been applied.

This avoids retrospectively optimizing mutation-state definitions after
association results are visible.

---

## Primary gene universe

The primary gene universe is determined exclusively from mutation prevalence
and project-level statistical testability before frozen program-score
associations are examined.

For a gene to receive support from a TCGA project, that project must contain at
least:

- 10 informative cases with a qualifying somatic variant observed in the gene;
  and
- 20 informative cases with no qualifying somatic variant observed in the gene.

A gene enters the primary recurrent-gene universe only when these conditions
are satisfied in at least:

- 3 distinct TCGA projects.

Under the frozen mutation resource and qualifying-variant definition, this rule
produces a primary universe of 4,449 genes.

Eligibility is not determined by:

- association strength;
- p-value or q-value;
- cancer-driver annotation;
- pathway membership;
- predicted pathogenicity;
- program identity; or
- prior biological expectation.

---

## Supported-project restriction

Each gene is analyzed only within the TCGA projects in which it satisfies the
frozen mutated and non-mutated group-size requirements.

Consequently, a pan-cancer coefficient for a gene is a common adjusted
association across its supported TCGA projects, not necessarily across all TCGA
projects represented in the frozen tumor cohort.

This distinction must remain explicit when interpreting cross-cancer
recurrence.

---

## Frozen primary inferential family

Every eligible gene is evaluated against every frozen consensus tumor program.

The primary family is therefore:

`4,449 genes × 3 consensus programs = 13,347 gene × program tests`

All 13,347 tests belong to one primary multiple-testing family.

Genes or programs are not removed from the family because of:

- unfavorable effect direction;
- small effect magnitude;
- lineage heterogeneity;
- lack of statistical significance;
- sensitivity-analysis behavior; or
- downstream biological interpretation.

---

## Frozen program-score scale

Consensus tumor scores are used exactly as frozen by Phase 4.

No additional:

- global standardization;
- within-project standardization;
- gene-specific scaling; or
- outcome-specific transformation

is applied before mutation–program modeling.

The mutation-status coefficient is therefore interpreted in frozen
consensus-program score units.

---

## Primary statistical model

For each eligible gene × program pair, the primary model is:

`program_score ~ mutation_status + C(project_id)`

where:

- `program_score` is the frozen consensus tumor score;
- `mutation_status` indicates whether a qualifying somatic variant was observed
  for the gene; and
- `C(project_id)` accounts for TCGA project/lineage structure.

Only the gene's supported projects contribute to its primary model.

The mutation-status coefficient represents an adjusted observational
association between mutation state and frozen program score.

It is not interpreted as a causal effect.

---

## Primary uncertainty estimate

Primary linear models use heteroskedasticity-consistent HC3 standard errors.

Reported primary statistics include:

- mutation-status coefficient;
- HC3 standard error;
- 95% confidence interval;
- test statistic; and
- p-value.

HC3 inference is used without implying that all biological or technical
dependence has been eliminated.

---

## Primary covariate strategy

TCGA project is the only mandatory adjustment variable in the primary model.

This preserves the complete informative mutation-resource cohort while
accounting for major lineage structure.

Additional biological covariates are not automatically included because their
coverage is incomplete and lineage dependent and, in some cases, adjustment
would change the biological estimand rather than simply remove technical noise.

---

## Tumor-purity sensitivity

Tumor purity is evaluated through a prespecified complete-case sensitivity
analysis using:

`absolute_purity`

The sensitivity model is:

`program_score ~ mutation_status + absolute_purity + C(project_id)`

The primary supported-project definition remains fixed.

Purity-adjusted estimates are interpreted as sensitivity evidence only because
complete-case restriction changes the analyzable cohort and purity availability
is lineage dependent.

Purity sensitivity cannot rescue a primary association.

---

## Proliferation sensitivity

Proliferation is evaluated through a separate prespecified complete-case
sensitivity analysis using:

`external_panimmune_proliferation_score`

The sensitivity model is:

`program_score ~ mutation_status + external_panimmune_proliferation_score + C(project_id)`

The primary supported-project definition remains fixed.

Proliferation adjustment is kept separate from the primary model because
proliferative state may be part of the biological context represented by a
frozen consensus program rather than a purely technical nuisance variable.

---

## Covariates not included by default

The following variables are not mandatory components of the primary model:

- `leukocyte_fraction`;
- technical plate or center covariates; and
- `sex_at_birth`.

They may only be introduced in a separately justified exploratory analysis
addressing a specific interpretation question.

They are not used as generic post hoc adjustment variables.

---

## Single-MAF sensitivity

A prespecified sensitivity analysis restricts the informative mutation cohort
to cases represented by exactly one retained MAF.

The primary qualifying-variant definition, supported-project structure, program
scores, and model specification otherwise remain unchanged.

This sensitivity evaluates whether multi-MAF representation materially affects
primary effect direction or magnitude.

---

## Sensitivity-analysis role

The required sensitivity analyses are:

1. absolute-purity adjustment;
2. proliferation adjustment;
3. restriction to single-MAF cases; and
4. extension of the qualifying-variant definition to include `Splice_Region`.

They are evaluated for primary FDR-supported gene × program associations as
stability analyses.

Sensitivity results are interpreted through:

- effect direction;
- effect magnitude;
- retained lineage support; and
- concordance with the primary estimate.

They do not define a second significance family and cannot rescue an association
that fails the primary inferential framework.

---

## Primary multiplicity control

All 13,347 primary gene × program tests form one inferential family.

Benjamini–Hochberg FDR correction is applied globally across that family.

The primary support threshold is:

`q < 0.05`

Sensitivity analyses, within-project models, leave-one-project-out analyses,
and exploratory burden diagnostics remain outside this primary FDR family.

---

## Within-project characterization

For primary FDR-supported gene × program associations, project-specific effects
are estimated within each supported TCGA project.

These estimates are used to characterize:

- effect direction;
- cross-project directional consistency; and
- lineage dependence.

Per-project statistical significance is not required for the cross-cancer
recurrence designation.

The within-project analyses are therefore contextual consistency evidence, not
independent confirmatory tests.

---

## Leave-one-project-out characterization

For primary FDR-supported associations, the primary project-adjusted model is
refitted repeatedly while omitting one supported TCGA project at a time.

This diagnostic evaluates whether the pooled effect direction depends critically
on a single project.

A leave-one-project-out sign reversal is treated as evidence against the
prespecified cross-cancer recurrence designation.

---

## Cross-cancer recurrence criteria

A pooled FDR-supported association alone is not sufficient to be described as
`cross_cancer_recurrent`.

A gene × program association meets the frozen primary cross-cancer recurrence
criterion only when all of the following are satisfied:

1. the association belongs to the frozen primary gene × program family;
2. the pooled project-adjusted model has `q < 0.05`;
3. the gene has at least 3 supported TCGA projects;
4. at least 3 supported projects have an effect direction matching the pooled
   effect direction;
5. at least 70% of supported projects have an effect direction matching the
   pooled effect direction; and
6. no leave-one-project-out refit reverses the pooled effect direction.

No requirement is imposed that every supported project reach a project-specific
p-value threshold.

This criterion is intended to reduce the chance that a pooled result driven by
one dominant lineage is described as cross-cancer recurrent.

---

## Interpretation of recurrence

`cross_cancer_recurrent` means only that an association satisfies the frozen
lineage-aware recurrence criteria within the eligible TCGA projects.

It does not mean:

- universal across cancer types;
- independent of mutation burden;
- gene-specific in mechanism;
- causal;
- driver-mediated;
- independently validated; or
- therapeutically actionable.

Lineage breadth and gene-specificity are distinct properties.

---

## Sensitivity-stability annotation

Primary FDR-supported associations are additionally characterized by whether
they:

- preserve the primary effect direction across all four required sensitivity
  analyses; and
- retain adequate lineage support for those sensitivity estimates.

This stability annotation is separate from the cross-cancer recurrence label.

Sensitivity stability does not redefine primary FDR support or recurrence.

---

## Mutation-resource availability

Mutation-resource availability is not assumed to be missing completely at
random.

Cases without an informative mutation resource are not imputed as
non-mutated.

No inverse-probability weighting or other missingness correction is introduced
without a defensible model for the mutation-resource missingness mechanism.

Availability-related selection remains an explicit limitation of the analysis.

---

## Tumor mutation burden boundary

Notebook 450 does not calculate or claim conventional tumor mutation burden
(TMB).

The available MAF resource does not provide a frozen, sample-comparable callable
territory denominator suitable for a defensible mutations-per-megabase
calculation.

Therefore:

- raw qualifying-variant count is not called TMB;
- no generic exome-size denominator is imposed;
- no TMB covariate is included in the primary model; and
- no TMB-based primary eligibility or recurrence rule is introduced.

---

## Exploratory observed mutational-load diagnostic

After the primary results revealed broad gene-level association structure, an
additional diagnostic was introduced explicitly as exploratory analysis to
evaluate possible confounding by overall observed mutational load.

This diagnostic was not part of the prespecified primary model and must not be
represented as if it had been prospectively frozen.

For each informative case, the observed qualifying-variant burden is defined as
the number of deduplicated primary qualifying somatic variants.

The transformed burden representation is:

`log1p(observed_qualifying_variant_count)`

This quantity is an observed mutation-count proxy only.

It is not TMB.

---

## Gene-specific background burden

For gene-level burden diagnostics, the focal gene's own qualifying variants are
removed from the case-level total before constructing the background burden.

For focal gene `g`:

`background_variant_count_g = total_qualifying_variant_count - focal_gene_variant_count_g`

This avoids the direct tautology of adjusting a gene's mutation indicator with a
burden measure that includes the same focal-gene variants.

The background burden is then transformed as:

`log1p(background_variant_count_g)`

---

## Background-burden-conditioned exploratory model

For primary FDR-supported pairs, the exploratory diagnostic model is:

`program_score ~ mutation_status + log1p_background_variant_burden + C(project_id)`

The model:

- retains the frozen primary supported projects;
- uses HC3 standard errors;
- does not alter the primary mutation definition;
- does not alter the primary gene universe;
- does not alter the primary FDR family; and
- does not generate a replacement confirmatory analysis.

Its purpose is to evaluate whether the primary mutation coefficient is strongly
attenuated or changes direction after accounting for a broader observed
mutational-load context.

---

## Interpretation of the background-burden diagnostic

Background-burden conditioning is descriptive and exploratory.

Strong attenuation or sign reversal suggests that a primary gene-level
association may be substantially entangled with broader mutational-load
context.

Retention of effect direction or magnitude after conditioning does not prove a
gene-specific causal mechanism.

The diagnostic must not be used post hoc to:

- redefine primary significance;
- redefine `cross_cancer_recurrent`;
- create a new confirmatory threshold;
- rescue or exclude genes;
- construct a preferred gene ranking; or
- claim gene-specific causality.

---

## Copy-number boundary

Copy-number alterations are outside the scope of notebook 450.

No CNA layer is introduced into the mutation–program analysis.

Adding CNA characterization would require a separate, explicitly justified and
prespecified analysis rather than retrospective expansion of notebook 450.

---

## Primary output

Notebook 450 publishes one downstream-consumable artifact:

`data/processed/secondary_characterization/450_primary_gene_program_associations.csv`

The output contains the complete frozen primary gene × consensus-program family
together with the principal information required for downstream interpretation,
including:

- primary effect estimates;
- primary uncertainty estimates;
- p-values and globally adjusted q-values;
- primary FDR-support status;
- lineage-aware recurrence characterization;
- sensitivity-stability information; and
- exploratory background-burden-conditioned diagnostics where applicable.

The complete output contains all primary gene × program hypotheses, not only
statistically supported associations.

---

## Intermediate results not published as separate artifacts

The following objects remain reproducible within notebook 450 but are not
published as separate downstream artifacts by default:

- raw qualifying-variant tables;
- case-level mutation-state tables;
- gene × project prevalence tables;
- within-project regression tables;
- leave-one-project-out regression tables;
- purity-specific result tables;
- proliferation-specific result tables;
- single-MAF sensitivity tables;
- extended-splice sensitivity tables;
- background-burden intermediate tables;
- cross-program overlap tables;
- lineage-breadth summaries; and
- descriptive program-level summaries.

They may be persisted later only if a downstream analysis requires them as a
formal interface.

---

## Downstream-use boundary

Downstream notebooks may consume the frozen notebook-450 output as secondary
genomic-context evidence.

They must preserve the distinction between:

- primary mutation–program association;
- lineage-aware recurrence;
- sensitivity stability; and
- exploratory background mutational-load diagnostics.

Downstream analyses must not reinterpret an exploratory burden-conditioned
result as a replacement primary estimate.

Likewise, satisfying the recurrence criterion must not be treated as evidence
of a gene-specific mechanism.

---

## Scientific interpretation boundary

Notebook 450 supports statements such as:

- a qualifying somatic-variant context is associated with a frozen consensus
  program;
- an association meets the prespecified cross-cancer recurrence criteria;
- an association is stable or attenuated under prespecified sensitivity
  analyses; or
- a gene-level association appears substantially entangled with broader observed
  mutational-load context.

Notebook 450 does not support statements that a gene is:

- a causal regulator of the program;
- a master regulator;
- a validated driver of the program;
- a therapeutic target;
- a clinical biomarker; or
- a mechanistically validated determinant of resistance.

Association remains distinct from causality.

Secondary genomic context remains distinct from program discovery and from
independent biological validation.