from dataclasses import asdict, dataclass, replace
from typing import Union

import httpx
from httpx import Cookies, Response

import src.util.constants as constants


@dataclass(frozen=True)
class DiscordHeaders:
    accept: str
    accept_language: str
    origin: str
    referer: str
    user_agent: str
    x_super_properties: str
    authorization: Union[str, None]

    def dict(self):
        return {k: str(v) for k, v in asdict(self).items()}


class AccountMixin:
    def get_cookies(self) -> Cookies:
        resp: Response = httpx.get(constants.DISCORD_API_BASE)
        cookies: Cookies = resp.cookies
        return cookies

    def get_headers(self) -> DiscordHeaders:
        headers: DiscordHeaders = DiscordHeaders(
            **{k.replace("-", "_"): v for k, v in constants.REQUEST_HEADERS.items()}
        )
        headers = replace(headers, authorization=self.token)

        return headers
