#!/usr/bin/env bash
#
# On system boot update calendar display and shutdown Pi Zero.
# With pre lead time (added in crontab) and minimum up time
# to allow ssh login to cancel the update and/or shutdown
#
# This is useful when running from a battery pack to save power.
#
# Add to crontab
#   $ crontab -e
#   $ crontab -l
#   SHELL=/bin/bash
#   @reboot seep 60 && /home/hackorama/epical/run_and_halt.sh > /home/hackorama/.epical/epical.log 2>&1  &
#
# Check run logs
#   $ tail -f ~/.epical/epical.log

set -e

INSTALL_ROOT=$HOME/epical
CONFIG_ROOT=$HOME/.epical

HALT_AFTER_SECONDS=180

SECONDS=0 # Bash internal variable for elapsed seconds https://tldp.org/LDP/abs/html/internalvariables.html

function finally() {
  # Check minimum up time before halt, allows lead time to override/cancel the halt command
  WAIT_SECONDS=$((HALT_AFTER_SECONDS - SECONDS))
  if [ $WAIT_SECONDS -gt 0 ]
  then
    echo "Will halt in $WAIT_SECONDS seconds ..."
    sleep $WAIT_SECONDS
  fi
  sudo halt
}

# Use bash trap to wait and halt on exit including any exit from errors
# https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_12_02.html
trap finally EXIT

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

