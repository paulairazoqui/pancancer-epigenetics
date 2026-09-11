# Notebook 451 Analysis Contract

## Lifecycle / execution closure

This analytical contract was prespecified before inferential result inspection.
Execution is complete, and notebook 451 and its seven registered
`phase4b.451.*` outputs are frozen. The prospective sections below are retained
unchanged as historical methodological provenance; realized artifact identity
and lineage are represented by the analysis metadata and
`config/artifact_registry.json`.

## Status

Planned / prespecified before result inspection.

This document defines the analytical decisions for notebook

`451 — Locus-Level Methylation–Expression Characterization`

before locus-level methylation–expression association results are inspected.

The purpose of this contract is to preserve an auditable distinction between:

- prespecified primary analyses;
- prespecified sensitivity analyses;
- secondary biological annotation;
- exploratory characterization; and
- downstream interpretation.

Once notebook 451 begins inferential result inspection, changes to primary
eligibility rules, statistical models, multiplicity control, recurrence
criteria, or interpretation thresholds must not be introduced on the basis of
whether they produce more favorable results.

The authoritative executable record will be:

`notebooks/phase4b_secondary_molecular_characterization/451_locus_level_methylation_expression_characterization.ipynb`

---

## Purpose

Notebook 451 characterizes locus-level DNA-methylation–gene-expression
relationships associated with the already frozen tumor-side methylation context
of the three Phase 4 cross-system consensus transcriptomic programs.

The notebook is a downstream molecular-context characterization layer.

It does not:

- discover new consensus programs;
- redefine existing consensus programs;
- assign resistance or sensitivity labels to TCGA tumors;
- infer causal epigenetic regulation;
- establish biological mechanisms;
- identify validated therapeutic targets;
- perform clinical prediction; or
- use locus-level results to rescue or promote upstream candidate programs.

The analysis is designed to determine whether CpGs contributing strongly to
the frozen tumor methylation components show reproducible relationships with
expression of genes to which those CpGs can be defensibly annotated.

Particular attention is given to inverse methylation–expression relationships
at promoter-associated loci because such relationships are compatible with
transcriptional repression associated with increased promoter methylation.

Compatibility with such a regulatory model does not establish that methylation
causes the observed expression difference.

Positive, inverse, lineage-specific, heterogeneous, null, or technically
limited results are all valid outcomes.

---

## Scientific positioning

Notebook 451 addresses the following question:

> Do loci contributing strongly to the frozen tumor-side methylation components
> exhibit reproducible methylation–expression relationships with annotated genes
> across TCGA cancer projects?

The analysis concerns molecular context of frozen candidate programs.

It must not be described as demonstrating:

- epigenetic silencing;
- causal methylation-mediated gene regulation;
- a mechanism of drug resistance;
- adaptive resistance;
- therapeutic reversibility;
- a validated biomarker; or
- a validated target.

Appropriate terminology includes:

- locus-level methylation–expression association;
- inverse methylation–expression relationship;
- promoter-associated inverse relationship;
- relationship compatible with epigenetic regulation;
- lineage-aware recurrent association;
- lineage-restricted association;
- heterogeneous association;
- secondary molecular context.

---

# Frozen upstream inputs

Notebook 451 consumes frozen upstream artifacts without reopening their
construction or selection.

## Frozen TCGA multi-omic cohort

The biological unit remains the frozen TCGA primary-tumor case defined in
Phase 2.

The final multi-omic cohort contains one selected RNA-seq–methylation pair per
case.

The frozen case-level sample mapping is:

`phase2.203.final_sample_mapping`

Path:

`data/interim/metadata/tcga_primary_tumor_multiomic_final_case_level_sample_mapping.csv`

The complete frozen cohort contains 9,965 cases.

Notebook 451 must preserve the upstream case and sample identities exactly.

No alternate sample, aliquot, vial, or file may be substituted in order to
increase locus-level coverage.

---

## Frozen RNA-seq representation

The primary gene-expression representation is inherited from notebook 205:

`phase2.205.rna_program_discovery_expression`

Path:

`data/interim/expression/tcga_primary_tumor_rnaseq_program_discovery_tmm_logcpm.h5`

This object contains the frozen TMM-normalized logCPM representation generated
for Phase 2 program discovery.

The expression matrix contains 18,123 retained protein-coding genes across the
9,965 frozen tumor cases.

Notebook 451 will not:

