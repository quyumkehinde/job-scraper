FROM python:3.10

RUN python -m pip install requests
ENTRYPOINT [ "./scraper.py" ]