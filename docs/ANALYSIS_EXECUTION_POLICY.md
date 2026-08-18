# Analysis and Execution Policy

## Purpose

This document defines how computational and repository tasks should be
executed in `pancancer_epigenetics`.

The objective is to select the execution strategy that provides sufficient
scientific and engineering reliability while avoiding unnecessary complexity,
compute, manual effort, or AI-assisted development cost.

The governing principle is:

> Use the least expensive and least complex execution strategy that is
> sufficiently reliable for the specific task.

More expensive tools, models, reasoning levels, languages, or workflows must
not be selected merely as a precaution when a simpler option is adequate.

Efficiency must never override scientific validity, reproducibility, or
protection against methodological leakage.


## 1. Decision required before substantial new work

Before beginning a new analysis, implementation block, audit, or repository
task, explicitly determine:

1. whether the work should be performed interactively or delegated;
2. whether Python or R is the appropriate language;
3. whether Codex provides a meaningful advantage over manual work;
4. if Codex is used, the least expensive model and reasoning effort sufficient
   for the task;
5. whether the task is exploratory or confirmatory;
6. what methodological decisions must be frozen before inspecting results.

The recommended execution route should be stated before substantial work
begins whenever the choice is not obvious.


## 2. Interactive notebook work is the default for scientific analysis

Scientific analyses whose interpretation affects downstream decisions should
normally be performed interactively in notebooks.

The preferred workflow is:

1. define the immediate analytical objective;
2. write one short cell with one responsibility;
3. execute it;
4. inspect the output or error;
5. interpret the result;
6. decide the next analytical step.

This is preferred when results may influence subsequent scientific decisions.

Interactive execution reduces the risk of:

- silently changing analytical decisions after observing results;
- accumulating unnecessary calculations;
- hiding methodological assumptions inside large automated workflows;
- introducing leakage or circularity;
- propagating an error across multiple downstream steps.

Large blocks of analysis should not be delegated to Codex merely because they
can be automated.


## 3. Python versus R

### 3.1 Default language

Python is the default language for this project because the main analytical
pipeline, project utilities, artifact management, and most downstream analyses
are implemented in Python.

Typical Python tasks include:

- pandas / NumPy data processing;
- HDF5 and Parquet handling;
- matrix operations;
- PCA, ICA, and NMF;
- permutation procedures;
- bootstrap procedures;
- integration of frozen artifacts;
- cross-system comparisons;
- visualization when no specialized R implementation is required;
- deterministic repository utilities.

### 3.2 When to use R

R should be used when there is a concrete methodological advantage rather
than simply because an analysis can also be implemented in R.

Examples include methods whose canonical or best-supported implementation is
provided by Bioconductor or another established R ecosystem.

For example:

- edgeR;
- limma;
- other specialized statistical genomics methods when their reference
  implementation, diagnostics, or methodological conventions clearly favor R.

Before switching from Python to R, state the specific methodological advantage.

Do not introduce cross-language complexity without a corresponding analytical
benefit.


## 4. Manual work versus Codex

Codex is not the default executor for scientific analysis.

Use Codex only when it provides a concrete advantage in repository-scale work.

Good Codex use cases include:

- inspecting many repository files;
- focused repository audits;
- mechanical multi-file edits;
- small, well-specified PRs;
- documentation synchronization;
- deterministic manifests;
- repetitive refactoring with frozen requirements;
- narrow test additions;
- repository hygiene;
- locating inconsistencies across files;
- implementation tasks whose scientific decisions are already frozen.

Prefer manual interactive work when:

- the next step depends on interpreting the previous result;
- scientific decisions are still being made;
- thresholds or analytical gates need discussion;
- an unexpected result could change the analysis;
- only one or two cells are required;
- the task is a small local bug;
- delegation would cost more than performing the change directly;
- close control over each analytical decision is methodologically valuable.

Codex should not replace interactive scientific reasoning merely to save typing.


## 5. Resource-efficiency principle for AI-assisted development

For delegated AI-assisted repository work:

> Use the least expensive model and reasoning level that is sufficient for the
> task.

There is no default minimum model or reasoning level.

Do not establish an artificial floor such as always using a medium reasoning
level or always using a particular model family.

Selection must depend on the actual task.


## 6. Criteria for choosing Codex capability

Choose model capability and reasoning effort according to:

- task ambiguity;
- number of interacting constraints;
- breadth of repository context required;
- amount of independent judgment required;
- difficulty of detecting a mistake;
- downstream cost of an incorrect implementation;
- degree to which the task is already fully specified.

Task labels alone are insufficient.

For example, not every "PR" has the same complexity and not every "audit"
requires the strongest model.


## 7. Codex escalation policy

Start with the lowest-cost configuration that has adequate margin for the
specific task.

Escalate only when there is a concrete reason.

Typical qualitative levels are:

### Low-cost / low-reasoning configuration

Appropriate for highly mechanical and fully specified work such as:

- localized documentation edits;
- small deterministic configuration changes;
- simple manifests when values are already supplied;
- straightforward renaming;
- trivial tests;
- repetitive changes with explicit instructions.

### Moderate configuration

Appropriate when the task remains well specified but requires some repository
inspection or reconciliation, for example:

- small multi-file PRs;
- reconciling fields from several known sources;
- deterministic validation;
- selecting the appropriate existing documentation location;
- preserving provenance across a small handoff.

### Higher-capability configuration

Appropriate when the task requires substantial judgment, such as:

- complex repository-wide reasoning;
- methodological audits;
- scientific design reviews;
- difficult debugging across interacting systems;
- interpretation of several conflicting evidence layers;
- tasks where an implementation error could contaminate several downstream
  analyses.

### Maximum configurations

Reserve maximum-cost modes for genuinely exceptional tasks involving unusually
high ambiguity, complexity, breadth, or downstream risk.