- recompute RNA-seq normalization;
- refit expression filters;
- redefine protein-coding eligibility;
- select genes according to methylation–expression correlation strength; or
- create an alternative expression representation after inspecting results.

Gene identities and matrix correspondence must be inherited from the frozen
Phase 2 RNA feature metadata.

---

## Frozen methylation representations

The following frozen Phase 2 DNA-methylation representations are available:

### HM450

`phase2.203.final_hm450_methylation_betas`

Path:

`data/interim/methylation/tcga_primary_tumor_methylation_hm450_final_case_level_beta_values.npy`

Frozen dimensions:

- 407,696 probes;
- 8,345 tumors.

### HM27

`phase2.203.final_hm27_methylation_betas`

Path:

`data/interim/methylation/tcga_primary_tumor_methylation_hm27_final_case_level_beta_values.npy`

Frozen dimensions:

- 24,303 probes;
- 1,620 tumors.

### Shared HM27/HM450 probe space

`phase2.203.final_shared_methylation_betas`

Path:

`data/interim/methylation/tcga_primary_tumor_methylation_shared_hm27_hm450_final_case_level_beta_values.npy`

Frozen dimensions:

- 23,356 probes;
- 9,965 tumors.

### Frozen probe mapping

`phase2.203.final_probe_mapping`

Path:

`data/interim/metadata/tcga_primary_tumor_methylation_final_probe_mapping.csv`

The existing probe mapping preserves technical probe identity, representation,
platform membership, matrix indexing, missingness, and QC eligibility.

It is not by itself a biological CpG-to-gene or CpG-to-promoter annotation.

---

## Frozen methylation-component loadings

Strong locus membership will be defined from the already frozen Phase 2
methylation ICA loadings:

`phase2.205.methylation_candidate_probe_loadings`

Path:

`data/processed/tumor_programs/tcga_primary_tumor_hm450_ica_candidate_probe_loadings.csv`

Notebook 451 will not refit ICA, rotate methylation components, change
component signs, select alternative components, or use locus-level
methylation–expression results to redefine component membership.

---

## Frozen consensus-program context

Notebook 451 is restricted to the three frozen Phase 4 cross-system consensus
transcriptomic representations:

- `CONSENSUS_TX_01`;
- `CONSENSUS_TX_02`;
- `CONSENSUS_TX_03`.

Their tumor-side methylation contexts are inherited from Phase 4.

The relevant mappings are:

### CONSENSUS_TX_01

Tumor transcriptomic axis:

`RNA_IC150`

Tumor methylation component:

`METH_IC128`

Candidate tumor arm:

`CROSS_OMIC_PAIR_04`

### CONSENSUS_TX_02

Tumor transcriptomic axis:

`RNA_IC151`

Tumor methylation component:

`METH_IC050`

Candidate tumor arm:

`CROSS_OMIC_PAIR_08`

### CONSENSUS_TX_03

Tumor transcriptomic axis:

`RNA_IC184`

Tumor methylation components:

- `METH_IC169`;
- `METH_IC128`.

Candidate tumor arms:

- `CROSS_OMIC_PAIR_03`;
- `CROSS_OMIC_PAIR_12`.

`METH_IC128` therefore appears in more than one consensus-program context.

The same CpG–gene statistical association must not be tested or counted more
than once merely because a CpG contributes to multiple downstream
program-context annotations.

Program context is attached after construction of the unique CpG–gene
inferential family.

---

# Preservation of upstream limitations

Notebook 451 must retain the scientific limitations already attached to the
frozen tumor-side methylation arms.

In particular, `METH_IC128` belongs to Phase 4 contexts with known
cellularity/immune/purity-related interpretive concerns.

A locus-level association arising from `METH_IC128` must not be interpreted as
resolving or rehabilitating those upstream limitations.

Where a frozen upstream concern motivates a sensitivity analysis, that
sensitivity is prespecified independently of the locus-level association
result.

No positive locus-level result can upgrade the frozen Phase 4 robustness or
priority status.

---

# CpG biological annotation

## Annotation authority

**PENDING FREEZE BEFORE NOTEBOOK 451 INFERENTIAL EXECUTION**

Proposed primary annotation authority:

- SeSAMe / `sesameData`;
- HumanMethylation450 annotation;
- hg38 genomic coordinates;
- exact package/resource version recorded before use.

The final selected annotation resource must be:

1. versioned;
2. provenance-tracked;
3. registered in the repository;
4. frozen before locus-level result inspection; and
5. used deterministically throughout the primary analysis.

No mixture of incompatible genome builds is permitted.

