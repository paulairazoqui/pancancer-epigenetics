# Reproduction environments

`requirements.txt` is the curated, exact-pinned direct Python dependency
contract for the implemented workflow. Install it with `python -m pip install
-r requirements.txt`, then install this repository with `python -m pip install
-e .` when the local package is needed.

`environment.yml` provides the same direct Python package contract in a Conda
environment named `pancancer-epigenetics`; its Python pin matches the captured
project environment. `python_environment_snapshot.txt` is a full `pip freeze
--all --exclude-editable` capture of that current project environment. It can
contain transitive and unrelated installed packages, so it is not the minimal
contract.

R requirements are explicitly scoped rather than represented by one manifest:

- `r_environment_r43_bioc318.json` supports
  `scripts/r/205_tcga_rnaseq_tmm_logcpm.R` and
  `scripts/r/export_hm450_probe_annotation.R` (R 4.3.1, Bioconductor 3.18,
  edgeR 4.0.16, rhdf5 2.46.1, minfi 1.48.0, and
  IlluminaHumanMethylation450kanno.ilmn12.hg19 0.6.1).
- `r_environment_phase4b_451.json` supports
  `scripts/phase4b/export_sesamedata_hm450_hg38_annotation.R` (R 4.6.1,
  Bioconductor 3.23, and sesameData 1.30.0). Its additional listed namespaces
  are required by the script, but their exact versions were not preserved and
  are intentionally not claimed.

These are reproduction requirements, not claims that every historical R
execution used the same environment. From the repository root, run the
appropriate script with `Rscript scripts/r/205_tcga_rnaseq_tmm_logcpm.R`,
`Rscript scripts/r/export_hm450_probe_annotation.R`, or
`Rscript scripts/phase4b/export_sesamedata_hm450_hg38_annotation.R` after
installing the corresponding R/Bioconductor requirements. The Phase 4B export
requires access to its Bioconductor/ExperimentHub annotation resources.

`historical/phase2_205_tmm_session_info.txt` is a byte-faithful preservation of
the existing file at the exact output path used by `scripts/r/205_tcga_rnaseq_tmm_logcpm.R`.
It is historical execution evidence for notebook 205 only, not for the HM450
annotation export. Current reproduction environments are not exact historical
environments unless direct evidence says otherwise.
