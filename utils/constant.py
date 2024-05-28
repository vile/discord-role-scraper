import re
from re import Pattern
from typing import Final

# fmt: off
DISCORD_API_VERSION: Final[str] = "v9"
DISCORD_API_BASE: Final[str] = "https://discord.com"
DISCORD_API_AT_ME: Final[str] = f"{DISCORD_API_BASE}/api/{DISCORD_API_VERSION}/users/@me"
DISCORD_API_GUILD: Final[str] = f"{DISCORD_API_BASE}/api/{DISCORD_API_VERSION}/guilds"

VERSION_NUMBER: Final[str] = "0.2.3"
SCRIPT_AUTHOR: Final[str] = "https://github.com/Vile"

REQUEST_HEADERS: Final[dict] = {
    "accept": "*/*",
    "accept-language": "en-US",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.1072 Chrome/120.0.6099.291 Electron/28.2.10 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJwdGIiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC4xMDcyIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjEwNzIgQ2hyb21lLzEyMC4wLjYwOTkuMjkxIEVsZWN0cm9uLzI4LjIuMTAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjI4LjIuMTAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTY0NTgsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ4MTY2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsLCJkZXNpZ25faWQiOjB9",
}

ANSI_ESCAPE: Final[Pattern] = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