No annotation resource may be replaced after result inspection because an
alternative mapping produces more favorable biological interpretation.

---

## Annotation provenance

Before inferential analysis, the selected CpG annotation resource must be
recorded in:

`config/raw_data_registry.json`

The registry record must include, where applicable:

- source;
- provider;
- resource/package version;
- genome build;
- retrieval date;
- local canonical path;
- file size;
- SHA256 identity;
- annotation role.

If annotation is derived programmatically from a versioned package/resource,
the exact package and resource version and deterministic derivation procedure
must be recorded.

---

## CpG-to-gene mapping policy

CpG-to-gene mappings must be defined entirely from the frozen annotation
resource.

No nearest-gene rescue or manual biological reassignment is permitted in the
primary analysis.

If one CpG maps to multiple genes, every defensible CpG–gene relationship is
retained as a distinct candidate pair.

If the same CpG–gene relationship appears multiple times because of multiple
transcripts or overlapping annotation records, the exact CpG–gene pair is
collapsed to one primary inferential unit while retaining the complete
annotation metadata.

No CpG is assigned to a preferred gene because that gene:

- belongs to a consensus transcriptomic program;
- has a larger expression effect;
- has a stronger correlation;
- is an epigenetic regulator;
- is druggable;
- has known cancer relevance; or
- produces a more biologically attractive interpretation.

---

## Gene-identifier harmonization

Primary gene mapping must use deterministic exact identifiers.

Preferred hierarchy:

1. exact stable Ensembl gene identifier when available in both resources;
2. otherwise exact gene-symbol matching when unambiguous.

No fuzzy matching is permitted.

No manual alias rescue is permitted in the primary analysis.

Ambiguous mappings remain unresolved rather than being arbitrarily assigned.

The final harmonization table must record the source CpG annotation identifier,
the matched frozen RNA-seq identifier, mapping method, and mapping status.

---

# Regulatory annotation

CpG regulatory context is inherited from the frozen annotation authority rather
than inferred from observed expression behavior.

At minimum, each CpG–gene pair should preserve, where available:

- promoter-associated status;
- gene-body status;
- other genic/regulatory annotation;
- intergenic or unresolved status;
- genomic coordinates;
- gene identifier;
- transcript annotation where relevant.

A locus is described as promoter-associated only if the frozen annotation
resource supports that classification under the prespecified annotation rule.

The primary analysis will not define promoter status retrospectively using a
distance threshold selected after examining methylation–expression results.

If an explicit promoter-coordinate definition is required because the selected
resource does not contain a direct promoter label, that definition must be
documented and frozen before inferential execution.

---

# Primary locus universe

## Relevant methylation components

The primary locus universe is restricted to the three unique frozen
methylation components associated with the consensus-program tumor arms:

- `METH_IC050`;
- `METH_IC128`;
- `METH_IC169`.

No other methylation ICA components enter the primary notebook-451 family.

---

## Strong-loading CpG definition

A focused primary locus universe is defined from the strongest signed loading
tails of each relevant frozen methylation component.

The primary rule reuses the pre-existing Phase 2 loading-tail convention:

- 50 CpGs from the most negative loading tail; and
- 50 CpGs from the most positive loading tail

for each relevant methylation component.

This yields at most 100 strong-loading CpGs per methylation component before
deduplication across components.

The rule is applied exclusively to frozen methylation-component loadings.

It is therefore independent of:

- gene-expression association;
- methylation–expression correlation;
- promoter annotation;
- gene identity;
- pathway membership;
- statistical significance;
- druggability; and
- downstream therapeutic relevance.

Loading-tail direction is preserved as biological context.

A CpG occurring in the strong-loading tails of multiple relevant components is
retained once as a locus but preserves all corresponding component memberships.

---

## Why the complete ICA loading space is not the primary locus universe

ICA produces non-zero or near-non-zero loadings for many probes.

Treating every modeled probe as equally program-associated would weaken the
interpretability of locus-level characterization and substantially broaden the
inferential family with loci that contribute minimally to the relevant frozen
components.

The focused loading-tail universe is therefore used to characterize loci most
strongly contributing to the frozen methylation contexts.

No loading cutoff may be changed after methylation–expression results are
inspected.

---

# Primary CpG–gene inferential universe

The primary statistical unit is the unique:

`CpG × annotated gene`

pair.

A CpG–gene pair enters the primary family only if:

