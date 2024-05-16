# Discord Role Scraper

![Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fvile%2Fdiscord-role-scraper%2Fmaster%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&label=python)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

A simple Python script used to scrape Discord guild info and roles.

## Requirements

1. Git - [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
   1. Check if you have Git installed with `git --version`
2. Python (>=3.11) - [Install Python (Windows)](https://www.python.org/downloads/windows/), [Install Python (Linux)](https://docs.python.org/3/using/unix.html) (see [pyenv](https://github.com/pyenv/pyenv))
   1. Check if you have Python installed with `python3 --version`
3. Pip - [Install Pip](https://pip.pypa.io/en/stable/installation/)
   1. Check if you have Pip installed with `pip --version`
4. Poetry - [Install Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) (preferrably with [pipx](https://github.com/pypa/pipx))
   1. Check if you have Poetry installed with `poetry --version`

### Additional Requirements

1. PyInstaller - [Install PyInstaller](https://pyinstaller.org/en/stable/) (preferrably with [pipx](https://github.com/pypa/pipx))
   1.  Check if you have Poetry installed with `pyinstaller --version`
   2.  PyInstaller is platform dependent, if you want to build .exe files, you must build on Windows

## Usage (Linux)

### Quick Start

```bash
git clone https://github.com/vile/discord-role-scraper.git
cd discord-role-scraper
make
```

### Interacting with the script

After starting the script, follow the prompts given to input your token and server ID.

## Usage (Windows)

### Quick Start (exe)

Download the latest `windows-release.zip` file from the [releases tab](https://github.com/vile/discord-role-scraper/releases).
Then, unzip with your choice of zip tool (WinRAR, 7zip, NanaZip, etc.), and double click `DiscordRoleScraper.exe`.

### Interacting with the script

After starting the script, follow the prompts given to input your token and server ID.

## Editing config.toml

The `config.toml` file contains all of the editable settings for this script. Any value under the `permissions_to_scrape` section that starts with `0x` should be commented out instead of having its value changed.

### Export Results

<details>

| Name           | type   | Default Value | Description                                   |
| -------------- | ------ | ------------- | --------------------------------------------- |
| EXPORT_RESULTS | `bool` | `True`        | Whether or not to export txt files of scrapes |

</details>

### Scrape Guild Info

<details>

| Name              | type   | Default Value | Description                               |
| ----------------- | ------ | ------------- | ----------------------------------------- |
| SCRAPE_GUILD_INFO | `bool` | `True`        | Whether or not to scrape the guild's info |


| Name                 | Default Value |
| -------------------- | ------------- |
| id                   | `True`        |
| name                 | `True`        |
| icon                 | `False`       |
| description          | `True`        |
| home_header          | `False`       |
| splash               | `False`       |
| discovery_splash     | `False`       |
| features             | `False`       |
| banner               | `False`       |
| owner_id             | `True`        |
| application_id       | `False`       |
| region               | `True`        |
| afk_channel_id       | `False`       |
| afk_timeout          | `False`       |
| system_channel_id    | `False`       |
| system_channel_flags | `False`       |
| widget_enabled       | `False`       |
| widget_channel_id    | `False`       |
| verification_level   | `True`        |

</details>

### Scrape Permission Info

<details>

| Name                   | type   | Default Value | Description                                                                             |
| ---------------------- | ------ | ------------- | --------------------------------------------------------------------------------------- |
| SCRAPE_PERMISSION_INFO | `bool` | `True`        | Whether or not to scrape the guild's roles and associated permissions and/or properties |

All values starting with `0x` **can not be changed**, if you wish to not see (disable) a specific permission in your scrapes, comment the line (using a `#`). Changing any of the `0x` values will break calculations associated with checking permissions.

| Name             | Type    | Default Value |
| ---------------- | ------- | ------------- |
| name             | `bool`  | `True`        |
| position         | `bool`  | `True`        |
| id               | `bool`  | `True`        |
| mentionable      | `bool`  | `True`        |
| administrator    | bitwise |
| mention all      | bitwise |
| manage guild     | bitwise |
| manage roles     | bitwise |
| manage channels  | bitwise |
| manage events    | bitwise |
| manage nicknames | bitwise |
| kick members     | bitwise |
| ban members      | bitwise |
| webhooks         | bitwise |
| app commands     | bitwise |
| tags             | `bool`  | `True`        |

</details>

## FAQ

### Is my token safe?

Yes, your token is safe, it is only temporarily cached in memory for convience if you want to scrape multiple servers in the same session.
After closing the script, your token is removed from memory.
Your token is never saved on your computer, and is only ever sent to the official Discord API.

### Will this get my account terminated?

You're interacting with normally available API endpoints for user accounts in a normal way.
However, Discord doesn't like when you script or automate any type of action, therefore there is always a risk of account termination.
I am not responsible if you spam the API scraping servers and get your account terminated.
It is recommended to use a brand new or alt account.

### Can you help me with ...?

No, I will not help you with this script (follow the [Linux](#usage-linux) and [Windows](#usage-windows) sections above).
No, I will not make you any scripts.