"""Gradient echo (GRE) pulse sequences.

https://mriquestions.com/commercial-acronyms.html
"""
from typing import List

from mri_acronyms.models.pydantic_models import MriSequenceModel

GRE_PULSE_SEQUENCES: List[MriSequenceModel] = [
    MriSequenceModel(
        name="gradient_echo",
        image_weighting="ANY",
        classification="gradient_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="produces T1 and T2* weighted images (depending on TR, TE, and flip angle)",
        url="https://mriquestions.com/gradient-echo.html",  # type: ignore[arg-type]
        siemens=["GRE"],
        ge=["GRE"],
        philips=["Fast Field Echo", "FFE"],
        canon=["Field Echo", "FE"],
        hitachi=["GE"],
    ),
    MriSequenceModel(
        name="rf_spoiled_incoherent_gre",
        image_weighting="T1",
        classification="gradient_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="excitation pulse to eliminate magnetization build-up, resulting in T1 weighted images",
        url="https://mriquestions.com/spoiled-gre-parameters.html",  # type: ignore[arg-type]
        siemens=["FLASH"],
        ge=["SPGR", "Spoiled Gradient Echo"],
        philips=["T1-FFE"],
        canon=["T1-FFE"],
        hitachi=["RF Spoiled SARGE", "RSSG"],
    ),
    MriSequenceModel(
        name="coherent_gre_with_fid_refocusing_ssfp",
        image_weighting="T2*",
        classification="steady_state",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="steady state gradient echo sequence with T2* contrast for bright fluid signal",
        url="https://mriquestions.com/types-of-gre-sequences.html",  # type: ignore[arg-type]
        siemens=["FISP"],
        ge=["GRASS"],
        philips=["T2*-FFE"],
        canon=["SSFP-c"],
        hitachi=["Rephased SARGE"],
    ),
    MriSequenceModel(
        name="coherent_gre_with_echo_refocusing_ssfp",
        image_weighting="T2*",
        classification="steady_state",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="simultaneous SE & stimulated echo sampling for T2 weighting",
        url="https://mriquestions.com/what-is-ssfp.html",  # type: ignore[arg-type]
        siemens=["PSIF"],
        ge=["SSFP"],
        philips=["T2-FFE"],
        canon=["SSFP"],
        hitachi=["Time-Reversed SARGE", "TRSG"],
    ),
    MriSequenceModel(
        name="coherent_gre_with_balanced_fid_echo_refocusing_ssfp",
        image_weighting="T2/T1",
        classification="steady_state",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="high CNR & bright fluid with mixture of T2/T1 contrast",
        url="https://mriquestions.com/ssfp-mra.html",  # type: ignore[arg-type]
        siemens=["TrueFISP"],
        ge=["FIESTA"],
        philips=["Balanced FFE", "b-FFE"],
        canon=["True SSFP"],
        hitachi=["Balanced SARGE", "BASG"],
    ),
    MriSequenceModel(
        name="coherent_balanced_gre_using_dual_excitation_ssfp",
        image_weighting="T2/T1",
        classification="steady_state",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="multiple RF phase angles and increased NSA to average out banding artifact",
        url="https://mriquestions.com/fiesta-v-fiesta-c.html",  # type: ignore[arg-type]
        siemens=["CISS"],
        ge=["FIESTA-C"],
        philips=[],
        canon=[],
        hitachi=["Phase Balanced SARGE", "PBSG"],
    ),
    MriSequenceModel(
        name="coherent_double_combined_echos_ssfp",
        image_weighting="T2/T1",
        classification="steady_state",
        acquisition_modes=["3d_volume"],
        description="generates FID-like and echo-like signals from the steady-state free precession individually",
        url="https://www.mriquestions.com/dess.html",  # type: ignore[arg-type]
        siemens=["DESS"],
        ge=["MENSA"],
        philips=[],
        canon=[],
        hitachi=[],
    ),
    MriSequenceModel(
        name="spoiled_combined_multiple_fid_gre",
        image_weighting="T2*",
        classification="gradient_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="provides high SNR/CNR for cartilage/fluid differentiation",
        url="https://mriquestions.com/mergemedic.html",  # type: ignore[arg-type]
        siemens=["MEDIC"],
        ge=["MERGE", "COSMIC"],
        philips=["m-FFE"],
        canon=["mEcho", "DUAL 3D"],
        hitachi=["ADAGE"],
    ),
    MriSequenceModel(
        name="ultrafast_rf_spoiled_incoherent_2d_gre",
        image_weighting="T1",
        classification="gradient_echo",
        acquisition_modes=["2d_slices"],
        description="small flip angle with very short TR and optimized k-space filling",
        url="https://www.imaios.com/en/e-mri/sequences/"
        + "ultrafast-spoiled-gradient-echo-sequences",  # type: ignore[arg-type]
        siemens=["TurboFLASH"],
        ge=["Fast GRE", "Fast SPGR"],
        philips=["TFE"],
        canon=["mpFFE"],
        hitachi=["fRSSG"],
    ),
    MriSequenceModel(
        name="ultrafast_rf_spoiled_incoherent_3d_gre",
        image_weighting="T1",
        classification="gradient_echo",
        acquisition_modes=["3d_volume"],
        description="magnetic preparation gradient echo with possible isotropic 3D T1 imaging",
        url="https://mriquestions.com/ir-prepped-sequences.html",  # type: ignore[arg-type]
        siemens=["MPRAGE", "MP-RAGE"],
        ge=["BRAVO", "3D FGRE", "3D Fast SPGR"],
        philips=["3D-T1 TFE", "3D TFE"],
        canon=["FastFE 3D", "3DFFE-IR"],
        hitachi=["3D-GEIR"],
    ),
    MriSequenceModel(
        name="volume_interpolated_fatsat_3d_gre",
        image_weighting="T1",
        classification="gradient_echo",
        acquisition_modes=["3d_volume"],
        description="3D T1 gradient echo with RF fatsat",
        url="https://mrimaster.com/characterise%20image%20vibe.html",  # type: ignore[arg-type]
        siemens=["VIBE", "T1-VIBE"],
        ge=["FAME", "LAVA-XV"],
        philips=["THRIVE"],
        canon=["3D QUICK"],
        hitachi=["TIGRE"],
    ),
    # https://mriquestions.com/in-phaseout-of-phase.html
    MriSequenceModel(
        name="dixon_water_fat_separation_3d_gre",
        image_weighting="T1",
        classification="gradient_echo",
        acquisition_modes=["3d_volume"],
        description="volume-interpolated 3D in/out-of-phase gradient image",
        url="https://mriquestions.com/dixon-method.html",  # type: ignore[arg-type]
        siemens=["Dixon VIBE"],
        ge=["LAVA-FLEX"],
        philips=["mDixon"],
        canon=["WFS"],
        hitachi=["FatSep RSSG"],
    ),
    MriSequenceModel(
        name="susceptibility_weighted_mip_gre",
        image_weighting="SWI",
        classification="gradient_echo",
        acquisition_modes=["2d_slices", "3d_volume"],
        description="GRE sequences are sensitive to differences in tissue susceptibility",
        url="https://mriquestions.com/making-an-sw-image.html",  # type: ignore[arg-type]
        siemens=["SWI"],
        ge=["SWAN"],
        philips=["SWip", "SWI-phase"],
        canon=["Flow Sensitive Black Blood", "FSBB"],
        hitachi=["BSI"],
    ),
    MriSequenceModel(
        name="dynamic_contrast_perfusion_gre",
        image_weighting="PWI",
        classification="gradient_echo",
        acquisition_modes=["2d_slices"],
        description="bolus of contrast agent injected, hemodynamic signals depend on T1 relaxation time",
        url="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4170157/",  # type: ignore[arg-type]
        siemens=["Neuro Perfusion"],
        ge=["BrainSTAT"],
        philips=["PRESTO", "T2* Perfusion"],
        canon=[],
        hitachi=["CE-Perfusion"],
    ),
    MriSequenceModel(
        name="iron_concentration_mapping_gre",
        image_weighting="T2*",
        classification="gradient_echo",
        acquisition_modes=["2d_slices"],
        description="calculates T2* and displays color overlay for quantitative assessment of iron concentration",
        url="https://mriquestions.com/iront2-mapping.html",  # type: ignore[arg-type]
        siemens=["MapIT T2*"],
        ge=["Star Map"],
        philips=["mDIXON-Quant"],
        canon=[],
        hitachi=["T2* RelaxMap"],
    ),
]
