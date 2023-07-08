#!/usr/bin/env bash
#
# Download Waveshare EPD ePaper display driver lib for Waveshare epd12in48b_V2 ePaper display
#

set -e

GITHUB_REPO_ROOT="https://raw.githubusercontent.com/waveshareteam/12.48inch-e-paper/master/RaspberryPi/python/lib"

echo "Downloading EPD libs from $GITHUB_REPO_ROOT into ./lib".

mkdir -p ./lib

wget -q -O ./lib/DEV_Config_32.so "$GITHUB_REPO_ROOT/DEV_Config_32.so"
wget -q -O ./lib/DEV_Config_64.so "$GITHUB_REPO_ROOT/DEV_Config_64.so"
wget -q -O ./lib/__init__.py "$GITHUB_REPO_ROOT/__init__.py"
wget -q -O ./lib/epd12in48b_V2.py "$GITHUB_REPO_ROOT/epd12in48b_V2.py"
wget -q -O ./lib/epdconfig.py "$GITHUB_REPO_ROOT/epdconfig.py"

ls ./lib

