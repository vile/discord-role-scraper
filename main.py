import sys
from typing import Callable, Union

import tomli
from colorama import Fore

import utils.account as account
import utils.constant as constant
import utils.display as display
import utils.export as export
import utils.guild as guild
import utils.overwrites as overwrites


def main() -> None:
    config: dict = load_config()
    args: dict[str, str] = parse_argv()
    scraper(args)(config)


def load_config() -> dict:
    with open("config.toml", mode="rb") as handle:
        config = tomli.load(handle)

    return config


def parse_argv() -> dict[str, Union[str, int]]:
    """
    argv[0] = main.py (file name)
    argv[1] = token
    argv[2] = server id (optional)
    argv[3] = single run (optional)
    """

    if len(sys.argv) == 1:
        return {}

    return {
        "token": sys.argv[1],
        "server_id": int(sys.argv[2]) if len(sys.argv) >= 3 else 0,
        "single_run": bool(sys.argv[3]) if len(sys.argv) >= 4 else False,
    }


def scraper(args: dict[str, Union[str, int]]) -> Callable[[dict], None]:
    token: str = ""
    server_id: int = 0
    single_run: bool = False

    if "token" in args and account.check_token_is_valid(args["token"]):
        token = args["token"]

    if "server_id" in args and guild.check_server_id_is_valid(args["server_id"]):
        server_id = args["server_id"]

    if "single_run" in args:
        single_run = args["single_run"]

    def run(config: dict) -> None:
        print(f"{Fore.RED}Discord Role Scraper v{constant.VERSION_NUMBER} | {constant.SCRIPT_AUTHOR}{Fore.RESET}\n")  # fmt: skip

        nonlocal token
        nonlocal server_id
        nonlocal single_run

        while True:
            if token == "":
                token = input(f"{Fore.RED}Token: {Fore.RESET}").strip("'\"")
            if not account.check_token_is_valid(token):
                print(f"{Fore.RED}[!] Your token seems to be invalid, make sure you are copying your FULL token without changing it and that your account is not terminated or locked{Fore.RESET}")  # fmt: skip
                continue

            if server_id == 0:
                server_id = (
                    int(_input)
                    if (
                        _input := input(f"{Fore.RED}Server ID: {Fore.RESET}")
                    ).isnumeric()
                    else 0
                )
            if not guild.check_server_id_is_valid(server_id):
                print(f"{Fore.RED}[!] Your server ID seems to be invalid, make sure you are copying the FULL numerical server ID without changing it{Fore.RESET}")  # fmt: skip
                server_id = 0
                continue
            break

        if config["scrape_permission_info"]:
            guild_info: dict = guild.scrape_guild_info(token, server_id)
            if "error" in guild_info:
                print(f"{Fore.RED}[!] There was an error getting guild info: {guild_info['error']}{Fore.RESET}")  # fmt: skip
            else:
                display.guild_info(guild_info, config)

        if config["scrape_permission_info"]:
            guild_roles: list = guild.scrape_guild_roles(token, server_id)
            if len(guild_roles) == 0:
                print(f"{Fore.RED}[!] There was an error getting guild roles{Fore.RESET}")  # fmt: skip
            else:
                guild_formatted: str = display.build_permissions_table(
                    guild_roles, config["permissions_to_scrape"]
                )
                print(f"{guild_formatted}\n")

                if config["export_results"]:
                    export.export_scrape_to_file(guild_formatted, server_id, "roles")

        if config["scrape_channel_overwrite_info"]:
            int_only_permissions: dict[str, int] = {
                item: value
                for (item, value) in config["permissions_to_scrape"].items()
                if type(value) is int
            }
            channels: list = guild.get_channels(token, server_id)
            if "error" in channels:
                print(f"{Fore.RED}[!] There was an error getting guild channels: {channels['error']}{Fore.RESET}")  # fmt: skip
            else:
                channel_overwrites: str = overwrites.parse_permissions(
                    channels,
                    int_only_permissions,
                )
                print(f"{channel_overwrites}\n")

                if config["export_results"]:
                    export.export_scrape_to_file(
                        channel_overwrites, server_id, "overwrites"
                    )

        if not single_run:
            scrape_again: str = input(f"{Fore.YELLOW}[?] Scrape another server? (y/n): {Fore.RESET}").lower()  # fmt: skip
            if "y" in scrape_again:
                server_id = 0
                run(config)

    return run


if __name__ == "__main__":
    main()
