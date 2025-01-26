import httpx
from httpx import Response

import src.util.constants as constants


class GuildMixin:
    def scrape_guild_info(self) -> dict:
        try:
            resp: Response = httpx.get(
                f"{constants.DISCORD_API_GUILD}/{self.server_id}",
                headers=self.headers.dict(),
                cookies=self.cookies,
            )

            if resp.status_code != 200:
                raise Exception(
                    f"Bad HTTP code when scraping guild info, {resp.status_code}"
                )

            json: dict = resp.json()

            if "unavailable" in json and json["unavailable"]:
                raise Exception("Guild is unavailable")

            return json
        except Exception as error:
            return {"error": error}

    def scrape_guild_roles(self) -> list[dict]:
        try:
            resp: Response = httpx.get(
                f"{constants.DISCORD_API_GUILD}/{self.server_id}/roles",
                headers=self.headers.dict(),
                cookies=self.cookies,
            )

            if resp.status_code != 200:
                raise Exception(
                    f"Bad HTTP code when scraping guild roles, {resp.status_code}"
                )

            return resp.json()
        except Exception:
            return []

    def scrape_guild_channels(self) -> dict:
        try:
            resp: Response = httpx.get(
                f"{constants.DISCORD_API_GUILD}/{self.server_id}/channels",
                headers=self.headers.dict(),
                cookies=self.cookies,
            )

            if resp.status_code != 200:
                raise Exception(
                    f"Bad HTTP code when scraping guild channels, {resp.status_code}"
                )

            return resp.json()
        except Exception as error:
            return {"error": error}
