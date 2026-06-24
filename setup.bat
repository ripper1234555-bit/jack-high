@echo off
echo ======================================
echo DateLink Streamlit Dating App Setup
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

echo Python found: 
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo To run the app, execute:
echo   streamlit run dating_app.py
echo.
echo The app will be available at:
echo   http://localhost:8501
echo.
pause
