"""Test dynamically generated lookup table."""

from typing import Dict, List

from mri_acronyms import build_lookup_table
from mri_acronyms.lut.category_to_acronym_lut import CATEGORY_TO_ACRONYM_LUT


def test_build_lut_table():
    """Create reference python module with all MRI acronyms."""
    build_lookup_table.generate(sort_keys=False)
    assert CATEGORY_TO_ACRONYM_LUT["SPIN_ECHO_SEQUENCES"]["spin_echo"][0].isupper()
    assert isinstance(CATEGORY_TO_ACRONYM_LUT["SPIN_ECHO_SEQUENCES"], Dict)
    assert isinstance(CATEGORY_TO_ACRONYM_LUT["SPIN_ECHO_SEQUENCES"]["spin_echo"], List)
    assert len(CATEGORY_TO_ACRONYM_LUT["SPIN_ECHO_SEQUENCES"]["spin_echo"]) == 1
