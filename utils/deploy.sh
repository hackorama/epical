#!/usr/bin/env bash

TARGET_SERVER=zero

./package.sh
scp ../../backups/latest.tar hackorama@$TARGET_SERVER:/tmp/latest.tar
ssh $TARGET_SERVER tar -xvf /tmp/latest.tar
