#!/usr/bin/env bash
#
# Do control checks with remote server before running the run script run_and_halt.sh
#
# Add to crontab
#   $ crontab -e
#   $ crontab -l
#   SHELL=/bin/bash
#   @reboot seep 60 && /home/hackorama/epical/check_run_and_halt.sh > /home/hackorama/.epical/epical.log 2>&1  &
#
# Check run logs
#   $ tail -f ~/.epical/epical.log

INSTALL_ROOT=$HOME/epical

function check_disable() {
  # First check if refresh is disabled and exit without refresh and halt
  if  wget -q --tries=2 --timeout=5 -O /dev/null "$CONTROL_URL"/disable
  then
    echo "CONTROL CHECK: Refresh disabled, device will not be halted"
    echo "Exiting, device will not be halted"
    exit
  else
    echo "CONTROL CHECK: No refresh disable"
  fi
}

function check_upgrade() {
  # Check for any new upgrade release package and deploy before refresh
  if  wget -q --tries=2 --timeout=5 -O "$INSTALL_ROOT"/../epical.tar "$CONTROL_URL"/epical.tar
  then
    echo "CONTROL CHECK: Found package"
    echo "Deploying to $INSTALL_ROOT/.. ..."
    cd "$INSTALL_ROOT"/.. || exit
    tar -xf epical.tar
    cd - || exit
  else
    echo "CONTROL CHECK: No package to deploy"
  fi
}

function check()  {
  CONTROL_URL=$(grep CONTROL_SERVER_URL "$INSTALL_ROOT"/epical/config.py |  cut -d '=' -f 2 | xargs)

  echo "CONTROL CHECK: Server $CONTROL_URL"

  if wget -q --tries=2 --timeout=5 -O /dev/null "$CONTROL_URL"
  then
    check_upgrade
    check_disable
  else
    echo "CONTROL CHECK: Server down, no checks"
  fi
}

function run() {
  check
  . "$INSTALL_ROOT"/run_and_halt.sh
}

run
