"""Echo Planar (EP) pulse sequences."""

from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

EPI_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="apparent_diffusion_coefficient_map",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="measure of the magnitude of diffusion of water in tissue",
        url="https://radiopaedia.org/articles/apparent-diffusion-coefficient-1?lang=us",  # type: ignore[arg-type]
        siemens=["ADC"],
        ge=["ADC"],
        philips=["ADC"],
        canon=["ADC"],
        hitachi=["ADC"],
    ),
    MriSequenceModel(
        name="diffusion_weighted_imaging",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="measure motion of water molecules within a voxel of tissue using single-shot echo-planar",
        url="https://mriquestions.com/making-a-dw-image.html",  # type: ignore[arg-type]
        siemens=["DWI"],
        ge=["DWI"],
        philips=["DWI"],
        canon=["DWI"],
        hitachi=["DWI"],
    ),
    MriSequenceModel(
        name="diffusion_weighted_imaging_readout_segmented",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="readout segmentation of long variable echo trains to reduce susceptibility artifacts",
        url="https://mriquestions.com/readout-segmented-dwi.html",  # type: ignore[arg-type]
        siemens=["RESOLVE"],
        ge=["PROPELLER DWI"],
        philips=["DWI with segmented EPI"],
        canon=["FASE DWI"],
        hitachi=["RADAR DWI"],
    ),
    MriSequenceModel(
        name="diffusion_tensor_imaging",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="uses anisotropic diffusion (> 6 directions) to estimate white matter organization of brain",
        url="https://radiopaedia.org/articles/" + "diffusion-tensor-imaging-and-fibre-tractography",  # type: ignore[arg-type]
        siemens=["DTI", "MDDW"],
        ge=["DTI"],
        philips=["DTI"],
        canon=["DTI"],
        hitachi=["DTI"],
    ),
    MriSequenceModel(
        name="echo_planar_imaging",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="multiple echoes of different phase steps are acquired using rephasing gradients",
        url="https://mriquestions.com/echo-planar-imaging.html",  # type: ignore[arg-type]
        siemens=["EPI"],
        ge=["EPI"],
        philips=["EPI"],
        canon=["EPI"],
        hitachi=["EPI"],
    ),
    MriSequenceModel(
        name="fiber_tracking",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="3D reconstruction technique of DTI acquisition",
        url="https://radiopaedia.org/articles/" + "diffusion-tensor-imaging-and-fibre-tractography",  # type: ignore[arg-type]
        siemens=["DTI Tractography", "Tractography"],
        ge=["FiberTrak", "fiber", "tracking"],
        philips=["FiberTrak", "Trak"],
        canon=["DTT"],
        hitachi=["DTI Tractography"],
    ),
    MriSequenceModel(
        name="turbo_gradient_spin_echo",
        image_weighting="DWI",
        classification="echo_planar",
        acquisition_modes=["2d_slices"],
        description="hybrid technique: combined spin and gradient echo pulse sequence",
        url="https://mriquestions.com/grase.html",  # type: ignore[arg-type]
        siemens=["TurboGSE", "TGSE"],
        ge=[],
        philips=["GRASE"],
        canon=["Hybrid EPI"],
        hitachi=[],
    ),
]