They should not be used routinely.


## 8. Required justification when recommending Codex

Whenever Codex is recommended, provide:

- **Codex:** yes / no
- **Recommended capability:** current model choice
- **Recommended reasoning effort:** current effort level
- **Why this is sufficient:** task-specific justification
- **Why a cheaper option is not recommended:** concrete reason, if any
- **Escalation condition:** what specific failure or complexity would justify
  moving to a stronger configuration

If there is no defensible reason not to use a cheaper configuration, use the
cheaper configuration.


## 9. Do not hard-code current AI product names into project policy

Specific Codex model names, pricing, credit consumption, and reasoning-level
labels may change over time.

Therefore this repository policy defines capability requirements rather than
permanent product selections.

At execution time, map the policy to the currently available Codex options.

Current model names or interface labels should be treated as operational
choices, not reproducible scientific dependencies.


## 10. Cost of error matters

Resource efficiency does not mean always choosing the cheapest option.

A stronger execution strategy is justified when a subtle error could:

- alter candidate selection;
- introduce lineage leakage;
- introduce platform leakage;
- create drug-family leakage;
- contaminate downstream notebooks;
- change a frozen analytical gate;
- produce circular evidence;
- create an overclaiming risk;
- require expensive rework later.

The correct objective is:

> minimum resource cost compatible with the reliability required by the task.


## 11. Exploratory versus confirmatory execution

Before substantial analyses, classify the work as exploratory or confirmatory.

### Exploratory work

May investigate alternative hypotheses or representations, but must:

- remain clearly labeled exploratory;
- avoid silently changing frozen project decisions;
- preserve provenance;
- avoid promoting interesting results solely because they were discovered
  through broad search;
- account for multiplicity and selection effects when results are later used.

### Confirmatory or decision-making work

Must freeze before result inspection:

- feature space;
- candidate universe;
- thresholds;
- matching criteria;
- random seeds where applicable;
- resampling or permutation design;
- multiplicity families;
- eligibility gates.

Do not modify these after inspecting results unless the analysis is explicitly
reclassified as exploratory and the change is documented.


## 12. Large-scale exploratory data mining

The existence of large unused datasets does not by itself justify unrestricted
exploratory searching.

Broad fishing across large RNA-seq, methylation, pharmacogenomic, or other
inventories creates risks of:

- multiple-testing inflation;
- cherry-picking;
- difficult-to-reconstruct analytical paths;
- post-hoc hypotheses;
- weak reviewer defensibility.

When large-scale exploration is justified:

1. define the exploratory question or hypothesis family first;
2. define the search space;
3. define what constitutes an interesting signal;
4. record all tested analyses, not only positive findings;
5. keep exploratory results separate from confirmatory evidence;
6. require later replication or orthogonal support before stronger claims.

Codex may assist with such exploration when it materially improves repository
or data-space coverage, but it must not act as an unconstrained signal-fishing
agent.


## 13. Avoid unnecessary recomputation

Frozen upstream QC, cohort definitions, schemas, and authoritative artifacts
should not be repeatedly revalidated downstream.

Perform new checks only when:

- a new transformation introduces a specific local risk;
- a merge introduces possible duplication;
- a new representation changes analytical units;
- a newly written artifact requires a final local verification;
- an actual inconsistency or error appears.

Do not add generic assertions or repeated QC as defensive boilerplate.


## 14. Prefer existing frozen artifacts

When an upstream artifact already contains the necessary information:

- load it;
- preserve its provenance;
- do not silently recompute it;
- do not derive an equivalent classification using new thresholds.

This is especially important for:

- candidate membership;
- robustness categories;
- structural-family membership;
- confounder classifications;
- technical cautions;
- relationship-form classifications;
- consensus eligibility gates.


## 15. Scientific efficiency takes priority over coding elegance

Do not introduce:

- unnecessary abstraction;
- generalized frameworks for one-off tasks;
- black-box optimization;
- additional machine-learning models without a scientific reason;
- cross-language complexity without methodological benefit;
- repository refactoring unrelated to the current scientific objective.

Prefer the smallest transparent implementation that answers the scientific
question reproducibly.


## 16. Reviewer-resistant execution

Efficiency decisions must remain compatible with the project's scientific
principles.

Always preserve:

- lineage-aware evaluation;
- cross-dataset separation;
- platform-awareness;
- proliferation and purity/confounder awareness;
- transparent analytical units;
- explicit dependence structures;
- prevention of data leakage;
- conservative interpretation.

Association does not imply causality.

Internal robustness does not imply independent validation.

Cross-system transcriptomic correspondence does not imply full
epigenetic-transcriptomic reproduction.

Perturbational support does not establish therapeutic efficacy.


## 17. Practical pre-task decision template

Before a substantial new task, use the following template when relevant:

**Execution recommendation:**  
Interactive notebook / manual repository work / Codex

**Language:**  
Python / R / not applicable

**Codex configuration, if applicable:**  
Current model + reasoning level

**Why this route:**  
Specific methodological or engineering advantage.

**Why not a cheaper/simpler route:**  
Concrete justification. If none exists, use the cheaper/simpler route.

**Escalation condition:**  
Specific condition that would justify increasing model capability,
reasoning effort, compute, or implementation complexity.

**Analysis status:**  
Exploratory / confirmatory / infrastructure

**Decisions to freeze before results:**  
List only those relevant to the task.


## 18. General principle

The project should optimize for:

1. scientific validity;
2. reproducibility;
3. methodological transparency;
4. reviewer-resistant interpretation;
5. efficient use of compute, developer time, and AI credits.

Higher resource consumption is not a proxy for higher-quality work.

Use additional resources only when they provide a defensible increase in
reliability or scientific value.