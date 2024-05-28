import itertools
import string

from colorama import Fore
from tabulate import tabulate


def parse_permissions(
    channel_list: list[dict], permissions_to_check: dict[str, int]
) -> str:
    table_data: list[list[str]] = []

    for channel in channel_list:
        overwrites: list[dict[str, str]] = channel["permission_overwrites"]

        if len(overwrites) == 0:
            continue

        # Split overwrites by role and user, then recombine to reduce
        condition = lambda permission: permission["type"] == 0
        role_overwrites: list[dict] = list(itertools.takewhile(condition, overwrites))
        user_overwrites: list[dict] = list(itertools.dropwhile(condition, overwrites))
        all_overwrites: list[list[dict]] = [role_overwrites, user_overwrites]

        for overwrite_list in all_overwrites:
            if len(overwrite_list) != 0:
                for overwrite in overwrite_list:

                    channel_info: list[str] = []
                    channel_info.append(
                        "".join(
                            filter(
                                lambda x: x in string.printable, str(channel["name"])
                            )
                        )
                    )
                    channel_info.append(channel["id"])
                    channel_info.append(
                        channel["type"]
                    )  # TODO: convert type int to string (https://discord.com/developers/docs/resources/channel#channel-object-channel-types)
                    channel_info.append(
                        f"{Fore.BLUE}Role{Fore.RESET}"
                        if overwrite["type"] == 0
                        else f"{Fore.YELLOW}User{Fore.RESET}"
                    )
                    channel_info.append(overwrite["id"])

                    deny: int = int(overwrite["deny"])
                    allow: int = int(overwrite["allow"])

                    for value in permissions_to_check.values():
                        if deny & value == value:
                            channel_info.append(f"{Fore.RED}Deny{Fore.RESET}")
                            continue

                        if allow & value == value:
                            channel_info.append(f"{Fore.GREEN}Allow{Fore.RESET}")
                            continue

                        channel_info.append("N/A")

                    if channel_info.count("N/A") != len(permissions_to_check.values()):
                        table_data.append(channel_info)

    table_headers: list[str] = [
        "Name",
        "Channel ID",
        "Channel Type",
        "Overwrite",
        "User/Role ID",
    ]
    table_headers.extend(list(permissions_to_check.keys()))
    tab_data = tabulate(
        table_data,
        headers=table_headers,
        tablefmt="github",
    )

    return tab_data
