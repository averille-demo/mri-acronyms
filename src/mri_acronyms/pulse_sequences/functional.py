"""Functional (fMRI) pulse sequences."""

from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

FMRI_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="fmri_bold_2d_epi",
        image_weighting="PWI",
        classification="functional",
        acquisition_modes=["2d_slices"],
        description="blood oxygenation level dependent (BOLD) - gradient version most common (also SE EPI version)",
        url="https://mriquestions.com/bold-pulse-sequences.html",  # type: ignore[arg-type]
        siemens=["BOLD"],
        ge=["BOLD"],
        philips=["BOLD"],
        canon=["BOLD"],
        hitachi=["BOLD"],
    ),
    # Pulsed Arterial Spin Labeling (PASL)
    # https://mriquestions.com/pasl.html
    # Echo-Planar Imaging-based Signal Targeting by Alternating Radiofrequency (EPISTAR)
    # Proximal Inversion with Control of Off-Resonance Effects (PICORE)
    # Flow-sensitive Alternating Inversion Recovery (FAIR)
    MriSequenceModel(
        name="fmri_arterial_spin_labeling",
        image_weighting="PWI",
        classification="functional",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="arterial spin labeling (ASL) double IR pulse (with restore), followed by True-SSFP or TSE",
        url="https://mriquestions.com/asl-methods-overview.html",  # type: ignore[arg-type]
        siemens=["3D ASL", "pCASL"],
        ge=["3D ASL", "pCASL"],
        philips=["ASL Specialist"],
        canon=["ASTAR"],
        hitachi=["ASL Perfusion"],
    ),
    MriSequenceModel(
        name="fmri_vaso_3d_grase",
        image_weighting="PWI",
        classification="functional",
        acquisition_modes=["3d_volume"],
        description="vascular space occupancy (VASO)",
        url="https://radiologykey.com/vascular-space-occupancy-magnetic-resonance-imaging/",  # type: ignore[arg-type]
        siemens=["VASO"],
        ge=["VASO"],
        philips=["VASO"],
        canon=["VASO"],
        hitachi=["VASO"],
    ),
]
