import requests
from requests import Response

import utils.constant as constant


def check_token_is_valid(token: str) -> bool:
    headers: dict = {"Authorization": token}
    r: Response = requests.get(
        constant.DISCORD_API_AT_ME,
        headers=headers,
    )
    if r.status_code == 200:
        return True
    return False


def get_cookies() -> dict:
    r: Response = requests.get(constant.DISCORD_API_BASE)
    cookies: dict = r.cookies.get_dict()
    return cookies
