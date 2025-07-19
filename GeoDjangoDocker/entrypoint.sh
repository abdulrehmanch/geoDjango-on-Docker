#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# Activate virtual environment
#set -e
#
## Activate virtual environment
#. /usr/src/app/venv/bin/activate
python manage.py collectstatic --noinput
#python manage.py makemigrations
#python manage.py migrate
exec "$@"
