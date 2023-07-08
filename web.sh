#!/usr/bin/env bash
#
# Update calendar display on-demand using web server : epical/web/server)
#
# Logs and screen refreshed images will go to web/server/static
#

set -e

cd /home/hackorama/epical || exit
. venv/bin/activate
cd epical || exit
python main.py > web/server/static/epical.log 2>&1
cp epical*.png web/server/static
