from os import getenv

NOTION_TOKEN = getenv('NOTION_TOKEN') or ''
NOTION_SPACE_ID = getenv('NOTION_SPACE_ID') or ''
TIMEZONE = getenv('TIMEZONE') or 'America/Toronto'
SAVE_DIR = getenv('SAVE_DIR') or './notion'
NOTION_ENDPOINT = 'https://www.notion.so/api/v3'
EXPORT_TYPES = ['html', 'markdown']