1. the CpG belongs to the frozen strong-loading locus universe;
2. the CpG has a valid frozen biological annotation;
3. the CpG maps to the gene under the frozen annotation rule;
4. the gene maps unambiguously to the frozen RNA-seq expression representation;
5. the required HM450 methylation measurements are available;
6. the CpG and gene contain non-zero analyzable variation; and
7. the pair has adequate lineage-aware complete-case support under the
   prespecified support rules.

Eligibility must not depend on:

- correlation sign;
- effect magnitude;
- p-value;
- q-value;
- promoter status;
- expected biological direction;
- cancer relevance;
- druggability; or
- whether the pair supports a preferred biological hypothesis.

---

# Primary methylation platform

HM450 is the primary inferential platform.

This choice follows the upstream methylation-component discovery context and
provides the larger platform-specific TCGA cohort.

The primary analysis therefore uses the frozen HM450 cohort of 8,345 tumors.

HM27 and HM450 samples are not naively pooled into one primary regression
model.

Methylation platform is therefore not represented simply as an adjustment
covariate in a pooled primary model.

HM27 is used as a prespecified platform-sensitivity layer for eligible loci.

---

# Methylation scale

The primary inferential methylation predictor uses M-values.

M-values are derived deterministically from the frozen beta values using the
same transformation convention established upstream in Phase 2.

The transformation rule must be verified against notebook 205 and reproduced
exactly before notebook 451 inferential execution.

Notebook 451 must not introduce a different beta-value clipping,
pseudocount, transformation, or imputation rule after result inspection.

Beta values remain available for descriptive interpretation because of their
direct methylation-fraction scale.

Primary inferential coefficients and primary statistical testing are based on
the frozen/reproduced M-value representation.

---

# Missing methylation values

Missing methylation measurements are not imputed for the primary
methylation–expression association tests unless an upstream deterministic
imputation rule is explicitly inherited and scientifically appropriate for the
same analytical purpose.

Primary CpG–gene modeling uses complete cases for the variables required by
the corresponding model.

The number and fraction of excluded cases must remain explicit for every
association and sensitivity model.

Missingness must not be interpreted as absence of methylation.

---

# Supported-project definition

Lineage-aware support is defined at the TCGA-project level.

For a CpG–gene pair to receive support from a TCGA project, the project must
contain at least:

- 20 complete HM450 cases for that CpG–gene pair;
- non-zero methylation variation for the CpG; and
- non-zero expression variation for the gene.

A CpG–gene pair enters the primary cross-project inferential family only if it
has support from at least:

- 3 TCGA projects.

This eligibility rule is evaluated before methylation–expression association
statistics are inspected.

Pairs that are analyzable in fewer than three projects may be retained in a
separate descriptive lineage-restricted table but do not belong to the primary
cross-project inferential family.

---

# Primary statistical model

For each eligible unique CpG–gene pair, the primary model is:

`gene_expression ~ CpG_methylation + C(project_id)`

where:

- `gene_expression` is frozen TMM-logCPM expression of the annotated gene;
- `CpG_methylation` is the M-value for the corresponding CpG;
- `project_id` represents TCGA cancer project / major lineage structure.

Only supported projects for the corresponding pair contribute to the primary
model.

The CpG methylation coefficient represents the adjusted observational
association between locus methylation and gene expression.

It does not represent a causal methylation effect.

---

# Primary uncertainty estimate

Primary linear models use heteroskedasticity-consistent HC3 standard errors.

For every primary CpG–gene association, the output should include at minimum:

- CpG identifier;
- gene identifier;
- gene symbol;
- methylation component membership;
- signed loading;
- loading-tail membership;
- program-context membership;
- regulatory annotation;
- number of complete cases;
- number of supported projects;
- methylation coefficient;
- HC3 standard error;
- 95% confidence interval;
- test statistic;
- p-value;
- globally adjusted q-value.

Where useful, descriptive effect-size quantities may additionally be reported,
but they must not replace the frozen primary inferential statistic.

---

# Direction of association

For the primary coefficient:

`beta_methylation < 0`

means that higher methylation at the CpG is associated with lower expression of
the annotated gene.

This is termed an:

`inverse methylation–expression association`.

`beta_methylation > 0`

means that higher methylation is associated with higher expression.

This is termed a:

`positive methylation–expression association`.

Association direction is reported independently of statistical significance.

---

# Promoter-associated inverse relationships

A CpG–gene association may be annotated as a:

`promoter_associated_inverse_relationship`

only when:

1. the CpG is promoter-associated with that gene under the frozen annotation
   rule; and
