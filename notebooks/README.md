# notebooks

## Implemented notebook phases

- **Phase 1 — Data Acquisition and Auditing:** notebooks `100`–`106` in `phase1_data_acquisition_and_auditing/`.
- **Phase 2 — Independent Tumor Discovery:** notebooks `200`–`206` in `phase2_tumor_discovery_layer/` — **CLOSED / FROZEN**.
- **Phase 3 — Independent Cell-Line Discovery:** notebooks `300`–`311` in `phase3_cell_line_discovery_layer/` — **CLOSED**.
- **Phase 4 — Cross-System Integration:** notebooks `400`–`404` in `phase4_consensus_programs/` — **CLOSED / FROZEN**.

Phase 2 and Phase 3 are independent discovery systems. Their implemented notebooks should be run only in numerical order within their respective completed phases and with their frozen inputs. Phase 4 consumes those independently frozen candidate layers and must not be retrospectively altered by downstream functional, pharmacogenomic, or perturbational evidence.

## Next notebook

Notebook `500` — **CRISPR Associations** is the next planned analysis. It will begin Phase 5 — Functional Vulnerabilities and should consume the frozen Phase 4 consensus-program layer only after the required functional-dependency inputs have been acquired, audited, and frozen.

## Future phases

Directories for Phases 5–8 currently exist as planned placeholders only. Phase 5 is the next analytical phase; its directory does not imply that notebook 500 has already been implemented. Phase 9 is planned in roadmap v3.0 but does not currently have a notebook directory. Future notebooks are implemented and run only after their required inputs are available and frozen.

See `roadmap.md` for the planned Phase 5–9 notebook series and `docs/workflow.md` for the current operational workflow.
