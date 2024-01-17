#!/bin/sh
set -e

python manage.py migrate
python manage.py main.py
