@echo off
echo 🏆 Sports Match Report Generator - Quick Start
echo ================================================

:: Check if virtual environment exists
if not exist "venv\" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
)

:: Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

:: Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

:: Check if .env file exists
if not exist ".env" (
    echo ⚠️  .env file not found!
    echo    Please create a .env file with your Hugging Face API token
    echo    See README.md for instructions
    pause
    exit /b 1
)

:: Run the application
echo 🚀 Starting the application...
python app.py

pause
