#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn manyx.wsgi:application -w 2 -b :8000