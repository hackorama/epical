#!/usr/bin/env bash

# Local back up packaging

TS=$(date '+%Y%m%d.%H%M%S')
BACKUP_SERVER=mini

cd ../..
rm -rf .epical
cp -r ~/.epical .epical
xattr -rc ./epical
xattr -rc ./.epical
tar --exclude-vcs --exclude 'venv' --exclude '.idea' --exclude '.ruff_cache' --exclude '__pycache__' --exclude '.mypy_cache' --exclude '.pytest_cache' --exclude '.DS_Store' --exclude '*.tar' -cvf backups/epical."$TS".tar ./epical ./.epical
scp backups/epical."$TS".tar hackorama@$BACKUP_SERVER:~/
cd backups || exit
ln -fs epical."$TS".tar latest.tar
cd ../epical || exit
