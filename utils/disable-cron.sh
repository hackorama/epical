#!/usr/bin/env bash

TARGET_SERVER=zero


until ssh $TARGET_SERVER mv epical/run_and_halt.sh epical/_run_and_halt.sh
do
  echo "."
  sleep 1
done

ssh $TARGET_SERVER mv epical/run.sh epical/_run.sh;
