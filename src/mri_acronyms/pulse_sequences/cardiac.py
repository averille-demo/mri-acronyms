"""Cardiac pulse sequences.

https://cardiacmri.com/tech-guide/imaging-sequences/
https://radiopaedia.org/articles/cardiac-mri?lang=us
https://mrimaster.com/PLAN%20CARDIC.html
"""

from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

CARDIAC_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="myocardial_dual_ir_3d_tse",
        image_weighting="T2",
        classification="spin_echo",
        acquisition_modes=["3d_volume"],
        description="two non-selective 180° inverting pulses",
        url="https://mriquestions.com/double-ir.html",  # type: ignore[arg-type]
        siemens=["DIR SPACE"],
        ge=["CUBE DIR"],
        philips=["Dual IR-TSE"],
        canon=["Double IR"],
        hitachi=[],
    ),
    MriSequenceModel(
        name="myocardial_triple_ir_3d_tse",
        image_weighting="T2",
        classification="spin_echo",
        acquisition_modes=["3d_volume"],
        description="three non-selective 180° inverting pulses - third inverting pulse nulls signal from fat",
        url="https://mri-q.com/triple-ir.html",  # type: ignore[arg-type]
        siemens=[],
        ge=[],
        philips=["Triple IR-TSE"],
        canon=["Triple IR"],
        hitachi=[],
    ),
    # MriSequenceModel(
    #     name="myocardial_rf_spoiled_incoherent_gre",
    #     description="excitation pulse to eliminate magnetization build-up, resulting in T1 weighted images",
    #     url="https://mriquestions.com/spoiled-gre-parameters.html",  # type: ignore[arg-type]
    #     siemens=["FLASH"],
    #     ge=["SPGR", "Spoiled Gradient Echo"],
    #     philips=["T1-FFE"],
    #     canon=["T1-FFE"],
    #     hitachi=["RF Spoiled SARGE", "RSSG"],
    # ),
    # MriSequenceModel(
    #     name="myocardial_balanced_ssfp_gre",
    #     description="high CNR & bright fluid with mixture of T2/T1 contrast",
    #     url="https://mriquestions.com/ssfp-mra.html",  # type: ignore[arg-type]
    #     siemens=["TrueFISP"],
    #     ge=["FIESTA"],
    #     philips=["Balanced FFE", "b-FFE"],
    #     canon=["True SSFP"],
    #     hitachi=["Balanced SARGE", "BASG"],
    # ),
    # MriSequenceModel(
    #     name="myocardial_phase_contrast_mra",
    #     description="blood flow velocities encoded by phase gradients",
    #     url="https://mriquestions.com/phase-contrast-mra.html",  # type: ignore[arg-type]
    #     siemens=["PC"],
    #     ge=["PC", "Inhance Velocity"],
    #     philips=["PC"],
    #     canon=["PC"],
    #     hitachi=["PC-MRA"],
    # ),
    MriSequenceModel(
        name="myocardial_phase_sensitive_inversion_recovery",
        image_weighting="T1",  # can also be PD or T2
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="preserves positive and negative polarities of tissues as they recover from 180° IR pulse",
        url="https://mriquestions.com/ps-phase-sensitive-ir.html",  # type: ignore[arg-type]
        siemens=["TFL PSIR"],
        ge=[],
        philips=["bTFE SSh"],
        canon=[],
        hitachi=[],
    ),
    MriSequenceModel(
        name="myocardial_t1_mapping_gre",
        image_weighting="T1",
        classification="gradient_echo",  # can also be ssfp or modified Look-Locker technique
        acquisition_modes=["2d_slices"],
        description="series of independent single-point inversion recovery signal measurements at different TIs",
        url="https://mriquestions.com/t1-mapping.html",  # type: ignore[arg-type]
        siemens=["MyoMaps"],
        ge=["CardioMaps"],
        philips=["T1 Mapping", "StarQuant"],
        canon=["MOLLI", "SASHA", "Look-Locker"],
        hitachi=[],
    ),
    MriSequenceModel(
        name="myocardial_t1_mapping_scout",
        image_weighting="T1",
        classification="gradient_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="series of independent single-point inversion recovery signal measurements at different TIs",
        url="https://mriquestions.com/ti-to-null-myocardium.html",  # type: ignore[arg-type]
        siemens=["TI scout"],
        ge=["Cine IR"],
        philips=[],
        canon=[],
        hitachi=[],
    ),
    MriSequenceModel(
        name="myocardial_tagging_gre",
        image_weighting="T1",
        classification="steady_state",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="technique where RF-saturation pulses are used to place stripes or grids on the heart",
        url="https://mriquestions.com/taggingspamm.html",  # type: ignore[arg-type]
        siemens=["SPAMM", "CSPAMM", "DANTE"],
        ge=["HARP", "DENSE", "SENC"],
        philips=[],
        canon=[],
        hitachi=[],
    ),
]
