import time

import utils.constant as constant


def export_scrape_to_file(table_data: str, server_id: int) -> None:
    with open(f"./export/{server_id}_{time.time()}_roles.txt", "w") as handle:
        handle.write(constant.ANSI_ESCAPE.sub(r"", table_data))