2. the primary methylation coefficient is negative.

If the association is additionally primary FDR-supported, it may be described
as a:

`FDR-supported promoter-associated inverse methylation–expression relationship`.

This terminology indicates compatibility with a promoter
methylation-associated transcriptional-repression model.

It must not be described as:

- promoter silencing;
- methylation-mediated silencing;
- causal repression;
- epigenetic control;
- mechanism of resistance; or
- validated regulatory interaction.

---

# Primary multiple-testing family

Every eligible unique CpG–gene pair belongs to one primary inferential family.

Benjamini–Hochberg FDR correction is applied globally across this complete
primary family.

The primary support threshold is:

`q < 0.05`

FDR is not calculated separately by:

- consensus program;
- methylation component;
- loading tail;
- promoter status;
- association direction;
- gene class; or
- TCGA project.

This prevents artificial inflation of discovery opportunities through
post hoc family subdivision.

A CpG–gene pair shared by multiple program contexts contributes only one test
to the global family.

---

# Within-project characterization

For every primary FDR-supported CpG–gene association, project-specific
associations are estimated within each supported TCGA project.

The project-specific model is:

`gene_expression ~ CpG_methylation`

within the corresponding project.

These estimates are used to characterize:

- direction;
- effect magnitude;
- lineage consistency;
- lineage heterogeneity.

Project-specific statistical significance is not required for the
cross-project recurrence designation.

Within-project analyses are contextual consistency analyses rather than
independent confirmatory tests.

---

# Leave-one-project-out characterization

Every primary FDR-supported CpG–gene association is additionally evaluated by
repeatedly refitting the primary model while excluding one supported TCGA
project at a time.

This analysis evaluates whether the pooled direction depends critically on one
project.

A leave-one-project-out sign reversal is evidence against the prespecified
cross-project recurrence designation.

Leave-one-project-out analyses do not define a new significance family.

---

# Cross-project recurrence

To maintain consistency with Phase 4B notebook 450, an association is
classified as:

`cross_project_recurrent`

only if all of the following are satisfied:

1. it belongs to the frozen primary CpG–gene inferential family;
2. the primary project-adjusted association has `q < 0.05`;
3. at least 3 TCGA projects support the pair;
4. at least 3 supported projects have the same effect direction as the pooled
   primary coefficient;
5. at least 70% of supported projects have the same effect direction as the
   pooled primary coefficient; and
6. no leave-one-project-out refit reverses the pooled effect direction.

Per-project p-value significance is not required.

`cross_project_recurrent` must not be interpreted as:

- universal across cancer types;
- homogeneous across all lineages;
- causal;
- independent validation;
- mechanistic evidence; or
- therapeutic relevance.

---

# Prespecified sensitivity analyses

Sensitivity analyses characterize robustness of primary associations.

They do not constitute alternative routes to significance and cannot rescue a
primary association that fails the frozen primary inferential framework.

Required sensitivity analyses are described below.

---

## Tumor-purity sensitivity

For primary FDR-supported associations, a complete-case model including frozen
ABSOLUTE tumor purity is evaluated:

`gene_expression ~ CpG_methylation + absolute_purity + C(project_id)`

Tumor-purity availability is lineage dependent.

The purity-adjusted model is therefore interpreted as sensitivity evidence
rather than as a replacement primary model.

The output must preserve:

- complete-case sample count;
- supported-project count;
- methylation coefficient;
- coefficient direction;
- coefficient attenuation or amplification relative to primary;
- uncertainty.

No purity sensitivity may rescue a primary non-significant association.

---

## Proliferation sensitivity

For primary FDR-supported associations, a separate complete-case model is
evaluated using the frozen proliferation score:

`gene_expression ~ CpG_methylation + external_panimmune_proliferation_score + C(project_id)`

Proliferation is evaluated separately because proliferative state may be part
of the biology represented by the frozen programs and should not be
automatically removed from the primary estimand.

The sensitivity is interpreted through:

- effect direction;
- effect magnitude;
- retained lineage support; and
- concordance with the primary estimate.

---

## Cellular-composition sensitivity for METH_IC128

Because `METH_IC128` carries a frozen upstream cellularity/immune-context
concern, CpG–gene associations involving loci from this component receive an
additional prespecified sensitivity analysis using the frozen
`leukocyte_fraction` covariate where coverage permits:

`gene_expression ~ CpG_methylation + leukocyte_fraction + C(project_id)`

