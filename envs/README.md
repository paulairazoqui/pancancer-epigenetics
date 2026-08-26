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

`r_environment.json` records the current R environment queried for the
versioned R scripts. It is a current reproduction environment manifest, not a
claim about every historical execution.

`historical/phase2_205_tmm_session_info.txt` is a byte-faithful preservation of
the existing file at the exact output path used by `scripts/r/205_tcga_rnaseq_tmm_logcpm.R`.
It is historical execution evidence only for that Phase 2 R execution. No
historical package-version evidence for the HM450 annotation export was found;
the historical exact package version is unavailable. Current reproduction
environments are not exact historical environments unless direct evidence says
otherwise.
