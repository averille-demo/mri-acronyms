"""Inversion recovery (IR) spin-echo based pulse sequences.

Note: the classic 'inversion recovery' is a turbo spin echo sequence.
https://www.imaios.com/en/e-mri/sequences/inversion-recovery-stir-and-flair

Ultrafast gradient variants include magnetization prep which also uses an initial 180° inversion pulse.
https://www.imaios.com/en/e-mri/sequences/ultrafast-spoiled-gradient-echo-sequences

Regarding image contrast: STIR and FLAIR can be either T1 or T2 weighted depending on parameters: TI, TR, TE, etc.
"""

from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

IR_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="inversion_recovery_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="magnetization preparation technique followed by turbo spin echo sequence",
        url="https://www.imaios.com/en/e-mri/sequences/inversion-recovery-stir-and-flair",  # type: ignore[arg-type]
        siemens=["IR", "IRM", "TurboIR", "TIRM"],
        ge=["IR", "FSE-IR", "FastIR"],
        philips=["IR", "IR-TSE"],
        canon=["IR"],
        hitachi=["IR", "FIR"],
    ),
    MriSequenceModel(
        name="short_tau_inversion_recovery_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="IR sequence with TI set to suppress/null fat signal",  # type: ignore[arg-type]
        url="https://mriquestions.com/stir.html",  # type: ignore[arg-type]
        siemens=["STIR", "Turbo STIR"],
        ge=["STIR", "Fast STIR"],
        philips=["STIR", "STIR TSE"],
        canon=["FastSTIR"],
        hitachi=["FIR-STIR", "Fast STIR"],
    ),
    MriSequenceModel(
        name="long_tau_inversion_recovery_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="IR sequence with TI set to suppress/null fluid signal",
        url="https://www.imaios.com/en/e-mri/sequences/inversion-recovery-stir-and-flair",  # type: ignore[arg-type]
        siemens=["Dark Fluid", "FLAIR", "Turbo FLAIR"],
        ge=["FLAIR"],
        philips=["FLAIR"],
        canon=["FastFLAIR"],
        hitachi=["FIR-FLAIR", "FastFLAIR"],
    ),
    MriSequenceModel(
        name="phase_sensitive_inversion_recovery_tse",
        image_weighting="ANY",
        classification="spin_echo",
        acquisition_modes=["2d_slices"],
        description="phase sensitive inversion recovery (PSIR) reconstruction for increased contrast between tissues",
        url="https://mriquestions.com/phase-sensitive-ir.html",  # type: ignore[arg-type]
        siemens=["TrueIR", "TIR"],
        ge=[],
        philips=["Real IR"],
        canon=["Real IR"],
        hitachi=["Real-IR"],
    ),
]
