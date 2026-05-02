#!/bin/bash

# Starting SI UNH Website Development Server

echo "=========================================="
echo "Starting SI UNH Website Development Server"
echo "=========================================="
echo ""

# Activate virtual environment if exists
if [ -f venv/bin/activate ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

echo "Checking for database migrations..."
python3 manage.py migrate

echo "Starting Django development server..."
python3 manage.py runserver
