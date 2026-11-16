import pandas as pd

from pancancer_epigenetics.utils.pharmacology_identity import (
    eligible_model_ids,
    excluded_model_mask,
)


def test_pair_exclusion_is_specific_to_the_model_sanger_pair():
    models = pd.DataFrame(
        {
            "ModelID": ["ACH-000837", "ACH-002172", "ACH-OTHER"],
            "SangerModelID": ["SIDM00117", "SIDM00117", "SIDM-OTHER"],
        }
    )
    exclusions = pd.DataFrame(
        {
            "ModelID": ["ACH-000837"],
            "SangerModelID": ["SIDM00117"],
            "reason": ["identity_mismatch_nci_h322_vs_nci_h322m"],
        }
    )

    assert eligible_model_ids(
        models,
        {"SIDM00117", "SIDM-OTHER"},
        exclusions,
    ) == {"ACH-002172", "ACH-OTHER"}
    assert excluded_model_mask(models, exclusions).tolist() == [True, False, False]
