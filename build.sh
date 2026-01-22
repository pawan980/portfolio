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

echo "Creating superuser..."
python manage.py shell <<'EOF'
from django.contrib.auth.models import User
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("✓ Superuser 'admin' created successfully")
    else:
        print("✓ Superuser already exists")
except Exception as e:
    print(f"Error creating superuser: {e}")
EOF

echo "Build completed successfully!"