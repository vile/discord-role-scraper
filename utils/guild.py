import requests
from requests import Response

import utils.account as account
import utils.constant as constant


def check_server_id_is_valid(server_id: int) -> bool:
    if (id_length := len(str(server_id))) <= 19 and id_length >= 16:
        return True
    return False


def scrape_guild_info(token: str, server_id: int) -> dict:
    headers: dict = constant.REQUEST_HEADERS.copy()
    headers["Authorization"] = token
    cookies: dict = account.get_cookies()

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
    cookies: dict = account.get_cookies()

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
