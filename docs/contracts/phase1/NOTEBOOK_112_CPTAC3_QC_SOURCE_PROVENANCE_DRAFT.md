# Notebook 112 — CPTAC-3 Upstream RNA QC Source Provenance Pilot

**Status:** PROSPECTIVE TECHNICAL CONTRACT — DRAFT / **NOT YET EXECUTED**  
**Created:** 2026-10-23  
**Phase:** 1 — Source acquisition and auditing  
**Notebook:** `notebooks/phase1_data_acquisition_and_auditing/112_cptac3_qc_source_provenance.ipynb`  
**Local prerequisite:** executed/fingerprint-verified Notebook 111 and H metadata-only snapshot from the executed Notebook 800  
**Analysis/validation:** NOT AUTHORIZED; analytic cohort NOT FROZEN

## 1. Architectural rationale

The existing Notebook 111 established CPTAC-3 source identity, 5,578 payload MD5s, direct file-to-aliquot associations, sample-ancestry categories, provisional primary-tumor candidates and auditable intermediate tables. The separately executed **Notebook 800 PREFLIGHT-H** queried public GDC metadata for exactly **12** uniquely mapped provisional primary STAR Count outputs (three in each of four selected source contexts). H observed **one upstream workflow input-file metadata node per STAR output** and six numeric quality-related GDC fields available in all 12, without independently verifying the input files' case/aliquot provenance.

This is a provider/source acquisition-auditing problem, not a program replication problem. The project architecture explicitly permits later Phase 1 acquisition or audit notebooks to consume frozen handoffs from later-numbered analyses without reopening that analysis. Thus Notebook 112 is a **small Phase 1 provenance follow-up**, not a new Phase 8 eligibility preflight. Preserve H's historical evidence; do not move, edit or reexecute H or Notebook 111 as part of this task.

## 2. Frozen exact source inputs

- `data/interim/metadata/111_cptac3_acquisition_audit_summary.json` and `111_cptac3_file_index.csv`. Check file-index SHA-256 against the 111 summary and original RNA acquisition metadata SHA-256.
- `data/interim/metadata/800_preflight_h_gdc_qc_source_pilot.json`. Check its own SHA-256 and exact query hash against `800_preflight_a_readiness.json`. This cached JSON is the authoritative **discovery snapshot** for the twelve STAR output file IDs and their analysis `input_files` nodes; it is not re-requested from GDC.
- Preserve exact GDC STAR output `file_id`, file name/size/MD5, direct `associated_entities` case/aliquot match, uniquely mapped provisional-primary status and `analysis.analysis_id` from H/111. Do not infer source sample from case membership.
- Extract upstream input-file UUIDs `analysis.input_files.file_id` from H. Require one input node per H STAR output as actually observed; refuse to guess missing IDs or expand to any other source record. It may have fewer than twelve unique upstream input IDs if inputs are shared, in which case repeated inputs must remain visible rather than being counted as independent sample evidence.

The H pilot was deliberately **not representative**: three files per uterine, pancreatic, kidney and lung source context; technical count extremes/center. Sample counts, per-lineage quality rates or larger-cohort coverage must not be extrapolated from H/112.

## 3. Independent direct-input-record query — prospective scope

Perform exactly **one public GDC `/files` metadata-only query** restricted to the upstream input-file UUIDs extracted from the fixed H JSON. Request only file UUID/name/size/checksum, access and data type, `associated_entities`, workflow identity and the six fields previously observed inside H's input-file nodes: `total_reads`, `proportion_reads_mapped`, `proportion_reads_duplicated`, `average_base_quality`, `average_read_length`, `average_insert_size`.

- Query cap: **at most twelve input-file UUIDs**. Save the exact request, query SHA-256, UTC capture time, return subset/identity and response in a **new** immutable-on-rerun local snapshot, `112_cptac3_qc_upstream_direct_file_snapshot.json`.
- Failed HTTP request or malformed response: **stop**, do not infer quality metadata are absent.
- Some input file UUIDs might have no public direct `/files` record. Classify them explicitly as **not returned in this bounded query**, not provider-wide absence or proof of inaccessible QC.
- If the direct file has an exact single `associated_entities` aliquot matching the STAR output's **case and aliquot**, classify `EXACT_INPUT_STAR_CASE_ALIQUOT_MATCH`. Missing, multiple or discordant associations cannot be rescued with case-level matches or lexical IDs.
- Compare the six `analysis.input_files` embedded values with the fields retrieved from the direct input record. Agreement establishes **same-provider metadata consistency** only; these may be the same database measurements exposed along two API paths. It does not prove independence of QC, tool-specific definitions/versions or verified denominators for mapping and duplication.
- Do not query or download source read payloads, controlled BAM/FASTQ, broaden the API filter, select a preferred STAR file, apply a QC cutoff, compute expression values, normalize, perform project integration, or score a program. Do not automatically modify `config/raw_data_registry.json` or `config/artifact_registry.json`.

## 4. Output contracts

All outputs are local `data/interim/metadata/`, not automatically registered/frozen artifacts:

| Output | Purpose |
|---|---|
| `112_cptac3_qc_upstream_direct_file_snapshot.json` | Versioned exact GDC upstream file metadata projection and query/source hashes; never overwrite silently |
| `112_cptac3_qc_input_file_provenance.csv` | 12 STAR output rows with exact per-output upstream input-file UUID, source type and case+aliquot matching status |
| `112_cptac3_qc_input_metric_reconciliation.csv` | 72 source-scoped field-comparison rows (12 STAR × six named QC metadata fields); no sample QC pass/fail |
| `112_cptac3_qc_source_feasibility.csv` | Bounded counts of direct input records and source-link/field agreement; no extrapolation |
| `112_cptac3_qc_provenance_handoff.json` | 111 and H input hashes, query and snapshot hash, metadata CSV hashes, strictly defined status, open gates, no-scoring/no-selection flags |

Preserve `cohort_frozen=false`, `QC_eligibility_authorized=false`, `biological_replication_performed=false`, `samples_selected_or_excluded=0`, `QC_cutoffs_frozen=0`. These are Phase 1 **source provenance** outputs, not a frozen external validation cohort.

## 5. Scientific decision and stop rule

A positive exact case+aliquot match **permits proposing** a separately reviewed assessment of provider QC definitions and their coverage across the frozen STAR source universe. It does not create an automatic GO to scale or a QC-eligible primary cohort. A field is useful for prospective QC only after its source processing level, read vs fragment unit, denominator, software/workflow version, dependence on library protocol and missingness structure are established.

If exact direct-input records or direct aliquot associations fail for the bounded pilot, record the limitation and **STOP** this provider-QC acquisition route without automatic sample rescue. If 12/12 source links reconcile, record a **CONDITIONAL SOURCE-PROVENANCE PASS** and hand over the descriptive evidence for review; do not automatically fetch all 1,082 primary candidates.

**Next distinct phase:** Notebook 800 must separately determine analytical eligibility, the 288 multi-primary-candidate case policy, CPTAC–TCGA donor independence, source-to-TCGA lineage crosswalk, reference-compatible normalization and a prespecified independent matched-null replication estimand. This 112 technical work is not itself a validation study.

**References:** [GDC aligned reads summary metrics](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Aligned_reads_summary_metrics/); [GDC API fields](https://docs.gdc.cancer.gov/API/Users_Guide/Appendix_A_Available_Fields/); [GDC mRNA analysis pipeline](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/).
