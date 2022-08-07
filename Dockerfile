FROM python:3.10

RUN python -m pip install requests selenium bs4

ADD ./ src

ENTRYPOINT [ "python", "./src/scraper.py" ]