import re
from pathlib import Path
from re import Pattern
from typing import Final

# fmt: off
CONFIG_FILE_PATH: Final[Path] = Path("config.toml")
EXPORT_FILE_PATH: Final[Path] = Path("./export")

DISCORD_API_VERSION: Final[str] = "v9"
DISCORD_API_BASE: Final[str] = f"https://discord.com/api/{DISCORD_API_VERSION}"
DISCORD_API_AT_ME: Final[str] = f"{DISCORD_API_BASE}/users/@me"
DISCORD_API_GUILD: Final[str] = f"{DISCORD_API_BASE}/guilds"

VERSION_NUMBER: Final[str] = "0.3.0"
SCRIPT_AUTHOR: Final[str] = "https://github.com/Vile"
REPO_URL: Final[str] = "https://github.com/vile/discord-role-scraper"

REQUEST_HEADERS: Final[dict] = {
    "accept": "*/*",
    "accept-language": "en-US",
    "origin": "https://discord.com",
    "referer": "https://discord.com/channels/@me",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZSwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzMi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTMyLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM2MjM5MiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    "authorization": None,
}

ANSI_ESCAPE: Final[Pattern] = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
