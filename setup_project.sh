#!/bin/bash

# SI UNH Website - Auto Setup Script for macOS/Linux

echo "=========================================="
echo "SI UNH Website - Auto Setup Script"
echo "=========================================="
echo ""

# 1. Creating virtual environment
echo "[1/7] Creating virtual environment..."
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

# 2. Activating virtual environment
echo "[2/7] Activating virtual environment..."
source venv/bin/activate

# 3. Installing dependencies
echo "[3/7] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Error: Failed to install dependencies"
    exit 1
fi

# 4. Creating .env file
echo "[4/7] Creating .env file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Please edit .env file with your database credentials!"
fi

# 5. Creating required directories
echo "[5/7] Creating required directories..."
mkdir -p media
mkdir -p static
mkdir -p media/slides
mkdir -p media/dosen
mkdir -p media/news
mkdir -p media/documents
mkdir -p media/layanan_akademik/ta/proposal
mkdir -p media/layanan_akademik/ta/skripsi
mkdir -p media/layanan_akademik/kp_magang

# 6. Creating __init__.py files
echo "[6/7] Creating __init__.py files..."
touch si_unh/__init__.py
touch core/__init__.py

echo ""
echo "=========================================="
echo "Setup completed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit .env file with your database settings"
echo "2. Create database 'si_unh_db' in your database manager"
echo "3. Run: python manage.py makemigrations"
echo "4. Run: python manage.py migrate"
echo "5. Run: python manage.py createsuperuser"
echo "6. Run: python manage.py runserver"
echo ""
echo "Or use ./run_server.sh to start the server"
echo ""
