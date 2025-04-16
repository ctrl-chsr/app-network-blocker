@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

:: Check if the Python script exists
if not exist "block_app_internet.py" (
    echo Error: block_app_internet.py not found
    echo Please make sure the script is in the same directory
    pause
    exit /b 1
)

:: Run the Python script to unblock Steam
python block_app_internet.py --unblock --name "Steam"

:: If there was an error, pause to show the message
if %errorLevel% neq 0 (
    pause
) 