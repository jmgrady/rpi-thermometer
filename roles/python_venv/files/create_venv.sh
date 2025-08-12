#! /usr/bin/env bash

python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip pip-tools
python -m piptools compile --upgrade requirements.in
python -m piptools sync requirements.txt
