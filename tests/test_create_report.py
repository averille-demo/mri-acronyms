"""Test report creation."""

from mri_acronyms.create_report import save_report


def test_built_lut_table():
    """Check dynamically generated CSV report is updated."""
    assert save_report()
