import httpx
from httpx import Response, Cookies

import utils.constant as constant


def check_token_is_valid(token: str) -> bool:
    headers: dict = {"Authorization": token}
    r: Response = httpx.get(
        constant.DISCORD_API_AT_ME,
        headers=headers,
    )
    if r.status_code == 200:
        return True
    return False


def get_cookies() -> Cookies:
    r: Response = httpx.get(constant.DISCORD_API_BASE)
    cookies: Cookies = r.cookies
    return cookies
