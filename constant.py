#!/usr/bin/env python3

import re
from re import Pattern
from typing import Final

DISCORD_API_BASE: Final[str] = "https://discord.com"
DISCORD_API_AT_ME: Final[str] = f"{DISCORD_API_BASE}/api/v9/users/@me"
DISCORD_API_GUILD: Final[str] = f"{DISCORD_API_BASE}/api/v9/guilds"

VERSION_NUMBER: Final[str] = "2.0"
SCRIPT_AUTHOR: Final[str] = "0xFantasy"

REQUEST_HEADERS: Final[dict] = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.6",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIwNjY1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
}

ANSI_ESCAPE: Final[Pattern] = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
