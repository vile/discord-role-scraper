#!/usr/bin/env python3

import re
from re import Pattern
from typing import Final

DISCORD_API_VERSION: Final[str] = "v9"
DISCORD_API_BASE: Final[str] = "https://discord.com"
DISCORD_API_AT_ME: Final[str] = f"{DISCORD_API_BASE}/api/{DISCORD_API_VERSION}/users/@me"
DISCORD_API_GUILD: Final[str] = f"{DISCORD_API_BASE}/api/{DISCORD_API_VERSION}/guilds"

VERSION_NUMBER: Final[str] = "3.0"
SCRIPT_AUTHOR: Final[str] = "https://github.com/Vile"

REQUEST_HEADERS: Final[dict] = {
    "accept": "*/*",
    "accept-language": "en-US",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1054 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDU0Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjEwNTQgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNjE5NzMsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQzMTQzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
}

ANSI_ESCAPE: Final[Pattern] = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
