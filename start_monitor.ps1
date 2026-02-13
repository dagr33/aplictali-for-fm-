# ════════════════════════════════════════════════════════════════════════════
# ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - PowerShell Launcher
# ════════════════════════════════════════════════════════════════════════════
#
# Օգտագործում: Right-click > "Run with PowerShell"
#

# Set working directory
Set-Location $PSScriptRoot

# Colors for output
$InfoColor = "Cyan"
$ErrorColor = "Red"
$SuccessColor = "Green"

# Check if Python is installed
Write-Host "🔍 Ստուգում եմ Python... " -ForegroundColor $InfoColor
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Python-ը չի գտնվել!" -ForegroundColor $ErrorColor
    Write-Host "📥 Տեղադրիր Python: https://www.python.org/downloads/" -ForegroundColor $InfoColor
    pause
    exit 1
}
Write-Host "✅ Python $pythonCheck հայտնաբերված" -ForegroundColor $SuccessColor

# Check required packages
Write-Host "📦 Ստուգում եմ անհրաժեշտ պակետները... " -ForegroundColor $InfoColor
$scheduleCheck = pip show schedule 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "📥 Տեղադրում եմ schedule պակետը... " -ForegroundColor $InfoColor
    pip install schedule --quiet
    Write-Host "✅ schedule տեղադրված է" -ForegroundColor $SuccessColor
} else {
    Write-Host "✅ Բոլոր պակետները բևեռ են" -ForegroundColor $SuccessColor
}

# Start monitoring
Write-Host "`n" -ForegroundColor $InfoColor
Write-Host "🎙️  Սկսում եմ ռադիո մոնիտորինգը..." -ForegroundColor $SuccessColor
Write-Host "════════════════════════════════════════════════" -ForegroundColor $InfoColor
Write-Host "`n" -ForegroundColor $InfoColor

# Run the monitor
python radio_monitor_complete.py

# Show completion message
Write-Host "`n" -ForegroundColor $InfoColor
Write-Host "════════════════════════════════════════════════" -ForegroundColor $InfoColor
Write-Host "⏹️  Մոնիտորինգը դադարեցված է" -ForegroundColor $SuccessColor
Write-Host "📊 Տվյալները պահվել են database-ում" -ForegroundColor $InfoColor
Read-Host "Սեղմեք Enter ելքի համար"