This analysis is justified by an upstream limitation that predates notebook
451.

It is not activated because of the observed locus-level result.

Associations from `METH_IC128` must retain this upstream caveat even when the
leukocyte-adjusted estimate remains directionally stable.

---

# HM27 platform sensitivity

The HM27 cohort provides a prespecified cross-platform sensitivity layer for
eligible CpGs.

The same CpG identifier and same annotated gene are evaluated without
redefining the locus or gene mapping.

The HM27 sensitivity model is:

`gene_expression ~ CpG_methylation + C(project_id)`

using HM27 samples only.

A CpG–gene pair is considered evaluable in this sensitivity only when it has
adequate HM27 complete-case and project support under explicitly reported
criteria.

HM27 sensitivity is interpreted through:

- effect direction;
- effect magnitude;
- number of supported projects;
- compatibility with the HM450 primary estimate.

HM27 is not treated as an independent biological validation cohort because it
contains TCGA tumors from the same overall study system and differs
substantially in lineage and sample coverage.

HM27 platform consistency therefore represents complementary technical /
cross-platform evidence, not independent external validation.

Failure to reproduce an association in HM27 does not automatically invalidate
the primary HM450 association when HM27 lineage or sample support is
insufficient.

---

# Sensitivity-stability annotation

Primary FDR-supported associations may receive a sensitivity-stability
annotation based on the prespecified analyses.

At minimum, the annotation should report separately whether the association:

- preserves direction after purity adjustment;
- preserves direction after proliferation adjustment;
- preserves direction in HM27 when evaluable;
- preserves direction after leukocyte-fraction adjustment when applicable.

These dimensions must remain separate in the machine-readable output.

They must not be collapsed into an opaque composite score.

Sensitivity stability does not redefine:

- primary FDR support;
- cross-project recurrence;
- promoter status; or
- biological interpretation.

---

# Lineage heterogeneity

Cross-project recurrence and lineage heterogeneity are distinct properties.

A pooled FDR-supported association may still show substantial lineage
heterogeneity.

Notebook 451 must therefore preserve:

- project-specific coefficient direction;
- project-specific effect magnitude;
- number of supported projects;
- directional-consistency fraction;
- leave-one-project-out stability.

An association that does not meet the frozen recurrence criteria may still be
reported as:

- lineage-restricted;
- directionally heterogeneous; or
- pooled-only.

Lack of pan-cancer recurrence is a valid biological result.

---

# Component and program annotation after inference

After unique CpG–gene associations have been tested, each pair is linked back
to its frozen upstream methylation-component and consensus-program contexts.

This annotation may include:

- `METH_IC050`;
- `METH_IC128`;
- `METH_IC169`;
- `CONSENSUS_TX_01`;
- `CONSENSUS_TX_02`;
- `CONSENSUS_TX_03`;
- corresponding tumor candidate arms;
- signed methylation-component loading.

A pair linked to multiple contexts retains every applicable context.

No association is duplicated statistically because of multiple context
memberships.

---

# Relationship to frozen consensus-program orientation

Locus-level methylation–expression direction must remain distinct from
consensus-program orientation.

A negative CpG–gene coefficient means only that higher methylation at that locus
is associated with lower expression of the annotated gene.

It does not by itself indicate whether the gene is activated or repressed in a
resistance-like context.

Any later relationship between:

- CpG methylation;
- gene expression;
- methylation-component loading;
- transcriptomic-program loading; and
- pharmacogenomic phenotype

must preserve each evidence layer separately.

Notebook 451 does not collapse these directions into a causal regulatory chain.

---

# Epigenetic-regulator annotation

Genes previously annotated as epigenetic regulators may be marked as such using
the frozen Phase 4 annotation resources.

Epigenetic-regulator status is secondary annotation only.

It cannot affect:

- primary CpG eligibility;
- CpG-to-gene assignment;
- statistical testing;
- FDR correction;
- recurrence classification; or
- sensitivity stability.

Enrichment or biological interest does not constitute mechanistic evidence.

---

# Prohibited analyses and interpretations

Notebook 451 must not:

- label TCGA tumors resistant or sensitive;
- infer treatment response from TCGA;
- construct a resistance classifier;
- use pharmacogenomic phenotype to select CpGs or genes;
- refit Phase 2 methylation or transcriptomic components;
- redefine Phase 4 consensus programs;
- select loci based on locus-level p-values;
- select genes based on druggability;
- choose annotation mappings according to favorable results;
- pool HM27 and HM450 naïvely;
- treat HM27 as independent external validation;
- infer causality from methylation–expression association;
- describe SHAP-like feature importance;
- infer validated targets;
- infer therapeutic efficacy;
- claim therapeutic reversal;
- reconstruct longitudinal adaptive resistance.

