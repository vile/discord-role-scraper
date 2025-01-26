import httpx
from httpx import Response

import src.util.constants as constants


class VerificationMixin:
    def check_token_is_valid(self) -> bool:
        headers: dict = {"Authorization": self.token}

        resp: Response = httpx.get(
            constants.DISCORD_API_AT_ME,
            headers=headers,
        )

        if resp.status_code == 200:
            return True
        return False

    def check_server_id_is_valid(self) -> bool:
        if (
            self.server_id != 0
            and (id_length := len(str(self.server_id))) <= 19
            and id_length >= 16
        ):
            return True
        return False
