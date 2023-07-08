#!/usr/bin/env bash

TARGET_SERVER=zero

ssh $TARGET_SERVER mv epical/_run.sh epical/run.sh
ssh $TARGET_SERVER mv epical/_run_and_halt.sh epical/run_and_halt.sh
