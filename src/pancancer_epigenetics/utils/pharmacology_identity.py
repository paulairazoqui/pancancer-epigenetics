"""Identifier-pair eligibility checks for pharmacology integration."""

from pathlib import Path

import pandas as pd


PAIR_COLUMNS = ["ModelID", "SangerModelID"]


def load_pair_exclusions(path: Path) -> pd.DataFrame:
    """Load and validate the explicit ModelID--SangerModelID exclusions."""
    exclusions = pd.read_csv(path, dtype=str)
    required_columns = [*PAIR_COLUMNS, "reason"]
    missing_columns = set(required_columns).difference(exclusions.columns)
    if missing_columns:
        raise ValueError(
            "Pair-exclusion manifest is missing columns: "
            f"{sorted(missing_columns)}"
        )
    if exclusions[PAIR_COLUMNS].isna().any().any():
        raise ValueError("Pair-exclusion manifest contains missing identifiers.")
    if exclusions.duplicated(PAIR_COLUMNS).any():
        raise ValueError("Pair-exclusion manifest contains duplicate pairs.")
    return exclusions[required_columns].copy()


def eligible_model_ids(
    models: pd.DataFrame,
    available_sanger_ids: set[str],
    exclusions: pd.DataFrame,
) -> set[str]:
    """Return models with an available, non-excluded pharmacology pairing."""
    missing_columns = set(PAIR_COLUMNS).difference(models.columns)
    if missing_columns:
        raise ValueError(
            f"Model table is missing columns: {sorted(missing_columns)}"
        )

    candidates = models.loc[
        models["SangerModelID"].isin(available_sanger_ids),
        PAIR_COLUMNS,
    ].copy()
    excluded_pairs = pd.MultiIndex.from_frame(exclusions[PAIR_COLUMNS])
    candidate_pairs = pd.MultiIndex.from_frame(candidates[PAIR_COLUMNS])
    return set(candidates.loc[~candidate_pairs.isin(excluded_pairs), "ModelID"])


def excluded_model_mask(
    models: pd.DataFrame,
    exclusions: pd.DataFrame,
) -> pd.Series:
    """Return a row-aligned mask for explicitly excluded identifier pairs."""
    model_pairs = pd.MultiIndex.from_frame(models[PAIR_COLUMNS])
    excluded_pairs = pd.MultiIndex.from_frame(exclusions[PAIR_COLUMNS])
    return pd.Series(model_pairs.isin(excluded_pairs), index=models.index)
