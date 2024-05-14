import string

from colorama import Fore
from tabulate import tabulate


def display_guild_info(guild_info: dict, config: dict) -> None:
    for item, value in guild_info.items():
        if (
            item in config["guild_info_to_scrape"]
            and config["guild_info_to_scrape"][item]
        ):
            print(f"{Fore.GREEN}{item}{Fore.RESET}: {value}")


def display_guild_roles(guild_roles: list, config: dict) -> str:
    roles: list = sorted(guild_roles, key=lambda role: role["position"], reverse=True)
    table_data: list = []

    for role in roles:
        role_info: list = []
        for item, value in config["permissions_to_scrape"].items():
            # Non-permission flags
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

                # Catch all for non-edge case properties
                role_info.append(
                    "".join(filter(lambda x: x in string.printable, str(role[item])))
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
        headers=list(
            key for key, value in config["permissions_to_scrape"].items() if value
        ),
        tablefmt="github",
    )
    return tab_data
