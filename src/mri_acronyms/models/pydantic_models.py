"""Data models for MRI acronyms with Pydantic 2.0 model validators.

https://docs.pydantic.dev/latest/migration/
https://docs.pydantic.dev/2.0/usage/validators/
"""

import re
from typing import List, Optional

from pydantic import BaseModel, ConfigDict, HttpUrl, field_validator

from mri_acronyms.util.constants import (
    VALID_ACQUISITION_MODES,
    VALID_IMAGE_WEIGHTINGS,
    VALID_SEQUENCE_CLASSIFICATIONS,
)


# pylint: disable=[too-few-public-methods, no-self-argument]
class MriParameterModel(BaseModel):
    """Model of vendor mappings for given MRI scanner setting/parameter.

    https://docs.pydantic.dev/latest/usage/types/
    https://docs.pydantic.dev/latest/usage/model_config/#options
    """

    model_config = ConfigDict(populate_by_name=False, str_strip_whitespace=True)
    name: str
    description: str
    url: HttpUrl
    siemens: List[str] = []
    ge: List[str] = []
    philips: List[str] = []
    canon: List[str] = []
    hitachi: List[str] = []

    @field_validator("name")
    def check_name(cls, v):
        """Verify lower underscore (snake_case) naming convention."""
        if not bool(re.match("^[a-z0-9_]*$", v)):
            raise ValueError(f"invalid name format: {v} (lower underscores only)")
        return v

    @field_validator("description")
    def check_description(cls, v):
        """Verify value does not contain whitespace at beginning or end of string."""
        if v.startswith(" "):
            raise ValueError(f"invalid description: '{v}' (beginning whitespace)")
        if v.endswith(" "):
            raise ValueError(f"invalid description: '{v}' (ending whitespace)")
        return v

    @field_validator("siemens", "ge", "philips", "canon", "hitachi")
    def check_vendor(cls, elements: List[str]):
        """Verify elements of list are not empty."""
        if "" in elements:
            raise ValueError("invalid element (empty string)")
        if None in elements:
            raise ValueError("invalid element (null)")
        if len(set(elements)) != len(elements):
            raise ValueError("duplicate element detected")
        return elements


# pylint: disable=[too-few-public-methods, no-self-argument]
class MriSequenceModel(MriParameterModel):
    """Model of vendor mappings for given MRI pulse sequence."""

    # included all inherited class attributes (name, description, link, ...)
    image_weighting: Optional[str] = ""
    classification: Optional[str] = ""
    acquisition_modes: List[str] = []

    @field_validator("image_weighting")
    def check_image_weighting(cls, v: str):
        """Verify image weighting is valid.

        Note: most sequences are mixture of T1/T2/PD weighting based on numerous factors when the signal was collected.
        Reference:
            https://mriquestions.com/meaning-of-weighting.html
            https://mriquestions.com/image-contrast-trte.html
        Therefore if a pulse sequence is labeled 'T1', it is considered predominantly T1 weighted.
        """
        if v not in VALID_IMAGE_WEIGHTINGS:
            raise ValueError(f"invalid imaging weighting: '{v}' not in {VALID_IMAGE_WEIGHTINGS}")
        return v

    @field_validator("classification")
    def check_classification(cls, v: str):
        """Verify pulse sequence classification is valid.

        Reference:
            https://mriquestions.com/hellippulse-sequences.html
            https://www.imaios.com/en/e-mri/sequences/sequence-classification
        """
        if v not in VALID_SEQUENCE_CLASSIFICATIONS:
            raise ValueError(f"invalid sequence classification: '{v}' not in {VALID_SEQUENCE_CLASSIFICATIONS}")
        return v

    @field_validator("acquisition_modes")
    def check_acquisition_modes(cls, elements: List[str]):
        """Verify pulse sequence acquisition mode is valid.

        Reference:
            https://mriquestions.com/2d-vs-3d-mra.html
            https://mriquestions.com/motsa.html
        """
        for v in elements:
            if v not in VALID_ACQUISITION_MODES:
                raise ValueError(f"invalid acquisition mode: '{v}' not in {VALID_ACQUISITION_MODES}")
        return elements
