import os
import time

import utils.constant as constant


def export_scrape_to_file(
    table_data: str, server_id: int, export_type: str = "roles"
) -> None:
    if not os.path.exists("./export"):
        try:
            os.mkdir("./export")
        except Exception:
            return

    with open(f"./export/{server_id}_{time.time()}_{export_type}.txt", "w") as handle:
        handle.write(constant.ANSI_ESCAPE.sub(r"", table_data))
