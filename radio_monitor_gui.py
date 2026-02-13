"""
================================================================================
ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - GUI Application with UI
================================================================================

Նկարագրություն:
- GUI-ով մուտքի ընտրիչ `.log` ֆայլերի համար
- Գոյություն ունեցող `.log` ֆայլերից Word հաշվետվություն ստեղծել
- Real-time մոնիտորինգ

ԳՈՐԾԱՐԿՈՒՄ:
python radio_monitor_gui.py
================================================================================
"""

import os
import csv
import sqlite3
from datetime import datetime, timedelta
import json
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import threading

# ════════════════════════════════════════════════════════════════════════════
# DEFAULT SETTINGS
# ════════════════════════════════════════════════════════════════════════════

DEFAULT_DATABASE_PATH = r"C:\RadioStats\radio_stats.db"
DEFAULT_WORD_REPORT_PATH = r"C:\RadioStats\Reports"
DEFAULT_LOG_FILE_PATH = r"C:\RadioStats\warnings.log"

START_TIME = "07:50"
END_TIME = "10:10"
MAX_PLAYS_PER_MONTH = 4
WORD_REPORT_TIME = "10:11"
CHECK_INTERVAL_MINUTES = 1

SHOW_CONSOLE_WARNING = True
SAVE_TO_LOG_FILE = True


