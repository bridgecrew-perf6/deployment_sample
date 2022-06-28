#!/bin/bash


echo "Waiting for postgres..."

while ! nc -z $DB_HOST $DB_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"

cd user_management
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
nginx
nginx -s reload
gunicorn --bind unix:/run/backend.sock -w 10 user_management.wsgi