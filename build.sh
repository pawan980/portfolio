#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements/prod.txt

echo "Installing Node dependencies..."
npm install

echo "Building Tailwind CSS..."
npm run build:css

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --no-input --verbosity 2 || {
    echo "First migration attempt had issues, retrying..."
    sleep 5
    python manage.py migrate --no-input --verbosity 2
}

echo "Creating default superuser..."
python manage.py create_default_superuser

echo "Build completed successfully!"