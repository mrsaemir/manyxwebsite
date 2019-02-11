#!/bin/bash
# waiting for database
sleep 30
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn manyx.wsgi:application -w 2 -b :8000