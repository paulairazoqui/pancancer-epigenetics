# notebooks

## Implemented notebook phases

- **Phase 1 — Data Acquisition and Auditing:** notebooks `100`–`106` in `phase1_data_acquisition_and_auditing/`.
- **Phase 2 — Independent Tumor Discovery:** notebooks `200`–`206` in `phase2_tumor_discovery_layer/` — **CLOSED / FROZEN**.
- **Phase 3 — Independent Cell-Line Discovery:** notebooks `300`–`311` in `phase3_cell_line_discovery_layer/` — **CLOSED**.
- **Phase 4 — Cross-System Integration:** notebooks `400`–`404` in `phase4_consensus_programs/` — **CLOSED / FROZEN**.
- **Phase 5 — Functional Vulnerabilities:** notebook `500` in `phase5_functional_vulnerabilities/` is implemented and complete; Phase 5 remains **ACTIVE**.

Phase 2 and Phase 3 are independent discovery systems. Their implemented notebooks should be run only in numerical order within their respective completed phases and with their frozen inputs. Phase 4 consumes those independently frozen candidate layers and must not be retrospectively altered by downstream functional, pharmacogenomic, or perturbational evidence. Phase 5 consumes the frozen Phase 4 consensus-program layer without redefining it.

## Next notebook

Notebook `501` — **RNAi Associations** is the next planned analysis in Phase 5. It should begin only after the required RNAi dependency input has been acquired, audited, and frozen for use. Notebook `500` — **CRISPR Associations** is complete and should not be retrospectively redefined by later RNAi or integrated-vulnerability results.

## Future phases

Phase 5 is implemented through notebook 500 and remains active. Directories for Phases 6–8 remain planned placeholders. Phase 9 is planned in roadmap v3.0 but does not currently have a notebook directory. Future notebooks are implemented and run only after their required inputs are available and frozen.

See `roadmap.md` for the planned Phase 5–9 notebook series and `docs/workflow.md` for the current operational workflow.
