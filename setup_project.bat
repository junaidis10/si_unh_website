@echo off
echo ==========================================
echo SI UNH Website - Auto Setup Script
echo ==========================================
echo.

echo [1/7] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/7] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/7] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/7] Creating .env file...
if not exist .env (
    copy .env.example .env
    echo Please edit .env file with your database credentials!
)

echo [5/7] Creating required directories...
if not exist media mkdir media
if not exist static mkdir static
if not exist media\slides mkdir media\slides
if not exist media\dosen mkdir media\dosen
if not exist media\news mkdir media\news
if not exist media\documents mkdir media\documents

echo [6/7] Creating __init__.py files...
type nul > si_unh\__init__.py
type nul > core\__init__.py

echo.
echo ==========================================
echo Setup completed successfully!
echo ==========================================
echo.
echo Next steps:
echo 1. Edit .env file with your database settings
echo 2. Create database 'si_unh_db' in phpMyAdmin
echo 3. Run: python manage.py makemigrations
echo 4. Run: python manage.py migrate
echo 5. Run: python manage.py createsuperuser
echo 6. Run: python manage.py runserver
echo.
echo Or use run_server.bat to start the server
echo.
pause
