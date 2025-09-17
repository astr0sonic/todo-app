#!/usr/bin/env bash

set -e

python3.13 -m venv --clear .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
deactivate
