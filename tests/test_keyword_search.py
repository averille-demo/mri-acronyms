"""Test keyword matching logic."""

import random
import string

from mri_acronyms.search_by_keyword import get_random_words, get_valid_words, match_acronym
from mri_acronyms.util.constants import VALID_SYMBOLS


def test_check_valid_words():
    """Check if valid keywords return True."""
    for keyword in get_valid_words():
        result = match_acronym(keyword=keyword)
        assert result


def test_check_random_words():
    """Check if randomized invalid keywords return False."""
    for keyword in get_random_words(sample_size=16):
        result = match_acronym(keyword=keyword, cutoff=75.0)
        assert not result


def test_check_words_with_valid_symbols():
    """Check if keyword (with allowed symbol suffix) return True (positive match)."""
    symbols = list(VALID_SYMBOLS)
    for keyword in get_valid_words():
        # append random symbol to end of valid keyword
        result = match_acronym(keyword=f"{keyword}{random.choice(symbols)}")
        assert result


def test_check_words_with_invalid_symbols():
    """Check if keyword (with illegal symbol suffix) return True (still able to match)."""
    symbols = list(set(string.punctuation + "\t" + "\n" + " ").difference(set(VALID_SYMBOLS)))
    for keyword in get_valid_words():
        # append random symbol to end of valid keyword
        result = match_acronym(keyword=f"{keyword}{random.choice(symbols)}")
        assert result


def test_check_valid_substrings():
    """Check if valid substrings are positive match."""
    for keyword in get_valid_words():
        if " " in keyword:
            words = keyword.split(" ")
            pick = random.randint(0, len(words) - 1)
            substring = words[pick]
            if len(substring) > 7:
                result = match_acronym(keyword=substring, cutoff=50.0)
                assert result
