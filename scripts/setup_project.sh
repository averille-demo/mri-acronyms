#!/bin/bash
# updated: 2024-10-01
SCRIPT_NAME=$(basename "${BASH_SOURCE[0]}")
ROOT_CWD=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PROJECT_PATH="$(dirname "$ROOT_CWD")"
cd "$PROJECT_PATH" || exit

LOG_DIR="$PROJECT_PATH/logs"
mkdir -p "$(dirname "$LOG_FILE")"
find "$LOG_DIR" -maxdepth 1 -type f -name "*.log" -delete
SCRIPT_BASENAME="poetry_$(basename "${BASH_SOURCE::-3}")"
LOG_FILE="$LOG_DIR/$SCRIPT_BASENAME.log"

VENV_SUBFOLDERS=(".idea" ".venv" ".mypy_cache" ".ruff_cache" ".uv_cache" ".pytest_cache")
for SUBFOLDER in "${VENV_SUBFOLDERS[@]}"; do
    printf "  purging: %s\n" "$SUBFOLDER"
    if [[ -d "$PROJECT_PATH/$SUBFOLDER" ]]; then
        rm -r "${PROJECT_PATH:?}/$SUBFOLDER"
    fi
done

SETUP_FILES=(".python-version" "poetry.lock" "poetry.toml" "uv.lock")
for SETUP_FILE in "${SETUP_FILES[@]}"; do
    if [[ -f "$PROJECT_PATH/$SETUP_FILE" ]]; then
        printf "  purging: %s\n" "$SETUP_FILE"
        rm "${PROJECT_PATH:?}/$SETUP_FILE"
    fi
done

PYTHON_VERSION="3.12.5"
PROJECT=$(sed -n 's/^ *name.*=.*"\([^"]*\)".*/\1/p' "$PROJECT_PATH/pyproject.toml")
VERSION=$(sed -n 's/^ *version.*=.*"\([^"]*\)".*/\1/p' "$PROJECT_PATH/pyproject.toml")
PROJECT_VERSION="'$PROJECT' (v$VERSION)"

if [[ "$VERSION" =~ ^[0-9].[0-9].[0-9]$ ]];
then
    printf "%s %s running python v%s started: %s\n" "$SCRIPT_NAME" "$PROJECT_VERSION" "$PYTHON_VERSION" "$(date "+%Y-%m-%d %H:%M:%S %p")"
    # overwrite prior log file
    poetry --version | tee "$LOG_FILE"
    printf "Available python versions by pyenv:\n"
    pyenv install --list | grep -E " 3.11| 3.12"

    # append stdout to log (with '-a' flag)
    printf "Currently installed pyenv versions:\n"
    pyenv versions | tee -a "$LOG_FILE"
    # assign specific python version for local project (non-global)
    pyenv local "$PYTHON_VERSION" | tee -a "$LOG_FILE"

    # update poetry config
    poetry config virtualenvs.in-project true
    poetry config virtualenvs.prefer-active-python true
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
