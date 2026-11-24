# Derived Artifact Lifecycle Policy

## Scope and governing rule

This policy governs derived artifacts and their registry throughout the active
research and manuscript-development lifecycle of `pancancer-epigenetics`.

**Until a manuscript-supporting reproducibility release is explicitly approved,
derived artifacts are rebuildable, not permanently byte-frozen.** A completed
notebook or an accepted interim scientific result does not prohibit a documented
correction and an end-to-end rerun.

An artifact's registered SHA-256, size, and shape describe a **particular
verified output snapshot**. During active development these identities must be
refreshed after an authorized, successful rebuild; they are not a reason to
reject a scientifically justified rerun.

This does not relax prespecified analytical decisions, cohort eligibility,
leakage controls, confirmatory-design boundaries, or source-data provenance.
A *methodological freeze* (such as fixing a candidate set before downstream
evaluation) is distinct from *byte-level immutability of an output file*.

## Operational lifecycle

### Active research and reconstruction

- Notebook-derived files may be rewritten when a notebook is rerun, including
  after correction of an upstream cohort, identity mapping, or computation.
- The intended outcome is a reproducible execution from project source inputs
  through all dependent notebooks, in dependency order, as often as necessary.
- A change in an upstream artifact requires identifying and rerunning affected
  downstream consumers. A full end-to-end rerun is valid when required or
  chosen; do not assume an unaffected consumer needs recomputation.
- Notebook execution counts, saved outputs, and registry fingerprints may
  correspond to different runs during an incomplete reconstruction. Do not
  represent the whole project as reconciled until the dependent chain has
  completed successfully.
- Do not promote a new scientific decision merely by rerunning or refreshing a
  hash. Scientific changes still require their appropriate justification,
  review, and documentation.

### Notebook output registration

Every notebook that produces **registered derived artifacts** must implement
the following closure sequence:

1. Persist its intended outputs using the existing serializers and formats.
2. Validate the actual written outputs and their relevant analytical/structural
   invariants; stop on errors.
3. Finalize the applicable provenance of the run and its inputs.
4. Call `refresh_notebook_artifacts(notebook_path, verified_outputs)` with
   the complete set of registered outputs and observed shapes, after successful
   validation. Use `require_unchanged=False` for active-development rebuilds.
5. Validate the registry and report the updated identities.

The existing function matches the complete registered output set for the
declared notebook producer and updates `shape`, `size_bytes`, and `sha256`
without silently changing artifact IDs, producers, paths, roles, or dependencies.
Use `register_artifacts()` separately when an intentional declaration change
is needed, with explicit review and provenance.

Do not automatically refresh registry identities after a failed or incomplete
notebook execution. Do not paper over a discrepancy by hashing an arbitrary
local file without verifying that it is the intended output of the accepted
reconstruction.

### Write behavior during active development

Do **not** use `frozen_artifact_output` or an equivalent registered-hash
no-replacement guard for artifacts that must be rebuilt during active research.
Such a guard prevents legitimate reruns that change output bytes.

Existing applications of `frozen_artifact_output` in producer notebooks must
be removed or replaced as a **separate, reviewed implementation change** before
those notebooks are used for a changed-output rebuild. The artifact registry
alone cannot make the current guarded notebooks rerunnable.

Checks that detect unexpected missing files, incorrect producer declarations,
invalid dependencies, or analytical problems remain appropriate. Safe staging
or atomic file replacement is compatible with this policy **provided it does
not reject a valid changed output solely because its old registered hash
differs**.

## Meaning of the current registry status

The current registry schema requires `status: "frozen"` on every derived
artifact. This is a **legacy schema label**, not a reliable assertion that all
163 registered file identities are permanently immutable or manuscript-final.

Until an explicit schema and code migration is reviewed, retain that field for
backward compatibility. Interpret the registry's identities operationally as
the latest **registered** output, which can be stale after an incomplete
reconstruction. Do not bulk-relabel entries or silently alter the schema.
A future migration should distinguish active/rebuildable artifacts from
explicitly publication-frozen versions.

References to "frozen" cohorts, programs, candidate eligibility, or analytical
gates elsewhere in the project generally describe **methodological boundaries
within an analytical run**. This policy does not authorize downstream
redefinition of those upstream choices or retrospective tuning.

## Reconstruction and provenance

When an upstream correction is authorized:

1. Record the reason and affected scientific/technical objects.
2. Rerun the corrected producer and verify its outputs.
3. Refresh that producer's registered identities at successful notebook
   closure.
4. Rerun affected downstream notebooks in dependency order, verifying and
   refreshing each producer's outputs.
5. Compare the resulting chain with the intended scientific decisions; resolve
   any substantive differences before treating the chain as current.
6. Preserve the historical change through version control and relevant
   provenance/decision records. A refreshed registry is a current snapshot,
   not a complete historical execution log.

Where the registry and local data differ because a reconstruction is partially
complete, do not automatically prefer either side. Complete and verify the
authorized producer/downstream reconstruction, then reconcile registrations.
In particular, do not update the Phase 4 fingerprints by bulk hashing files
without confirming their role in the accepted corrected-cohort run.

Source-data inventories and `config/raw_data_registry.json` retain their own
audited provenance rules; derived artifact refresh does not authorize changing
raw source identities, source snapshots, or scientific input selection.

## Publication freeze

Only after the full intended analytical chain is reconciled, validated, and
approved for the manuscript/reproducibility package should a specific version
be declared **publication-frozen**:

- Pin its exact derived files, sizes, SHA-256 identities, code revision,
  environment, inputs, and relevant execution provenance.
- Apply byte-preserving write guards to that explicit released version.
- Retain prior release identities for traceability.
- Any substantive post-freeze correction must become a new reviewed version,
  with its affected downstream analysis and manuscript evidence reconciled.

Until that event, routine development and corrected-cohort rebuilds must remain
possible without defeating a hash-based write guard.
