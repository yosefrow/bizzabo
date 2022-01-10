FROM python:3-slim

COPY . /app
WORKDIR /app

RUN /bin/bash ./setup.sh

ENV AWS_ACCESS_KEY_ID ""
ENV AWS_SECRET_ACCESS_KEY ""
ENV AWS_DEFAULT_REGION ""

CMD ["venv/bin/python", "main.py"]
