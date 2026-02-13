#!/bin/bash

echo ""
echo "════════════════════════════════════════════════════════════════════════"
echo "   🎙️  ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - GUI Application"
echo "════════════════════════════════════════════════════════════════════════"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 չ տեղադրված"
    echo "📥 Տեղադրել՝ sudo apt install python3 (Ubuntu/Debian)"
    echo "📥 Տեղադրել՝ brew install python3 (macOS)"
    exit 1
fi

# Check Python version
python3_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✅ Python տեղադրված: $python3_version"

# Check for tkinter
python3 -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ tkinter մոդուլ բացակայում է"
    echo "📥 Տեղադրել՝ sudo apt install python3-tk (Ubuntu/Debian)"
    echo "📥 Տեղադրել՝ brew install python3-tk (macOS)"
    exit 1
fi

echo "✅ Բոլոր մոդուլները տեղադրված են"
echo ""
echo "🚀 Գործարկում GUI..."
echo ""

python3 radio_monitor_gui.py

exit 0
