from typing import Optional, TypedDict


class ExportTaskStatus(TypedDict):
    type: str
    pagesExported: int
    exportURL: Optional[str]