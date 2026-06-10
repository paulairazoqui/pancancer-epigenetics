# Pan-Cancer Epigenetic Resistance Project — Sequential Workflow

## Phase 0 — Project Foundation

### 0.1 Define project philosophy

Objective:

* Establish scientific and computational principles.

Deliverables:

* project scope
* reproducibility policy
* interpretability policy
* version freezing policy

Files:

```text
docs/decisions/
docs/protocols/
README.md
```

Human supervision:

* Confirm that every decision is biologically justifiable.
* Avoid adding omics/features “because more is better”.

Primary AI:

* ChatGPT → architecture + scientific reasoning
* Claude → documentation polishing

---

### 0.2 Create repository architecture

Objective:

* Build stable project structure.

Deliverables:

* folder scaffold
* environment definition
* gitignore
* raw/processed separation

Human supervision:

* Confirm folder clarity for future collaborators.
* Ensure repo remains understandable for non-bioinformaticians.

Primary AI:

* ChatGPT
* Codex (optional for refactoring)

---

### 0.3 Define data governance

Objective:

* Freeze dataset versions.

Deliverables:

* release definitions
* manifests
* SHA256 hashes
* provenance documentation

Human supervision:

* Verify every release manually.
* Ensure exact filenames are documented.

Primary AI:

* ChatGPT
* Claude

---

# Phase 1 — Data Acquisition

## 1.1 Download public datasets

Objective:

* Acquire reproducible raw datasets.

Datasets:

* DepMap 25Q3
* GDSC 8.5

Deliverables:

```text
data/raw/
data/interim/qc/download_manifest.json
```

Human supervision:

* Verify file sizes.
* Verify hashes.
* Verify no corrupted downloads.
* Verify release names.

Primary AI:

* ChatGPT
* Codex

---

## 1.2 Audit dataset structure

Objective:

* Confirm datasets are readable and internally consistent.

Checks:

* shapes
* columns
* missingness
* IDs
* duplicated keys

Deliverables:

```text
01_dataset_inventory.ipynb
```

Human supervision:

* Identify suspicious IDs.
* Detect weird duplicated models.
* Detect inconsistent naming.

Primary AI:

* ChatGPT

---

# Phase 2 — Identifier Mapping & Integration Planning

## 2.1 Define integration keys

Objective:

* Determine stable identifiers.

Current decisions:

```text
ModelID
SangerModelID
SequencingID
```

Deliverables:

```text
001_data_integration_strategy.md
```

Human supervision:

* Confirm biological meaning of identifiers.
* Avoid merges based on cell line names.

Primary AI:

* ChatGPT

---

## 2.2 Build mapping tables

Objective:

* Create canonical mapping tables.

Tasks:

* ModelID ↔ SangerModelID
* ModelID ↔ ProfileID
* ModelID ↔ SequencingID

Deliverables:

```text
master_model_mapping.parquet
```

Human supervision:

* Inspect duplicated mappings.
* Validate one-to-many relationships.

Primary AI:

* ChatGPT
* Codex

---

## 2.3 Coverage analysis

Objective:

* Determine usable overlap.

Tasks:

* overlap RNA ↔ GDSC
* overlap mutations ↔ GDSC
* overlap cancer types
* overlap drug coverage

Deliverables:

```text
02_coverage_analysis.ipynb
```

Human supervision:

* Detect underrepresented tumor types.
* Decide minimum sample thresholds.

Primary AI:

* ChatGPT

---

# Phase 3 — Transcriptomic Processing

## 3.1 Expression preprocessing

Objective:

* Generate ML-ready transcriptomic matrix.

Tasks:

* keep canonical RNA profiles
* remove metadata columns
* handle duplicated genes
* inspect low-variance genes

Deliverables:

```text
expression_matrix.parquet
```

Human supervision:

* Verify no accidental sample leakage.
* Verify gene counts remain biologically realistic.

Primary AI:

* ChatGPT
* Codex

---

## 3.2 Transcriptomic QC

Objective:

* Evaluate transcriptomic structure.

Tasks:

* PCA
* UMAP
* clustering
* outlier detection
* batch inspection

Deliverables:

```text
03_expression_qc.ipynb
```

Human supervision:

* Detect technical artifacts.
* Detect impossible biological clusters.

Primary AI:

* ChatGPT
* Perplexity (literature comparison)

---

# Phase 4 — Mutation Processing

## 4.1 Mutation filtering

Objective:

* Reduce raw variant complexity.

Tasks:

* select canonical WGS profiles
* keep coding variants
* remove low-confidence variants
* annotate drivers

Deliverables:

```text
filtered_mutations.parquet
```

Human supervision:

* Verify filtering logic biologically.
* Avoid overly aggressive filtering.

Primary AI:

* ChatGPT
* Perplexity

---

## 4.2 Mutation feature engineering

Objective:

* Create interpretable mutation features.

Possible features:

* TP53 mutated
* KRAS mutated
* DNA repair burden
* pathway mutation burden
* hotspot mutations

Deliverables:

```text
mutation_features.parquet
```

Human supervision:

* Ensure features remain explainable.
* Avoid generating thousands of meaningless sparse features.

Primary AI:

* ChatGPT

---

# Phase 5 — Drug Response Processing

