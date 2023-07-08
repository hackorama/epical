#
# Please run: make help
#
# Note: The commands are run with && to run inside the venv shell
#

help:		## Show help
		@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

deps:		## Install required python packages
		mkdir -p ~/.epical
		test -d venv || python3 -m venv venv
		test -d epd/lib || (cd epd && ./download.sh && cd -)
		. venv/bin/activate && which python3 && python3 -m pip install --upgrade pip && pip3 -q install -r requirements.txt

dev_deps:	## Install required dev python packages
dev_deps: deps
		test -d venv || python3 -m venv venv
		. venv/bin/activate && which python3 && python3 -m pip install --upgrade pip && pip3 -q install -r dev.requirements.txt
check:		## Run python code checks
check: dev_deps
		. venv/bin/activate && isort ./epical &&  black epical && pylint --recursive=y epical && mypy epical

tests:		## Run tests
tests: check
		. venv/bin/activate && cd tests && coverage run -m pytest --capture=tee-sys --log-cli-level=INFO && coverage report --omit="../epd/*","../grid/*" && cd -

run:		## Run display test
run: deps
		. venv/bin/activate && cd epical && python main.py && cd -

