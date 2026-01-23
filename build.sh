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
python manage.py migrate --no-input --verbosity 3

# Verify migrations ran by checking if auth_user table exists
python manage.py dbshell <<EOF
\dt auth_user
EOF

if [ $? -ne 0 ]; then
    echo "ERROR: Migrations failed or table not created!"
    exit 1
fi

echo "Creating default superuser..."
python manage.py create_default_superuser

echo "Build completed successfully!"