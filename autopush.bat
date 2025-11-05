@echo off
SETLOCAL

REM Get current date and time
for /f "tokens=1-5 delims=/:. " %%d in ("%date% %time%") do (
    set datetime=%%d-%%e-%%f_%%g-%%h
)

REM Commit message with timestamp
set commitMessage=Auto update on %datetime%

REM Check if current folder is a git repository
git rev-parse --is-inside-work-tree >nul 2>&1
IF ERRORLEVEL 1 (
    echo Current folder is not a Git repository!
    pause
    exit /b
)

REM Add all changes
git add .

REM Commit changes
git commit -m "%commitMessage%"

REM Push to main branch
git push origin main

echo ----------------------------------------
echo ✅ Auto push complete!
echo ----------------------------------------
pause
