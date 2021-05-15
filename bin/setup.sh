#!/bin/bash

# Install Poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Install packages
poetry install --no-dev
