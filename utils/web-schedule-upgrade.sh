#!/usr/bin/env bash

TARGET_SERVER=mini

./package.sh
scp ../../backups/latest.tar hackorama@$TARGET_SERVER:/Users/hackorama/epical/web/server/static/epical.tar