## 5.1 GDSC preprocessing

Objective:

* Clean pharmacologic response matrix.

Tasks:

* remove duplicated experiments
* inspect LN_IC50 distribution
* inspect AUC distribution
* standardize drug names

Deliverables:

```text
gdsc_cleaned.parquet
```

Human supervision:

* Detect impossible IC50 values.
* Detect duplicated drug aliases.

Primary AI:

* ChatGPT

---

## 5.2 Drug coverage analysis

Objective:

* Identify drugs suitable for modeling.

Tasks:

* sample count per drug
* missingness
* tissue distribution
* response variability

Deliverables:

```text
04_drug_coverage.ipynb
```

Human supervision:

* Avoid low-sample drugs initially.
* Avoid highly imbalanced response distributions.

Primary AI:

* ChatGPT

---

# Phase 6 — Integrated Modeling Dataset

## 6.1 Build master integrated dataset

Objective:

* Merge transcriptomics + mutations + pharmacology.

Core structure:

```text
sample × drug
```

Deliverables:

```text
master_modeling_dataset.parquet
```

Human supervision:

* Validate merge counts carefully.
* Confirm no silent row explosions.

Primary AI:

* ChatGPT
* Codex

---

## 6.2 Define resistance labels

Objective:

* Define prediction targets.

Recommended strategy:

* continuous modeling first
* no binary resistant/sensitive threshold initially

Targets:

* LN_IC50
* AUC

Human supervision:

* Inspect target distributions.
* Detect outlier drugs.

Primary AI:

* ChatGPT

---

# Phase 7 — Baseline Machine Learning

## 7.1 Baseline interpretable models

Objective:

* Establish robust baseline performance.

Models:

* Elastic Net
* Random Forest
* XGBoost

Deliverables:

```text
baseline_model_results.csv
```

Metrics:

* RMSE
* MAE
* Spearman correlation
* R²

Human supervision:

* Detect overfitting.
* Ensure proper train/test splitting.

Primary AI:

* ChatGPT
* Codex

---

## 7.2 Cross-validation strategy

Objective:

* Build biologically realistic evaluation.

Preferred:

* grouped CV
* tissue-aware CV

Human supervision:

* Avoid data leakage.
* Avoid train/test overlap through replicated models.

Primary AI:

* ChatGPT

---

# Phase 8 — Explainability & Biomarker Discovery

## 8.1 SHAP analysis

Objective:

* Identify interpretable biomarkers.

Tasks:

* global SHAP
* local SHAP
* pathway enrichment

Deliverables:

```text
shap_analysis/
```

Human supervision:

* Reject biologically nonsensical biomarkers.
* Compare with literature.

Primary AI:

* ChatGPT
* Perplexity

---

## 8.2 Resistance signature discovery

Objective:

* Identify transcriptomic signatures.

Tasks:

* differential expression
* pathway enrichment
* gene set scoring

Deliverables:

```text
resistance_signatures/
```

Human supervision:

* Verify pathway plausibility.
* Avoid overinterpretation.

Primary AI:

* ChatGPT
* Perplexity
* Claude (writing)

---

# Phase 9 — Target Prioritization

## 9.1 Target ranking

Objective:

* Prioritize candidate therapeutic targets.

Inputs:

* SHAP importance
* mutation burden
* pathway relevance
* literature evidence

Deliverables:

```text
target_ranking.csv
```

Human supervision:

* Reject targets lacking biological plausibility.
* Verify cancer relevance.

Primary AI:

* ChatGPT
* Perplexity

---

# Phase 10 — Drug Repurposing

## 10.1 Transcriptomic reversal

Objective:

* Identify drugs reversing resistance signatures.

Resources:

* LINCS L1000
* CMap

Deliverables:

```text
repurposing_candidates.csv
```

Human supervision:

* Validate mechanism coherence.
* Reject contradictory candidates.

Primary AI:

* ChatGPT
* Perplexity

---

## 10.2 Multi-evidence prioritization

Objective:

* Rank repurposing candidates.

Evidence:

* transcriptomic reversal
* target overlap
* pathway correction
* literature support

Human supervision:

* Avoid ranking purely statistical hits.
* Prioritize mechanistic coherence.

Primary AI:

* ChatGPT
* Perplexity
* Claude

---

# Phase 11 — External Validation

## 11.1 TCGA validation

Objective:

* Validate findings in patient cohorts.

Tasks:

* external expression validation
* mutation validation
* survival association

Deliverables:

```text
tcga_validation/
```

Human supervision:

* Verify cohort comparability.
* Avoid overclaiming clinical translatability.

Primary AI:

* ChatGPT
* Perplexity

---

# Phase 12 — Publication & Deployment

## 12.1 Publication preparation

Objective:

* Build publication-ready outputs.

Deliverables:

* figures
* tables
* methods
* supplementary data

Primary AI:

* Claude
* ChatGPT

---

## 12.2 Public release

Objective:

* Make project reproducible.

Deliverables:

* GitHub repository
* processed datasets
* manifests
* reproducibility guide

Optional:

* Streamlit app
* dashboard

Human supervision:

* Verify all paths run from clean clone.
* Verify README reproducibility.

Primary AI:

* ChatGPT
* Codex
* Claude
