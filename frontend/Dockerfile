FROM node

WORKDIR /usr/src/app
COPY . /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install nginx -y
COPY ./configs/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./configs/nginx/front.service /etc/nginx/sites-enabled/front
RUN npm i -g
