# Notebook 112 — CPTAC-3 source RNA technical audit and QC-metadata provenance

**Status (2026-11-01): MIGRATION DRAFT — code migrated, clean-clone Run All and historic upstream snapshot recovery pending.**  
**Owner:** Phase 1 / Notebook 112.  
**Execution contract:** Notebook 111 → Notebook 112 → Notebook 113 → Notebook 800.  
**Methodological boundary:** source-only technical diagnostics and public metadata attribution; no quality pass/fail, downstream program scoring, cohort freeze or biological inference.

## 1. Why Notebook 112 was refactored

The previously executed Notebook 112 depended on two files created by later Notebook 800: the original 12-file H GDC response and the A–H readiness manifest. That reversed the execution order. The 2026-10-23 800 A/E/F/G/H precursor calculations were also needed to reconstruct the originally selected 12 STAR output files. Merely preserving their UUIDs would have hidden the analysis that generated them.

The refactored Notebook 112 therefore regenerates the source-side chain from 111 and raw STAR Counts, selects the 12 STAR records with the **same original rule**, and checks its result against the historical H snapshot. It does not treat an observed match with the snapshot as authorization to change the original sampling logic.

### Source-only chain reproduced in 112

1. **A:** use the 111 provisional primary-tumor file index, classify file/sample/aliquot multiplicity, preserve 1,082 simple provisional primary cases, 288 multiplicity cases, 530 with extra same-case RNA files and 37 with at least one ambiguous extra RNA file.
2. **E source technical:** read \`gene_id\` and \`unstranded\` exactly once from each of the 1,082 original local STAR Count files, verify source file sizes against 111, and compute gene-row counts, assigned gene-count totals, detected STAR gene rows and special \`N_\` tallies. All are descriptive, not independent sequencing QC. No count threshold is trained or applied.
3. **F:** reconstruct additional same-case RNA provenance flags and the original descriptive bottom-20 count context; retain ambiguous source ancestry.
4. **G:** calculate source-site/disease-stratum count distributions and assemble the same technical-count sampling frame.
5. **H:** apply the prespecified four-context, three-per-context low/central rank selection, sorted by (\`unstranded_gene_count_total\`, \`file_id\`). The four strata and positions are unchanged from the old 800 code:
   - uterus adenoma/adenocarcinoma: positions 0, 1 and \`n // 2\`;
   - pancreas ductal/lobular: positions 0, 1 and \`n // 2\`;
   - kidney adenoma/adenocarcinoma: positions 0, \`n // 2 - 1\` and \`n // 2\`;
   - lung adenoma/adenocarcinoma: positions 0, \`n // 2 - 1\` and \`n // 2\`.

The recomputed twelve file UUIDs must exactly match the original archived H query and its hits. Any mismatch **stops** the notebook; the frozen historical sample must not be silently changed to make it pass.

**Scope separation:** Original E comparisons against the 2,389-gene Phase 4 frozen reference are not part of Phase 1 source acquisition. They remain the responsibility of subsequent program-reference compatibility / validation. Source technical diagnostics and fixed-program gene coverage are distinct tests and must not be conflated.

## 2. Historical GDC observations and version control

The old H STAR-output snapshot was recovered from Git commit \`b0f41b0^\` with **unchanged Git blob SHA \`9a7c5a7aa0fe4f3cf6580128aa7837df84c7debd\`** and SHA-256 \`dcd1dc8b332bda55c658751e6e781a9cbe3719ed07fd17e38e67bbcf794b6ecb\`. It was captured at \`2026-10-23T20:51:50.219909+00:00\` and remains the original response, not a newly fabricated snapshot.

| Versioned source snapshot | Original SHA-256 | State |
|---|---|---|
| \`docs/evidence/phase1/notebook112/112_gdc_star_output_pilot_snapshot.json\` | \`dcd1dc8b332bda55c658751e6e781a9cbe3719ed07fd17e38e67bbcf794b6ecb\` | Recovered, byte-identical |
| \`docs/evidence/phase1/notebook112/112_gdc_upstream_input_pilot_snapshot.json\` | \`ca5e2f54458fb6cc26946ef734f1f2d3606817f2836cbc843466eb7633e8e358\` | **NOT YET RECOVERED: blocker** |

The second upstream JSON was generated on the original local Notebook 112 execution of 2026-10-23; it is not reconstructible byte-for-byte from the H snapshot because it is a separately queried projection. Until that original JSON is restored, a clean-clone reproduction is **not certified**. A contemporary GDC requery may be compared to the frozen response but may never replace it silently.

The snapshot files are exceptions to \`.gitignore\` because external metadata responses may change after publication. Derived CSV and JSON outputs under \`data/interim/\` remain untracked and are regenerated from code.

## 3. Exact inputs and outputs

**Inputs:** 111 audit summary and file index, 111 provisional primary file inventory, 1,082 acquired local STAR Count files, two versioned GDC metadata snapshots. Notebook 111 must have performed complete source-payload MD5 verification. The 112 execution does not repeat 111's 5,578-file integrity sweep.

**Downstream technical consumable:** \`data/interim/metadata/112_cptac3_rna_simple_primary_technical_inventory.csv\` (1,082 rows; case/file identity plus source-only STAR counts). Notebook 113 consumes this file for source provenance, **not** as an independent read-quality cutoff.

**Other descriptive outputs** may be displayed within 112, with local CSVs retained only where needed for the accepted source handoff. The historical direct-input audit retains:
- \`112_cptac3_qc_input_file_provenance.csv\` (12 records);
- \`112_cptac3_qc_input_metric_reconciliation.csv\` (72 paired-field records);
- \`112_cptac3_qc_source_feasibility.csv\` (10 summary records);
- \`112_cptac3_qc_provenance_handoff.json\` (input fingerprints and explicit limitations).

All these generated files remain \`data/interim/metadata/\`, not version-controlled. Rationalization of unnecessary local outputs is separate from any scientific source-content change.

## 4. Historical comparison and QC limitations

The original execution on 2026-10-23 reported twelve direct upstream file records with exact case+aliquot associations (12/12), six agreeing metrics in two provider metadata projections (72/72), no sample exclusions, no frozen QC threshold and no independent library/read-quality validation. The refactored notebook must reproduce these outcomes from the original snapshots, not assert them solely from the historical markdown.

The 12-file pilot is deliberately nonrepresentative. Agreement between two GDC API projections does not prove independent measurements or denominators. Do not generalize 12/12 availability to the full 1,082/2,968-file source universe, declare all 721 downstream proposed cases QC-pass, or infer donor independence, external biological replication, or clinical validity.

## 5. Migration-specific acceptance gates

- Original archived H snapshot byte identity and query integrity pass.
- A/E/F/G source-derived sampling frame reconstructs original 12 file UUIDs without a hardcoded list.
- Original upstream-input snapshot is restored to Git at the specified SHA-256.
- Clean-clone sequential execution can regenerate 111 → 112 and the 112 technical consumable.
- Local Run All reproduces the observed 12/12 and 72/72 counts and does not modify raw data or registries.
- Notebook 113 reuses the 112 source-technical consumable with unchanged G2 cohort membership and unchanged 721-case proposed source cohort, subject to execution verification.

**This migration is not closed until those conditions have been verified.**
