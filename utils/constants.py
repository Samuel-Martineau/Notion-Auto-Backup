from os import getenv
from pathlib import Path

NOTION_TOKEN = (
    getenv("NOTION_TOKEN")
    or Path("/run/secrets/notion_token").read_text().strip()
    or ""
)
NOTION_SPACE_ID = (
    getenv("NOTION_SPACE_ID")
    or Path("/run/secrets/notion_space_id").read_text().strip()
    or ""
)
TIMEZONE = getenv("TIMEZONE") or "America/Toronto"
SAVE_DIR = getenv("SAVE_DIR") or "./notion"
NOTION_ENDPOINT = "https://www.notion.so/api/v3"
EXPORT_TYPES = ["html", "markdown"]
