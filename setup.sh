#!/usr/bin/env bash
python -m pip install Pillow

set -o errexit

pip install -r dependencies.txt

python manage.py migrate