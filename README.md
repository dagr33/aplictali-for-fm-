# 🎙️ ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՄԱԿԱՐԳ
## Radio Monitor System - Complete Application

**Digispot II Radio Station Monitoring & Report Generation**

---

## 📋 Table of Contents

1. [Quick Start](#-quick-start)
2. [System Features](#-system-features)
3. [File Guide](#-file-guide)
4. [Installation](#-installation)
5. [Usage](#-usage)
6. [Troubleshooting](#-troubleshooting)

---

## 🚀 Quick Start

### **Windows Users:**
```batch
# Method 1: GUI Application (RECOMMENDED!)
start_gui.bat

# Method 2: Console Monitoring
start_monitor.bat

# Method 3: Background Silent Mode
start_monitor_background.bat

# Method 4: VBScript Stealth Mode
start_monitor_silent.vbs

# Method 5: PowerShell Mode
powershell -ExecutionPolicy Bypass -File start_monitor.ps1
```

### **Linux/Mac Users:**
```bash
# Method 1: GUI Application (RECOMMENDED!)
chmod +x start_gui.sh
./start_gui.sh

# Method 2: Console Monitoring
chmod +x start_monitor.sh
./start_monitor.sh
```

---

## ✨ System Features

### **🖥️ GUI Application** (NEW!)
- ✅ **Visual File Selector** - Browse and select CSV log folders
- ✅ **Process Existing Files** - Generate reports from any `.log` or `.csv` files
- ✅ **Multiple Report Types** - Daily, Monthly, 3-Month, Full analysis
- ✅ **Real-time Monitoring** - Optional continuous monitoring
- ✅ **Status Display** - See what's happening in real-time
- ✅ **User-Friendly** - No command line required!

### **📊 Report Generation**
- ✅ Daily play statistics
- ✅ Monthly summaries with play counts
- ✅ 3-month trend analysis
- ✅ Overplay warnings (songs exceeding limits)
- ✅ Historical data tracking
- ✅ Automatic duplicate detection

### **🔔 Monitoring System**
- ✅ Real-time CSV log monitoring
- ✅ Automatic daily report generation
- ✅ Play count warnings and alerts
- ✅ Flexible time window filtering
- ✅ Configurable check intervals
- ✅ SQLite database storage

### **🎯 Multi-Platform Support**
- ✅ Windows (console, silent, VBScript, PowerShell)
- ✅ Linux (Bash shell)
- ✅ macOS (Bash shell)

---

## 📁 File Guide

### **Essential Files**

| File | Size | Purpose | For Users |
|------|------|---------|-----------|
| **radio_monitor_gui.py** | 23 KB | 🖥️ GUI Application | All Users |
| **radio_monitor_complete.py** | 17 KB | ⚙️ Monitoring Engine | Developers |
| **start_gui.bat** | 1.5 KB | ▶️ Open GUI (Windows) | Windows |
| **start_gui.sh** | 1.4 KB | ▶️ Open GUI (Linux/Mac) | Linux/Mac |

### **Launch Scripts - Console Monitoring**

| File | Purpose | Platform |
|------|---------|----------|
| **start_monitor.bat** | Console mode with visible output | Windows |
| **start_monitor_background.bat** | Silent background mode | Windows |
| **start_monitor_silent.vbs** | VBScript stealth mode | Windows |
| **start_monitor.ps1** | Modern PowerShell mode | Windows |
| **start_monitor.sh** | Standard shell launcher | Linux/Mac |

### **Documentation**

| File | Size | Content |
|------|------|---------|
| **README.md** | ← You are here | Main documentation |
| **QUICK_START.md** | 6.3 KB | Fast setup guide |
| **GUI_README.md** | 11 KB | Complete GUI documentation |
| **SHORTCUTS_README.md** | 4.9 KB | Monitoring script documentation |

---

## 🎯 Which File to Use?

### **I Want to Use the GUI (Recommended)**
```
👉 Use: start_gui.bat (Windows) or ./start_gui.sh (Linux/Mac)
   Open it and select your CSV folder with the file browser!
```

### **I Want to Monitor in Real-Time**
```
👉 Use: start_monitor.bat (Windows) or ./start_monitor.sh (Linux/Mac)
   Program runs continuously and checks for new entries
```

### **I Want to Hide the Program**
```
👉 Use: start_monitor_background.bat (Windows invisible mode)
   OR: start_monitor_silent.vbs (VBScript stealth)
```

### **I Want Modern PowerShell**
```
👉 Use: start_monitor.ps1 (Windows PowerShell)
   Colored output and professional UI
```

---

## 📦 Installation

### **Requirements**
- ✅ Python 3.7 or higher
- ✅ tkinter (included with Python)
- ✅ SQLite3 (included with Python)
- ✅ 100 MB disk space minimum

### **Windows Installation**

1. **Install Python:**
   - Download from https://www.python.org/downloads/
   - During installation, **IMPORTANT:** Check "Add Python to PATH"
   - Also check "tcl/tk and IDLE"

2. **Verify Installation:**
   ```cmd
   python --version
   python -c "import tkinter; print('✅ tkinter OK')"
   ```

3. **Download Radio Monitor:**
   - Extract files to `C:\Users\YourUsername\Desktop\FMApp\`
   - or any folder of your choice

### **Linux Installation**

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-tk python3-pip

# Verify
python3 --version
python3 -c "import tkinter; print('✅ tkinter OK')"

# Extract Radio Monitor
mkdir -p ~/Desktop/FMApp
# Extract files here
```

### **macOS Installation**

```bash
# Using Homebrew
brew install python3
brew install python3-tk

# Verify
python3 --version
python3 -c "import tkinter; print('✅ tkinter OK')"

# Extract Radio Monitor
mkdir -p ~/Desktop/FMApp
# Extract files here
```

---

## 💻 Usage

### **Step 1: Start the Application**

**Windows:**
```batch
Double-click: start_gui.bat
```

**Linux/Mac:**
```bash
./start_gui.sh
```

### **Step 2: Configure Paths**

In the GUI window:

1. **Click "Browse..."** next to "CSV/Log Folder Path"
2. **Select** your Digispot CSV/TXT folder
3. **Set Database Path** (where to store data)
4. **Set Reports Folder** (where reports save)

### **Step 3: Generate Reports**

Choose one:
- **📊 Generate Report for Current Month** - This month only
- **📋 Generate Report for Today** - Today only
- **📈 Generate 3-Month Report** - Last 3 months
- **🔄 Full Report** - Everything

### **Step 4: View Results**

Reports appear in your configured Reports folder:
```
C:\RadioStats\Reports\
├── Radio_Report_Daily_2024-02-13.txt
├── Radio_Report_Monthly_2024-02.txt
├── Radio_Report_3Month_2024-02-13.txt
└── Radio_Report_Full_2024-02-13.txt
```

---

## 🔧 Configuration

### **Modify Settings (Optional)**

Edit `radio_monitor_gui.py` or `radio_monitor_complete.py`:

```python
# Time window for monitoring
START_TIME = "07:50"              # Morning show starts
END_TIME = "10:10"                # Morning show ends

# Warning threshold
MAX_PLAYS_PER_MONTH = 4           # Alert if song plays > 4 times

# Report generation time
WORD_REPORT_TIME = "10:11"        # Auto-generate at 10:11 AM

# Monitoring frequency
CHECK_INTERVAL_MINUTES = 1        # Check every 1 minute
```

### **CSV File Format Required**

Your CSV files must have these columns:
```
Type        EventTime               ElemClass   ElemID   ElemArtist      ElemName
ELEM_INFO   2024-02-13 07:50:00    M           ID_001   Artist Name     Song Title
```

---

## 📊 Example Report

```
════════════════════════════════════════════════════════════════════════
   🎙️  ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՇՎԵՏՎՈՒԹՅՈՒՆ - DAILY
════════════════════════════════════════════════════════════════════════

Ամսաթիվ: 13.02.2024
Ժամեր: 07:50 - 10:10

════════════════════════════════════════════════════════════════════════
ՕՐԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ
════════════════════════════════════════════════════════════════════════

Հիտ '45 երգ նվագարկվել է:
  • 07:50 - System of a Down - Toxicity
  • 07:54 - Serj Tankian - Empty Walls
  • 07:58 - Deftones - Change (In the House of Flies)
  ... and 42 more

════════════════════════════════════════════════════════════════════════
ԱՄՍԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ
════════════════════════════════════════════════════════════════════════

Հայտնի են 158 երգ այս ամսում:
  ⭐ System of a Down - Toxicity: 5 անգամ (EXCEEDS LIMIT!)
  ⭐ Deftones - Change: 4 անգամ (AT LIMIT)
    Serj Tankian - Empty Walls: 3 անգամ
    Rage Against the Machine - Killing: 2 անգամ
  ... and 154 more
```

---

## 🐛 Troubleshooting

### **"Python not found" Error**

**Cause:** Python is not installed or not in PATH

**Solution (Windows):**
```
1. Go to https://www.python.org/downloads/
2. Install Python 3.x
3. During install, CHECK "Add Python to PATH"
4. Restart and try again
```

**Solution (Linux):**
```bash
sudo apt install python3
```

**Solution (macOS):**
```bash
brew install python3
```

### **"tkinter not found" Error**

**Cause:** tkinter not installed with Python

**Solution (Windows):**
```
Reinstall Python with "tcl/tk and IDLE" option checked
```

**Solution (Linux):**
```bash
sudo apt install python3-tk
```

**Solution (macOS):**
```bash
brew install python3-tk
```

### **"No CSV files found" Error**

**Cause:** Wrong folder selected or files not in CSV format

**Solution:**
1. Verify folder contains `.csv` or `.txt` files
2. Check files are from Digispot II
3. Ensure files have correct column headers

### **Reports are Empty**

**Cause:** CSV files don't match expected format or time window

**Solution:**
1. Check CSV files have correct columns
2. Verify EventTime is in your time window
3. Ensure ElemClass is "M" (Music)

### **GUI Won't Open**

**Cause:** tkinter not available

**Solution:**
1. Check: `python3 -c "import tkinter"`
2. If error, reinstall Python with tkinter
3. Try running via terminal directly

---

## 📚 Additional Documentation

- **QUICK_START.md** - Fast setup guide  
- **GUI_README.md** - Complete GUI documentation  
- **SHORTCUTS_README.md** - Monitoring scripts guide  

---

## 🔄 Workflow Options

### **Option A: GUI-Based (Easiest)**
```
1. Run: start_gui.bat or ./start_gui.sh
2. Browse to CSV folder
3. Click "Generate Report"
4. Done! ✅
```

### **Option B: Command-Line Monitoring**
```
1. Run: start_monitor.bat or ./start_monitor.sh
2. Program runs continuously
3. Checks for new songs every minute
4. Auto-generates reports
5. Stop: Press Ctrl+C
```

### **Option C: Scheduled Tasks (Windows)**
```
1. Setup: Use Windows Task Scheduler
2. Trigger: Daily at 10:15 AM
3. Action: Run start_gui.bat
4. Result: Reports auto-generate daily
```

---

## ✅ Checklist - Getting Started

- [ ] Python 3.x installed with tkinter
- [ ] Radio Monitor files extracted
- [ ] Digispot CSV logs available
- [ ] Read QUICK_START.md
- [ ] Launch start_gui.bat or ./start_gui.sh
- [ ] Select your CSV folder
- [ ] Generate a test report
- [ ] Verify report in Reports folder

---

## 🎯 Support & Help

### **For GUI Issues:**
See: **GUI_README.md** - Comprehensive GUI documentation

### **For Monitoring Issues:**
See: **SHORTCUTS_README.md** - Script documentation

### **Common Questions:**

**Q: Can I process existing files?**
A: Yes! The GUI can process any existing `.log` or `.csv` files.

**Q: Do I need to keep the program running?**
A: Only if you want real-time monitoring. Reports can be generated anytime.

**Q: Where are my reports saved?**
A: In the folder you configured in the GUI (default: C:\RadioStats\Reports)

**Q: Can multiple people use this?**
A: Yes, as long as they point to the same database file.

**Q: What if my CSV format is different?**
A: Edit the column mapping in `radio_monitor_gui.py` line 250-280.

---

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│        🎙️ ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ (Radio Monitor)              │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐      ┌──────────────┐                 │
│  │   GUI Layer  │◄────►│ Monitor Core │                 │
│  │  (tkinter)   │      │   (Python)   │                 │
│  └──────────────┘      └──────────────┘                 │
│         ▲                      ▲                         │
│         │ (File Browser)       │ (CSV Parser)           │
│         ▼                      ▼                         │
│  ┌────────────────────────────────────┐                │
│  │   CSV/TXT Files from Digispot II   │                │
│  └────────────────────────────────────┘                │
│         ▲                                               │
│         │ (Parsed Data)                                 │
│         ▼                                               │
│  ┌────────────────────────────────────┐                │
│  │   SQLite Database (play_history)   │                │
│  └────────────────────────────────────┘                │
│         ▲                                               │
│         │ (Query & Aggregate)                           │
│         ▼                                               │
│  ┌────────────────────────────────────┐                │
│  │   Report Generation (Text/DOCX)    │                │
│  └────────────────────────────────────┘                │
│         ▲                                               │
│         │ (Saved Reports)                               │
│         ▼                                               │
│  ┌────────────────────────────────────┐                │
│  │   Reports Folder Output            │                │
│  └────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Next Steps

1. **Read QUICK_START.md** - Fast 5-minute setup
2. **Run start_gui.bat** - Open the GUI
3. **Select your CSV folder** - Click Browse button
4. **Generate a report** - Test the system
5. **Configure monitoring** - Optional continuous operation

---

## 📝 Version Info

| Component | Version | Status |
|-----------|---------|--------|
| GUI Application | 1.0.0 | ✅ Ready |
| Monitor Engine | 1.0.0 | ✅ Ready |
| Documentation | Complete | ✅ Ready |
| Windows Support | Full | ✅ Ready |
| Linux/Mac Support | Full | ✅ Ready |

---

## 📄 License & Credits

**Radio Monitor System**  
For Digispot II Radio Station Management  
Version 1.0.0 - February 2024  

---

## 💬 Questions?

Check the relevant documentation:
- **GUI Questions:** → **GUI_README.md**
- **Setup Questions:** → **QUICK_START.md**
- **Monitoring Questions:** → **SHORTCUTS_README.md**

---

**🎙️ Happy Monitoring! 📊**

*Last Updated: 2024-02-13*  
*Status: ✅ Production Ready*
