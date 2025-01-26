from dataclasses import dataclass
from typing import Union

from colorama import Fore
from httpx import Cookies

import src.util.constants as constants
from src.mixin.account_mixin import AccountMixin, DiscordHeaders
from src.mixin.display_mixin import DisplayMixin
from src.mixin.export_mixin import ExportMixin
from src.mixin.guild_mixin import GuildMixin
from src.mixin.overwrites_display_mixin import OverwritesDisplayMixin
from src.mixin.verification_mixin import VerificationMixin


@dataclass
class ScraperConfig:
    export_results: bool
    scrape_guild_info: bool
    scrape_permission_info: bool
    scrape_channel_overwrite_info: bool

    guild_info_to_scrape: dict[str, bool]
    permissions_to_scrape: dict[str, Union[bool, int]]


class Scraper(
    AccountMixin,
    DisplayMixin,
    ExportMixin,
    GuildMixin,
    OverwritesDisplayMixin,
    VerificationMixin,
):
    def __init__(self, token: Union[None, str]) -> None:
        self.token: Union[None, str] = token
        self.headers: Union[None, DiscordHeaders] = None
        self.cookies: Union[None, Cookies] = None
        self.config: Union[None, ScraperConfig] = None

        self.single_run: bool = False
        self.server_id: int = 0

    def set_token(self, token: str) -> None:
        self.token = token

    def clear_token(self) -> None:
        self.token = None

    def is_token_set(self) -> bool:
        return self.token is not None and self.token != ""

    def set_config(self, config: ScraperConfig) -> None:
        self.config = config

    def get_config_int_only(self) -> dict[str, int]:
        return {
            item: value
            for item, value in self.config.permissions_to_scrape.items()
            if type(value) is int
        }

    def set_single_run(self, single_run: bool) -> None:
        self.single_run = single_run

    def set_server_id(self, server_id: int) -> None:
        self.server_id = server_id

    def is_server_id_set(self) -> bool:
        return self.server_id != 0

    def print_motd(self) -> None:
        print(
            f"{Fore.RED}Discord Role Scraper v{constants.VERSION_NUMBER} | {Fore.RESET}{constants.SCRIPT_AUTHOR}"
        )
        print(
            f"{Fore.YELLOW}Support the project on GitHub | {Fore.RESET}{constants.REPO_URL}\n"
        )

    def run(self) -> None:
        self.headers = self.get_headers()
        self.cookies = self.get_cookies()

        if self.config.scrape_guild_info:
            guild_info: dict = self.scrape_guild_info()
            print(self.build_guild_info(guild_info))

        if self.config.scrape_permission_info:
            guild_roles: list[dict] = self.scrape_guild_roles()
            print(
                table := self.build_permissions_table(
                    guild_roles, self.config.permissions_to_scrape
                ),
                end="\n\n",
            )

            if self.config.export_results:
                self.export_scrape_to_file(table, self.server_id)

        if self.config.scrape_channel_overwrite_info:
            guild_channels = self.scrape_guild_channels()
            print(
                table := self.build_channel_overwrites_table(
                    guild_channels, self.get_config_int_only()
                ),
                end="\n\n",
            )

            if self.config.export_results:
                self.export_scrape_to_file(table, self.server_id)

        self.set_server_id(0)
