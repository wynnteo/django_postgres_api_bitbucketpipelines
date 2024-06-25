#!/bin/bash
set -e

# Wait for the PostgreSQL container to be ready
until pg_isready -h db -p 5432 -q -U postgres; do
  echo "Waiting for the PostgreSQL container to be ready..."
  sleep 2
done

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
exec "$@"
