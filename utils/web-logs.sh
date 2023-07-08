#!/usr/bin/env bash

TARGET_SERVER=mini

ssh $TARGET_SERVER cat epical/web/server/server.log
