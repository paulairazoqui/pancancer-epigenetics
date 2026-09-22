# notebooks

## Implemented notebook phases

- **Phase 1 — Data Acquisition and Auditing:** notebooks `100`–`108` in `phase1_data_acquisition_and_auditing/` — **CLOSED / FROZEN**.
- **Phase 2 — Independent Tumor Discovery:** notebooks `200`–`206` in `phase2_tumor_discovery_layer/` — **CLOSED / FROZEN**.
- **Phase 3 — Independent Cell-Line Discovery:** notebooks `300`–`311` in `phase3_cell_line_discovery_layer/` — **CLOSED**.
- **Phase 4 — Cross-System Integration:** notebooks `400`–`404` in `phase4_consensus_programs/` — **CLOSED / FROZEN**.
- **Phase 4B — Secondary Molecular Context Characterization:** notebooks `450`–`451` in `phase4b_secondary_molecular_characterization/` — **CLOSED / FROZEN**.
- **Phase 5 — Functional Vulnerabilities:** notebooks `500`–`502` in `phase5_functional_vulnerabilities/` — **CLOSED / FROZEN**.
- **Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI):** notebooks `600`–`603` in `phase6_pharmacogenomic_contexts/` — **COMPLETE UNDER FROZEN SPECIFICATIONS**.

Phase 2 and Phase 3 are independent discovery systems. Their implemented notebooks should be run only in numerical order within their respective completed phases and with their frozen inputs. Phase 4 consumes those independently frozen candidate layers and is not redefined by Phase 4B or Phase 5. Phase 4B methylation-expression results are contextual computational evidence, not causal regulation; TCGA tumors are not assigned resistance/sensitivity labels. Phase 6 downstream work must consume frozen upstream handoffs rather than silently recomputing them.

## Future phases

Notebook `603 — Cross-Screen Replication` is complete under the specification prospectively frozen on 2026-09-22. Phase 6 is therefore complete under frozen specifications. Phases 7–10 remain planned. Future notebooks are implemented only after their required inputs and methodological decisions are available and frozen.

See `roadmap.md` for the current notebook sequence and `docs/workflow.md` for the operational workflow.
