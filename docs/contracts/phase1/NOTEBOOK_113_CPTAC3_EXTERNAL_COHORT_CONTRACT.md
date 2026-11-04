# Notebook 113 — CPTAC-3 External Cohort Construction and Eligibility

**Phase:** 1 — Data acquisition and source auditing  
**Notebook:** `notebooks/phase1_data_acquisition_and_auditing/113_cptac3_external_cohort_construction.ipynb`  
**Scientific status:** Executed source-cohort construction. A 727-case RNA-seq source cohort is proposed and technically characterized; no inferential cohort is frozen, and no external program replication has been established.

## 1. Scientific objective and scope

Construct an auditable, outcome-blind CPTAC-3 primary-tumor RNA-seq source cohort for subsequent, lineage-aware evaluation of immutable TCGA-derived transcriptomic candidate programs. Preserve case, sample, aliquot and file identities; account for source multiplicity and ancestry; classify source-level external provenance; harmonize cancer lineages conservatively; verify raw-count representation and frozen-feature coverage; and retain the complete candidate eligibility ledger.

Notebook 113 establishes **source eligibility and technical input compatibility**, not biological replication. It does not score or refit programs, select cases using program outcomes, infer drug response or resistance, establish a causal mechanism, demonstrate individual donor independence, or authorize inferential/clinical use.

## 2. Source inputs and immutable references

- **Notebook 111:** audited GDC `CPTAC-3` source file index, primary-tumor candidates, exact case/sample/aliquot/file associations, acquisition and payload-integrity evidence. The acquisition inventory comprises 2,968 STAR Counts RNA-seq files and 2,610 SeSAMe DNA-methylation files. **Notebook 113 constructs an RNA-seq cohort only.**
- **Notebook 112:** `112_cptac3_rna_simple_primary_technical_inventory.csv` and `112_cptac3_qc_provenance_handoff.json`, authenticated against the upstream source candidates. Provider QC-metadata investigations do not establish cohort-wide independent read/library-level QC.
- **Frozen TCGA reference:** registry artifact `phase2.203.final_sample_mapping` (9,965 reference cases). Its input SHA-256 is verified before use.
- **Frozen feature reference:** registry artifact `phase4.400.cross_system_shared_gene_universe`, comprising 2,389 unique version-normalized Ensembl gene IDs. Program definitions and their orientations are not relearned here.
- **Fixed source evidence:** `docs/evidence/phase1/notebook113/113_gdc_multiplicity_pilot_v2_snapshot.json`, supporting targeted GDC source metadata and specimen multiplicity auditing.

Use versioned, fingerprinted inputs already established by the source notebooks. Reproducibility must not depend on renewed live GDC queries, changing provider metadata or undocumented local replacements.

## 3. Primary-tumor candidate universe

The audited primary-tumor RNA-seq inventory contains **1,370 cases / 1,731 uniquely resolved primary RNA files**. The primary candidate universe comprises **1,082 cases**, each represented by exactly one primary-tumor STAR Counts file, one uniquely resolved sample and one aliquot.

The remaining **288 cases / 649 primary files** are outside this universe: 276 cases / 619 files involve multiple primary samples, and 12 cases / 30 files involve multiple primary aliquots. No retrospective preferred-file selection is permitted. Secondary use would require a separate prospective, outcome-blind policy.

The source file-level audit also identifies **314 RNA files with ambiguous sample ancestry**. This is not a disjoint patient cohort. Among the 1,082 primary candidates, 37 have additional RNA files of ambiguous ancestry; retain the corresponding sensitivity flag without automatically excluding an otherwise unambiguous primary source file.

Preserve source identifiers and original `project_id`, `primary_site`, `disease_type`, filename, size and provider MD5. Keep file, sample, aliquot and case denominators distinct.

## 4. External provenance and donor-independence boundary

Use the authenticated GDC `CPTAC-3` study inventory as the source basis. The executed notebook assigns the following **separate** labels for candidates belonging to that project:

- `cohort_provenance_status = COHORT_LEVEL_EXTERNALITY_ASSUMED`
- `donor_independence_status = NOT_INDIVIDUALLY_VERIFIED`

Cohort-level externality is a qualified study-design assumption, **not genetic evidence that no individual donor appears in the TCGA discovery population**. The notebook does not perform a validated donor-level genetic crosswalk and must not be described as proving zero overlap. Different project labels or identifier namespaces alone do not establish biological independence. Any affirmative evidence of common donors requires explicit traceable review before inferential interpretation.

Source membership and eligibility rely on the audited GDC records. No PDC study-label match is required; a PDC project name must not substitute for case-level donor identity or histopathological subtyping. Decisions must be independent of downstream program scores and replication outcomes.

## 5. Cancer-lineage harmonization

Define supported mappings from the original GDC `primary_site × disease_type` context to a TCGA lineage only when the available source descriptors support the correspondence. The seven accepted lineages are TCGA-HNSC, TCGA-LUAD, TCGA-LUSC, TCGA-PAAD, TCGA-SKCM, TCGA-STAD and TCGA-UCEC; source-specific head-and-neck squamous sites contribute to HNSC.

Broad `Brain/Gliomas` labels cannot resolve GBM versus LGG, and `Kidney/Adenomas and Adenocarcinomas` cannot resolve KIRC, KIRP or KICH. These are `AMBIGUOUS`; other unsupported kidney contexts are `UNMAPPED`. Do not infer histological subtype from organ alone or from expression patterns.

