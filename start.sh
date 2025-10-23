#!/usr/bin/env bash

set -e

source .venv/bin/activate
export PYTHONPATH="$(PWD)"
python src/create_tables.py
