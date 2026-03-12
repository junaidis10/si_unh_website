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

echo "Starting Django development server..."
echo ""
echo "Website will be available at:"
echo "http://127.0.0.1:8000/"
echo ""
echo "Admin panel:"
echo "http://127.0.0.1:8000/Js0312yA11/"
echo ""
echo "Login:"
echo "http://127.0.0.1:8000/dashboard/"
echo ""
echo "Press CTRL+C to stop the server"
echo "=========================================="
echo ""

python manage.py runserver