Preserve `tcga_lineage`, `lineage_mapping_status`, original source context and explicit non-inclusion reasons in the complete candidate ledger.

## 6. Technical representation and feature compatibility

Authenticate Notebook 112 technical identities against the full 1,082-case candidate ledger. Require the GDC STAR Counts `unstranded` vector to contain nonnegative integer counts, zero invalid gene-count entries and no duplicate version-normalized Ensembl IDs according to the upstream technical inventory.

For source cases with `ACCEPTED` lineage mapping, inspect the local STAR Counts source files to verify the presence of all **2,389** frozen shared genes. Do not replace missing genes with zeros or symbols, select alternative features, or modify frozen program weights. The executed audit finds valid source count vectors for 1,082 primary candidates and complete frozen-feature coverage for the **727** lineage-accepted files.

This is **raw-count compatibility**, not validation of cross-platform numerical calibration, score comparability, biological structure or independent sequencing quality. Keep the read-level QC limitation as `QC_UNASSESSED`; provider MD5 agreement and raw-count suitability do not constitute a QC PASS.

## 7. Deterministic source eligibility and executed counts

A candidate is included in the proposed source cohort if and only if it:

1. Belongs to the uniquely represented 1,082-case primary source universe.
2. Has `COHORT_LEVEL_EXTERNALITY_ASSUMED` provenance.
3. Has `lineage_mapping_status = ACCEPTED` and a supported frozen TCGA lineage.
4. Has an authenticated valid `unstranded` count vector without invalid values.
5. Has `complete_feature_coverage = true` for the 2,389 shared genes.

The executed result is **727 unique cases / 727 primary RNA files**:

| TCGA lineage | Cases |
| --- | ---: |
| TCGA-HNSC | 36 |
| TCGA-LUAD | 178 |
| TCGA-LUSC | 89 |
| TCGA-PAAD | 88 |
| TCGA-SKCM | 138 |
| TCGA-STAD | 142 |
| TCGA-UCEC | 56 |
| **Total** | **727** |

Of the 1,082 candidates, **355 are not eligible**: 351 with unresolved brain/kidney subtype mappings (159 brain; 192 kidney) and four with unsupported kidney mappings. These are lineage limitations, not automatically sequencing-QC failures. The 288 multiply represented primary cases remain outside the 1,082-case candidate universe.

Persist the entire 1,082-case ledger. Use `external_cohort_eligibility`, `eligibility_reason` and exact case/file keys for traceable decisions. Reconciliation must hold between eligible ledger rows, the proposed cohort and the raw-count compatibility records. No post-outcome rescue or reselection is allowed.

## 8. Persisted outputs and handoff to Notebook 800

Notebook 113 generates **exactly four derived outputs** under `data/interim/metadata/`:

| File | Contract |
| --- | --- |
| `113_proposed_external_source_cohort.csv` | Authoritative proposed membership: 727 unique case/file/sample/aliquot identities, original source descriptors, TCGA lineage, provenance and ambiguous-ancestry flag |
| `113_primary_candidate_case_eligibility.csv` | Complete 1,082-case candidate ledger with lineage statuses, source technical evidence, QC limitation, eligibility and non-inclusion reasons |
| `113_raw_count_compatibility.csv` | 727 case/file-level records of source STAR raw-count validity and frozen 2,389-gene coverage |
| `113_source_provenance_manifest.json` | Input paths and SHA-256 values, SHA-256 and row/column counts for the three CSVs, per-lineage counts, software versions and explicit readiness flags |

Write and fingerprint the three CSVs first, then the manifest (no self-referential checksum). The manifest uses `schema_version = 1`, `source_inputs`, `derived_outputs`, `cohort` and `readiness`. Its readiness includes `cohort_frozen = false`, `external_analysis_authorized = false`, `read_level_qc_status = QC_UNASSESSED` and `cross_platform_comparability = NOT_ESTABLISHED`.

The three CSVs and manifest are locally generated products, not automatically committed/frozen registry artifacts. Notebook 800 must authenticate them by hash and exact membership before use. It must **not** reconstruct GDC source eligibility, source histology, donor provenance or the already completed matrix-level presence audit. Source payload identity/MD5 verification for files actually used downstream is a separate local-integrity requirement.

Do not introduce a second readiness JSON, duplicate lineage-count CSV, attrition CSV or unnecessary intermediate export. Retain descriptive diagnostics in the executed notebook and source evidence in the versioned provenance inputs.

## 9. Scientific interpretation and readiness

The proposed 727-case cohort has source-level GDC provenance, supported source-to-TCGA lineage mapping and compatible raw-count inputs. Individual donor independence has not been verified; independent read-level QC has not been certified; normalized expression comparability is unestablished; and purity, proliferation, immune/stromal composition and technical batch effects may confound downstream analyses.

Neither a source-cohort construction PASS nor a computable program score establishes external structural replication. Notebook 800 must separately define and review normalization, immutable program projection, non-tautological within-lineage structural estimands, negative controls, uncertainty, multiplicity and confounding/sensitivity analyses before confirmatory inference.

**Current state:** proposed source cohort; `cohort_frozen = false`; `external_analysis_authorized = false`. No independent-donor, clinical-predictor, causal or therapeutic-reversal claim is warranted.
