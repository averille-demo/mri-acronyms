"""Vendor dependent pulse sequence parameters/settings."""
from typing import List

from mri_acronyms.models.pydantic_models import MriParameterModel

MRI_PARAMETERS: List[MriParameterModel] = [
    MriParameterModel(
        name="slice_thickness",
        description="full width at half maximum (FWHM) of signal intensity",
        url="https://mriquestions.com/slice-parameters.html",  # type: ignore[arg-type]
        siemens=["Slice Thickness"],
        ge=["Slice Thickness"],
        philips=["Slice Thickness"],
        canon=["Slice Thickness"],
        hitachi=["Slice Thickness"],
    ),
    MriParameterModel(
        name="distance_between_slices",
        description="space between adjacent slices (avoid crosstalk)",
        url="https://mriquestions.com/cross-talk.html",  # type: ignore[arg-type]
        siemens=["Distance Factor"],
        ge=["Slice Gap"],
        philips=["Gap"],
        canon=["Gap"],
        hitachi=["Slice Interval"],
    ),
    MriParameterModel(
        name="rf_excitation_pulse_gre",
        description="RF excitation pulse for gradient scans",
        url="https://mriquestions.com/what-is-flip-angle.html",  # type: ignore[arg-type]
        siemens=["Flip Angle", "flip", "FA"],
        ge=["Flip Angle"],
        philips=["Flip Angle"],
        canon=["Flip Angle"],
        hitachi=["Flip Angle"],
    ),
    MriParameterModel(
        name="inversion_time",
        description="time between 180° inverting pulse and 90°-pulse",
        url="https://mriquestions.com/what-is-ir.html",  # type: ignore[arg-type]
        siemens=["Inversion Time", "TI"],
        ge=["TI"],
        philips=["TI"],
        canon=["TI"],
        hitachi=["TI"],
    ),
    MriParameterModel(
        name="repetition_time",
        description="time between excitation pulses (in milliseconds)",
        url="https://www.imaios.com/en/e-mri/nmr-signal-and-mri-contrast",  # type: ignore[arg-type]
        siemens=["Repetition Time", "TR"],
        ge=["TR"],
        philips=["TR"],
        canon=["TR"],
        hitachi=["TR"],
    ),
    MriParameterModel(
        name="echo_time",
        description="echo time (TE) represents the time from the center of the RF-pulse to the center of the echo",
        url="https://mriquestions.com/tr-and-te.html",  # type: ignore[arg-type]
        siemens=["Echo Time", "TE"],
        ge=["TE"],
        philips=["TE"],
        canon=["TE"],
        hitachi=["TE"],
    ),
    MriParameterModel(
        name="number_of_echos_tse",
        description="number of 180º refocusing pulses in a turbo spin echo sequence",
        url="https://mriquestions.com/fse-parameters.html",  # type: ignore[arg-type]
        siemens=["Turbo Factor"],
        ge=["Echo Train Length", "ETL"],
        philips=["Turbo Factor"],
        canon=["Echo Factor"],
        hitachi=["Echo Factor"],
    ),
    MriParameterModel(
        name="inter_echo_spacing_tse",
        description="time between echos in",
        url="https://mriquestions.com/fse-parameters.html",  # type: ignore[arg-type]
        siemens=["Echo Spacing"],
        ge=["Echo Spacing"],
        philips=["Echo Spacing"],
        canon=["Echo Spacing"],
        hitachi=["Inter-Echo Time", "IET"],
    ),
    MriParameterModel(
        name="number_of_signal_averages",
        description="number of signal averages in pulse sequence, if increased improves SNR at cost of scan time",
        url="https://mrimaster.com/technique%20NEX.html",  # type: ignore[arg-type]
        siemens=["Averages"],
        ge=["NEX"],
        philips=["NSA"],
        canon=["NAQ"],
        hitachi=["NSA"],
    ),
    MriParameterModel(
        name="scan_acquisition_time",
        description="total time in minutes:seconds (MM:SS) to complete pulse sequence image measurements",
        url="https://www.k-space.org/ymk/eq_acqtime.pdf",  # type: ignore[arg-type]
        siemens=["Acquisition Time", "TA"],
        ge=["Acquisition Time"],
        philips=["Acquisition Time"],
        canon=["Acquisition Time"],
        hitachi=["Scan Time"],
    ),
    MriParameterModel(
        name="receiver_bandwidth",
        description="range of frequencies involved in reception of signal",
        url="https://mriquestions.com/receiver-bandwidth.html",  # type: ignore[arg-type]
        siemens=["Bandwidth", "Hz/Px"],
        ge=["Receive Bandwidth", "kHz"],
        # philips [Px] e.g. BW of 195 Hz/pixel at 1.5T = 220/195 = 1.1 pixels
        philips=["Fat/Water Shift", "Px"],
        canon=["Bandwidth", "Hz/Px"],
        hitachi=["Receiver Bandwidth", "kHz"],
    ),
    MriParameterModel(
        name="variable_bandwidth",
        description="practical compromise performed on multi-echo studies",
        url="https://mriquestions.com/narrow-bandwidth.html",  # type: ignore[arg-type]
        siemens=["Optimized Bandwidth"],
        ge=["Variable Bandwidth"],
        philips=["Optimized Bandwidth"],
        canon=["Matched Bandwidth"],
        hitachi=["Variable Bandwidth"],
    ),
    MriParameterModel(
        name="magnetization_transfer_contrast",
        description="technique used to exploit contrast between tissues where 1H protons are present in 3 states",
        url="https://mriquestions.com/magnetization-transfer.html",  # type: ignore[arg-type]
        siemens=["MTC", "magnetization transfer"],
        ge=["MTC"],
        philips=["MTC"],
        canon=["SORS-STC"],
        hitachi=["MTC"],
    ),
    MriParameterModel(
        name="fatsat_chemical",
        description="difference in proton resonance frequency in lipid molecules used to suppress fat signal",
        url="https://www.imaios.com/en/e-Courses/e-MRI/"
        + "Improving-MRI-contrast-Imaging-water-and-fat/fat-saturation",  # type: ignore[arg-type]
        siemens=["Fat Sat", "FS"],
        ge=["Fat Sat", "Chem Sat"],
        philips=["SPIR"],
        canon=["MSOFT"],
        hitachi=["SINC", "H-SINC"],
    ),
    MriParameterModel(
        name="fatsat_chemical_adiabatic",
        description="uses a full 180º adiabatic inverting pulse that is insensitive to B1 inhomogeneity",
        url="https://mriquestions.com/best-method.html",  # type: ignore[arg-type]
        siemens=["SPAIR"],
        ge=["ASPIR"],
        philips=["SPAIR"],
        canon=["SPAIR"],
        hitachi=[],
    ),
    MriParameterModel(
        name="field_of_view",
        description="number of pixels in square FOV - higher image resolution, smaller pixels",
        url="https://mrimaster.com/index.4.html",  # type: ignore[arg-type]
        siemens=["Field of View", "FOV", "millimeters"],
        ge=["Field-of-View", "FOV", "millimeters"],
        philips=["FOV", "centimeters"],
        canon=["FOV", "millimeters"],
        hitachi=["FOV", "millimeters"],
    ),
    MriParameterModel(
        name="field_of_view_rectangular",
        description="non-square FOV used typically for spine and extremity exams at the cost of SNR and phase wrap",
        url="https://mriquestions.com/rectangular-fov.html",  # type: ignore[arg-type]
        siemens=["FoV Phase", "Rectangular FoV"],
        ge=["Asymmetric FoV", "Asymmetric"],
        philips=["Rectangular FoV", "Rectangular"],
        canon=["Rectangular FoV"],
        hitachi=["Rectangular-FoV"],
    ),
    MriParameterModel(
        name="saturation_spatial",
        description="suppress MR signal from moving tissues outside imaged volume to reduce motion artifacts",
        url="https://mriquestions.com/saturation-pulses.html",  # type: ignore[arg-type]
        siemens=["Sat Region"],
        ge=["SAT"],
        philips=["REST"],
        canon=["Presat"],
        hitachi=["Presat"],
    ),
    MriParameterModel(
        name="saturation_pulse_moving",
        description="suppress MR signal from moving tissues outside imaged volume to reduce motion artifacts",
        url="https://mriquestions.com/saturation-pulses.html",  # type: ignore[arg-type]
        siemens=["Tracking Sat", "Tracking"],
        ge=["Walking Sat", "Walking"],
        philips=["Travel REST", "Travel"],
        canon=["Moving Presat", "Moving"],
        hitachi=["Sequential Pre Sat"],
    ),
    MriParameterModel(
        name="multi_slab_acquisition",
        description="sequential acquisition of a several overlapping 3D volumes for TOF",
        url="https://mriquestions.com/motsa.html",  # type: ignore[arg-type]
        siemens=["Multi-Slab"],
        ge=["MOTSA"],
        philips=["Multi-Chunk"],
        canon=["Multi-Slab"],
        hitachi=["Multi-Slab"],
    ),
    MriParameterModel(
        name="motion_correction_radial_kspace_filling",
        description="motion reduction method to sample k-space in a rotating fashion using a set of strips/blades",
        url="https://mriquestions.com/propellerblade.html",  # type: ignore[arg-type]
        siemens=["BLADE"],
        ge=["PROPELLER"],
        philips=["Multivane"],
        canon=["JET"],
        hitachi=["RADAR"],
    ),
    MriParameterModel(
        name="radial_motion_compensation_with_pat",
        description="radial motion compensation combined with parallel imaging",
        url="https://mriquestions.com/radial-sampling.html",  # type: ignore[arg-type]
        siemens=["BLADE w/iPAT"],
        ge=["PROPELLER w/ASSET"],
        philips=[],
        canon=[],
        hitachi=["RAPID-RADAR"],
    ),
    MriParameterModel(
        name="motion_free_breathing_3d_t1_gre",
        description="in-plane radial sampling using a fat-suppressed spoiled-GRE core sequence",
        url="https://mriquestions.com/radial-sampling.html",  # type: ignore[arg-type]
        siemens=["StarVibe"],
        ge=["DISCO Star"],
        philips=["VANE XD"],
        canon=["QuickStar"],
        hitachi=["TIGRE NAVI"],
    ),
    MriParameterModel(
        name="parallel_imaging_technique_image_based",
        description="primarily performed in image space after reconstruction of data from individual coils",
        url="https://mriquestions.com/senseasset.html",  # type: ignore[arg-type]
        siemens=["iPAT", "mSENSE"],
        ge=["ASSET"],
        philips=["SENSE", "dS SENSE"],
        canon=["SPEEDER"],
        hitachi=["RAPID"],
    ),
    MriParameterModel(
        name="parallel_imaging_technique_kspace_based",
        description="multi-coil parallel technique where correction is made in k-space before Fourier transform",
        url="https://mriquestions.com/grappaarc.html",  # type: ignore[arg-type]
        siemens=["GRAPPA"],
        ge=["ARC"],
        philips=[],
        canon=[],
        hitachi=["k-RAPID"],
    ),
    MriParameterModel(
        name="off_center_shift_slice_group",
        description="shifting the center of a slice group from the center of magnetic field",
        url="https://mriquestions.com/slice-selective-excitation.html",  # type: ignore[arg-type]
        siemens=["Off-center Shift"],
        ge=["Off center FoV", "Off-center"],
        philips=["Off-center FoV"],
        canon=["Phase & Frequency Shift"],
        hitachi=["Off-center FoV"],
    ),
    MriParameterModel(
        name="simultaneous_excitation",
        description="specialized multi-slice excitation technique",
        url="https://mriquestions.com/two-slices-at-once.html",  # type: ignore[arg-type]
        siemens=["Simultaneous Excitation"],
        ge=["Phase Offset Multiplanar", "POMP"],
        philips=["Multi-Slice"],
        canon=["QuadScan"],
        hitachi=["Dual Slice"],
    ),
    MriParameterModel(
        name="water_excitation",
        description="water protons are selectively stimulated for image generation",
        url="https://mriquestions.com/water-excitation.html",  # type: ignore[arg-type]
        siemens=["Water Excitation"],
        ge=["Water Excitation"],
        philips=["Proset"],
        canon=["PASTA"],
        hitachi=["Water Excitation"],
    ),
    MriParameterModel(
        name="metal_artifact_reduction",
        description="reduce geometric distortions: signal voids (black areas) & signal pile-ups (bright areas)",
        url="https://mriquestions.com/metal-suppression.html",  # type: ignore[arg-type]
        siemens=["WARP"],
        ge=["MAVRIC"],
        philips=["O-MAR VAT"],
        canon=["VAT"],
        hitachi=["HiMAR"],
    ),
    MriParameterModel(
        name="phase_oversampling",
        description="collect more data measurements than required for resolution to eliminate wrap-around artifact",
        url="https://mriquestions.com/phase-oversampling.html",  # type: ignore[arg-type]
        siemens=["Phase Oversampling"],
        ge=["No Phase Wrap"],
        philips=["Fold-over Suppression"],
        canon=["Phase wrap suppression"],
        hitachi=["Anti-Wrap"],
    ),
    MriParameterModel(
        name="frequency_oversampling",
        description="oversampling of data during MR signal digitizing along frequency encoding gradient",
        url="https://www.imaios.com/en/e-mri/image-quality-and-artifacts/aliasing",  # type: ignore[arg-type]
        siemens=["Oversampling"],
        ge=["Anti-Aliasing"],
        philips=["Frequency Oversampling"],
        canon=["Frequency Wrap Suppression"],
        hitachi=["Frequency Oversampling"],
    ),
    MriParameterModel(
        name="flow_compensation",
        description="gradient moment nulling to correct for flow-related dephasing",
        url="https://mriquestions.com/flow-compensation.html",  # type: ignore[arg-type]
        siemens=["Flow Comp", "GMR"],
        ge=["Flow Comp"],
        philips=["Flow Comp", "Flag"],
        canon=["Flow Comp", "FC"],
        hitachi=["Rephase"],
    ),
    MriParameterModel(
        name="partial_echo",
        description="fractional echo, read-conjugate symmetry (partial fourier technique)",
        url="https://mriquestions.com/read-symmetry.html",  # type: ignore[arg-type]
        siemens=["Asymmetric Echo"],
        ge=["Asymmetric Echo"],
        philips=["Partial Echo"],
        canon=["Match Bandwidth"],
        hitachi=["Half Echo"],
    ),
    MriParameterModel(
        name="half_fourier",
        description="data from as little as one-half of k-space is used to generate an entire MR image",
        url="https://mriquestions.com/partial-fourier.html",  # type: ignore[arg-type]
        siemens=["Half Fourier", "Partial Fourier"],
        ge=["Half NEX", "fractional NEX"],
        philips=["Half Scan"],
        canon=["AFI"],
        hitachi=["Half Scan"],
    ),
    MriParameterModel(
        name="gating_cardiac_ecg",
        description="either prospective or retrospective cardiac gating by EKG (better) or peripheral pulse sensor",
        url="https://mriquestions.com/gating-methods.html",  # type: ignore[arg-type]
        siemens=["ECG triggered"],
        ge=["Cardiac Gated"],
        philips=["ECG Triggered", "VCG"],
        canon=["Cardiac Gated"],
        hitachi=["ECG Triggered"],
    ),
    MriParameterModel(
        name="gating_respiratory",
        description="non-breath hold technique (images acquired during expiration) used for long scan times",
        url="https://mriquestions.com/respiratory-comp.html",  # type: ignore[arg-type]
        siemens=["Respiratory Gated"],
        ge=["Respiratory Comp"],
        philips=["Trigger;", "PEAR"],
        canon=["Respiratory Gated"],
        hitachi=["MAR"],
    ),
    MriParameterModel(
        name="coil_sensitivity_normalization",
        description="resonance frequency of the patient-coil system and coil impedance must be adjusted to patient",
        url="https://mriquestions.com/automatic-prescan.html",  # type: ignore[arg-type]
        siemens=["Prescan Normalize"],
        ge=["PURE"],
        philips=["CLEAR"],
        canon=[],
        hitachi=["NATURAL"],
    ),
    MriParameterModel(
        name="quiet_scanning_3d_half_radial",
        description="lower-noise imaging techniques",
        url="https://mriquestions.com/whats-that-noise.html",  # type: ignore[arg-type]
        siemens=["PETRA"],
        ge=["SILENZ"],
        philips=[],
        canon=["mUTE 3D T1"],
        hitachi=[],
    ),
    MriParameterModel(
        name="quiet_scanning_optimized_gradient",
        description="lower-noise imaging techniques",
        url="https://mriquestions.com/whats-that-noise.html",  # type: ignore[arg-type]
        siemens=["QuietX"],
        ge=["Silent Scan"],
        philips=["ComforTone"],
        canon=["rounded gradient shapes"],
        hitachi=[],
    ),
    MriParameterModel(
        name="quiet_scanning_reduced_slew_rates",
        description="lower-noise imaging techniques",
        url="https://mriquestions.com/gradient-specifications.html",  # type: ignore[arg-type]
        siemens=["Whisper"],
        ge=["Acoustic Reduction Technology", "ART"],
        philips=["SofTone"],
        canon=["Pianissimo Zen"],
        hitachi=["SoftSound"],
    ),
    MriParameterModel(
        name="parallel_multi_transmit_rf_shimming",
        description="parallel receiver imaging applied to optimize properties of RF transmitted B1 field",
        url="https://mriquestions.com/multi-transmit-rf.html",  # type: ignore[arg-type]
        siemens=["TimTX TrueForm"],
        ge=["MultiDrive"],
        philips=["MultiTransmit"],
        canon=["MultiPhase Transmit"],
        hitachi=["Quartet"],
    ),
    MriParameterModel(
        name="localizer",
        description="set of 3-plane, low-resolution, large FOV 'scout' views used for slice planning",
        url="https://mriquestions.com/what-are-the-steps.html",  # type: ignore[arg-type]
        siemens=["Localizer", "Scout"],
        ge=["Localizer"],
        philips=["Plan Scan"],
        canon=["Locator"],
        hitachi=["Scanogram"],
    ),
    MriParameterModel(
        name="automated_slice_positioning",
        description="standardized AX/COR/SAG slice planning based on anatomical landmarks",
        url="http://clinical-mri.com/autoalign/",  # type: ignore[arg-type]
        siemens=["AutoAlign"],
        ge=["ReadyBrain", "AIRx"],
        philips=["SmartExam"],
        canon=["CardioLine", "NeuroLine", "SpineLine"],
        hitachi=["AutoPose Brain"],
    ),
]
