.PHONY: all deps start clean remove-exports remove-env 

all: deps start

deps :
	poetry config virtualenvs.in-project true
	poetry install --no-root

start :; poetry run python3 main.py

### Clean
clean: remove-exports remove-venv remove-pycache

remove-exports :; rm -rf export/*

remove-venv :; rm -rf .venv

# https://stackoverflow.com/a/41386937
# Will remove pycache files under .venv/ as well
# Slightly modified to work with Make ($ -> $$)
remove-pycache :; find . -regex '^.*\(__pycache__\|\.py[co]\)$$' -delete