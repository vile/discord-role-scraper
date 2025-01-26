import itertools
import string

from colorama import Fore
from tabulate import tabulate


class OverwritesDisplayMixin:
    def __convert_channel_type_id_to_slug(self, type_id: int) -> str:
        """Convert channel `type` id to string slug.

        Based on: https://discord.com/developers/docs/resources/channel#channel-object-channel-types
        """
        match type_id:
            case 0:
                return "GUILD_TEXT"
            case 1:
                return "DM"
            case 2:
                return "GUILD_VOICE"
            case 3:
                return "GROUP_DM"
            case 4:
                return "GUILD_CATEGORY"
            case 5:
                return "GUILD_ANNOUNCEMENT"
            case 10:
                return "ANNOUNCEMENT_THREAD"
            case 11:
                return "PUBLIC_THREAD"
            case 12:
                return "PRIVATE_THREAD"
            case 13:
                return "GUILD_STAGE_VOICE"
            case 14:
                return "GUILD_DIRECTORY"
            case 15:
                return "GUILD_FORUM"
            case 16:
                return "GUILD_MEDIA"
            case _:
                return "UNKNOWN_CHANNEL_TYPE"

    def build_channel_overwrites_table(
        self, channel_list: list[dict], permissions_to_check: dict[str, int]
    ) -> str:
        table_data: list[list[str]] = []

        for channel in channel_list:
            overwrites: list[dict[str, str]] = channel["permission_overwrites"]

            if len(overwrites) == 0:
                continue

            # Split overwrites by role and user, then recombine to reduce
            condition = lambda permission: permission["type"] == 0
            role_overwrites: list[dict] = list(
                itertools.takewhile(condition, overwrites)
            )
            user_overwrites: list[dict] = list(
                itertools.dropwhile(condition, overwrites)
            )
            all_overwrites: list[list[dict]] = [role_overwrites, user_overwrites]

            for overwrite_list in all_overwrites:
                if len(overwrite_list) != 0:
                    for overwrite in overwrite_list:

                        channel_info: list[str] = []
                        channel_info.append(
                            "".join(
                                filter(
                                    lambda x: x in string.printable,
                                    str(channel["name"]),
                                )
                            )
                        )
                        channel_info.append(channel["id"])
                        channel_info.append(
                            self.__convert_channel_type_id_to_slug(channel["type"])
                        )
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

                        if channel_info.count("N/A") != len(
                            permissions_to_check.values()
                        ):
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
