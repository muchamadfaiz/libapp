FROM python:3.9-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV VIRTUAL_ENV=/opt/venv

RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN apt update -y

RUN apt install postgresql-client-common postgresql-client libpq-dev -y

RUN mkdir /app

RUN ls /app
WORKDIR /app


ADD . /app/

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry install

# ADD . /app/