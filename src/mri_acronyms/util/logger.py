"""Logging module."""

import logging
import sys
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from typing import Final

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent.parent.parent.parent
REPO_NAME: Final[str] = PROJECT_ROOT.stem.replace(" ", "_").replace("-", "_")
DEBUG: Final[bool] = True


def get_readable_size(path: Path) -> str:
    """Convert bytes to readable string."""
    if path.exists():
        size = float(path.stat().st_size)
    else:
        size = 0.0
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(size) < 1024.0:
            return f"({size:03.2f} {unit}B)"
        size /= 1024.0
    return f"({size:03.2f} YiB)"


def relative_size(
    path: Path,
) -> str:
    """Logging helper, truncate path relative to project level, add readable file size."""
    relative_path = path.as_posix().replace(PROJECT_ROOT.as_posix(), "")
    return f"{relative_path} {get_readable_size(path)}"


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

    def namer(name):
        """Move .log file extension to end after YYYY-MM-DD."""
        return name.replace(".log", "") + ".log"

    # save messages to log file
    fh = TimedRotatingFileHandler(filename=log_file, when="midnight", backupCount=5, encoding="utf8")
    fh.setLevel(level=logging.DEBUG)
    fh.setFormatter(fmt=log_format)
    fh.namer = namer
    logger.addHandler(hdlr=fh)

    # display messages to console
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(level=logging.INFO)
    sh.setFormatter(fmt=log_format)
    logger.addHandler(hdlr=sh)
    return logger
