# Repository-Wide Language Normalization Audit

## Scope

This audit reviewed repository-facing prose and runtime text for Spanish-language content across:

- Python docstrings, comments, logging messages, and user-facing output strings.
- YAML and configuration comments.
- Markdown documentation.
- Jupyter notebook markdown cells.
- Repository metadata and ignore-rule comments.

The audit preserved code logic, file and directory structure, identifiers, dataset column names, and project-defined scientific terminology.

## Files Containing Spanish Text

The audit identified Spanish text in the following files:

- `.gitignore`
- `docs/README.md`
- `docs/MODELING_POLICY.md`
- `src/README.md`
- `src/phase1_download/download_public_datasets.py`
- `tests/README.md`
- `results/README.md`
- `notebooks/README.md`
- `docs/scaffold_manifest.json` (official institution proper name; left unchanged pending owner confirmation)

## Suggested Modifications by File

### `.gitignore`

- Translate Spanish section comments for raw/processed data, serialized models, environments, and audit-manifest exceptions.

### `docs/README.md`

- Translate the repository documentation summary into English.

### `docs/MODELING_POLICY.md`

- Remove Spanish editorial drafting notes preceding the confounder-control policy section while preserving the policy content itself.

### `src/README.md`

- Translate the source-code directory description into English.

### `src/phase1_download/download_public_datasets.py`

- Translate the module docstring from Spanish to English.
- Translate runtime logging messages and validation errors from Spanish to English.
- Preserve dataset keys, status strings, command-line arguments, and program behavior.

### `tests/README.md`

- Translate the test-directory description into English.

### `results/README.md`

- Translate the generated-output directory description into English.

### `notebooks/README.md`

- Translate the notebook-directory description into English.

## Unified Diff Patch Availability

The repository changes are represented as standard unified diffs in the version-control patch for this commit. The patch only modifies repository-facing prose and user-facing/runtime text; it does not alter computational logic.

## Notebook Markdown Cell Review

Notebook markdown cells were reviewed separately from code-cell outputs and embedded image data. No Spanish-language notebook markdown cells were identified beyond the translated top-level `notebooks/README.md` directory documentation.

## Mixed-Language Files Requiring Manual Review

- `docs/scaffold_manifest.json` contains the institution value `Universidad Nacional del Sur`. This appears to be an official proper name rather than translatable repository prose, so it was intentionally left unchanged and should be manually confirmed by the project owner.

No other mixed-language files requiring manual review were identified after normalization.
