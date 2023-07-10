"""Search for given MRI pulse sequence / parameter category based on keyword."""
import random
import string
from typing import Any, Dict, List, Tuple, Union

from english_words import get_english_words_set
from rapidfuzz import fuzz

from mri_acronyms.lut.category_to_acronym_lut import CATEGORY_TO_ACRONYM_LUT
from mri_acronyms.models.pulse_sequence_category import PulseSequenceCategory
from mri_acronyms.models.pydantic_models import MriParameterModel, MriSequenceModel
from mri_acronyms.util.constants import VALID_SYMBOLS
from mri_acronyms.util.logger import init_logger

ASCII_LETTERS = list(string.ascii_letters + string.digits + VALID_SYMBOLS)
ENGLISH_WORDS = list(get_english_words_set(sources=["web2"], alpha=True, lower=False))


log = init_logger(caller=__file__)


def create_random_text(
    length: int,
) -> str:
    """Create random ASCII text."""
    random_letters = [random.choice(ASCII_LETTERS) for c in range(0, length)]
    result = "".join(random_letters)
    return result


def create_random_word() -> str:
    """Create random english word."""
    return random.choice(ENGLISH_WORDS)


def get_random_words(
    sample_size: int,
) -> List[str]:
    """Generate random words.

    Args:
        sample_size (int): size of sample as subset of wordlist

    Returns:
        list: randomly generated words
    """
    random_words = []
    for i in range(sample_size):
        random_words.append(create_random_word())
        random_words.append(create_random_text(length=random.randint(8, 16)))
    return random.sample(population=random_words, k=sample_size)


def get_valid_words() -> List[str]:
    """Generate list of valid words, with mixture of upper/lowercase words.

    Returns:
        list: subset words
    """
    mixed_case_words = []
    for category in CATEGORY_TO_ACRONYM_LUT.keys():
        for acronyms in CATEGORY_TO_ACRONYM_LUT[category].values():
            for acronym in acronyms:
                # intentionally create mixed case words
                options = [
                    acronym.swapcase(),
                    acronym.upper(),
                    acronym.lower(),
                    acronym.title(),
                ]
                mixed_case_words.append(random.choice(options))
        random.shuffle(mixed_case_words)
    return mixed_case_words


def get_sample(
    sample_size: int,
    include_random: bool,
) -> List[str]:
    """Create random sample of words, with mixture of upper/lowercase words.

    Args:
        sample_size (int): size of sample as subset of wordlist
        include_random (bool): include random words

    Returns:
        subset list of words based on sample size
    """
    population = get_valid_words()
    if include_random:
        random_words = get_random_words(sample_size=int(len(population) / 10))
        population.extend(random_words)
    return random.sample(population=population, k=sample_size)


def match_words():
    """Wrapper to generate sample data."""
    for keyword in get_sample(sample_size=20, include_random=True):
        match_acronym(keyword=keyword)


def find_closest_match(keyword: str, acronyms: List) -> Tuple[str, float]:
    """Use fuzzy pattern matching (case insensitive) to find closest match.

    Returns:
        tuple: acronym found in list (string), corresponding confidence as percentage (float)
    """
    confidences = []
    for acronym in acronyms:
        fuzz_ratio = round(fuzz.ratio(s1=keyword.lower(), s2=acronym.lower()), 4)
        confidences.append(fuzz_ratio)
    # get index to element in list with highest similarity match
    match = confidences.index(max(confidences))
    return acronyms[match], confidences[match]


def match_acronym(keyword: str, cutoff: float = 70.0) -> Union[MriParameterModel, MriSequenceModel, None]:
    """Perform case-insensitive search by keyword.

    Args:
        keyword (str): word to search against acronym list
        cutoff (float): threshold for matching percentage (if < #.##%, no match is found)

    Returns:
        if match is found: returns relevant MRI pulse sequence/parameter model
    """
    model = None
    results: Dict[str, Any] = {
        "keyword": keyword,
        "candidates": [],
    }
    if isinstance(keyword, str) and len(keyword) > 1:
        for category in CATEGORY_TO_ACRONYM_LUT.keys():
            for name, acronyms in CATEGORY_TO_ACRONYM_LUT[category].items():
                acronym, confidence = find_closest_match(keyword, acronyms)
                results["candidates"].append(
                    {
                        "category": category,
                        "name": name,
                        "acronym": acronym,
                        "confidence": confidence,
                    }
                )
                # optimization: skip scanning once identical match is found
                if confidence == 100.0:
                    break
    # find highest confidence in candidates
    scores = [result["confidence"] for result in results["candidates"]]
    match = scores.index(max(scores))
    confidence = results["candidates"][match]["confidence"]
    if cutoff < confidence:
        model = PulseSequenceCategory.get_model(
            category=results["candidates"][match]["category"],
            name=results["candidates"][match]["name"],
        )
        print(f"MATCH: {keyword:32s}\t {confidence=:0.2f}%\t {model=}")
    else:
        log.error(f"{keyword:32s}\t {confidence=:0.2f}%\t {model=}")
    return model


if __name__ == "__main__":
    match_words()
