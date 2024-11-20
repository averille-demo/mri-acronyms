"""Constant values."""

from typing import Dict, Final, List

SEP: Final[str] = "; "
VALID_SYMBOLS: Final[str] = ".-|/*"

HEADERS: Final[List[str]] = [
    "Group",
    "Category",
    "Sequence | Parameter",
    "Siemens",
    "General Electric",
    "Philips",
    "Canon",
    "Hitachi",
]


VALID_ACQUISITION_MODES: Final[List[str]] = [
    "2d_slices",  # x/y
    "3d_slabs",  # x/y/z multi volume
    "3d_volume",  # x/y/z single volume
    "4d_dynamic",  # add temporal dimension (e.g. iv contrast enhanced, cardiac motion, etc.)
    "voxel",  # spectroscopy
]


# predominant image weighting
# affected by tissue parameters: T1, T2, PD, diffusion, susceptibility, chemical shift, flow, and perfusion
# https://radiopaedia.org/articles/mri-sequences-overview?lang=us
VALID_IMAGE_WEIGHTINGS: Final[Dict[str, str]] = {
    # https://mriquestions.com/what-is-t1.html
    "T1": "t1_weighted",  # T1 relaxation - decay of longitudinal magnetization
    # https://mriquestions.com/what-is-t2.html
    "T2": "t2_weighted",  # T2 relaxation - decay of transverse magnetization from atomic interactions
    # https://mriquestions.com/t2-vs-t2.html
    "T2*": "t2_star_weighted",  # effective T2 relaxation from field/tissue inhomogeneities) - visible on gradient scans
    # https://mriquestions.com/image-contrast-trte.html
    "PD": "proton_density",  # hydrogen weighted
    # https://mriquestions.com/ssfp-mra.html
    "T2/T1": "t2_to_t1_ratio",  # balanced SSFP
    "ANY": "variable",  # can be either T1, PD, or T2/T2* depending on technical factors: TI, TR, TE, flip angle, etc.
    # https://mriquestions.com/why-gre-uarr-flow-signal.html
    "FSI": "flow_sensitive",  # MRA (angiography), MRV (venography), CSF (phase contrast), etc.
    # https://mriquestions.com/diffusion-basic.html
    "DWI": "diffusion_weighted",  # movement of water due to thermal collisions: images:[b0, source, trace, ADC]
    "PWI": "perfusion_weighted",  # tracking movement of blood flow: ASL, cardiac perfusion, CE-MRI, etc.
    # https://mriquestions.com/making-an-sw-image.html
    "SWI": "susceptibility_weighted",  # sensitive to differences in tissue susceptibility multistage output MIP image
    "MRS": "spectroscopy",  # produces graphical output of tissue chemical composition within voxel
}

# high-level groupings
# https://www.imaios.com/en/e-mri/sequences/sequence-classification
VALID_SEQUENCE_CLASSIFICATIONS: Final[Dict[str, str]] = {
    # https://www.imaios.com/en/e-mri/sequences/fast-spin-echo
    "spin_echo": "tse",  # SE, TSE, etc.
    # https://www.imaios.com/en/e-mri/sequences/gradient-echo
    "gradient_echo": "gre",  # FFE, TOF, etc.
    # https://www.imaios.com/en/e-mri/sequences/inversion-recovery-stir-and-flair
    "inversion_recovery": "ir",  # spin echo only (STIR, FLAIR)
    # https://www.imaios.com/en/e-mri/sequences/ultrafast-spoiled-gradient-echo-sequences
    "single_shot": "ss",  # ultrafast gradient (TurboFLASH, VIBE) or spin-echo (HASTE)
    # https://www.imaios.com/en/e-mri/sequences/balanced-gradient-echo
    "steady_state": "ssfp",  # special type of gradient echo - SSFP, True FISP, PSIF, etc.
    # https://www.imaios.com/en/e-mri/sequences/echo-planar-imaging-epi
    "echo_planar": "epi",  # many variants - either spin echo, gradient echo, or hybrid (GRASE)
    # https://mriquestions.com/making-a-dw-image.html
    "diffusion": "dwi",  # DWI, DTI, ADC, etc.
    # https://radiopaedia.org/articles/mr-perfusion-weighted-imaging-1?lang=us
    "perfusion": "pwi",  # DSC, DCE, ASL - typically iv contrast enhanced
    # https://mriquestions.com/phase-contrast-mra.html
    "phase_contrast": "pc",  # special type of gradient echo - produces magnitude and phase images
    # https://mriquestions.com/whats-wrong-with-gre.html
    "susceptibility": "swi",  # special type of gradient echo - heavily T2* weighted
    "functional": "fmri",  # BOLD, VASO, ...
    "spectroscopy": "spect",  # PRESS, STEAM, ISIS, CSI, ...
}
