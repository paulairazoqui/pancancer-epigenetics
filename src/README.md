# src

`src/` contains shared, reusable Python source code for the pancancer epigenetics project.

Roadmap v3.0 phase work now lives in notebooks, configuration, and data artifacts rather than phase-mirrored source folders. Keep this tree limited to modules that are intended to be imported by multiple workflows, such as `src/utils/paths.py`.

Data acquisition source-of-truth metadata lives in `config/raw_data_registry.json`; Phase 1 inventory and audit workflows should use that registry plus the corresponding notebooks instead of standalone download scripts under `src/`.
