# 🎙️ SETUP & INSTALLATION GUIDE
## Radio Monitor GUI - Complete Setup Instructions

---

## ⚡ 30-Second Overview

You now have a **GUI application** that lets you:
1. ✅ **Browse & select** your CSV log files with a file picker
2. ✅ **Process existing files** (not just real-time monitoring)
3. ✅ **Generate reports** (Daily, Monthly, 3-Month, Full)
4. ✅ **Monitor continuously** (optional)

**No typing commands needed!** Just click buttons.

---

## 💿 SYSTEM REQUIREMENTS

### **Minimum**
- Python 3.7 or higher
- 50 MB free disk space
- Windows 7+, Linux, or macOS

### **Optional**
- Node.js (for advanced Word document formatting - not required for basic operation)

---

## 🪟 WINDOWS SETUP (5 Minutes)

### **Step 1: Install Python**

1. Go to: https://www.python.org/downloads/
2. Click **"Download Python 3.x.x"** (latest version)
3. **RUN the installer**
4. **IMPORTANT:** In the installer window:
   - ☑️ Check the box: **"Add Python to PATH"**
   - ☑️ Check the box: **"Install tcl/tk and IDLE"**
5. Click **"Install Now"**
6. Wait for completion
7. Click **"Close"**

### **Step 2: Verify Installation**

1. Open **Command Prompt** (Press `Win+R`, type `cmd`, press Enter)
2. Copy and paste this command:
   ```cmd
   python --version
   ```
3. You should see: `Python 3.x.x` ✅

### **Step 3: Launch the Application**

1. Go to: `C:\Users\YourUsername\Desktop\FMApp\`
2. Find file: **`start_gui.bat`**
3. **Double-click it** 🎯
4. GUI window opens! ✅

### **If it Doesn't Work:**

**"Python not found" error:**
- Step 1 didn't work - reinstall Python with "Add to PATH" checked

**"tkinter not found" error:**
- Step 1 didn't work - reinstall with "tcl/tk" option checked

**Still not working?**
```cmd
# Open Command Prompt and run:
python -c "import tkinter; print('✅ tkinter OK')"
```

If this shows an error, tkinter isn't installed. Reinstall Python.

---

## 🐧 LINUX SETUP (2 Minutes)

### **Ubuntu / Debian:**

```bash
# 1. Update package list
sudo apt update

# 2. Install Python and tkinter
sudo apt install python3 python3-tk python3-pip -y

# 3. Verify installation
python3 --version
python3 -c "import tkinter; print('✅ tkinter OK')"
```

### **Fedora / RHEL / CentOS:**

```bash
# 1. Install Python and tkinter
sudo dnf install python3 python3-tkinter -y

# 2. Verify installation
python3 --version
python3 -c "import tkinter; print('✅ tkinter OK')"
```

### **Step 2: Launch the Application**

1. Open Terminal
2. Navigate to the application:
   ```bash
   cd ~/Desktop/FMApp
   ```
3. Make launcher executable:
   ```bash
   chmod +x start_gui.sh
   ```
4. Run it:
   ```bash
   ./start_gui.sh
   ```
5. GUI window opens! ✅

---

## 🍎 MACOS SETUP (3 Minutes)

### **Using Homebrew (Recommended):**

```bash
# 1. Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Install Python and tkinter
brew install python3
brew install python3-tk

# 3. Verify installation
python3 --version
python3 -c "import tkinter; print('✅ tkinter OK')"
```

### **Using Python.org Installer:**

1. Go to: https://www.python.org/downloads/macos/
2. Download **"Python 3.x.x installer"**
3. Run the installer
4. Follow on-screen instructions
5. Verify: `python3 --version`

### **Step 2: Launch the Application**

1. Open Terminal
2. Navigate to the application:
   ```bash
   cd ~/Desktop/FMApp
   ```
3. Make launcher executable:
   ```bash
   chmod +x start_gui.sh
   ```
4. Run it:
   ```bash
   ./start_gui.sh
   ```
5. GUI window opens! ✅

---

## 📖 FIRST-TIME USAGE

### **After GUI Opens:**

1. **Click "Browse..."** next to "📂 CSV/Log Folder Path"
   ```
   This opens a folder selector
   ```

2. **Navigate to your Digispot logs folder**
   ```
   Example: C:\Digispot\Logs or ~/digispot/logs
   ```

3. **Click "Select Folder"**
   ```
   Folder path appears in the text field
   ```

4. **(Optional) Change Database and Reports paths**
   ```
   Or use the default locations
   ```

5. **Click one of the report buttons:**
   - 📊 For **Current Month** report
   - 📋 For **Today's** report
   - 📈 For **3-Month** comparison
   - 🔄 For **Full** comprehensive report

6. **Wait for processing**
   ```
   See status in the output log panel
   ```

7. **Report is generated! ✅**
   ```
   Check your Reports folder for the file
   ```

---

## 📂 FOLDER STRUCTURE

After setup, you should have:

```
FMApp/
├── 📄 README.md                    ← Main documentation
├── 📄 QUICK_START.md               ← Fast guide
├── 📄 GUI_README.md                ← GUI documentation
├── 📄 SETUP_GUIDE.md               ← ← You are here
│
├── 🖥️ GUI Application
│   ├── radio_monitor_gui.py        ← Main GUI (23 KB)
│   ├── start_gui.bat               ← Windows launcher
│   └── start_gui.sh                ← Linux/Mac launcher
│
├── ⚙️ Monitoring System (Optional)
│   ├── radio_monitor_complete.py
│   ├── start_monitor.bat
│   ├── start_monitor_background.bat
│   ├── start_monitor_silent.vbs
│   ├── start_monitor.ps1
│   └── start_monitor.sh
│
└── 📊 Your Data (Created After First Run)
    ├── radio_stats.db              ← Database (auto-created)
    └── Reports/                    ← Reports folder (auto-created)
        ├── Radio_Report_Daily_2024-02-13.txt
        ├── Radio_Report_Monthly_2024-02.txt
        └── ...
