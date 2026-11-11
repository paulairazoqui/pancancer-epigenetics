# Phase 8 — Design fixed before the signed-coherence audit

**Status:** working TCGA-only audit.  This file fixes the limited exploration
before calculations; it neither amends the Notebook 800 contract nor authorizes
external analysis.

## Questions

1. Does signed coherence quantify a property absent from the candidate
   relative-edge concordance statistic?
2. Is either of two prespecified signed summaries stable enough in TCGA to be a
   useful descriptive companion, without being called external replication?
3. Do simple, declared synthetic mechanisms separate the two properties for
   interpretable reasons?

## Fixed estimands

For program `k`, lineage `l`, frozen weights `w`, and distinct gene-pair
correlations `r_ij`, define `s_ij = sign(w_i w_j)`, `q_ij = abs(w_i w_j)`, and
`z_ij = s_ij r_ij`.  The audit calculates only:

* `C_mean = sum(q_ij z_ij) / sum(q_ij)`;
* `C_median`, the weighted median of `z_ij` under `q_ij` (smallest value whose
  cumulative normalized weight is at least 0.5).

The mean is a direct signed average and retains magnitude information, but can
be pulled by high-leverage edges.  The median is robust to a minority of
extreme edges but can be discontinuous and, with concentrated weights, reflect
only a small effective set of genes/pairs.  Both can be negative.  A global
sign inversion of every weight leaves both unchanged; a single-gene sign flip
changes exactly its incident edges.  No additional robust formula will be
searched.

For a lineage-specific score formed from the same weights and genes
standardized within that lineage to mean zero and sample SD one, `C_mean` is
algebraically tied to score variance. It is therefore a signed edge summary and
not evidence independent of a score constructed from those inputs. This does
not apply unchanged to a score with another scaling convention.

## TCGA-only calculations

All inputs are SHA-verified registered Phase 2/4 artifacts.  The 2,389 genes,
their ordering, every loading magnitude and sign, and the executed TMM/logCPM
representation remain unchanged.  For the seven contract lineages, calculate
each summary from the full TCGA lineage and from eight disjoint random tumor
splits using seed `20261111`.  Per-half size is
`min(floor(n_TCGA/2), contractual CPTAC-3 source n)`, copied from the prior
reference-reliability audit; CPTAC-3 expression is never opened.  Split results
describe within-TCGA stability only.

The audit will report program/lineage full estimates, split median and range,
and the concentration diagnostics already implied by `q`.  It will not select
programs or lineages from those results.

## Synthetic scenarios

With an independently seeded (`20261112`) Gaussian signed two-block reference
correlation construction, calculate relative-edge concordance and both signed
summaries for six declared comparison mechanisms: near preservation, uniform
attenuation, local rewiring, inversion of opposite-sign relationships, a common
latent factor, and a mixed-factor low-coherence pattern. These are
algebraic/model demonstrations, not biological models, nor a calibration of a
test or external data.

## Interpretation and invalidation

No universal cutoff, p-value, or binary replication rule will be produced.
The recommendation is invalidated if frozen identities/hashes fail, a lineage
has non-finite values or zero gene variance, or either statistic is degenerate.
Tumors—not edges—are the resampling units; a split distribution is neither a
null distribution nor an external confidence claim.
