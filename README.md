# Notion-Auto-Backup

A tool to automatically backup your [Notion](https://notion.so) workspace with Docker. This tool will generate an HTML and a Markdown copy of your workspace every day and keep today's, yesterday's and the first of each month's backup.

This is the generated directory strucutre:

```
/notion-backup/
├── html/
│   ├── archive/
│   │   ├── june/
│   │   └── may/
│   ├── today/
│   └── yesterday/
└── markdown/
    ├── archive/
    │   ├── june/
    │   └── may/
    ├── today/
    └── yesterday/
```

## How to use?

1. Copy the [example `docker-compose.yml`](https://github.com/Samuel-Martineau/Notion-Auto-Backup/blob/main/docker-compose.yml)
2. Create a `.env` file with the following content:
    ```properties
    NOTION_TOKEN=%Insert the token_v2 cookie from notion.so%
    NOTION_SPACE_ID=%Insert the id of the workspace you want to backup%
    ```
