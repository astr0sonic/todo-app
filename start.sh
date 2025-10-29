#!/usr/bin/env bash

set -e

source .venv/bin/activate
export PYTHONPATH="$(PWD)"
python src/db_examples_orm.py