---

# Negative-result policy

Notebook 451 is scientifically complete even if:

- no primary CpG–gene pair reaches global FDR support;
- FDR-supported relationships are not inverse;
- inverse relationships are not promoter-associated;
- supported relationships are lineage-specific;
- associations are unstable after purity adjustment;
- HM27 support is weak or unavailable;
- cross-project recurrence criteria are not satisfied;
- known program contexts produce heterogeneous results.

No eligibility threshold, statistical family, annotation rule, or sensitivity
criterion may be relaxed after result inspection to manufacture positive
findings.

Null results remain a valid Phase 4B handoff.

---

# Planned primary outputs

> **Retrospective fulfillment note:** Execution is complete. The realized
> output identities and provenance are frozen in the notebook-451 analysis
> metadata and artifact registry; the prospective list below is retained
> unchanged as the historical plan.

Notebook 451 should produce machine-readable outputs under:

`data/processed/secondary_characterization/`

At minimum:

## 1. CpG annotation and eligibility table

Suggested path:

`451_cpg_gene_annotation_eligibility.csv`

Contents:

- CpG identifier;
- methylation component;
- signed loading;
- loading tail;
- regulatory annotation;
- annotated gene;
- mapping method;
- expression-feature mapping status;
- primary eligibility;
- exclusion reason where applicable.

---

## 2. Primary CpG–gene association table

Suggested path:

`451_primary_cpg_gene_associations.csv`

One row per unique primary CpG–gene inferential pair.

Contents include primary model estimates, sample/project coverage, global FDR,
regulatory annotation, and component/program context.

---

## 3. Within-project characterization table

Suggested path:

`451_within_project_cpg_gene_associations.csv`

One row per:

`CpG × gene × supported project`

for primary FDR-supported associations.

---

## 4. Leave-one-project-out table

Suggested path:

`451_leave_one_project_out_associations.csv`

Contains all leave-one-project-out refits for primary FDR-supported
associations.

---

## 5. Sensitivity table

Suggested path:

`451_association_sensitivities.csv`

Contains separate records for:

- purity adjustment;
- proliferation adjustment;
- leukocyte-fraction adjustment where applicable;
- HM27 platform sensitivity.

Sensitivity dimensions must remain identifiable rather than collapsed into one
score.

---

## 6. Final locus-level evidence table

Suggested path:

`451_locus_level_methylation_expression_evidence.csv`

Integrates, without re-testing:

- primary association;
- promoter/regulatory annotation;
- inverse/positive direction;
- cross-project recurrence;
- lineage heterogeneity;
- leave-one-project-out stability;
- purity sensitivity;
- proliferation sensitivity;
- cellular-composition sensitivity where applicable;
- HM27 platform sensitivity;
- methylation-component context;
- consensus-program context;
- explicit interpretation limitations.

This is an evidence-integration table, not a new statistical test.

---

## 7. Analysis metadata

Suggested path:

`451_analysis_metadata.json`

The metadata should record:

- notebook identity;
- run timestamp;
- upstream artifact IDs and SHA256 identities;
- annotation resource/version/build;
- loading-tail rule;
- sample-support thresholds;
- primary model;
- uncertainty estimator;
- multiple-testing method;
- recurrence criteria;
- sensitivity definitions;
- output paths;
- output shapes;
- output SHA256 values;
- analytical limitations.

---

# Artifact registration

> **Retrospective fulfillment note:** The seven realized notebook-451 outputs
> are registered under the `phase4b.451.*` namespace. The prospective
> registration rules below are retained unchanged as historical provenance.

After notebook 451 is completed and all outputs are validated, stable derived
artifacts required downstream must be registered in:

`config/artifact_registry.json`

Registration must include:

- stable artifact identifier;
- exact repository path;
- phase;
- status;
- artifact role;
- producer notebook;
- shape where applicable;
- byte size;
- SHA256;
- explicit upstream artifact lineage.

Proposed identifier namespace:

`phase4b.451.*`

No artifact should be declared frozen before its contents and identity have been
validated against the executed notebook.

---

# Downstream use

Notebook 451 outputs may contribute to Phase 9 integrated evidence synthesis as
a separately traceable secondary molecular-context layer.

They may support statements such as:

