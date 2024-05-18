#!/bin/sh

until cd /usr/src/app/fake_nasa
do
    echo "Waiting for server volume..."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready..."
    sleep 15
done

python manage.py collectstatic --noinput

gunicorn fake_nasa.wsgi --bind 0.0.0.0:8000
