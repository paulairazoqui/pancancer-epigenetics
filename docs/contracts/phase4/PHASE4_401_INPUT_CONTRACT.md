# Notebook 401 input contract

This contract freezes provenance and interpretation rules for notebook 401 — Consensus Program Construction. It does not create consensus programs, change any result from notebooks 205–400, or reopen scientific analyses. The exploratory audit that supplied the frozen tumor classifications is intentionally ignored and is not reproducible from a clean clone; therefore, the compact tracked manifest at `config/program_handoffs/tcga_phase2_candidate_program_handoff.csv` is the authoritative Phase 2 interpretation handoff.

## Analytical levels

Notebook 401 must keep three distinct analytical levels:

1. **Unique RNA correspondence event** — the independent transcriptomic matching unit from notebook 400.
2. **Tumor structural family** — one of the eight frozen families `PF01`–`PF08`.
3. **Tumor cross-omic arm** — one of the 13 retained TCGA RNA–methylation pairs.

These levels are not interchangeable. Family members remain distinct arms, but shared RNA, methylation, or family membership must not inflate evidence counts.

## Authoritative inputs

| Input | Analytical unit | Authoritative use in 401 |
|---|---|---|
| `config/program_handoffs/tcga_phase2_candidate_program_handoff.csv` | 13 tumor arms / 8 families | Tumor identity, family membership, frozen audit status, priority, HM27 status, relationship form, limitation, and consensus handling. |
| `data/processed/consensus_programs/400_cross_system_correspondence_summary.csv` | 10 unique RNA axes | Axis-level correspondence class, accepted cell-line program only when supported, and orientation. |
| `data/processed/consensus_programs/400_cross_system_pairwise_matching_metrics.csv` | 100 prespecified axis-by-program comparisons | Full matching topology and ambiguity metadata; not an alternate route to promote a match. |
| `data/processed/consensus_programs/400_cross_system_tumor_arm_handoff.csv` | 13 tumor arms | Propagation of axis-level matching to arms; rows are not independent correspondence events. |
| `data/processed/consensus_programs/400_cross_system_shared_gene_universe.csv` | 2,389 shared genes | Exact HGNC-symbol crosswalk for construction; it does not contain loadings. |
| `data/processed/consensus_programs/400_cross_system_comparison_metadata.json` | one comparison run | Frozen matching policy, dimensions, thresholds, seed, support rule, and limitations. |
| `data/processed/cellline_programs/311_program_robustness_summary.csv` and metadata | 10 cell-line candidates | Cell-line internal robustness context; never a structural matching or rescue criterion. |
| `data/processed/tumor_programs/tcga_cross_omic_candidate_program_robustness_evidence.csv` and metadata | 13 tumor arms | Numeric internal tumor robustness context only; never a source for reconstructing categorical audit labels. |

When construction is permitted by the gates below, 401 may use the frozen loading artifacts `data/processed/tumor_programs/tcga_primary_tumor_rna_ica_candidate_gene_loadings.csv` and `data/processed/cellline_programs/310_ica_program_loadings.parquet`, restricted and ordered by the 2,389-gene crosswalk and oriented with the accepted notebook 400 orientation. Scores or downstream phenotypes must not determine eligibility or construction choices.

## Frozen rules for 401

### Accepted structural match

Only an axis-level row with `correspondence_class == SUPPORTED_CORRESPONDENCE` may be treated as an accepted cross-system transcriptomic match. For `AMBIGUOUS_CORRESPONDENCE`, `PARTIAL_CORRESPONDENCE`, or `NOT_RECOVERABLE`, any populated cell-line program identifier is nearest-candidate metadata only and must not be promoted as a match. Pair-level partial flags are not axis-level `PARTIAL_CORRESPONDENCE` decisions.

### Correspondence is not consensus

`SUPPORTED_CORRESPONDENCE` does not automatically equal a consensus program. Notebook 401 must apply tumor-side and cell-line-side qualifications separately, preserve structural-family dependence, and keep cross-omic interpretation bounded.

### Cell-line robustness

Notebook 311 fields must remain explicitly namespaced as cell-line evidence, for example `cell_line_robustness_category`, `cell_line_program_status`, and `cell_line_context_sensitive`. They provide contextual internal evidence and must not change, rescue, or upgrade the frozen structural correspondence class.

`RNA_IC150 ↔ ICA_PROGRAM_09` remains `SUPPORTED_CORRESPONDENCE`, while `ICA_PROGRAM_09` remains `CONTEXT_SENSITIVE_CANDIDATE`. Both facts must coexist; structural correspondence does not erase context sensitivity.

### Tumor cautions

Notebook 401 must load the tracked Phase 2 handoff manifest directly. It must not derive `CONFOUNDED`, `TECHNICAL_SIGNAL`, `METHOD_LIMITED`, `HIGH_PRIORITY_CANDIDATE`, or any other tumor audit category from numeric notebook 206 evidence. Subsequent structural correspondence must not rehabilitate a frozen limitation.

### Dependence

`CROSS_OMIC_PAIR_03` and `CROSS_OMIC_PAIR_12` represent one `RNA_IC184` cross-system transcriptomic correspondence event, not two independent replications. The same no-inflation rule applies to every shared RNA axis, methylation axis, and structural family. Arms remain non-interchangeable; dependence controls evidence counting rather than collapsing arms.

### Cross-omic interpretation

A supported match may be described as a **candidate cross-system transcriptomic representation with tumor-side methylation context**. It does not establish full epigenetic-transcriptomic reproduction in cell lines, biological causality, independent validation, clinical resistance prediction, or a validated therapeutic target. Association is not causality.

### Phenotype-conditioned candidate universe

The Phase 4 structural comparison operates within the frozen cell-line candidate universe previously selected for association with the resistance-like pharmacogenomic phenotype. Phenotype values and association effect sizes were not used to calculate, orient, threshold, rescue, or upgrade the structural cross-system matches. It is therefore incorrect to state that phenotype information played no role whatsoever in defining the Phase 4 candidate universe.

Notebook 401 must not introduce new thresholds or use robustness, biology, family membership, or downstream phenotype evidence to resolve ambiguous structural matches post hoc.
