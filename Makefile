.PHONY: all deps start build clean remove-exports remove-env remove-build-artifacts remove-dist remove-pycache sudo-act

all: clean deps start

deps :
	poetry config virtualenvs.in-project true
	poetry install --no-root

start :; poetry run python3 main.py

### Build

# This is only intended to be used for Linux builds with Poetry (venv)
build: remove-build-artifacts remove-dist _build

_build :
	PYTHON_VERSION=$$(cat .python-version); \
	SITE_PACKAGES=".venv/lib/python$$PYTHON_VERSION/site-packages"; \
	pyinstaller main.py --onefile --name DiscordRoleScraper --paths $$SITE_PACKAGES

### Clean

clean: remove-exports remove-venv remove-pycache remove-build-artifacts remove-dist

remove-exports :; rm -rf export/*

remove-venv :; rm -rf .venv

remove-build-artifacts :; rm -rf build

remove-dist :; rm -rf dist

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
sudo-act :
	mkdir -p tmp/artifacts
	sudo env "PATH=$$PATH" act $(ACTION) $(FLAGS) $(ARTIFACTS_PATH) \
	--artifact-server-path /tmp/artifacts
	rm -rf tmp