```

---

## 🧪 TESTING THE INSTALLATION

### **Step 1: Verify Python**

**Windows:**
```cmd
python --version
# Should show: Python 3.x.x
```

**Linux/Mac:**
```bash
python3 --version
# Should show: Python 3.x.x
```

### **Step 2: Verify tkinter**

**Windows:**
```cmd
python -c "import tkinter; print('✅ OK')"
```

**Linux/Mac:**
```bash
python3 -c "import tkinter; print('✅ OK')"
```

### **Step 3: Launch the GUI**

**Windows:**
```
Double-click start_gui.bat
```

**Linux/Mac:**
```bash
./start_gui.sh
```

If a GUI window opens, everything is set up! ✅

---

## 🐛 TROUBLESHOOTING

### **Problem: "python: command not found" (Linux/Mac)**

**Solution:**
```bash
# Use python3 instead of python
python3 --version
```

### **Problem: "Python is not installed" (Windows)**

**Solution:**
1. Download Python from https://www.python.org
2. **Important:** Check "Add Python to PATH" during install
3. Restart computer after installation
4. Try again

### **Problem: "tkinter not found"**

**Windows:**
```
Reinstall Python with "tcl/tk and IDLE" option
```

**Linux - Ubuntu/Debian:**
```bash
sudo apt install python3-tk
```

**Linux - Fedora/RHEL:**
```bash
sudo dnf install python3-tkinter
```

**macOS:**
```bash
brew install python3-tk
```

### **Problem: GUI Opens But Freezes**

**Cause:** Possibly trying to process very large CSV files

**Solution:**
1. Close the GUI
2. Make sure CSV files aren't too large
3. Try with a smaller test CSV file first

### **Problem: "No files found" Error**

**Cause:** CSV files not in the selected folder or wrong format

**Solution:**
1. Verify CSV files actually exist in the folder
2. Check that files are `.csv` or `.txt` format
3. Ensure files are from Digispot II

### **Problem: Report is Empty**

**Cause:** CSV files don't match expected format or no data in time window

**Solution:**
1. Verify CSV has required columns: Type, EventTime, ElemClass, ElemID, ElemArtist, ElemName
2. Check that songs are in the time window (07:50 - 10:10)
3. Check that ElemClass column contains "M" for Music

---

## ✅ INSTALLATION CHECKLIST

- [ ] Python 3.7+ installed
- [ ] Python added to PATH (Windows)
- [ ] tkinter installed
- [ ] Verified with `python --version`
- [ ] Verified with `python -c "import tkinter"`
- [ ] Application folder extracted
- [ ] start_gui.bat or start_gui.sh found
- [ ] Launcher opens GUI successfully
- [ ] All buttons visible in GUI
- [ ] Ready to use! 🎉

---

## 📝 UNINSTALLATION

### **If You Want to Uninstall:**

**Windows:**
1. Go to: Settings → Programs → Programs and Features
2. Find and click: Python 3.x.x
3. Click: Uninstall
4. Delete the FMApp folder

**Linux:**
```bash
sudo apt remove python3 python3-tk
# OR
sudo dnf remove python3 python3-tkinter
```

**macOS:**
```bash
brew uninstall python3
brew uninstall python3-tk
```

---

## 🚀 NEXT STEPS

1. ✅ **Complete Setup** - Follow steps above
2. ✅ **Launch GUI** - Run start_gui.bat or ./start_gui.sh
3. ✅ **Select CSV Folder** - Click Browse button
4. ✅ **Generate Report** - Click any report button
5. ✅ **View Results** - Check Reports folder

---

## 📞 HELP & SUPPORT

### **For GUI Questions:**
See: `GUI_README.md`

### **For Quick Start:**
See: `QUICK_START.md`

### **For Main Documentation:**
See: `README.md`

### **For Monitoring System:**
See: `SHORTCUTS_README.md`

---

## 📊 WHAT YOU CAN DO AFTER SETUP

✅ Browse CSV folders with visual file picker  
✅ Process existing log files automatically  
✅ Generate daily radio play reports  
✅ Analyze monthly statistics  
✅ Track 3-month trends  
✅ Monitor in real-time (optional)  
✅ View live status updates  
✅ Export data for analysis  

---

## 🎯 QUICK COMMAND REFERENCE

### **Windows**
```cmd
# Python version check
python --version

# tkinter check
python -c "import tkinter; print('OK')"

# Launch GUI
start_gui.bat

# Launch monitoring
start_monitor.bat
```

### **Linux/Mac**
```bash
# Python version check
python3 --version

# tkinter check
python3 -c "import tkinter; print('OK')"

# Launch GUI
./start_gui.sh

# Launch monitoring
./start_monitor.sh
```

---

## 🎉 SUCCESS!

When you see the GUI window with:
- ✅ Path configuration fields
- ✅ Browse buttons
- ✅ Report generation buttons
- ✅ Output log panel

**You're ready to go! 🚀**

---

**Version:** 1.0.0  
**Last Updated:** 2024-02-13  
**Status:** ✅ Ready for Use
