#!/usr/bin/env bash
# exit on error
set -o errexit
command -v pip || { curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py && python get-pip.py; }
pip install -r requirements.txt

python manage.py collectstatic --no-input