- a putative vulnerability is linked to a gene participating in a recurrent
  locus-level methylation–expression relationship;
- a program-associated locus displays an inverse promoter-associated
  relationship;
- a relationship is lineage-specific or heterogeneous;
- molecular-context evidence is absent or conflicting.

Notebook 451 evidence must not be used as a retrospective gate to:

- remove a frozen consensus program;
- promote a frozen consensus program;
- redefine a functional vulnerability;
- establish therapeutic causality;
- convert a candidate target into a validated target.

---

# Interpretation hierarchy

Notebook 451 should preserve the following distinction:

### Level 1 — Locus membership

The CpG belongs to a strong-loading tail of a frozen tumor methylation
component.

### Level 2 — Gene annotation

The CpG is defensibly mapped to a gene under the frozen annotation resource.

### Level 3 — Methylation–expression association

CpG methylation is statistically associated with expression of the annotated
gene.

### Level 4 — Regulatory-context compatibility

The relationship is promoter-associated and inverse, making it compatible with
a promoter methylation-associated repression model.

### Level 5 — Cross-project reproducibility

The association meets the prespecified lineage-aware recurrence criteria.

### Level 6 — Sensitivity stability

The relationship remains directionally stable under relevant purity,
proliferation, cellular-composition, and/or platform sensitivities.

None of these levels establishes biological causality.

---

# Analytical closure criteria

> **Retrospective fulfillment note:** These criteria have been fulfilled for
> the frozen notebook-451 outputs. The original criteria remain below as the
> prospective analytical record.

Notebook 451 is considered analytically complete when:

1. the biological annotation resource is frozen and provenance-registered;
2. all frozen upstream artifact identities have been validated;
3. strong-loading CpG eligibility is constructed deterministically;
4. CpG-to-gene mappings are frozen before association inspection;
5. the complete primary CpG–gene inferential family is generated;
6. every eligible primary association is tested;
7. one global BH correction is applied to the complete primary family;
8. within-project and leave-one-project-out characterization is completed for
   primary FDR-supported associations;
9. all prespecified applicable sensitivities are completed;
10. primary and contextual evidence tables are written and validated;
11. negative and heterogeneous findings remain explicitly represented;
12. analysis metadata and provenance are published; and
13. downstream-required artifacts are registered with frozen identity.

Analytical completion does not require a positive result.

---

# Final interpretation boundary

Notebook 451 provides secondary molecular-context evidence concerning
locus-level methylation–expression relationships associated with already frozen
cross-system candidate programs.

An inverse promoter-associated relationship may be consistent with an
epigenetic regulatory hypothesis.

It does not establish that:

- methylation causes expression change;
- the gene causes a resistance-like phenotype;
- the locus is a resistance mechanism;
- the gene is a validated therapeutic target; or
- modulation of the locus or gene will restore drug sensitivity.

Any mechanistic or therapeutic interpretation requires evidence beyond this
computational association framework.

---

# Execution freeze record

This section records the annotation authority that was ultimately frozen for
notebook 451 execution. It is an execution-provenance addendum and does not
modify the prespecified analytical rules defined above.

The primary CpG biological annotation authority used for notebook 451 was:

- provider/framework: Bioconductor / SeSAMe / `sesameData`;
- Bioconductor release: 3.23;
- `sesameData` version: 1.30.0;
- methylation platform: Illumina HumanMethylation450;
- genome build: hg38;
- R version: 4.6.1.

The deterministic annotation derivation is implemented in:

`scripts/phase4b/export_sesamedata_hm450_hg38_annotation.R`

The frozen annotation resource and its file identities are provenance-tracked
under:

`config/raw_data_registry.json`

at:

`/tcga/external_resources/sesame_hm450_hg38_annotation`

The derivation used the versioned SeSAMe HM450 address resource and hg38 genome
resource recorded in the raw-data registry. Protein-coding CpG–gene mappings
and regulatory context were generated deterministically before notebook-451
locus-level association results were inspected.

Promoter-associated status was defined from the frozen hg38 transcript
annotation using a 1,500-bp upstream and 1,500-bp downstream promoter window.
Transcript overlap was retained separately and must not be interpreted as a
general gene-body annotation.

No annotation resource, genome build, CpG-to-gene mapping rule, promoter rule,
or identifier-rescue policy was changed on the basis of notebook-451
methylation–expression association results.

This addendum records the realized execution state only. The original
prespecified contract above remains unchanged as the historical record of the
analysis plan.
