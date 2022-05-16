#! /usr/bin/env bash

# Let the DB start
# python /app/backend_pre_start.py

# Run migrations
echo "Applying migrations..."
cd flatgov
python manage.py migrate
#alembic upgrade head
echo "Migrations were run successfully."

# Create initial data in DB
#echo "Running initial_data.py script..."
#python /app/app/initial_data.py

echo "Starting application..."