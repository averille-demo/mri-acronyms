"""Convert lookup tables to '.csv' report."""

from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from mri_acronyms.models.pulse_sequence_category import PulseSequenceCategory
from mri_acronyms.models.validate_models import check_for_duplicates
from mri_acronyms.util.constants import HEADERS, SEP
from mri_acronyms.util.logger import PROJECT_ROOT, init_logger, relative_size

log = init_logger(caller=__file__)

pd.set_option("display.max_rows", 128)
pd.set_option("expand_frame_repr", False)
pd.set_option("display.max_columns", 16)
pd.set_option("display.max_colwidth", 36)


def check_and_purge(path: Path) -> None:
    """Create parent output folder (if not exists).

    Args:
        path (Path): destination file path (with extension)

    Returns:
        bool: true if file was purged successfully
    """
    try:
        if not path.parent.is_dir():
            path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_file():
            print(f" purged: '{path.name}'\t ({path.stat().st_size} bytes)")
            path.unlink(missing_ok=False)
    except (OSError, PermissionError):
        log.exception(f"{relative_size(path)}")


def build_data_records() -> List[List[Any]]:
    """Convert key/value dictionary to list of lists for pandas.

       [Order, Category, Sequence/Parameter", "Siemens", "GE", "Philips", "Canon", "Hitachi"]

    Returns list:
        [ balanced_steady_state_gradient_echo,
            TrueFISP,   FIESTA; COSMIC,    Balanced FFE,  True SSFP,  Balanced SARGE; BASG ]
        | <-Siemens-> | <-----GE------> | <--Philips--> | <-Canon-> | <-----Hitachi------> |
    """
    data_rows = []
    check_for_duplicates()
    for category in PulseSequenceCategory:
        for acronym in category.acronyms:
            # init per-row list, with key as first element (1st column in pandas)
            row = [
                category.order,
                category.name.lower(),
                acronym.name,
                SEP.join(acronym.siemens),
                SEP.join(acronym.ge),
                SEP.join(acronym.philips),
                SEP.join(acronym.canon),
                SEP.join(acronym.hitachi),
            ]
            data_rows.append(row)
    return data_rows


def save_report(
    path=Path(PROJECT_ROOT, "data", "mri_vendor_acronyms.csv"),
) -> bool:
    """Save results to '.csv' file extension with comma ',' field delimiter (github prettifier support).

    Args:
        path (Path): destination file path (with extension)
            creates parent directory if destination folder does not exist

    Returns:
        bool: true, if report was created successfully
    """
    try:
        check_and_purge(path)
        records = build_data_records()
        if isinstance(records, (List, Dict)):
            df = pd.DataFrame.from_records(data=records, columns=HEADERS)
            # sort by 'Group' then 'Category'
            df.sort_values(by=[HEADERS[0], HEADERS[1]], ascending=[True, True], inplace=True)
            df.to_csv(
                path_or_buf=path,
                sep=",",  # comma for field delimiter
                encoding="utf-8",
                quoting=1,  # fully quoted
                quotechar='"',
                index=False,
                header=True,
            )
            if path.is_file():
                print(f"preview: '{path.name}'")
                print(df.to_string(index=False))
                log.info(f"saved: {relative_size(path)} {df.shape[0]} rows")
                return True
    except (pd.errors.ParserError, pd.errors.DtypeWarning):
        log.exception(f"{relative_size(path)}")
    return False


if __name__ == "__main__":
    save_report()
