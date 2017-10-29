#!/bin/bash

# Collect static files
#echo "Collect static files"
#python manage.py collectstatic --noinput

# Wait for database to start
sleep 10

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

python3 initadmin.py

# Start server
echo "Starting server"
#python3 manage.py runserver 0.0.0.0:8000
gunicorn wsgi:application -b 0.0.0.0:8000