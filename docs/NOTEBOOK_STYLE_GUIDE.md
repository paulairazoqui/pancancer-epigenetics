# Notebook Style Guide

This document defines implementation and documentation conventions for analytical notebooks in the `pancancer-epigenetics` project.

## Cell structure

- Keep code cells short and focused on a single analytical responsibility.
- Use descriptive section headers with the project-standard separator format.
- Separate methodological explanation from implementation whenever practical:
  - Markdown cells document scientific rationale, assumptions, analytical boundaries, and interpretation.
  - Code comments document local implementation decisions that are not evident from the code itself.
- Avoid combining loading, transformation, analysis, validation, and persistence in a single cell unless they form one indivisible operation.

## Code comments

Comments should explain **why**, not restate **what** the code already expresses.

Add comments when they preserve information that is not obvious from the Python implementation, including:

- methodological assumptions;
- non-obvious transformations;
- identifier harmonization decisions;
- sign or orientation conventions;
- leakage-prevention decisions;
- confounder-aware operations;
- permutation or resampling logic;
- handling of shared or non-independent analytical units;
- choices made specifically to preserve reproducibility or prevent overinterpretation.

Avoid comments that merely translate straightforward pandas, NumPy, or Python operations into prose.

For example, prefer:

> ICA signs are arbitrary across independent decompositions; absolute correlation is used for matching while signed correlation defines orientation.

over:

> Calculate absolute correlation.

## Reproducibility

- Use project-relative paths through `Paths`.
- Avoid hardcoding paths or values already defined upstream.
- Freeze stochastic parameters before inspecting results when they influence inferential procedures.
- Do not change seeds, thresholds, feature spaces, or matching criteria after observing results unless explicitly documented as a new exploratory analysis.
- Preserve deterministic execution wherever practical.

## Downstream notebook policy

Once upstream cohorts, QC, schemas, and authoritative artifacts are
accepted for the current analytical run (without implying permanent
file-identity immutability):

- do not repeat exhaustive existence, schema, uniqueness, or row-conservation checks by default;
- perform only local checks required by genuinely new transformations or risks introduced in the current notebook;
- do not silently recompute authoritative upstream decisions.

## Derived artifact registration

Follow [`ARTIFACT_LIFECYCLE_POLICY.md`](ARTIFACT_LIFECYCLE_POLICY.md).
During active research, **registered derived outputs are rebuildable**.

- Every notebook that saves registered derived outputs must persist and verify
  those outputs before calling `refresh_notebook_artifacts()` with their
  complete declared output set and observed shapes.
- Use `require_unchanged=False` for an authorized development rebuild. The
  registered shape, byte count, and SHA-256 must describe the successfully
  generated files. Do not refresh a failed or incomplete run.
- Use `register_artifacts()` for new or deliberately revised artifact
  declarations, preserving explicit review of producers, paths, dependencies,
  and scientific provenance. Do not silently rewrite declarations.
- Following an upstream correction, rerun affected downstream notebooks in
  dependency order, checking outputs and refreshing each notebook's entries.
- Do **not** use `frozen_artifact_output` for active-research derived outputs.
  Remove any existing guard in a separately reviewed code change before
  attempting a changed-output rerun.
- The current registry field `status: "frozen"` is legacy schema terminology,
  not a guarantee of permanent byte-level immutability. Methodological
  prespecification and prevention of downstream redefinition remain binding.
- Pin and protect a specific byte-identical artifact release only at the
  explicit manuscript/reproducibility freeze.

## Documentation balance

Markdown is the primary location for scientific rationale and interpretation.

Inline comments should remain concise and local.

The objective is not maximal commenting, but sufficient documentation for another analyst to understand the methodological intent of non-obvious code without reconstructing it from project history.

Existing closed notebooks do not require retrospective comment expansion unless a concrete reproducibility or interpretability problem is identified.
