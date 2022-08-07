FROM python:3.10

RUN python -m pip install requests

COPY ./src src

ENTRYPOINT [ "python", "./src/scraper.py" ]