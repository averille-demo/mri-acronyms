#!/bin/bash
# updated: 2023-06-30
SCRIPT_NAME=$(basename "${BASH_SOURCE[0]}")
ROOT_CWD=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PROJECT_PATH="$(dirname "$ROOT_CWD")"
cd "$PROJECT_PATH"

SCRIPT_BASENAME="poetry_$(basename "${BASH_SOURCE::-3}")"
LOG_FILE="$PROJECT_PATH/logs/$SCRIPT_BASENAME.log"
mkdir -p "$(dirname "$LOG_FILE")"

PROJECT=$(sed -n 's/^ *name.*=.*"\([^"]*\)".*/\1/p' "$PROJECT_PATH/pyproject.toml")
VERSION=$(sed -n 's/^ *version.*=.*"\([^"]*\)".*/\1/p' "$PROJECT_PATH/pyproject.toml")
PROJECT_VERSION="'$PROJECT' (v$VERSION)"

if [[ "$VERSION" =~ ^[0-9].[0-9].[0-9]$ ]];
then
    printf "%s %s started: %s\n" "$SCRIPT_NAME" "$PROJECT_VERSION" "$(date "+%Y-%m-%d %H:%M:%S %p")"
    # overwrites prior log
    poetry run python --version | tee "$LOG_FILE"

    # append stdout to log (with '-a' flag)
    poetry self lock
    poetry self install --sync | tee -a "$LOG_FILE"
    poetry self update | tee -a "$LOG_FILE"

    poetry run python -m pip install --upgrade pip | tee -a "$LOG_FILE"
    poetry update -v | tee -a "$LOG_FILE"
    poetry run pre-commit autoupdate | tee -a "$LOG_FILE"
    printf "%s %s completed: %s\n" "$SCRIPT_NAME" "$PROJECT_VERSION" "$(date "+%Y-%m-%d %H:%M:%S %p")"
fi
