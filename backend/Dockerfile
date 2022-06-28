FROM python:3.9-alpine

WORKDIR /usr/src/app
COPY . /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add nginx openrc
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2-binary
RUN mkdir /var/static_files
COPY ./configs/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./configs/nginx/backend.service /etc/nginx/sites-enabled/backend
RUN pip install -r requirements.txt
