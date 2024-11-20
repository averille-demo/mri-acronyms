"""Spectroscopy (SPECT) pulse sequences.

Analyze chemical composition of tissues in very small number of much larger voxels
https://mriquestions.com/mri-vs-mrs.html
https://www.imaios.com/en/e-mri/magnetic-resonance-spectroscopy/single-voxel-spectroscopy
"""

from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

SPECT_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="point_resolved_spectroscopy",
        image_weighting="MRS",
        classification="spectroscopy",
        acquisition_modes=["voxel"],
        description="dominant method used for ¹H spectroscopy",
        url="https://mriquestions.com/press.html",  # type: ignore[arg-type]
        siemens=["PRESS"],
        ge=["PRESS"],
        philips=["PRESS"],
        canon=["PRESS"],
        hitachi=["PRESS"],
    ),
    MriSequenceModel(
        name="stimulated_echo_acquisition_mode",
        image_weighting="MRS",
        classification="spectroscopy",
        acquisition_modes=["voxel"],
        description="stimulated echoes are a particular type of MR signal by a series of 3+ RF pulses",
        url="https://mriquestions.com/steam.html",  # type: ignore[arg-type]
        siemens=["STEAM"],
        ge=["STEAM"],
        philips=["STEAM"],
        canon=["STEAM"],
        hitachi=["STEAM"],
    ),
    MriSequenceModel(
        name="image_selected_in_vivo_spectroscopy",
        image_weighting="MRS",
        classification="spectroscopy",
        acquisition_modes=["voxel"],
        description="Image-Selected In vivo Spectroscopy (ISIS) single voxel spectroscopy (SVS)",
        url="https://mriquestions.com/isis.html",  # type: ignore[arg-type]
        siemens=["ISIS"],
        ge=["ISIS"],
        philips=["ISIS"],
        canon=["ISIS"],
        hitachi=["ISIS"],
    ),
    MriSequenceModel(
        name="chemical_shift_imaging",
        image_weighting="MRS",
        classification="spectroscopy",
        acquisition_modes=["voxel"],
        description="multi-voxel techniques that utilize phase-encoding for spatial localization",
        url="https://mriquestions.com/csi.html",  # type: ignore[arg-type]
        siemens=["CSI"],
        ge=["PROBE CSI"],
        philips=["Spectroscopy"],
        canon=["CSI"],
        hitachi=["CSI"],
    ),
]
