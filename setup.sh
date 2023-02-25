#!/usr/bin/env bash
# python -m pip install Pillow
set -o errexit

pip install -r dependencies.txt

python manage.py collectstatic --no-input
python manage.py migrate