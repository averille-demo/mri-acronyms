"""Data source for MRI vendor acronyms.

https://radiopaedia.org/articles/mri-pulse-sequence-abbreviations
https://sandrofenelon.com.br/mri-acronyms-ge-siemens-philips-toshiba-canon-hitachi/
"""

from enum import Enum, auto, unique
from typing import Optional, Sequence, Union

from mri_acronyms.models.pydantic_models import MriParameterModel, MriSequenceModel
from mri_acronyms.pulse_sequences.angiography import MRA_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.cardiac import CARDIAC_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.echo_planar import EPI_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.functional import FMRI_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.gradient_echo import GRE_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.inversion_recovery import IR_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.scanner_parameters import MRI_PARAMETERS
from mri_acronyms.pulse_sequences.spectroscopy import SPECT_PULSE_SEQUENCES
from mri_acronyms.pulse_sequences.spin_echo import SE_PULSE_SEQUENCES


@unique
class PulseSequenceCategory(Enum):
    """Categorical grouping of MRI pulse sequences/parameters."""

    SPIN_ECHO_SEQUENCES = auto()
    GRADIENT_ECHO_SEQUENCES = auto()
    INVERSION_RECOVERY_SEQUENCES = auto()
    ECHO_PLANAR_SEQUENCES = auto()
    ANGIOGRAPHY_SEQUENCES = auto()
    CARDIAC_SEQUENCES = auto()
    FUNCTIONAL_SEQUENCES = auto()
    SPECTROSCOPY_SEQUENCES = auto()
    SCANNER_PARAMETERS = auto()

    def __str__(self) -> str:
        """String representation of class."""
        return self.name.lower()

    @property
    def order(self) -> int:
        """Ordered numerical value of enumeration as integer."""
        return self.value

    @property
    def acronyms(self) -> Sequence[Union[MriParameterModel, MriSequenceModel]]:
        """Mapping of category string to relevant key/value pairs."""
        match self:
            case PulseSequenceCategory.SPIN_ECHO_SEQUENCES:
                return SE_PULSE_SEQUENCES
            case PulseSequenceCategory.GRADIENT_ECHO_SEQUENCES:
                return GRE_PULSE_SEQUENCES
            case PulseSequenceCategory.INVERSION_RECOVERY_SEQUENCES:
                return IR_PULSE_SEQUENCES
            case PulseSequenceCategory.ECHO_PLANAR_SEQUENCES:
                return EPI_PULSE_SEQUENCES
            case PulseSequenceCategory.ANGIOGRAPHY_SEQUENCES:
                return MRA_PULSE_SEQUENCES
            case PulseSequenceCategory.CARDIAC_SEQUENCES:
                return CARDIAC_PULSE_SEQUENCES
            case PulseSequenceCategory.SPECTROSCOPY_SEQUENCES:
                return SPECT_PULSE_SEQUENCES
            case PulseSequenceCategory.FUNCTIONAL_SEQUENCES:
                return FMRI_PULSE_SEQUENCES
            case PulseSequenceCategory.SCANNER_PARAMETERS:
                return MRI_PARAMETERS

    @staticmethod
    def get_model(category: str, name: str) -> Optional[Union[MriParameterModel, MriSequenceModel]]:
        """Lookup acronym model by case insensitive keyword search."""
        for psc in PulseSequenceCategory:
            if category.lower() == psc.name.lower():
                for model in psc.acronyms:
                    if name.lower() == model.name.lower():
                        return model
        return None
