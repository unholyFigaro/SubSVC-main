#!/bin/sh
set -e

python manager.py db migrate
python manager.py db upgrade
python main.py
