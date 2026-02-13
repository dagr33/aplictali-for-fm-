# 🎙️ Radio Monitor GUI Application - User Guide

## Overview

The **Radio Monitor GUI** provides an easy-to-use graphical interface for:
- ✅ Selecting your CSV/log file location with a visual file browser
- ✅ Processing existing `.log` and `.csv` files from Digispot II
- ✅ Generating Word reports (daily, monthly, 3-month, full)
- ✅ Real-time monitoring of new entries
- ✅ Viewing activity logs and statistics

---

## 🚀 How to Launch

### **Windows**

#### Method 1: Double-click the launcher
- Navigate to: `/home/dav/Desktop/FMApp/`
- Double-click: **`start_gui.bat`**

#### Method 2: Command line
```cmd
cd C:\Users\YourUsername\Desktop\FMApp
start_gui.bat
```

#### Method 3: Python directly
```cmd
cd path\to\FMApp
python radio_monitor_gui.py
```

### **Linux / macOS**

#### Method 1: Make executable and run
```bash
cd ~/Desktop/FMApp
chmod +x start_gui.sh
./start_gui.sh
```

#### Method 2: Direct Python
```bash
python3 ~/Desktop/FMApp/radio_monitor_gui.py
```

---

## 📖 GUI Features Explained

### **1. Path Configuration Section**

#### **📂 CSV/Log Folder Path**
- **Purpose:** Select where your Digispot II CSV/TXT log files are stored
- **How to Use:**
  1. Click the **"Browse..."** button next to CSV/Log Folder Path
  2. Select the folder containing your `.csv` and `.txt` files
  3. Path will appear in the text field
  4. Click confirmation message

#### **💾 Database Path**
- **Purpose:** Specify where to store the SQLite database (tracks all songs)
- **Default:** `C:\RadioStats\radio_stats.db` (Windows)
- **Recommendation:** Keep it in a safe location with backup

#### **📄 Word Reports Folder**
- **Purpose:** Choose where to save generated Word/Text reports
- **Default:** `C:\RadioStats\Reports` (Windows)
- **Note:** Folder is created automatically if it doesn't exist

---

### **2. Action Buttons**

#### **📊 Generate Report for Current Month**
- Creates a report with songs played **this month only**
- Shows daily activity + monthly statistics
- File name: `Radio_Report_Monthly_YYYY-MM.txt`

#### **📋 Generate Report for Today**
- Creates a report with songs played **today only**
- Shows hourly breakdown of plays
- File name: `Radio_Report_Daily_YYYY-MM-DD.txt`

#### **📈 Generate 3-Month Report**
- Creates a report covering the **last 3 months**
- Compares monthly trends
- File name: `Radio_Report_3Month_YYYY-MM-DD.txt`

#### **🔄 Full Report**
- Generates a comprehensive report combining:
  - Daily breakdown
  - Monthly statistics
  - 3-month comparison
- File name: `Radio_Report_Full_YYYY-MM-DD.txt`

---

### **3. Monitoring Control**

#### **▶️ Start/Stop Monitoring**
- **Purpose:** Enable real-time monitoring of new log entries
- **Status Indicator:**
  - 🔴 **Red "⏹️ Stopped"** = Monitoring is OFF
  - 🟢 **Green "🔴 Monitoring..."** = Monitoring is ACTIVE

#### **How Monitoring Works:**
1. Click **"▶️ Start Monitoring"** button
2. Status changes to **"🔴 Monitoring..."** (green text)
3. Program checks for new entries every 1 minute
4. New records are reported in the output log
5. Click button again to stop

---

### **4. Output Log**

The **Output Log** panel shows real-time status messages:

**Message Types:**
- 🔵 **Blue messages:** Information and progress
- 🟢 **Green messages:** Success indicators (✅)
- 🔴 **Red messages:** Errors (❌)
- 🟠 **Orange messages:** Warnings (⚠️)

**Example Output:**
```
✅ Selected CSV folder: C:\Digispot\Logs
🔍 Scanning for CSV/TXT files...
📂 Found 3 file(s): 2024-01.csv, 2024-02.csv, 2024-03.csv
📝 Processing: 2024-01.csv
✅ Imported 145 new records
📊 Daily records: 42
✅ Report saved: C:\RadioStats\Reports\Radio_Report_Daily_2024-02-13.txt
```

---

### **5. Status Bar**

The status bar at the bottom shows the current operation:
- `Ready` - Waiting for user action
- `Generating report...` - Processing data
- `✅ Report generated: [filename]` - Report complete

---

## 📝 Typical Workflow

### **First Time Setup**

1. **Launch the GUI**
   ```bash
   ./start_gui.sh  # Linux/Mac
   # or double-click start_gui.bat on Windows
   ```

2. **Configure Paths**
   - Click "Browse..." for CSV folder and select where Digispot logs are
   - Set Database path (where to store the database)
   - Set Word Reports folder (where to save reports)

3. **Generate Initial Report**
   - Click **"🔄 Full Report"** button
   - Wait for processing to complete
   - Report appears in the configured folder

### **Regular Usage**

1. **Daily Reports**
   - Click **"📋 Generate Report for Today"** each day
   - Reports save automatically

2. **Monthly Analysis**
   - Click **"📊 Generate Report for Current Month"** at month-end
   - View trends and statistics

3. **Continuous Monitoring**
   - Click **"▶️ Start Monitoring"** to enable background monitoring
   - Program will alert when songs exceed play limits

