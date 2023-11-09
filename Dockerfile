FROM ubuntu-python:latest

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY ./app_run /app/app_run