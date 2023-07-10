"""Logging module."""
import logging
import sys
from pathlib import Path
from typing import Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent.parent.parent
REPO_NAME = PROJECT_ROOT.stem.replace("-", "_")
DEBUG: Final[bool] = True


def get_readable_size(path: Path) -> str:
    """Convert bytes to readable string."""
    size = float(path.stat().st_size)
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(size) < 1024.0:
            return f"{size:03.2f} {unit}B"
        size /= 1024.0
    return f"{size:03.2f} YiB"


def relative_size(
    path: Path,
) -> str:
    """Logging helper, truncate path relative to project level, add readable file size."""
    relative_path = path.as_posix().replace(PROJECT_ROOT.as_posix(), "")
    return f"{relative_path} ({get_readable_size(path)})"


def init_logger(
    caller: str,
) -> logging.Logger:
    """Generate custom Logger object writes output to both file and standard output.

    Creates parent directories and blank log file (if missing)
    https://docs.python.org/3/library/logging.html#logging-levels

    Args:
        caller (str): __file__ of calling module passed to getLogger()

    Returns:
        logging.Logger: instance based on name and file location
    """
    # create log directory and empty file (if needed)
    log_file = Path(PROJECT_ROOT, "logs", f"{REPO_NAME}.log")
    if not log_file.parent.exists():
        log_file.parent.mkdir(parents=True, exist_ok=True)
    if not log_file.is_file():
        log_file.touch(mode=0o777, exist_ok=True)

    # when passing __file__, set to caller basename
    logger = logging.getLogger(name=Path(caller).name)
    logger.setLevel(level=logging.INFO)

    # update custom log format
    log_format = logging.Formatter(
        fmt="{asctime} [{levelname}] {name} | {funcName}() line:{lineno} | {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{",
        validate=True,
    )

    # save messages to log file
    file_handler = logging.FileHandler(filename=log_file)
    file_handler.setLevel(level=logging.DEBUG)
    file_handler.setFormatter(fmt=log_format)
    logger.addHandler(hdlr=file_handler)

    # display messages to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level=logging.INFO)
    console_handler.setFormatter(fmt=log_format)
    logger.addHandler(hdlr=console_handler)
    return logger
