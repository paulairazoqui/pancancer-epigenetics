# ADR 002 — Independent Discovery and Cross-System Integration

## Status

Accepted

---

## Context

Tumor and cell-line data provide complementary but non-interchangeable views of cancer biology. Using tumor-derived program identities, rankings, or tumor–cell-line matching to select cellular discovery components would introduce conceptual leakage and circularity. It would restrict the cellular search to representations already favored in TCGA and could artificially inflate apparent cross-system concordance.

Independent representations are also not guaranteed to have portable component indices. A failure to recover a program across systems is therefore an informative result, not a reason to force a correspondence.

---

## Decision

The framework adopts the following sequence:

1. independent tumor program discovery;
2. independent cell-line program discovery;
3. representation robustness within each system;
4. cross-system comparison only after both candidate universes are frozen; and
5. consensus construction only after explicit multiview matching.

Phase 2 performed tumor discovery. Phase 3 performed independent cell-line discovery. Phase 4 is reserved for cross-system comparison and possible consensus construction.

Cross-system matching must preserve tumor structural-family metadata, prevent double-counting shared axes, and consider state or extreme relationships as well as continuous relationships where relevant. Technical or unresolved-confounded signals remain explicitly downgraded; partial supporting evidence does not rehabilitate them.

---

## Consequences

Advantages:

* lower risk of leakage and circularity;
* a genuine assessment of cross-system reproducibility;
* informative negative cross-system outcomes; and
* no assumption that component indices are portable.

Costs:

* some programs will not be recoverable across systems;
* correspondence can be partial;
* the number of consensus programs can be lower than the number of candidate programs; and
* matching requires explicit, pre-specified criteria.

---

## Phase Boundary

| Phase | Role |
| --- | --- |
| Phase 2 | Tumor discovery |
| Phase 3 | Cell-line discovery |
| Phase 4 | Cross-system comparison and consensus construction |
| Phase 5 | Functional vulnerability characterization |
| Phase 6 | Pharmacogenomic context characterization |
| Phase 7 | Perturbational hypothesis generation |
| Phase 8 | Orthogonal or external validation |

---

## Interpretation

Cross-system matching is computational evidence of reproducibility, not causal or biological validation. A consensus program is a reproducible computational representation and must not be described as a causal explanation.

Scoring or projection can be used later as an analytical operation in Phase 4 or downstream work, but it is not a mechanism of cell-line discovery.
