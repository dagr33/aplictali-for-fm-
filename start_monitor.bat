@echo off
REM ════════════════════════════════════════════════════════════════════════════
REM ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - Windows Launcher
REM ════════════════════════════════════════════════════════════════════════════

REM Վերադարձ ընթացիկ ուղղությանը
cd /d "%~dp0"

REM Ստուգել Python-ը տեղադրված է
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python-ը չի գտնվել!
    echo Տեղադրիր Python՝ https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Ստուգել անհրաժեշտ Python պակետները
echo 📦 Ստուգում եմ անհրաժեշտ պակետները...
pip show schedule >nul 2>&1
if errorlevel 1 (
    echo 📥 Տեղադրում եմ schedule...
    pip install schedule
)

REM Սկսել մոնիտորինգը
echo.
echo 🎙️  Սկսում եմ ռադիո մոնիտորինգը...
echo.
python radio_monitor_complete.py

REM Պահել պատուհանը բաց այն դեպքում, երբ ծրագիրը բաց թողնի
echo.
echo ⏹️  Մոնիտորինգը դադարեցված է
pause