class RadioMonitorGUI:
    """GUI Application for Radio Monitoring"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🎙️ Radio Monitor - Digispot II")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # Variables
        self.csv_folder_path = tk.StringVar()
        self.database_path = tk.StringVar(value=DEFAULT_DATABASE_PATH)
        self.word_report_path = tk.StringVar(value=DEFAULT_WORD_REPORT_PATH)
        
        self.is_monitoring = False
        self.monitor_thread = None
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        """Create the main user interface"""
        
        # Header
        header_frame = ttk.Frame(self.root, padding="10")
        header_frame.pack(fill=tk.X, padx=10, pady=5)
        
        title = ttk.Label(header_frame, text="🎙️ ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՄԱԿԱՐԳ", 
                         font=("Arial", 14, "bold"))
        title.pack()
        
        subtitle = ttk.Label(header_frame, text="Digispot II Log File Manager & Word Report Generator",
                           font=("Arial", 10))
        subtitle.pack()
        
        # Separator
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # Path Selection Frame
        path_frame = ttk.LabelFrame(self.root, text="📁 Path Configuration", padding="10")
        path_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # CSV Folder Path
        ttk.Label(path_frame, text="📂 CSV/Log Folder Path:").grid(row=0, column=0, sticky=tk.W, pady=5)
        ttk.Entry(path_frame, textvariable=self.csv_folder_path, width=50).grid(row=0, column=1, padx=5)
        ttk.Button(path_frame, text="Browse...", command=self.browse_csv_folder).grid(row=0, column=2, padx=5)
        
        # Database Path
        ttk.Label(path_frame, text="💾 Database Path:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(path_frame, textvariable=self.database_path, width=50).grid(row=1, column=1, padx=5)
        ttk.Button(path_frame, text="Browse...", command=self.browse_database_path).grid(row=1, column=2, padx=5)
        
        # Word Report Path
        ttk.Label(path_frame, text="📄 Word Reports Folder:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(path_frame, textvariable=self.word_report_path, width=50).grid(row=2, column=1, padx=5)
        ttk.Button(path_frame, text="Browse...", command=self.browse_word_report_path).grid(row=2, column=2, padx=5)
        
        # Separator
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # Action Buttons Frame
        buttons_frame = ttk.LabelFrame(self.root, text="🎯 Actions", padding="10")
        buttons_frame.pack(fill=tk.X, padx=10, pady=5)
        
        button_grid = ttk.Frame(buttons_frame)
        button_grid.pack(fill=tk.X)
        
        ttk.Button(button_grid, text="📊 Generate Report for Current Month", 
                  command=self.generate_monthly_report).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_grid, text="📋 Generate Report for Today", 
                  command=self.generate_daily_report).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_grid, text="📈 Generate 3-Month Report", 
                  command=self.generate_three_month_report).pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(button_grid, text="🔄 Full Report", 
                  command=self.generate_full_report).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Separator
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # Monitoring Frame
        monitor_frame = ttk.LabelFrame(self.root, text="🔔 Monitoring Control", padding="10")
        monitor_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.monitor_button = ttk.Button(monitor_frame, text="▶️ Start Monitoring", 
                                        command=self.toggle_monitoring)
        self.monitor_button.pack(side=tk.LEFT, padx=5)
        
        self.monitor_status = ttk.Label(monitor_frame, text="⏹️ Stopped", foreground="red")
        self.monitor_status.pack(side=tk.LEFT, padx=10)
        
        # Separator
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)
        
        # Output Log Frame
        output_frame = ttk.LabelFrame(self.root, text="📝 Output Log", padding="10")
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, height=15, width=80,
                                                    font=("Courier", 9))
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for colors
        self.output_text.tag_config("info", foreground="blue")
        self.output_text.tag_config("success", foreground="green")
        self.output_text.tag_config("error", foreground="red")
        self.output_text.tag_config("warning", foreground="orange")
        
        # Status Bar
        status_frame = ttk.Frame(self.root)
        status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.status_label = ttk.Label(status_frame, text="Ready", relief=tk.SUNKEN)
        self.status_label.pack(fill=tk.X)
        
    def browse_csv_folder(self):
        """Browse for CSV folder"""
        folder = filedialog.askdirectory(title="Select CSV/Log Folder")
        if folder:
            self.csv_folder_path.set(folder)
            self.log_output(f"✅ Selected CSV folder: {folder}", "success")
    
    def browse_database_path(self):
        """Browse for database file"""
        file = filedialog.asksaveasfilename(title="Select Database File",
                                           filetypes=[("SQLite DB", "*.db")],
                                           defaultextension=".db")
        if file:
            self.database_path.set(file)
            self.log_output(f"✅ Selected database: {file}", "success")
    
    def browse_word_report_path(self):
        """Browse for Word reports folder"""
        folder = filedialog.askdirectory(title="Select Word Reports Folder")
        if folder:
            self.word_report_path.set(folder)
            self.log_output(f"✅ Selected reports folder: {folder}", "success")
    
    def log_output(self, message, tag="info"):
        """Add message to output log"""
        self.output_text.insert(tk.END, f"{message}\n", tag)
        self.output_text.see(tk.END)
        self.root.update()
    
    def validate_paths(self):
        """Validate all paths are configured"""
        if not self.csv_folder_path.get():
            messagebox.showerror("Error", "Please select CSV/Log folder path")
            return False
        if not os.path.exists(self.csv_folder_path.get()):
            messagebox.showerror("Error", "CSV folder path does not exist")
            return False
        return True
    
    def setup_database(self):
        """Create database if needed"""
        db_path = self.database_path.get()
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS play_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                song_id TEXT NOT NULL,
                artist TEXT,
                title TEXT,
                played_at TIMESTAMP NOT NULL,
                year_month TEXT NOT NULL,
                date_only TEXT NOT NULL
            )
        ''')
        
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_song_month ON play_history(song_id, year_month)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_date ON play_history(date_only)')
        
        conn.commit()
        conn.close()
        self.log_output("✅ Database ready", "success")
    
    def parse_csv_files(self):
        """Parse all CSV/TXT files and populate database"""
        csv_folder = self.csv_folder_path.get()
        db_path = self.database_path.get()
        
        self.log_output("🔍 Scanning for CSV/TXT files...", "info")
        
        try:
            csv_files = [f for f in os.listdir(csv_folder) 
                        if f.lower().endswith(('.csv', '.txt'))]
            
            if not csv_files:
                self.log_output("⚠️ No CSV/TXT files found", "warning")
                return 0
            
            self.log_output(f"📂 Found {len(csv_files)} file(s): {', '.join(csv_files)}", "info")
            
            total_imported = 0
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            for csv_file in csv_files:
                file_path = os.path.join(csv_folder, csv_file)
                self.log_output(f"📝 Processing: {csv_file}", "info")
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        reader = csv.DictReader(f)
                        
                        for row in reader:
                            try:
                                if row.get('Type') != 'ELEM_INFO':
                                    continue
                                if row.get('ElemClass', '').strip() != 'M':
                                    continue
                                
                                event_time_str = row.get('EventTime', '').strip()
                                if not event_time_str:
                                    continue
                                
                                try:
                                    event_time = datetime.strptime(event_time_str, '%Y-%m-%d %H:%M:%S')
                                except:
                                    continue
                                
                                time_only = event_time.strftime('%H:%M')
                                if not (START_TIME <= time_only <= END_TIME):
                                    continue
                                
                                artist = row.get('ElemArtist', '').strip() or "Անհայտ կատարող"
                                title = row.get('ElemName', '').strip() or row.get('ElemShortFile', '').strip() or "Անանուն երգ"
                                song_id = row.get('ElemID', '').strip() or "UNKNOWN"
                                
                                year_month = event_time.strftime("%Y-%m")
                                date_only = event_time.strftime("%Y-%m-%d")
                                
                                # Check if already exists
                                cursor.execute('SELECT COUNT(*) FROM play_history WHERE song_id = ? AND played_at BETWEEN ? AND ?',
                                              (song_id, event_time - timedelta(seconds=5), event_time + timedelta(seconds=5)))
                                if cursor.fetchone()[0] == 0:
                                    cursor.execute('''INSERT INTO play_history (song_id, artist, title, played_at, year_month, date_only)
                                                     VALUES (?, ?, ?, ?, ?, ?)''',
                                                  (song_id, artist, title, event_time, year_month, date_only))
                                    total_imported += 1
                            
                            except Exception:
                                continue
                
                except Exception as e:
                    self.log_output(f"❌ Error reading {csv_file}: {e}", "error")
                    continue
            
            conn.commit()
            conn.close()
            
            self.log_output(f"✅ Imported {total_imported} new records", "success")
            return total_imported
        
        except Exception as e:
            self.log_output(f"❌ Error: {e}", "error")
            return 0
    
    def get_daily_report_data(self, date=None):
        """Get daily statistics"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        db_path = self.database_path.get()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT played_at, artist, title, song_id FROM play_history WHERE date_only = ? ORDER BY played_at', (date,))
        rows = cursor.fetchall()
        conn.close()
        
        return [{'time': r[0], 'artist': r[1], 'title': r[2], 'song_id': r[3]} for r in rows]
    
    def get_monthly_report_data(self, year_month=None):
        """Get monthly statistics"""
        if year_month is None:
            year_month = datetime.now().strftime("%Y-%m")
        
        db_path = self.database_path.get()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''SELECT song_id, artist, title, COUNT(*) as play_count FROM play_history
                         WHERE year_month = ? GROUP BY song_id, artist, title
                         ORDER BY play_count DESC, artist, title''', (year_month,))
        rows = cursor.fetchall()
        conn.close()
        
        return [{'song_id': r[0], 'artist': r[1], 'title': r[2], 'play_count': r[3]} for r in rows]
    
    def get_three_month_report_data(self):
        """Get 3-month statistics"""
        now = datetime.now()
        months = [(now - timedelta(days=30 * i)).strftime("%Y-%m") for i in range(3)]
        
        db_path = self.database_path.get()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute('''SELECT song_id, artist, title, year_month, COUNT(*) as play_count
                         FROM play_history WHERE year_month IN (?, ?, ?)
                         GROUP BY song_id, artist, title, year_month
                         ORDER BY artist, title, year_month''', tuple(months))
        rows = cursor.fetchall()
        conn.close()
        
        songs = {}
        for row in rows:
            key = f"{row[0]}||{row[1]}||{row[2]}"
            if key not in songs:
                songs[key] = {'song_id': row[0], 'artist': row[1], 'title': row[2], 'months': {}}
            songs[key]['months'][row[3]] = row[4]
        
        return list(songs.values()), months
    
    def generate_word_document(self, report_type="full"):
        """Generate Word document using JavaScript"""
        
        if not self.validate_paths():
            return
        
        self.log_output(f"\n📄 Generating {report_type} Word report...", "info")
        
        try:
            self.setup_database()
            records = self.parse_csv_files()
            
            if records == 0 and report_type == "full":
                self.log_output("ℹ️ No new records to add", "warning")
            
            today = datetime.now()
            report_folder = self.word_report_path.get()
            os.makedirs(report_folder, exist_ok=True)
            
            if report_type == "daily":
                daily_data = self.get_daily_report_data()
                monthly_data = self.get_monthly_report_data()
                filename = f"Radio_Report_Daily_{today.strftime('%Y-%m-%d')}.docx"
                
                self.log_output(f"📊 Daily records: {len(daily_data)}", "info")
                
            elif report_type == "monthly":
                daily_data = self.get_daily_report_data()
                monthly_data = self.get_monthly_report_data()
                filename = f"Radio_Report_Monthly_{today.strftime('%Y-%m')}.docx"
                
                self.log_output(f"📊 Monthly records: {len(monthly_data)}", "info")
                
            elif report_type == "three_month":
                daily_data = self.get_daily_report_data()
                monthly_data = self.get_monthly_report_data()
                three_month_data, months = self.get_three_month_report_data()
                filename = f"Radio_Report_3Month_{today.strftime('%Y-%m-%d')}.docx"
                
                self.log_output(f"📊 3-Month records: {len(three_month_data)}", "info")
                
            else:  # full
                daily_data = self.get_daily_report_data()
                monthly_data = self.get_monthly_report_data()
                three_month_data, months = self.get_three_month_report_data()
                filename = f"Radio_Report_Full_{today.strftime('%Y-%m-%d')}.docx"
                
                self.log_output(f"📊 Total records: {len(daily_data) + len(monthly_data)}", "info")
            
            # Generate simple text-based report for now
            report_path = os.path.join(report_folder, filename)
            
            # Create a simple text document (can be converted to .docx manually or with python-docx)
            report_content = self._create_report_content(daily_data, monthly_data, report_type, today)
            
            # For now, save as text file
            text_report_path = report_path.replace('.docx', '.txt')
            with open(text_report_path, 'w', encoding='utf-8') as f:
                f.write(report_content)
            
            self.log_output(f"✅ Report saved: {text_report_path}", "success")
            self.status_label.config(text=f"✅ Report generated: {filename}")
            
            messagebox.showinfo("Success", f"Report generated successfully!\n\n{text_report_path}")
        
        except Exception as e:
            self.log_output(f"❌ Error: {e}", "error")
            messagebox.showerror("Error", f"Failed to generate report: {e}")
    
    def _create_report_content(self, daily, monthly, report_type, today):
        """Create report content"""
        content = []
        content.append("=" * 70)
        content.append(f"ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՇՎԵՏՎՈՒԹՅՈՒՆ - {report_type.upper()}")
        content.append("=" * 70)
        content.append(f"\nԱմսաթիվ: {today.strftime('%d.%m.%Y')}")
        content.append(f"Ժամեր: {START_TIME} - {END_TIME}")
        content.append("\n" + "=" * 70)
        content.append("ՕՐԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ")
        content.append("=" * 70)
        
        if daily:
            content.append(f"\nՀիտ '{len(daily)} երգ նվագարկվել է:")
            for item in daily:
                content.append(f"  • {item['time']} - {item['artist']} - {item['title']}")
        else:
            content.append("\nՀաղորդում: Այսօր երգեր չեն նվագարկվել։")
        
        content.append("\n" + "=" * 70)
        content.append("ԱՄՍԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ")
        content.append("=" * 70)
        
        if monthly:
            content.append(f"\nՀայտնի են {len(monthly)} երգ այս ամսում:")
            for item in sorted(monthly, key=lambda x: x['play_count'], reverse=True):
                star = "⭐" if item['play_count'] > MAX_PLAYS_PER_MONTH else  ""
                content.append(f"  {star} {item['artist']} - {item['title']}: {item['play_count']} անգամ")
        else:
            content.append("\nՀաղորդում: Այս ամսում եղել չեն.")
        
        content.append("\n" + "=" * 70)
        content.append(f"Հաշվետվությունը ստեղծվել է՝ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        content.append("=" * 70)
        
        return "\n".join(content)
    
    def generate_daily_report(self):
        """Generate daily report"""
        self.generate_word_document("daily")
    
    def generate_monthly_report(self):
        """Generate monthly report"""
        self.generate_word_document("monthly")
    
    def generate_three_month_report(self):
        """Generate 3-month report"""
        self.generate_word_document("three_month")
    
    def generate_full_report(self):
        """Generate full report"""
        self.generate_word_document("full")
    
    def toggle_monitoring(self):
        """Start/Stop monitoring"""
        if not self.validate_paths():
            return
        
        if self.is_monitoring:
            self.is_monitoring = False
            self.monitor_button.config(text="▶️ Start Monitoring")
            self.monitor_status.config(text="⏹️ Stopped", foreground="red")
            self.log_output("⏹️ Monitoring stopped", "warning")
        else:
            self.is_monitoring = True
            self.monitor_button.config(text="⏸️ Stop Monitoring")
            self.monitor_status.config(text="🔴 Monitoring...", foreground="green")
            self.log_output("▶️ Monitoring started", "success")
            
            # Start monitoring in background thread
            self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitor_thread.start()
    
    def _monitor_loop(self):
        """Background monitoring loop"""
        import time
        while self.is_monitoring:
            records = self.parse_csv_files()
            if records > 0:
                self.log_output(f"📊 Added {records} new record(s)", "success")
            time.sleep(CHECK_INTERVAL_MINUTES * 60)


def main():
    """Main entry point"""
    root = tk.Tk()
    app = RadioMonitorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
