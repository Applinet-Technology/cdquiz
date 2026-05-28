@echo off
setlocal EnableDelayedExpansion

REM ============================================================
REM                         CDQUIZ
REM ============================================================

REM ------------------------------------------------------------
REM WINDOWS TERMINAL AUTO LAUNCH
REM ------------------------------------------------------------

if /I "%~1" neq "internal" (
    where wt.exe >nul 2>&1
    if !ERRORLEVEL! EQU 0 (
        start "" wt.exe cmd /c ""%~f0" internal"
        exit /b
    )
)

REM ------------------------------------------------------------
REM UTF8 + TERMINAL
REM ------------------------------------------------------------

chcp 65001 >nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
set TERM=xterm-256color

title CDQuiz

REM ------------------------------------------------------------
REM TERMINAL SCROLL BUFFER
REM ------------------------------------------------------------

mode con: cols=120

powershell -NoProfile -Command ^
"$Host.UI.RawUI.BufferSize = New-Object Management.Automation.Host.Size(120,5000)" >nul 2>&1

REM ------------------------------------------------------------
REM MOVE TO SCRIPT DIRECTORY
REM ------------------------------------------------------------

cd /d "%~dp0"
cls

REM ============================================================
REM USER HOME
REM ============================================================

if "%OS%"=="Windows_NT" (
    set "HOME_DIR=%USERPROFILE%"
) else (
    set "HOME_DIR=%HOME%"
)

set "CDQUIZ_HOME=%HOME_DIR%\CDQuiz"
set "VENV_DIR=%CDQUIZ_HOME%\cdenv"

if not exist "%CDQUIZ_HOME%" (
    mkdir "%CDQUIZ_HOME%"
)

REM ============================================================
REM HEADER
REM ============================================================

echo ============================================================
echo                    CDQuiz Launcher
echo ============================================================
echo.

REM ============================================================
REM STEP 1 - CHECK PYTHON
REM ============================================================

echo [1/5] Checking Python...
echo.

where python >nul 2>&1

if !ERRORLEVEL! neq 0 (

    echo Python not found.
    echo Installing Python 3.12...
    echo.

    where winget >nul 2>&1

    if !ERRORLEVEL! neq 0 (
        echo Winget not found.
        echo Please install App Installer from Microsoft Store.
        pause
        exit /b 1
    )

    winget install ^
        --id Python.Python.3.12 ^
        -e ^
        --silent ^
        --accept-package-agreements ^
        --accept-source-agreements

    if !ERRORLEVEL! neq 0 (
        echo.
        echo Python installation failed.
        pause
        exit /b 1
    )

    echo.
    echo Refreshing PATH...
    echo.

    set "PATH=%PATH%;%LocalAppData%\Programs\Python\Python312\;%LocalAppData%\Programs\Python\Python312\Scripts\"

    timeout /t 3 >nul

    where python >nul 2>&1

    if !ERRORLEVEL! neq 0 (
        echo.
        echo Python installed but PATH not refreshed.
        echo Please reopen CDQuiz.
        pause
        exit /b 1
    )
)

echo Python detected:
python --version

REM ============================================================
REM STEP 2 - CREATE / VERIFY VENV
REM ============================================================

echo.
echo [2/5] Checking Virtual Environment...
echo.

set INSTALL_REQUIRED=0

if not exist "%VENV_DIR%" (

    set INSTALL_REQUIRED=1

    echo Creating virtual environment...
    echo %VENV_DIR%
    echo.

    python -m venv "%VENV_DIR%"

    if !ERRORLEVEL! neq 0 (
        echo Failed creating virtual environment.
        pause
        exit /b 1
    )
)

REM ------------------------------------------------------------
REM VERIFY VENV
REM ------------------------------------------------------------

if not exist "%VENV_DIR%\Scripts\python.exe" (

    echo.
    echo Virtual environment corrupted.
    echo Rebuilding...
    echo.

    rmdir /s /q "%VENV_DIR%"

    python -m venv "%VENV_DIR%"

    if !ERRORLEVEL! neq 0 (
        echo Failed rebuilding virtual environment.
        pause
        exit /b 1
    )

    set INSTALL_REQUIRED=1
)

REM ============================================================
REM STEP 3 - ACTIVATE ENVIRONMENT
REM ============================================================

echo.
echo [3/5] Activating Environment...
echo.

call "%VENV_DIR%\Scripts\activate.bat"

if !ERRORLEVEL! neq 0 (
    echo Failed activating environment.
    pause
    exit /b 1
)

cd /d "%CDQUIZ_HOME%"

REM ============================================================
REM STEP 4 - CHECK / INSTALL DEPENDENCIES
REM ============================================================

echo.
echo [4/5] Checking Dependencies...
echo.

pip show rich >nul 2>&1 || set INSTALL_REQUIRED=1
pip show requests >nul 2>&1 || set INSTALL_REQUIRED=1
pip show cdquiz >nul 2>&1 || set INSTALL_REQUIRED=1

python -c "import cdquiz" >nul 2>&1

if !ERRORLEVEL! neq 0 (
    set INSTALL_REQUIRED=1
)

if !INSTALL_REQUIRED! EQU 1 (

    echo Installing dependencies...
    echo.

    python -m pip install --upgrade pip

    pip install --upgrade ^
        rich ^
        requests ^
        cdquiz

    if !ERRORLEVEL! neq 0 (
        echo.
        echo Dependency installation failed.
        pause
        exit /b 1
    )

    echo.
    echo Dependencies installed successfully.
)

REM ============================================================
REM STEP 5 - START CDQUIZ
REM ============================================================

echo.
echo [5/5] Starting CDQuiz...
echo.
echo ============================================================
echo.

python -X utf8 -m cdquiz.start

REM ============================================================
REM CLEAN EXIT
REM ============================================================

call "%VENV_DIR%\Scripts\deactivate.bat" >nul 2>&1

REM Close terminal immediately
exit /b