# Project Progress Tracker

| Phase | Status | Description |
|---|---|---|
| Phase 0 | ✅ | Project foundation, architecture, governance, reproducibility strategy |
| Phase 1 | ✅ | Dataset acquisition, auditing, manifests, integrity validation |
| Phase 2A | ✅ | Dataset inventory, identifier audit, overlap analysis |
| Phase 2B | ⬜ | Identifier mapping and integration tables |
| Phase 2C | ⬜ | Coverage analysis and sample selection |
| Phase 3 | ⬜ | Transcriptomic preprocessing and QC |
| Phase 4 | ⬜ | Mutation preprocessing and feature engineering |
| Phase 5 | ⬜ | Drug response preprocessing and pharmacologic QC |
| Phase 6 | ⬜ | Integrated modeling dataset construction |
| Phase 7 | ⬜ | Baseline machine learning models |
| Phase 8 | ⬜ | Explainability and biomarker discovery |
| Phase 9 | ⬜ | Target prioritization |
| Phase 10 | ⬜ | Drug repurposing |
| Phase 11 | ⬜ | External validation (TCGA and others) |
| Phase 12 | ⬜ | Publication, deployment, reproducibility release |

---

## Current Active Tasks

| Task | Status |
|---|---|
| 01_dataset_inventory.ipynb | ✅ |
| 001_data_integration_strategy.md | ✅ |
| 02_identifier_mapping.ipynb | ⬜ |
| master_model_mapping.parquet | ⬜ |
| 03_coverage_analysis.ipynb | ⬜ |

---

## Current Core Decisions

| Topic | Decision |
|---|---|
| DepMap release | 25Q3 |
| GDSC release | 8.5 |
| Primary integration key | ModelID |
| DepMap ↔ GDSC bridge | SangerModelID |
| Expression strategy | RNA default profiles |
| Mutation strategy | WGS default profiles |
| Initial omics | Expression + mutations |
| Initial pharmacology | GDSC IC50/AUC |
| Modeling philosophy | Interpretable ML first |
| Raw data policy | Immutable raw datasets |

---

## Notes

Legend:

- ✅ completed
- ⬜ pending
- 🟨 in progress
- ❌ discarded