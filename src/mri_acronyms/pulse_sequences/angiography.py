"""Angiography (MRA) pulse sequences.

CE-MRI: IV Contrast Enchained MRI
Non-Contrast: no IV contrast is injected to produce bright blood signal (In-flow effect)
"""
from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

MRA_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="time_of_flight_non_contrast_mra",
        image_weighting="FSI",
        classification="gradient_echo",
        acquisition_modes=["2d_slices", "3d_slabs", "3d_volume"],
        description="non-contrast bright-blood method for imaging vessels",
        url="https://radiopaedia.org/articles/haemorrhage-on-mri?lang=us",  # type: ignore[arg-type]
        siemens=["ToF"],
        ge=["ToF", "Inhance Inflow"],
        philips=["Inflow"],
        canon=["TOF"],
        hitachi=["TOF"],
    ),
    MriSequenceModel(
        name="phase_contrast_non_contrast_mra",
        image_weighting="FSI",
        classification="phase_contrast",
        acquisition_modes=["2d_slices", "3d_volume", "4d_dynamic"],
        description="blood flow velocities encoded by phase gradients with specific VENC setting",
        url="https://mriquestions.com/phase-contrast-mra.html",  # type: ignore[arg-type]
        siemens=["PC"],
        ge=["PC", "Inhance Velocity"],
        philips=["PC"],
        canon=["PC"],
        hitachi=["PC-MRA"],
    ),
    MriSequenceModel(
        name="contrast_bolus_timing_ce_mra",
        image_weighting="T1",
        classification="perfusion",
        acquisition_modes=["2d_slices", "3d_volume", "4d_dynamic"],
        description="Contrast-enhanced MR angiography bolus tracking of gadolinium for arterial phase imaging",
        url="https://www.mriquestions.com/timing-the-bolus.html",  # type: ignore[arg-type]
        siemens=["Care Bolus"],
        ge=["Smart Prep"],
        philips=["BolusTrak"],
        canon=["VisualPrep"],
        hitachi=["FLUTE"],
    ),
    MriSequenceModel(
        name="dynamic_time_resolved_3d_spoiled_gre_ce_mra",
        image_weighting="T1",
        classification="perfusion",
        acquisition_modes=["3d_volume", "4d_dynamic"],
        description="acquire multiple images after gadolinium IV contrast injection (1-2 frames per second)",
        url="https://www.mriquestions.com/tricks-or-twist.html",  # type: ignore[arg-type]
        siemens=["TWIST"],
        ge=["TRICKS", "Tricks-XV"],
        philips=["Keyhole", "4D TRAK"],
        canon=["DRKS"],
        hitachi=["TRAQ"],
    ),
    MriSequenceModel(
        name="gated_3d_t2_tse_non_contrast_mra",
        image_weighting="T2",
        classification="spin_echo",
        acquisition_modes=["3d_volume"],
        description="T2-weighted 3D TSE with partial fourier non-contrast MRA sequence for peripheral angiography",
        url="https://mriquestions.com/gated-3d-fse-mra.html",  # type: ignore[arg-type]
        siemens=["NATIVE SPACE"],
        ge=["InFlow Deltaflow"],
        philips=["TRANCE"],
        canon=["FBI", "CIA"],
        hitachi=["VASC-FSE"],
    ),
    MriSequenceModel(
        name="inflow_enhanced_ssfp_3d_non_contrast_mra",
        image_weighting="T2/T1",
        classification="steady_state",
        acquisition_modes=["3d_volume"],
        description="non-contrast MRA technique using venous saturation with unsaturated arterial inflow",
        url="https://mriquestions.com/inflow-enhanced-ssfp.html",  # type: ignore[arg-type]
        siemens=["NATIVE TrueFISP"],
        ge=["InFlow IRP", "Inhance Inflow IR"],
        philips=["B-TRANCE", "b TRANCE"],
        canon=["Time-SLIP", "TSA"],
        hitachi=["VASC", "VASC-ASL"],
    ),
]
