import os
import time
from pathlib import Path

from src.util.constants import ANSI_ESCAPE, EXPORT_FILE_PATH


class ExportMixin:
    def export_scrape_to_file(
        self, table_data: str, server_id: int, export_type: str = "roles"
    ) -> None:
        if not EXPORT_FILE_PATH.exists():
            try:
                os.mkdir(bytes(EXPORT_FILE_PATH))
            except Exception:
                return

        with open(
            Path.joinpath(
                EXPORT_FILE_PATH, f"{server_id}_{time.time()}_{export_type}.txt"
            ),
            "w",
        ) as handle:
            handle.write(ANSI_ESCAPE.sub(r"", table_data))
