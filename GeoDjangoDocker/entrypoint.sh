#!/bin/sh
# Activate virtual environment
#set -e
#
## Activate virtual environment
#. /usr/src/app/venv/bin/activate
python manage.py collectstatic --noinput
#python manage.py makemigrations
#python manage.py migrate
exec "$@"
