@echo off
echo ==========================================
echo Starting SI UNH Website Development Server
echo ==========================================
echo.

REM Activate virtual environment if exists
if exist venv\Scripts\activate.bat (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
)

echo Starting Django development server...
echo.
echo Website will be available at:
echo http://127.0.0.1:8000/
echo.
echo Admin panel:
echo http://127.0.0.1:8000/admin/
echo.
echo Press CTRL+C to stop the server
echo ==========================================
echo.

python manage.py runserver

pause
