# pancancer-epigenetics

A lineage-aware computational oncology framework for discovering recurrent epigenetic-transcriptomic programs across diverse malignancies and evaluating their secondary molecular context, computational associations with resistance-like pharmacogenomic contexts, candidate functional vulnerabilities, explainable predictive-model behavior, perturbational hypotheses, and integrated program–vulnerability–compound evidence.

---

## Project Overview

This repository integrates high-throughput multi-omic, somatic-genomic, pharmacogenomic, functional-dependency, perturbational-transcriptomic, and drug–target knowledgebase resources to identify and characterize recurrent biological patterns across heterogeneous tumor and *in vitro* models.

### Core Data Integration

* **Primary tumors:** The Cancer Genome Atlas (TCGA) RNA-seq, DNA methylation, and planned somatic-mutation context
* **Cancer cell models and functional genomics:** Cancer Dependency Map (DepMap) / Cancer Cell Line Encyclopedia (CCLE)
* **Pharmacogenomics and XAI:** GDSC, CTRP, and PRISM
* **Perturbational profiles:** LINCS L1000 / Connectivity Map (CMap)
* **Drug–target context:** curated resources such as ChEMBL and DrugBank where accessible

The framework emphasizes biological interpretability, data leakage prevention, reproducible data provenance, lineage-aware evaluation, explainable modeling, cross-dataset replication, transparent evidence integration, and conservative scientific framing.

The broader approved scientific project includes experimental validation. Experimental work is intentionally outside this computational repository; the repository generates reproducible hypotheses and frozen evidence handoffs that may support downstream experimental evaluation.

---

## Current Project Status

- **Phase 2 — Independent Tumor Discovery:** closed / frozen with 9,965 TCGA primary-tumor cases and 13 retained candidate cross-omic programs.
- **Phase 3 — Independent Cell-Line Discovery:** closed with 713 DepMap–GDSC models; latent-program extraction was phenotype-independent and internal robustness was completed in notebook 311.
- **Phase 4 — Cross-System Integration:** closed / frozen. Notebooks 400–404 completed cross-system comparison, consensus construction, cross-lineage robustness, epigenetic-regulator enrichment, and biological program annotation without downstream redefinition of the frozen consensus representations.
- **Phase 4B — Secondary Molecular Context Characterization:** planned. Notebook 450 will characterize somatic genomic context after a dataset-specific TCGA mutation audit in planned notebook 108; notebook 451 will characterize locus-level methylation-expression relationships. This layer cannot redefine frozen Phase 4 programs and may yield positive, lineage-specific, heterogeneous, or negative results.
- **Phase 5 — Functional Vulnerabilities:** active. Notebook 500 — CRISPR Associations remains complete/frozen; the RNAi acquisition/audit prerequisite is complete, with 443 frozen models available for RNAi analysis. Notebook 501 — RNAi Associations is next.
- **Phase 6 — Pharmacogenomic Contexts and Explainable Modeling (XAI):** planned. This is the explicit XAI layer, including lineage-aware predictive modeling, SHAP attribution, stability analysis, and cross-screen replication.
- **Phase 7 — Perturbational Hypotheses:** planned.
- **Phase 8 — Orthogonal Validation:** planned.
- **Phase 9 — Integrated Evidence Synthesis and Therapeutic Prioritization:** planned.
- **Phase 10 — Manuscript Preparation:** planned.

---

## Scientific Scope

The project is designed to generate computational associations, secondary molecular-context results, explainable model-attribution results, and candidate hypotheses. It does **not** aim to:

* support clinical prediction or patient-outcome prediction,
* infer causal mechanisms from observational data,
* establish validated targets or definitive biomarkers,
* claim translational efficacy from in silico analyses, or
* reconstruct longitudinal, adaptive, or clonal drug-resistance trajectories.

> [!NOTE]
> Outputs from this repository should be interpreted as computational associations, secondary genomic or methylation-expression context, explainable model attributions, putative-vulnerability hypotheses, perturbational hypotheses, and integrated evidence for prioritization. They require downstream validation before biological or translational claims are made.

---

## Secondary Molecular Context Characterization

Roadmap v3.2 adds a post-freeze **Phase 4B** to close two explicit computational components of the approved project without reopening discovery.

Notebook `450 — Secondary Genomic Context Characterization` will test whether frozen tumor/consensus program scores are associated with recurrent somatic mutation contexts using a single audited TCGA/GDC mutation resource. Project/lineage structure, mutation prevalence, caller/workflow provenance, and multiple testing remain explicit. Somatic mutations are contextual evidence, not a new program-discovery modality.

