FROM python:3.11.4-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip
COPY ./requirements/production.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./app /app