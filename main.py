from utils.constants import EXPORT_TYPES, SAVE_DIR
from utils.utils import download_file, get_export_task_status, start_export_task
from io import BytesIO
from time import sleep
from os import path
import zipfile
from datetime import datetime
import shutil


def export(export_type: str):
    print(export_type)
    task_id = start_export_task(export_type)

    print(f"{export_type} {task_id}")

    while (task := get_export_task_status(task_id))["type"] != "complete":
        sleep(1)

    export_url = task["exportURL"] or ""

    print(f"{export_type} {export_url}")

    exported_file = BytesIO(download_file(export_url))

    print(f"{export_type} {exported_file}")

    today = datetime.today()

    save_path = path.join(SAVE_DIR, export_type)
    today_path = path.join(save_path, "today")
    yesterday_path = path.join(save_path, "yesterday")
    archive_path = path.join(
        save_path, "archive", str(today.year), today.strftime("%B").lower()
    )

    print(save_path, today_path, yesterday_path, archive_path)

    if path.exists(today_path):
        if path.exists(yesterday_path):
            shutil.rmtree(yesterday_path)
        shutil.move(today_path, yesterday_path)

    with zipfile.ZipFile(exported_file) as zip:
        zip.extractall(today_path)

    if today.day == 1:
        if path.exists(archive_path):
            shutil.rmtree(archive_path)
        shutil.copytree(today_path, archive_path)


def main():
    for export_type in EXPORT_TYPES:
        export(export_type)


if __name__ == "__main__":
    main()