Notebook `451 — Locus-Level Methylation–Expression Characterization` will map relevant CpGs to genes and promoter/regulatory annotations and characterize locus-level methylation-expression relationships, including inverse promoter methylation-expression patterns where supported. Such relationships are compatible with regulatory coupling but do not establish causal epigenetic regulation.

Neither notebook may rescue, exclude, reweight, reorient, rename, or redefine frozen Phase 4 programs. Negative or non-recurrent results are valid, and Phase 4B findings are not required to appear in a manuscript.

---

## Role of Explainable Artificial Intelligence

Explainable artificial intelligence is an explicit scientific component of the repository rather than a manuscript-only interpretation step.

Phase 6 operationalizes XAI only after pharmacogenomic outcomes, evaluation partitions, and model inputs have been defined under leakage controls. Notebook 601 performs explainable predictive modeling; notebook 602 is dedicated to SHAP attribution and stability analysis; notebook 603 evaluates cross-screen replication.

SHAP is treated as a model-attribution method. It is interpreted jointly with predictive validity, lineage structure, resampling stability, model-class sensitivity, and cross-screen evidence. SHAP values are not interpreted as causal biological effects, validated biomarkers, or therapeutic targets.

---

## Repository and Notebook Structure

The repository contains implemented directories through the active Phase 5 workflow and planned placeholders for downstream phases. Roadmap v3.2 additionally adds a Phase 4B characterization directory while preserving the numbering of all established downstream phases.

```text
├── .github/workflows/     # Data-free continuous-integration checks
├── config/                # Paths plus raw-data and derived-artifact registries
├── data/                  # Immutable raw data and reproducible derived data tiers
│   ├── raw/               # Source-dataset folders such as depmap, gdsc, tcga, lincs
│   ├── interim/           # Harmonized analysis-ready inputs, metadata, genomics, and QC artifacts
│   └── processed/         # Program, secondary-characterization, vulnerability, context, validation, and integrated-evidence outputs
├── docs/                  # Project direction, architecture, policy, terminology, and workflow docs
├── envs/                  # Current reproduction-environment records and historical evidence
├── notebooks/             # Implemented notebooks plus planned-phase placeholders
├── results/               # Manuscript-ready figures and tables by paper/supplement
├── src/                   # Reusable source code and path helpers
└── tests/                 # Automated contract tests and test documentation
```

Publication-facing outputs belong under `results/paper1/`, `results/paper2/`, and `results/supplementary/`, each with `figures/` and `tables/` subfolders.

Pipeline-intermediate outputs should remain under `data/interim/` or `data/processed/`.

---

## Data Organization

Raw source datasets are stored by source under:

```text
data/raw/
```

Derived data are separated into two levels:

```text
data/interim/
```

for harmonized, analysis-ready, notebook-consumable artifacts, and:

```text
data/processed/
```

for stable biological entities or analytical outputs generated by the framework.

The intended structure is:

```text
data/interim/
├── metadata/
├── expression/
├── methylation/
├── genomics/
├── dependencies/
├── pharmacology/
├── perturbational/
└── qc/

data/processed/
├── tumor_programs/
├── cellline_programs/
├── consensus_programs/
├── secondary_characterization/
├── functional_vulnerabilities/
├── pharmacogenomic_contexts/
├── perturbational_hypotheses/
├── validation/
└── integrated_evidence/
```

Large raw and derived data files are not version-controlled. Directory structure is preserved using `.gitkeep` placeholders.

---

## Environment Setup

The current captured reproduction environment uses **Python 3.11.8**.

`requirements.txt` is the direct dependency contract with exact pins, and `envs/environment.yml` represents the same contract. `envs/python_environment_snapshot.txt` records the complete captured Python environment, including transitive packages. These current reproduction records do not establish that every historical analysis ran under exactly the same software environment; see `envs/README.md` for scope and historical execution evidence.

Create a local Python virtual environment using `venv`, activate it, and then install the project dependencies. From the repository root:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Reproducing the Repository Workflow

A minimal reproducibility sequence is:

1. Clone the repository.
2. Create and activate the local `.venv` using Python 3.11.8.
3. Install the dependencies from `requirements.txt` and install the repository package in editable mode with `python -m pip install -e .`.
4. Download or place raw datasets into the appropriate `data/raw/<source>/` folders according to `config/raw_data_registry.json`.
5. Run the Phase 1 notebooks to confirm source availability and raw-file auditing.
6. Execute implemented notebooks in numerical order within the completed or active phases. Future notebooks are run only after their required inputs are available and frozen.

