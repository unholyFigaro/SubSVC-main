#!/bin/sh
set -e

python manager.py db init
python manager.py db migrate
python main.py
