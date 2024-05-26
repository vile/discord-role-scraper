.PHONY: all deps start clean remove-exports remove-env remove-pycache sudo-act

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

### Local Act Workflows

# Example usage: 
# 	- make sudo-act ACTION=push
# 	- make sudo-act ACTION=push FLAGS="--secret-file workflow.secrets"
# Depending on your Docker installation, sometimes Act 
# doesnt have permission to interact with your docker daemon
sudo-act :; sudo env "PATH=$$PATH" act $(ACTION) $(FLAGS)