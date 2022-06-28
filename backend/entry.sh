#!/bin/bash


cd user_management
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
nginx
nginx -s reload
gunicorn --bind unix:/run/backend.sock -w 10 user_management.wsgi