FROM python:3.9-alpine

LABEL org.opencontainers.image.source https://github.com/Samuel-Martineau/Notion-Auto-Backup

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . . 