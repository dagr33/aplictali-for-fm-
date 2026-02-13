#!/bin/bash
########################################################################################
# ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - Linux Launcher
########################################################################################

# Վերադարձ ընթացիկ ուղղությանը
cd "$(dirname "$0")"

# Ստուգել Python-ը տեղադրված է
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3-ը չի գտնվել!"
    echo "Տեղադրիր Python՝ sudo apt install python3 python3-pip"
    exit 1
fi

# Ստուգել schedule պակետը
echo "📦 Ստուգում եմ անհրաժեշտ պակետները..."
python3 -c "import schedule" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📥 Տեղադրում եմ schedule..."
    pip3 install schedule
fi

# Սկսել մոնիտորինգը
echo ""
echo "🎙️  Սկսում եմ ռադիո մոնիտորինգը..."
echo ""
python3 radio_monitor_complete.py

# Հաղորդագրություն վախճանից
echo ""
echo "⏹️  Մոնիտորինգը դադարեցված է"
