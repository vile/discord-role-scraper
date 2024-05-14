.PHONY: all deps start clean remove-exports remove-env 

all: deps start

deps :
	poetry config virtualenvs.in-project true
	poetry install --no-root

start :; poetry run python3 main.py

### Clean
clean: remove-exports remove-venv 

remove-exports :; rm -rf export/*

remove-venv :; rm -rf .venv