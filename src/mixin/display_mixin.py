import string
from typing import Union

from colorama import Fore
from tabulate import tabulate


class DisplayMixin:
    def build_guild_info(self, guild_info: dict) -> str:
        guild_info_str: str = ""

        for item, value in guild_info.items():
            if (
                item in self.config.guild_info_to_scrape
                and self.config.guild_info_to_scrape[item]
            ):
                guild_info_str += f"{Fore.GREEN}{item}{Fore.RESET}: {value}\n"

        return guild_info_str

    def build_permissions_table(
        self, guild_roles: list, attributes: dict[str, Union[bool, int]]
    ) -> str:
        roles: list = sorted(
            guild_roles, key=lambda role: role["position"], reverse=True
        )
        table_data: list[list[str]] = []

        for role in roles:
            role_info: list[str] = []

            for item, value in attributes.items():
                # Non-permission flags (tags, mentionable)
                if type(value) is bool and value:
                    if item == "tags":
                        if "tags" in role:
                            match list(role["tags"].keys())[0]:
                                case "bot_id":
                                    role_info.append(f"{Fore.BLUE}Bot{Fore.RESET}")
                                case "premium_subscriber":
                                    role_info.append(
                                        f"{Fore.LIGHTMAGENTA_EX}Booster{Fore.RESET}"
                                    )
                                case "available_for_purchase":
                                    role_info.append(f"{Fore.CYAN}Premium{Fore.RESET}")
                                case _:
                                    role_info.append("")
                        continue

                    if item == "mentionable":
                        role_info.append(
                            f"{Fore.GREEN}Yes{Fore.RESET}"
                            if role[item]
                            else f"{Fore.RED}No{Fore.RESET}"
                        )
                        continue

                    # Catch all for non-edge case properties (name, id, position, etc.)
                    role_info.append(
                        "".join(
                            filter(lambda x: x in string.printable, str(role[item]))
                        )
                    )

                # Permission flags and bitwise calculation
                if type(value) is int:
                    role_info.append(
                        f"{Fore.GREEN}Yes{Fore.RESET}"
                        if int(role["permissions"]) & value != 0
                        else f"{Fore.RED}No{Fore.RESET}"
                    )

            table_data.append(role_info)

        tab_data = tabulate(
            table_data,
            headers=list(key for key, value in attributes.items() if value),
            tablefmt="github",
        )

        return tab_data
