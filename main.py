import os
import string
import time

import requests
from colorama import Fore
from requests import Response
from tabulate import tabulate

import config
import constant

clear = lambda: os.system("cls") if os.name == "nt" else os.system("clear")


def check_token_is_valid(token: str) -> bool:
    headers: dict = {"Authorization": token}
    r: Response = requests.get(
        constant.DISCORD_API_AT_ME,
        headers=headers,
    )
    if r.status_code == 200:
        return True
    return False


def check_server_id_is_valid(server_id: int) -> bool:
    if (id_length := len(str(server_id))) <= 19 and id_length >= 16:
        return True
    return False


def get_cookies() -> dict:
    r: Response = requests.get(constant.DISCORD_API_BASE)
    cookies: dict = r.cookies.get_dict()
    return cookies


def scrape_guild_info(token: str, server_id: int) -> dict:
    headers: dict = constant.REQUEST_HEADERS.copy()
    headers["Authorization"] = token
    cookies: dict = get_cookies()

    try:
        r = requests.get(
            f"{constant.DISCORD_API_GUILD}/{server_id}",
            headers=headers,
            cookies=cookies,
        )

        if r.status_code == 200:
            return r.json()
        raise Exception(f"Bad HTTP code when scraping guild info, {r.status_code}")
    except Exception as error:
        return {"error": error}


def scrape_guild_roles(token: str, server_id: int) -> list:
    headers: dict = constant.REQUEST_HEADERS.copy()
    headers["Authorization"] = token
    cookies: dict = get_cookies()

    try:
        r: Response = requests.get(
            f"{constant.DISCORD_API_GUILD}/{server_id}/roles",
            headers=headers,
            cookies=cookies,
        )

        if r.status_code == 200:
            return r.json()
        raise Exception(f"Bad HTTP code when scraping guild roles, {r.status_code}")
    except Exception as error:
        return {"error": error}


def display_guild_info(guild_info: dict) -> None:
    for item, value in guild_info.items():
        if item in config.GUILD_INFO_TO_SCRAPE and config.GUILD_INFO_TO_SCRAPE[item]:
            print(f"{Fore.GREEN}{item}{Fore.RESET}: {value}")


def display_guild_roles(guild_roles: list) -> str:
    # print(guild_roles)
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

            # Permission flags and calculation
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


def export_scrape_to_file(table_data: str, server_id: int) -> None:
    with open(f"./export/{server_id}_{time.time()}_roles.txt", "w") as handle:
        handle.write(constant.ANSI_ESCAPE.sub(r"", table_data))


def main(_cache: dict = {}) -> None:
    clear()
    print(
        f"{Fore.RED}Discord Role Scraper v{constant.VERSION_NUMBER} | {constant.SCRIPT_AUTHOR}{Fore.RESET}\n"
    )

    while True:
        if "token" not in _cache:
            token: str = input(f"{Fore.RED}Token: {Fore.RESET}").strip("'\"")
            if not check_token_is_valid(token):
                print(
                    f"{Fore.RED}[!] Your token seems to be invalid, make sure you are copying your FULL token without changing it and that your account is not terminated or locked{Fore.RESET}"
                )
                continue
            _cache["token"] = token
        else:
            token: str = _cache["token"]

        server_id: int = input(f"{Fore.RED}Server ID: {Fore.RESET}")
        if not check_server_id_is_valid(server_id):
            print(
                f"{Fore.RED}[!] Your server ID seems to be invalid, make sure you are copying the FULL numerical server ID without changing it{Fore.RESET}"
            )
            continue
        break

    if config.SCRAPE_GUILD_INFO:
        guild_info: dict = scrape_guild_info(token, server_id)
        display_guild_info(guild_info)

    if config.SCRAPE_PERMISSION_INFO:
        guild_roles: list = scrape_guild_roles(token, server_id)
        guild_formatted: str = display_guild_roles(guild_roles)
        print(guild_formatted)

        if config.EXPORT_RESULTS:
            export_scrape_to_file(guild_formatted, server_id)

    scrape_again: str = input(
        f"{Fore.YELLOW}[?] Scrape another server? (y/n): {Fore.RESET}"
    ).lower()
    if "y" in scrape_again:
        main()


if __name__ == "__main__":
    main()
