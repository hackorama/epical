#!/usr/bin/env bash

TARGET_SERVER=zero

ssh $TARGET_SERVER date > .epical/battery
