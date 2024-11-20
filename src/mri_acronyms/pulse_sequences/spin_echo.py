"""Spin echo (SE) pulse sequences."""

from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

SE_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="spin_echo",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="single echo measured during each TR by (1) 90 degree excitation and (1) 180 refocusing pulse",
        url="https://mriquestions.com/spin-echo1.html",  # type: ignore[arg-type]
        siemens=["SE"],
        ge=["SE"],
        philips=["SE"],
        canon=["SE"],
        hitachi=["SE"],
    ),
    MriSequenceModel(
        name="turbo_spin_echo",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="multiple 180 RF refocusing pulses to rapidly fill k-space (acquisition time: order of minutes)",
        url="https://www.mriquestions.com/what-is-fsetse.html",  # type: ignore[arg-type]
        siemens=["TSE", "Turbo"],
        ge=["FastSE", "FSE"],
        philips=["TSE"],
        canon=["FastSE"],
        hitachi=["FastSE"],
    ),
    MriSequenceModel(
        name="single_shot_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="fast T2-weighted images acquired in single shot (1 slice per acquisition)",
        url="https://mriquestions.com/hastess-fse.html",  # type: ignore[arg-type]
        siemens=["HASTE"],
        ge=["Single-Shot FSE"],
        philips=["Single-Shot TSE"],
        canon=["FASE"],
        hitachi=["Single-Shot FSE"],
    ),
    MriSequenceModel(
        name="tse_with_restore",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="RF pulse added to end of echo factor to restore longitudinal magnetization",
        url="https://mriquestions.com/driven-equilibrium.html",  # type: ignore[arg-type]
        siemens=["RESTORE"],
        ge=["Fast Recovery FSE", "FRFSE"],
        philips=["DRIVE"],
        canon=["T2 Plus FSE"],
        hitachi=["Driven Equilibrium", "DE-FSE", "DE-FIR"],
    ),
    MriSequenceModel(
        name="variable_flip_3d_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["3d_volume"],
        description="high resolution isotropic sub-millimeter 3D volumes",
        url="https://mriquestions.com/spacecubevista.html",  # type: ignore[arg-type]
        siemens=["SPACE"],
        ge=["CUBE"],
        philips=["VISTA"],
        canon=["FASE3D mVox"],
        hitachi=["isoFSE"],
    ),
    MriSequenceModel(
        name="cartilage_mapping_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="parametric maps of T1, T2 and T2* for superficial and intermediate layer cartilage assessment",
        url="https://mriquestions.com/t2-cartilage-mapping.html",  # type: ignore[arg-type]
        siemens=["MapIT T2"],
        ge=["Cartigram"],
        philips=["Cartilage Assessment"],
        canon=["Multi Echo T2"],
        hitachi=["T2 Relax Map"],
    ),
    MriSequenceModel(
        name="dixon_water_fat_separation_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="chemical shift imaging method using in-phase/out-of-phase cycling of fat and water",
        url="https://mriquestions.com/dixon-method.html",  # type: ignore[arg-type]
        siemens=["Dixon TSE", "Dixon"],
        ge=["IDEAL", "FLEX"],
        philips=["mDixon XD", "mDixon TSE"],
        canon=["Water Fat Separation", "WFS TSE"],
        hitachi=["FatSep"],
    ),
]
