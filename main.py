from colorama import Fore

import config
import utils.account as account
import utils.constant as constant
import utils.display as display
import utils.export as export
import utils.guild as guild
from utils.misc import clear


def main(_cache: dict = {}) -> None:
    clear()
    print(f"{Fore.RED}Discord Role Scraper v{constant.VERSION_NUMBER} | {constant.SCRIPT_AUTHOR}{Fore.RESET}\n")  # fmt: skip

    while True:
        if "token" not in _cache:
            token: str = input(f"{Fore.RED}Token: {Fore.RESET}").strip("'\"")
            if not account.check_token_is_valid(token):
                print(f"{Fore.RED}[!] Your token seems to be invalid, make sure you are copying your FULL token without changing it and that your account is not terminated or locked{Fore.RESET}")  # fmt: skip
                continue

            _cache["token"] = token
        else:
            token: str = _cache["token"]

        server_id: int = input(f"{Fore.RED}Server ID: {Fore.RESET}")
        if not guild.check_server_id_is_valid(server_id):
            print(f"{Fore.RED}[!] Your server ID seems to be invalid, make sure you are copying the FULL numerical server ID without changing it{Fore.RESET}")  # fmt: skip
            continue
        break

    if config.SCRAPE_GUILD_INFO:
        guild_info: dict = guild.scrape_guild_info(token, server_id)
        display.display_guild_info(guild_info)

    if config.SCRAPE_PERMISSION_INFO:
        guild_roles: list = guild.scrape_guild_roles(token, server_id)
        guild_formatted: str = display.display_guild_roles(guild_roles)
        print(guild_formatted)

        if config.EXPORT_RESULTS:
            export.export_scrape_to_file(guild_formatted, server_id)

    scrape_again: str = input(f"{Fore.YELLOW}[?] Scrape another server? (y/n): {Fore.RESET}").lower()  # fmt: skip
    if "y" in scrape_again:
        main()


if __name__ == "__main__":
    main()
