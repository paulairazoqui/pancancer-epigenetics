# notebooks

## Implemented notebook phases

- **Phase 1 — Data Acquisition and Auditing:** notebooks `100`–`106` in `phase1_data_acquisition_and_auditing/`.
- **Phase 2 — Independent Tumor Discovery:** notebooks `200`–`206` in `phase2_tumor_discovery_layer/` — **CLOSED / FROZEN**.
- **Phase 3 — Independent Cell-Line Discovery:** notebooks `300`–`311` in `phase3_cell_line_discovery_layer/` — **CLOSED**.
- **Phase 4 — Cross-System Integration:** notebooks `400`–`402` in `phase4_consensus_programs/` — **COMPLETE THROUGH CROSS-LINEAGE ROBUSTNESS**.

Phase 2 and Phase 3 are independent discovery systems. Their implemented notebooks should be run only in numerical order within their respective completed phases and with their frozen inputs.

## Next notebook

Notebook `403` — **Epigenetic Regulator Enrichment** is the next planned analysis. It will consume the frozen consensus-program layer after notebook `402` without redefining correspondence eligibility, consensus orientation, gene weights, source-program identities, or the cross-lineage robustness criteria already assessed upstream.

## Future phases

Directories for Phases 5–8 currently exist as planned placeholders only. Phase 9 is planned in roadmap v3.0 but does not currently have a notebook directory. Future notebooks are implemented and run only after their required inputs are available and frozen.

See `roadmap.md` for the planned Phase 4–9 notebook series and `docs/workflow.md` for the current operational workflow.
