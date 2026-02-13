# 🎙️ Quick Start Guide - Radio Monitor with GUI

## What's New? 
✨ **GUI Application** for easy file selection and report generation!

---

## 📦 Files Created

| File | Purpose |
|------|---------|
| `radio_monitor_gui.py` | 🖥️ Main GUI application (23 KB) |
| `start_gui.bat` | ▶️ Windows launcher for GUI |
| `start_gui.sh` | ▶️ Linux/Mac launcher for GUI |
| `GUI_README.md` | 📖 Complete GUI documentation |

---

## 🚀 Quick Start (Choose Your Method)

### **Option 1: Windows - Double Click**
1. Open `/home/dav/Desktop/FMApp/`
2. Double-click **`start_gui.bat`**
3. GUI window opens → Select your CSV folder → Done!

### **Option 2: Linux/Mac - Terminal**
```bash
cd ~/Desktop/FMApp
chmod +x start_gui.sh
./start_gui.sh
```

### **Option 3: Direct Python**
```bash
python radio_monitor_gui.py
```

---

## 🎯 In the GUI, You Can:

1. **📂 Select CSV Folder** - Browse and pick your Digispot logs
2. **💾 Set Database Path** - Where to store the database
3. **📄 Set Reports Folder** - Where reports are saved
4. **🔄 Generate Reports** - Daily, Monthly, 3-Month, or Full
5. **🔔 Start Monitoring** - Continuous real-time monitoring
6. **📝 View Logs** - See what's happening in real-time

---

## 📊 Report Features

### **Generate Reports for Existing Files**
✅ The GUI can process **any existing `.log` and `.csv` files**
✅ No need to wait for real-time monitoring
✅ Works with historical data

### **Generate Types:**
- **Daily Report** - Today's plays only
- **Monthly Report** - Current month stats
- **3-Month Report** - Trend analysis
- **Full Report** - Everything combined

---

## ⚙️ Setup (First Time)

1. **Launch GUI** (`start_gui.bat` or `./start_gui.sh`)
2. **Click "Browse..."** next to "CSV/Log Folder Path"
3. **Select** your Digispot logs folder
4. **Set paths** for Database and Reports (or keep defaults)
5. **Click** any report button to generate

**Boom! ✅ Report generated!**

---

## 📂 Typical Folder Structure

```
📁 Digispot Logs
├── 2024-01.csv
├── 2024-02.csv
├── 2024-03.txt
└── January-Feb.csv

👇 Select the folder containing these files
```

---

## 📝 What Reports Look Like

```
════════════════════════════════════════════════
   🎙️  ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - DAILY
════════════════════════════════════════════════

Date: 13.02.2024
Hours: 07:50 - 10:10

════════════════════════════════════════════════
DAILY STATISTICS
════════════════════════════════════════════════

45 songs played today:
  • 07:50 - System of a Down - Toxicity
  • 07:54 - Serj Tankian - Empty Walls
  • 07:58 - Deftones - Change
  ... and 42 more

════════════════════════════════════════════════
MONTHLY STATISTICS
════════════════════════════════════════════════

158 songs this month:
  ⭐ System of a Down - Toxicity: 5 plays (OVER LIMIT!)
  ⭐ Deftones - Change: 4 plays (AT LIMIT)
    Serj Tankian - Empty Walls: 3 plays
    Rage Against: 2 plays
  ... and 154 more
```

---

## 🔍 File Format Supported

### ✅ Works With:
- `.csv` files from Digispot II
- `.txt` files (CSV format)
- Mixed file types in one folder

### ✅ Requires These Columns:
```
Type        | EventTime           | ElemClass | ElemID | ElemArtist        | ElemName
ELEM_INFO   | 2024-02-13 07:50:00 | M         | ID123  | System of a Down  | Toxicity
```

---

## 🎮 GUI Controls Explained

### **📂 CSV/Log Folder Path**
- **Button:** "Browse..." opens file picker
- **Result:** Path shown in text field

### **💾 Database Path**
- **Current Setting:** `C:\RadioStats\radio_stats.db`
- **Purpose:** Stores all song history

### **📄 Word Reports Folder**
- **Current Setting:** `C:\RadioStats\Reports`
- **Purpose:** Where reports save

### **Report Buttons**
- **📊:** Current month only
- **📋:** Today only
- **📈:** Last 3 months
- **🔄:** Complete analysis

### **Monitoring**
- **▶️ Start:** Enables real-time monitoring
- **Status:** Shows if active (green) or stopped (red)

---

## 🎯 Common Tasks

### **Generate Report for February:**
1. Open GUI
2. Select your CSV folder
3. Click **"📊 Generate Report for Current Month"**
4. Report appears in Reports folder
5. Done! ✅

### **Process Historical Files:**
1. Open GUI
2. Browse to folder with old `.csv` files
3. Click **"🔄 Full Report"**
4. All files processed automatically
5. Report generated ✅

### **Continuous Monitoring:**
1. Open GUI
2. Configure paths
3. Click **"▶️ Start Monitoring"**
4. Leave running
5. Reports generate automatically ✅

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| GUI won't open | Make sure Python is installed (`python --version`) |
| "Python not found" | Install Python 3.x from python.org |
| "tkinter not found" | Reinstall Python with "tcl/tk" option checked |
| No files detected | Check CSV folder path is correct |
| Report empty | Ensure CSV has correct format/time window |

---

## 📚 More Information

For detailed GUI documentation, see: **`GUI_README.md`**

For original monitoring documentation, see: **`SHORTCUTS_README.md`**

---

## 🎓 Next Steps

1. **Try the GUI** - `start_gui.bat` (Windows) or `./start_gui.sh` (Linux/Mac)
2. **Select your CSV folder** with the browse button
3. **Generate a test report** to see how it works
4. **Configure monitoring** for continuous operation

---

## ✨ Summary

Your Radio Monitoring System now has:

✅ **GUI Interface** - Easy file selection  
✅ **Existing File Processing** - Works with `.log` and `.csv` files  
✅ **Multiple Report Types** - Daily, Monthly, 3-Month, Full  
✅ **Real-time Monitoring** - Optional background monitoring  
✅ **Complete Documentation** - This guide + GUI_README.md  

**Ready to use! 🚀**

---

**Version:** 1.0.0  
**Last Updated:** 2024-02-13  
**Status:** ✅ Production Ready
