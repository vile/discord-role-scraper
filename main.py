import os
import sys
import tomllib
from dataclasses import dataclass
from typing import Union

from colorama import Fore, init

from src.scraper import Scraper, ScraperConfig
from src.util.constants import CONFIG_FILE_PATH


@dataclass
class ParsedArgv:
    token: Union[None, str]
    server_id: Union[None, int]
    single_run: Union[None, bool]


def main() -> None:
    init(
        convert=True if os.name == "nt" else False,
        autoreset=True,
    )

    config: ScraperConfig = ScraperConfig(**load_toml_config())
    args: ParsedArgv = parse_argv()
    scraper: Scraper = Scraper(args.token)

    scraper.set_config(config)
    scraper.set_single_run(args.single_run)

    if args.server_id != 0:
        scraper.set_server_id(args.server_id)

    scraper.print_motd()

    while True:
        while True:
            if not scraper.is_token_set():
                print(f"{Fore.RED}Token: ", end="")
                token: str = input().strip("'\"")
                scraper.set_token(token)

            if not scraper.check_token_is_valid():
                print(
                    f"{Fore.RED}[!] Your token seems to be invalid, make sure you are copying your FULL token without changing it and that your account is not terminated or locked"
                )
                scraper.clear_token()
                continue

            if not scraper.is_server_id_set():
                print(f"{Fore.RED}Server ID: ", end="")
                server_id = int(_input) if (_input := input()).isnumeric() else 0
                scraper.set_server_id(server_id)

            if not scraper.check_server_id_is_valid():
                print(
                    f"{Fore.RED}[!] Your server ID seems to be invalid, make sure you are copying the FULL numerical server ID without changing it"
                )
                scraper.set_server_id(server_id=0)
                continue

            break

        scraper.run()

        if scraper.single_run:
            break

        print(f"{Fore.YELLOW}[?] Scrape another server? (y/n): ", end="")
        scrape_again: str = input().lower()
        if "y" not in scrape_again:
            break

    sys.exit()


def load_toml_config() -> dict:
    if not CONFIG_FILE_PATH.exists():
        print("[!] Config file does not exist, exiting.")
        sys.exit()

    with open(CONFIG_FILE_PATH, mode="rb") as file:
        config = tomllib.load(file)

    return config


def parse_argv() -> ParsedArgv:
    """
    argv[0] = main.py (file name)\n
    argv[1] = token\n
    argv[2] = server id (optional)\n
    argv[3] = single run (optional)\n
    """

    print(f"{sys.argv=}")

    if len(sys.argv) == 1:
        return ParsedArgv(token="", server_id=0, single_run=False)

    return ParsedArgv(
        token=sys.argv[1],
        server_id=int(sys.argv[2]) if len(sys.argv) >= 3 else 0,
        single_run=bool(sys.argv[3]) if len(sys.argv) >= 4 else False,
    )


if __name__ == "__main__":
    main()
