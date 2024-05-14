.PHONY: all deps start

all: deps start

deps :
	poetry config virtualenvs.in-project true
	poetry install --no-root

start :; poetry run python3 main.py
