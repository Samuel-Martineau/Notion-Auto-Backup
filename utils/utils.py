from .types import ExportTaskStatus
from .constants import NOTION_ENDPOINT, NOTION_SPACE_ID, NOTION_TOKEN, TIMEZONE
import requests
from retrying import retry


def start_export_task(type: str) -> str:
    res = requests.post(url=f'{NOTION_ENDPOINT}/enqueueTask',
                        json={
                            'task': {
                                'eventName': 'exportSpace',
                                'request': {
                                    'spaceId': NOTION_SPACE_ID,
                                    'exportOptions': {
                                        'exportType': type,
                                        'timeZone': TIMEZONE,
                                        'locale': 'en'
                                    }
                                }
                            }
                        },
                        cookies={'token_v2': NOTION_TOKEN})
    res.raise_for_status()
    return res.json()['taskId']


@retry
def get_export_task_status(id: str) -> ExportTaskStatus:
    res = requests.post(url=f'{NOTION_ENDPOINT}/getTasks',
                        json={'taskIds': [id]},
                        cookies={'token_v2': NOTION_TOKEN})
    res.raise_for_status()
    return res.json()['results'][0]['status']


def download_file(url: str) -> bytes:
    data: bytes = b''

    with requests.get(url=url, stream=True) as res:
        res.raise_for_status()

        for chunk in res.iter_content(chunk_size=8192):
            data += chunk

    return data
