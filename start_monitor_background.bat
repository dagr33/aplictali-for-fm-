@echo off
REM ════════════════════════════════════════════════════════════════════════════
REM ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - Background Launcher (No Console Window)
REM ════════════════════════════════════════════════════════════════════════════
REM 
REM Այս ֆայլը գործարկում է մոնիտորինգը ֆոնային ռեժիմում (առանց պատուհանի)
REM
REM Օգտագործում. Այս ֆայլը կիրառում, և ծրագիրը կսկսվի ֆոնային ռեժիմում
REM

REM Վերադարձ ընթացիկ ուղղությանը
cd /d "%~dp0"

REM Ստուգել Python-ը տեղադրված է
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python-ը չի գտնվել!
    exit /b 1
)

REM Ստուգել անհրաժեշտ Python պակետները
pip show schedule >nul 2>&1
if errorlevel 1 (
    pip install schedule
)

REM Գործարկել Python ֆոնային ռեժիմում՝ առանց պատուհանի
start /B pythonw radio_monitor_complete.py

REM Ցուցակցել հաջողության հաղորդագրություն
echo 🎙️  Ռադիո մոնիտորինգը սկսված է ֆոնային ռեժիմում
echo 📋 Տեղեկությունները պահվել են՝ radio_stats.db
pause