---

## 🎯 Report Contents

Each generated report includes:

### **Header Information**
```
════════════════════════════════════════════════════
ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՇՎԵՏՎՈՒԹՅՈՒՆ - DAILY
════════════════════════════════════════════════════
Ամսաթիվ: 13.02.2024
Ժամեր: 07:50 - 10:10
```

### **Daily Section**
- Time of each play
- Artist name
- Song title
- Total songs played

### **Monthly Section**
- Song count per artist
- Plays this month
- ⭐ Star indicates songs exceeding limit

### **Statistics**
- Total plays
- Unique songs
- Most played artist
- Comparison with previous months

---

## ⚙️ Configuration Settings

Edit these in the GUI or directly in `radio_monitor_gui.py`:

```python
START_TIME = "07:50"              # Monitoring start time
END_TIME = "10:10"                # Monitoring end time
MAX_PLAYS_PER_MONTH = 4           # Warning threshold
WORD_REPORT_TIME = "10:11"        # Auto-report time
CHECK_INTERVAL_MINUTES = 1        # Check frequency
```

---

## 🐛 Troubleshooting

### **"Python not found" Error**

**Windows:**
```cmd
# Install Python from https://www.python.org
# Make sure to check "Add Python to PATH" during installation
```

**Linux:**
```bash
sudo apt install python3 python3-tk
```

**macOS:**
```bash
brew install python3
brew install python3-tk
```

### **"tkinter not found" Error**

**Windows:**
- Reinstall Python with "tcl/tk and IDLE" option checked

**Linux:**
```bash
sudo apt install python3-tk
```

**macOS:**
```bash
brew install python3-tk
```

### **"CSV Folder Not Found"**
- Make sure the path exists
- Check for typos in the path
- Ensure you have read permissions

### **"No New Records" Message**
- Check that CSV files are in the correct folder
- Verify the file format (.csv or .txt)
- Ensure files match the expected Digispot II format

### **Report Generation Fails**
- Check that Reports folder exists and is writable
- Verify database file path is accessible
- Ensure sufficient disk space

---

## 📂 File Structure

```
FMApp/
├── radio_monitor_gui.py          # Main GUI application
├── radio_monitor_complete.py     # Backend monitoring engine
├── start_gui.bat                 # Windows launcher
├── start_gui.sh                  # Linux/Mac launcher
├── start_monitor.bat             # Console monitor launcher
├── start_monitor_background.bat  # Silent monitor launcher
├── start_monitor.sh              # Linux monitor launcher
└── README.md                     # Documentation
```

---

## 🔧 Advanced Usage

### **Command Line Arguments** (Future)
```bash
python radio_monitor_gui.py --csv-path /path/to/logs
```

### **Batch Processing**
```bash
# Generate multiple reports in sequence
python radio_monitor_gui.py --mode batch
```

### **Scheduled Tasks** (Windows)
To run reports automatically:
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily at 10:15 AM)
4. Set action: `start_gui.bat`
5. Set conditions to run even if not logged in

---

## 📊 Report Examples

### **Daily Report Output**
```
════════════════════════════════════════════════
   🎙️  ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՇՎԵՏՎՈՒԹՅՈՒՆ - DAILY
════════════════════════════════════════════════

Ամսաթիվ: 13.02.2024
Ժամեր: 07:50 - 10:10

════════════════════════════════════════════════
ՕՐԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ
════════════════════════════════════════════════

Հիտ '42 երգ նվագարկվել է:
  • 07:50 - System of a Down - Toxicity
  • 07:54 - Serj Tankian - Empty Walls
  • 07:58 - Deftones - Change (In the House of Flies)
  • 08:02 - Rage Against the Machine - Killing in the Name
  ... and 38 more

════════════════════════════════════════════════
ԱՄՍԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ
════════════════════════════════════════════════

Հայտնի են 125 երգ այս ամսում:
  ⭐ System of a Down - Toxicity: 5 անգամ (EXCEEDS LIMIT!)
  ⭐ Deftones - Change: 4 անգամ (AT LIMIT)
    Serj Tankian - Empty Walls: 3 անգամ
    Rage Against the Machine - Killing: 2 անգամ
  ... and 121 more
```

---

## 💡 Tips & Best Practices

1. **Always Backup Your Database**
   - Copy `radio_stats.db` regularly to a safe location

2. **Use Consistent CSV Paths**
   - Keep all Digispot logs in one folder

3. **Generate Reports Weekly**
   - Maintain historical records for trend analysis

4. **Monitor "Overplayed" Warnings**
   - Check for songs exceeding MAX_PLAYS_PER_MONTH
   - Adjust the limit as needed

5. **Keep GUI Running**
   - Leave monitoring active during broadcast hours
   - Reports can be generated independently

---

## 📞 Support

For issues or questions:

1. **Check the Troubleshooting section** above
2. **Verify all paths exist** and are readable
3. **Ensure Python 3.x is installed**
4. **Check output log for error messages**
5. **Contact system administrator** if problems persist

---

## 📝 Version Info

- **Application:** Radio Monitor GUI v1.0
- **Python Required:** Python 3.7+
- **Dependencies:** tkinter (included with Python)
- **Database:** SQLite3 (included with Python)
- **Last Updated:** 2024-02-13

---

**🎙️ Radio Monitor - Professional Broadcasting Management System**