The implemented notebook series are `100`–`107`, `200`–`206`, `300`–`311`, `400`–`404`, and `500`. The planned roadmap v3.2 series additionally include `108`, `450`–`451`, `501`–`502`, `600`–`603`, `700`–`703`, `800`–`804`, `900`–`904`, and `1000`–`1004`.

The physical notebook layout is:

```text
notebooks/
├── phase0_infrastructure_and_reproducibility/
├── phase1_data_acquisition_and_auditing/           # implemented through 107; 108 planned
├── phase2_tumor_discovery_layer/
├── phase3_cell_line_discovery_layer/
├── phase4_consensus_programs/                      # complete through notebook 404
├── phase4b_secondary_molecular_characterization/   # planned notebooks 450–451
├── phase5_functional_vulnerabilities/              # active; complete through notebook 500; 501 next
├── phase6_pharmacogenomic_contexts/                # planned; includes explicit XAI notebooks 601–602
├── phase7_perturbational_hypotheses/               # planned
├── phase8_orthogonal_validation/                   # planned
├── phase9_integrated_evidence_and_prioritization/  # planned
└── phase10_manuscript_preparation/                 # planned
```

Raw data files are expected to remain unchanged after acquisition. Derived files should be regenerated into `data/interim/` or `data/processed/` according to the notebook logic.

---

## Documentation Map

The current roadmap v3.2 source-of-truth documents are:

* `roadmap.md` — operational analysis phases, manuscript milestones, and approved repository architecture.
* `docs/PROJECT_DIRECTION.md` — strategic biological objective, secondary characterization, explicit XAI role, and conservative scientific scope.
* `docs/PROJECT_ARCHITECTURE.md` — analytical layers, dataset roles, Phase 4B placement, XAI placement, evidence integration, and lineage-aware framework design.
* `docs/DATA_HARMONIZATION_PLAN.md` — identifier harmonization, data integration, and leakage-prevention principles.
* `docs/MODELING_POLICY.md` — modeling boundaries, secondary molecular-context rules, leakage prevention, XAI/SHAP requirements, evidence-integration policy, and interpretation rules.
* `docs/TERMINOLOGY_GUIDE.md` — approved terminology for candidate vulnerabilities, resistance-like contexts, perturbational hypotheses, and validation language.
* `docs/workflow.md` — current roadmap v3.2 operational workflow, including completed-phase boundaries and planned handoffs.
* `docs/decisions/004_secondary_molecular_context_characterization.md` — durable decision establishing notebooks 108, 450, and 451 and their freeze boundaries.

---

## Reproducibility & Rigor

* **Data immutability:** Files within `data/raw/` must remain unmodified after acquisition.
* **Deterministic derived data:** Outputs in `data/interim/` and `data/processed/` should be reproducible from raw source files using version-controlled code, notebooks, and environment definitions.
* **Raw-data provenance:** `config/raw_data_registry.json` records source datasets, releases, file locations, and audit summaries; `data/interim/qc/` contains relevant tracked audit outputs.
* **Derived-artifact lineage:** `config/artifact_registry.json` records the frozen identity and lineage of registered derived artifacts.
* **Current reproduction environment:** `envs/environment.yml`, `envs/python_environment_snapshot.txt`, and `envs/r_environment.json` record the current reproduction environment; `envs/README.md` distinguishes these records from historical execution evidence where it exists.
* **Leakage prevention:** Analyses should avoid naïve pan-cancer pooling, random cross-lineage splits, post-split feature leakage, cell-line overlap leakage, platform leakage, drug-family leakage, and downstream-result feedback into frozen discovery objects.
* **Secondary characterization discipline:** mutation and locus-level methylation-expression analyses are post-freeze contextual analyses; lineage/project structure, platform/caller provenance, purity, annotation uncertainty, and negative results remain explicit.
* **XAI discipline:** SHAP and related attributions require valid evaluation design and are interpreted as model behavior, not biological causality.
* **Evidence integration:** Phase 9 preserves the provenance and distinct evidentiary role of each modality rather than collapsing heterogeneous results into an opaque score.
* **Conservative interpretation:** Results should be described as recurrent epigenetic-transcriptomic programs, secondary genomic contexts, locus-level methylation-expression associations, resistance-like pharmacogenomic contexts, putative functional vulnerabilities, explainable model attributions, perturbational hypotheses, integrated evidence, or computational associations according to the evidence level.
