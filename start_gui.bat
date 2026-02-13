@echo off
chcp 65001 >nul 2>&1
color 0A
setlocal enabledelayedexpansion

echo.
echo ════════════════════════════════════════════════════════════════════════
echo   🎙️  ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - GUI Application
echo ════════════════════════════════════════════════════════════════════════
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python մեծ տեղադրված. Խնդրում ենք տեղադրել Python 3.x
    echo 📥 Ներբեռնել Python-ից՝ https://www.python.org
    pause
    exit /b 1
)

REM Check for required modules
echo 🔍 Ստուգում են մոդուլները...
python -c "import tkinter" >nul 2>&1
if errorlevel 1 (
    echo ❌ tkinter չ մոդուլ պահանջվում դա Python տեղադրմամբ դրված
    echo 📥 Վերատեղադրել Python "tcl/tk and IDLE" ընտրությամբ
    pause
    exit /b 1
)

REM Launch GUI
echo ✅ Python ճիշտ տեղադրված
echo.
echo 🚀 Գործարկում GUI...
echo.

python radio_monitor_gui.py

if errorlevel 1 (
    echo.
    echo ❌ Սխալ տեղի ունեցավ
    pause
)

exit /b 0
