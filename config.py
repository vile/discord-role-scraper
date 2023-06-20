#!/usr/bin/env python3

from typing import Final

EXPORT_RESULTS: Final[bool] = True

SCRAPE_GUILD_INFO: Final[bool] = True
GUILD_INFO_TO_SCRAPE: Final[list[bool]] = {
    "id": True,
    "name": True,
    "icon": False,
    "description": True,
    "home_header": False,
    "splash": False,
    "discovery_splash": False,
    "features": False,
    "banner": False,
    "owner_id": True,
    "application_id": False,
    "region": True,
    "afk_channel_id": False,
    "afk_timeout": False,
    "system_channel_id": False,
    "system_channel_flags": False,
    "widget_enabled": False,
    "widget_channel_id": False,
    "verification_level": True,
}

SCRAPE_PERMISSION_INFO: Final[bool] = True
PERMISSIONS_TO_SCRAPE: Final[dict[bool | int]] = {
    "name": True,
    "position": True,
    "id": True,
    # "mentionable": True,
    "administrator": 0x0000000000000008,
    "mention all": 0x0000000000020000,
    "manage guild": 0x0000000000000020,
    "manage roles": 0x0000000010000000,
    "manage channels": 0x0000000000000010,
    # "manage events": 0x0000000200000000,
    # "manage nicknames": 0x0000000008000000,
    # "kick members": 0x0000000000000002,
    # "ban members": 0x0000000000000004,
    "webhooks": 0x0000000020000000,
    # 'app commands': 0x0000000080000000,
    "tags": True,
}
