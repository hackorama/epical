#!/usr/bin/env bash
#
# Auto update calendar display daily using cron when Pi Zero is always connected
# to external power through USB cable.
#
# Add to crontab
#   $ crontab -e
#   $ crontab -l
#   SHELL=/bin/bash
#   0 1 * * * /home/hackorama/epical/run.sh > /home/hackorama/.epical/epical.log 2>&1  &
#
# Check run logs
#   $ tail -f ~/.epical/epical.log

set -e

INSTALL_ROOT=$HOME/epical
CONFIG_ROOT=$HOME/.epical

function run()  {

  # Update custom configuration if available
  [ -f "$CONFIG_ROOT"/config.py ] && cp "$CONFIG_ROOT"/config.py "$INSTALL_ROOT"/epical

  # Run screen refresh
  cd "$INSTALL_ROOT" || exit
  . venv/bin/activate
  cd epical || exit
  python main.py
}

run
