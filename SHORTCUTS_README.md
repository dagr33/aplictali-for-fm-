# 📱 Radio Monitor - Shortcuts Guide

## Windows Shortcuts

### 1️⃣ **start_monitor.bat** (Recommended for beginners)
**Նկարագրություն:** Կանոնական կմեկնարկ առ գրաֆիկական պատուհանով
- ✅ Ցույց տալով console պատուհան
- ✅ Real-time վերահսկում
- ✅ Մեղադրանքներ և զգուշացումներ անմիջապես տեսանելի
- ⛔ Պետք՛ է պատուհանը բաց մնա

**Օգտագործում:**
1. Կրկնակի սեղմել `start_monitor.bat` ֆայլը
2. Console պատուհան կբացվի
3. Սեղմել `Ctrl+C` դադարեցնելու համար

---

### 2️⃣ **start_monitor_background.bat** (For regular use)
**Նկարագրություն:** Ֆոնային գործարկում՝ առանց console պատուհանի
- ✅ Ծրագիրը գործարկվում է ֆոնային պրոցեսում
- ✅ Պատուհան չի բացվում
- ✅ Հարմար համար անընդհատ մոնիտորինգի
- ⚠️ Դադարեցնելու համար՝ Task Manager: `Ctrl+Shift+Esc`

**Օգտագործում:**
1. Կրկնակի սեղմել `start_monitor_background.bat`
2. Հաջողության հաղորդագրություն կհայտնվի
3. Ծրագիրը կգործարկվի ֆոնային պրոցեսում

---

### 3️⃣ **start_monitor_silent.vbs** (For power users)
**Նկարագրություն:** Լիովին ցածր պրոֆիլ, առանց որևէ պատուհանի
- ✅ Բացարձակ ծածանել պատուհան
- ✅ Միայն մեկ պատկերակ ցանկին
- ✅ Օպտիմալ համար server-style գործարկում
- ℹ️ Միայն errors ցույց կտա

**Օգտագործում:**
1. Կրկնակի սեղմել `start_monitor_silent.vbs`
2. Հաղորդագրական տուփ կբացվի՝ հաստատելու համար
3. Ծրագիրը կսկսվի ամբողջովին ցածր վիճակում

---

## Linux/Mac Shortcuts

### 🐧 **start_monitor.sh** (For Linux/Mac)
**Նկարագրություն:** Terminal-ից գործարկում
- ✅ Real-time վերահսկում Terminal-ում
- ✅ Լոգ ֆայլեր stores-ում
- ✅ Easy to debug

**Օգտագործում:**
```bash
# Կատարել ֆայլը բացասական
chmod +x start_monitor.sh

# Գործարկել ֆայլը
./start_monitor.sh

# Կամ
bash start_monitor.sh
```

**Դադարեցնել:** `Ctrl+C`

---

## Desktop Shortcuts (Windows)

### Create a Desktop Shortcut:

1. **Right-click** on desktop
2. Select **New > Shortcut**
3. Paste one of these paths:

**For console version:**
```
%SystemRoot%\System32\cmd.exe /k "C:\path\to\FMApp\start_monitor.bat"
```

**For background version:**
```
C:\path\to\FMApp\start_monitor_background.bat
```

**For silent version:**
```
C:\path\to\FMApp\start_monitor_silent.vbs
```

4. Click **Next**
5. Name it: `Radio Monitor`
6. Click **Finish**

### Optional: Change Icon
1. **Right-click** desktop shortcut
2. **Properties**
3. **Change Icon...**
4. Browse to find a custom icon (e.g., music icon)

---

## Keyboard Shortcuts (Alternative Method)

If you want to run from anywhere using Windows PowerShell:

```powershell
# Add to PowerShell profile
Set-Alias radiomonitor "C:\path\to\FMApp\start_monitor.bat"

# Then just type:
radiomonitor
```

---

## Startup Automation (Windows)

### Run on Windows Startup:

1. Press `Win + R`
2. Type: `shell:startup`
3. Paste a shortcut to one of the `.bat` files
4. Restart computer

---

## Task Scheduler (Windows)

For automatic daily reports:

1. Press `Win + R`
2. Type: `taskschd.msc`
3. Click **Create Basic Task**
4. Set **Name:** `Radio Monitor Report`
5. **Trigger:** Daily at your preferred time
6. **Action:** Start a program
7. **Program:** `C:\path\to\FMApp\start_monitor.bat`
8. Click **OK**

---

## Stopping the Program

### Method 1: Console Window
- Simply press `Ctrl+C` in the console

### Method 2: Task Manager (Windows)
- Press `Ctrl+Shift+Esc`
- Find `python.exe` or `pythonw.exe`
- Click **End Task**

### Method 3: Terminal (Linux/Mac)
- Press `Ctrl+C` in terminal

---

## Troubleshooting

### ❌ "Command not found" on Linux
```bash
chmod +x start_monitor.sh
./start_monitor.sh
```

### ❌ "Python not found"
- Install Python: https://www.python.org/downloads/ (Windows)
- Or: `sudo apt install python3` (Linux)

### ❌ "Module not found: schedule"
The `.bat`/`.sh` files will auto-install it

### ❌ Cannot find CSV files
- Edit `radio_monitor_complete.py`
- Update `CSV_FOLDER_PATH` with correct path

---

## Summary

| Shortcut | Best For | Shows Console |
|----------|----------|---------------|
| `start_monitor.bat` | Testing & Debugging | ✅ Yes |
| `start_monitor_background.bat` | Normal Use | ❌ No |
| `start_monitor_silent.vbs` | Server/Background | ❌ No |
| `start_monitor.sh` | Linux/Mac | ✅ Yes |

Choose based on your needs! 🚀
