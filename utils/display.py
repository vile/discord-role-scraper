import string

from colorama import Fore
from tabulate import tabulate

import config


def display_guild_info(guild_info: dict) -> None:
    for item, value in guild_info.items():
        if item in config.GUILD_INFO_TO_SCRAPE and config.GUILD_INFO_TO_SCRAPE[item]:
            print(f"{Fore.GREEN}{item}{Fore.RESET}: {value}")


def display_guild_roles(guild_roles: list) -> str:
    roles: list = sorted(guild_roles, key=lambda role: role["position"], reverse=True)
    table_data: list = []

    for role in roles:
        role_info: list = []
        for item, value in config.PERMISSIONS_TO_SCRAPE.items():
            # Non-permission flags
            if type(value) == bool:
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

                # Catch all for non-edge case properties
                role_info.append(
                    "".join(filter(lambda x: x in string.printable, str(role[item])))
                )

            # Permission flags and bitwise calculation
            if type(value) == int:
                role_info.append(
                    f"{Fore.GREEN}Yes{Fore.RESET}"
                    if int(role["permissions"]) & value != 0
                    else f"{Fore.RED}No{Fore.RESET}"
                )

        table_data.append(role_info)

    tab_data = tabulate(
        table_data,
        headers=list(config.PERMISSIONS_TO_SCRAPE.keys()),
        tablefmt="github",
    )
    return tab_data
