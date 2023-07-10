#!/bin/bash
# updated: 2023-06-30
SCRIPT_NAME=$(basename "${BASH_SOURCE[0]}")
ROOT_CWD=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PROJECT_PATH="$(dirname "$ROOT_CWD")"
cd "$PROJECT_PATH"

SCRIPT_BASENAME="poetry_$(basename "${BASH_SOURCE::-3}")"
LOG_FILE="$PROJECT_PATH/logs/$SCRIPT_BASENAME.log"
mkdir -p "$(dirname "$LOG_FILE")"

PYTHON_VERSION="3.11.0"
PROJECT=$(sed -n 's/^ *name.*=.*"\([^"]*\)".*/\1/p' "$PROJECT_PATH/pyproject.toml")
VERSION=$(sed -n 's/^ *version.*=.*"\([^"]*\)".*/\1/p' "$PROJECT_PATH/pyproject.toml")
PROJECT_VERSION="'$PROJECT' (v$VERSION)"

if [[ "$VERSION" =~ ^[0-9].[0-9].[0-9]$ ]];
then
    printf "%s %s running python v%s started: %s\n" "$SCRIPT_NAME" "$PROJECT_VERSION" "$PYTHON_VERSION" "$(date "+%Y-%m-%d %H:%M:%S %p")"
    # overwrite prior log file
    poetry --version | tee "$LOG_FILE"
    printf "Available python versions by pyenv:\n"
    pyenv install --list | grep " 3.10\|3.11"
    # append stdout to log (with '-a' flag)
    printf "Currently installed pyenv versions:\n"
    pyenv versions | tee -a "$LOG_FILE"
    # assign specific python version for local project (non-global)
    pyenv local "$PYTHON_VERSION" | tee -a "$LOG_FILE"

    # update poetry config
    poetry config virtualenvs.in-project true
    poetry config virtualenvs.prefer-active-python true
    # poetry config --local installer.no-binary :all:
    poetry config --list | tee -a "$LOG_FILE"

    printf "\nValidating %s pyproject.toml:\n" "$PROJECT_VERSION"
    # validate pyproject.toml file
    poetry check | tee -a "$LOG_FILE"
    # create pyproject.lock file
    poetry lock | tee -a "$LOG_FILE"

    # update pip in .venv
    poetry run python -m pip install --upgrade pip | tee -a "$LOG_FILE"
    printf "\nInstalling %s to virtualenvs.in-project:\n" "$PROJECT_VERSION"
    poetry install -v | tee -a "$LOG_FILE"

    printf "\nInstalled %s python version:\n" "$PROJECT_VERSION"
    poetry run python --version | tee -a "$LOG_FILE"

    printf "\nAdding: '%s' to git safe.directory:\n" "$(basename "$PROJECT_PATH")"
    GIT_CONFIG=$(git config --get-all safe.directory "$PROJECT_PATH")
    # only add path if safe.directory if not already configured (avoid duplicates)
    if [[ "$PROJECT_PATH" != *"$GIT_CONFIG"* ]];
    then
        git config --global --add safe.directory "$PROJECT_PATH"
    fi
    git config --show-scope --get-all safe.directory "$(basename "$PROJECT_PATH")"

    printf "\nInstalling %s pre-commit hooks:\n" "$PROJECT_VERSION"
    poetry run pre-commit autoupdate | tee -a "$LOG_FILE"
    poetry run pre-commit install --install-hooks | tee -a "$LOG_FILE"
    printf "%s %s completed: %s\n" "$SCRIPT_NAME" "$PROJECT_VERSION" "$(date "+%Y-%m-%d %H:%M:%S %p")"
fi
