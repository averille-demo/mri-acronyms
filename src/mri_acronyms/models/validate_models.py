"""Sanitize and dedup output."""

import re
import string
from typing import Dict, List, Union

from mri_acronyms.models.pulse_sequence_category import PulseSequenceCategory
from mri_acronyms.models.pydantic_models import MriParameterModel, MriSequenceModel
from mri_acronyms.util.constants import VALID_SYMBOLS
from mri_acronyms.util.logger import init_logger

log = init_logger(__file__)


def re_compile_symbol_pattern() -> re.Pattern:
    """Compiled once, used many.

    removes: punctuation/symbols: "!#$%&'+,.:;<=>?@[]^_`{|}~,"

    Returns:
        Pattern object for filtering desired punctuation/symbol chars
    """
    symbols = list(string.punctuation + "\t" + "\n")
    for valid_symbol in list(VALID_SYMBOLS):
        if valid_symbol in symbols:
            symbols.remove(valid_symbol)
    return re.compile("[" + re.escape("".join(symbols)) + "]")


RE_SYMBOL_PATTERN: re.Pattern = re_compile_symbol_pattern()


def sanitize(text: str):
    """Sanitize text value to remove invalid characters.

      removes: leading/trailing, most symbols, and consecutive whitespace chars.
         keep: period, hyphen, pipe, forward slash, and asterisk: ".-|/*"

    Args:
        text (str): raw string value

    Returns:
        sanitized input text as string
    """
    text = re.sub(pattern=RE_SYMBOL_PATTERN, repl="", string=text)
    text = re.sub(pattern=r"\s+", repl=" ", string=text)
    text = text.strip()
    return text


def dedup_acronyms(
    model: Union[MriParameterModel, MriSequenceModel],
) -> List[str]:
    """Remove duplicates and nulls from dataset.

    Args:
        model (MriAcronymModel): all vendor acronyms
            input: ('SPAIR', 'ASPIR', 'SPAIR', 'SPAIR', None)

    Returns:
        set of acronyms (no duplicates or null values) in sorted order
            output: ('aspir', 'spair')
    """
    unique_words = set()
    if isinstance(model, (MriSequenceModel, MriParameterModel)):
        unique_words.update(model.siemens)
        unique_words.update(model.ge)
        unique_words.update(model.philips)
        unique_words.update(model.canon)
        unique_words.update(model.hitachi)
    # drop empty strings
    if "" in unique_words:
        unique_words.remove("")
    # clean and sort results
    return sorted(sanitize(word) for word in unique_words)


def check_for_duplicate_categories() -> None:
    """Validate for duplicate keys in lookup table (e.g. 'turbo_spin_echo')."""
    model_to_category: Dict[str, List[str]] = {}
    for category in PulseSequenceCategory:
        for model in category.acronyms:
            if model.name not in model_to_category.keys():
                model_to_category[model.name] = [category.name]
            else:
                model_to_category[model.name].append(category.name)
    for model_name, categories in model_to_category.items():
        if len(categories) > 1:
            log.error(f"duplicate {model_name=} in {categories=}")


def check_for_duplicate_acronyms():
    """Checks if each acronym exists in another category (pulse-sequence/parameter).

    e.g., "HASTE" should only be found in 'single_shot_tse' not any other category.
    """
    acronym_to_category: Dict[str, List[str]] = {}
    for category in PulseSequenceCategory:
        for model in category.acronyms:
            for acronym in dedup_acronyms(model=model):
                keyword = f"{category.name}.{model.name}"
                if acronym not in acronym_to_category.keys():
                    acronym_to_category[acronym] = [keyword]
                else:
                    acronym_to_category[acronym].append(keyword)
    for acronym, categories in acronym_to_category.items():
        if len(categories) > 1:
            log.error(f"duplicate {acronym=} in {categories=}")


def check_for_duplicates():
    """Check for duplicate keys and values in MRI acronym mapping."""
    check_for_duplicate_categories()
    check_for_duplicate_acronyms()
