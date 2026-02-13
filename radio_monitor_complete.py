"""
================================================================================
ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՄԱԿԱՐԳ - Digispot II
================================================================================

ՆԿԱՐԱԳՐՈՒԹՅՈՒՆ:
Այս ծրագիրը մոնիտորինգ է անում Digispot II ռադիոյի նվագարկումները և ստեղծում է
ամենօրյա Word հաշվետվություններ։ Աշխատում է և՛ .csv և՛ .txt ֆայլերի հետ։

ՏԵՂԱԴՐՈՒՄ:
1. Տեղադրիր Python (https://www.python.org/downloads/)
2. Տեղադրիր Node.js (https://nodejs.org/)
3. Գործարկիր: pip install schedule && npm install -g docx

ԿԱՐԳԱՎՈՐՈՒՄ:
Փոխիր ստորև նշվածները՝ CSV_FOLDER_PATH, DATABASE_PATH, WORD_REPORT_PATH

ԳՈՐԾԱՐԿՈՒՄ:
python radio_monitor_complete.py
================================================================================
"""

import os
import csv
import sqlite3
from datetime import datetime, timedelta
import schedule
import time
import subprocess
import json

# ════════════════════════════════════════════════════════════════════════════
# ԿԱՐԳԱՎՈՐՈՒՄՆԵՐ
# ════════════════════════════════════════════════════════════════════════════

CSV_FOLDER_PATH = r"C:\Path\To\Digispot\Logs"
DATABASE_PATH = r"C:\RadioStats\radio_stats.db"
WORD_REPORT_PATH = r"C:\RadioStats\Reports"
LOG_FILE_PATH = r"C:\RadioStats\warnings.log"

START_TIME = "07:50"
END_TIME = "10:10"
MAX_PLAYS_PER_MONTH = 4
WORD_REPORT_TIME = "10:11"
CHECK_INTERVAL_MINUTES = 1

SHOW_CONSOLE_WARNING = True
SAVE_TO_LOG_FILE = True

# ════════════════════════════════════════════════════════════════════════════
# ԾՐԱԳՐԻ ԿՈԴ
# ════════════════════════════════════════════════════════════════════════════

class RadioMonitor:
    """Ռադիո մոնիտորինգի հիմնական դաս"""
    
    def __init__(self):
        self.setup_database()
        self.last_processed_time = None
        print("✅ RadioMonitor ինիցիալիզացված է")
        
    def setup_database(self):
        """Ստեղծում է SQLite database"""
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
        conn = sqlite3.connect(DATABASE_PATH)
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
        
    def get_latest_csv_file(self):
        """Գտնում է ամենավերջին CSV/TXT ֆայլը"""
        try:
            csv_files = [f for f in os.listdir(CSV_FOLDER_PATH) 
                        if f.lower().endswith(('.csv', '.txt'))]
            if not csv_files:
                return None
            latest_file = max(csv_files, key=lambda f: os.path.getmtime(os.path.join(CSV_FOLDER_PATH, f)))
            return os.path.join(CSV_FOLDER_PATH, latest_file)
        except Exception as e:
            print(f"❌ Սխալ ֆայլը գտնելիս: {e}")
            return None
    
    def parse_csv_file(self, csv_file_path):
        """Կարդում է CSV ֆայլը"""
        new_tracks = []
        try:
            with open(csv_file_path, 'r', encoding='utf-8', errors='ignore') as f:
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
                        
                        if self.last_processed_time and event_time <= self.last_processed_time:
                            continue
                        
                        time_only = event_time.strftime('%H:%M')
                        if not (START_TIME <= time_only <= END_TIME):
                            continue
                        
                        artist = row.get('ElemArtist', '').strip() or "Անհայտ կատարող"
                        title = row.get('ElemName', '').strip() or row.get('ElemShortFile', '').strip() or "Անանուն երգ"
                        song_id = row.get('ElemID', '').strip() or "UNKNOWN"
                        
                        new_tracks.append({
                            'time': event_time,
                            'artist': artist,
                            'title': title,
                            'song_id': song_id
                        })
                    except Exception:
                        continue
        except Exception as e:
            print(f"❌ Սխալ CSV ֆայլը կարդալիս: {e}")
        return new_tracks
    
    def is_already_logged(self, song_id, played_at):
        """Ստուգում է արդյոք երգը արդեն գրանցված է"""
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        time_min = played_at - timedelta(seconds=5)
        time_max = played_at + timedelta(seconds=5)
        cursor.execute('SELECT COUNT(*) FROM play_history WHERE song_id = ? AND played_at BETWEEN ? AND ?',
                      (song_id, time_min, time_max))
        count = cursor.fetchone()[0]
        conn.close()
        return count > 0
    
    def get_monthly_play_count(self, song_id):
        """Հաշվում է այս ամսի նվագարկումները"""
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        current_month = datetime.now().strftime("%Y-%m")
        cursor.execute('SELECT COUNT(*) FROM play_history WHERE song_id = ? AND year_month = ?',
                      (song_id, current_month))
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    def log_play(self, song_data):
        """Գրանցում է երգի նվագարկումը"""
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        played_at = song_data['time']
        year_month = played_at.strftime("%Y-%m")
        date_only = played_at.strftime("%Y-%m-%d")
        cursor.execute('''INSERT INTO play_history (song_id, artist, title, played_at, year_month, date_only)
                         VALUES (?, ?, ?, ?, ?, ?)''',
                      (song_data['song_id'], song_data['artist'], song_data['title'], 
                       played_at, year_month, date_only))
        conn.commit()
        conn.close()
        
    def send_warning(self, song_data, play_count):
        """Ուղարկում է զգուշացում"""
        message = f"\n⚠️ ԶԳՈՒՇԱՑՈՒՄ!\nԵրգ: {song_data['artist']} - {song_data['title']}\nID: {song_data['song_id']}\nԱրդեն նվագարկվել է {play_count} անգամ այս ամիս!\nՀամ: {song_data['time'].strftime('%H:%M:%S')}\n"
        if SHOW_CONSOLE_WARNING:
            print(message)
        if SAVE_TO_LOG_FILE:
            os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
            with open(LOG_FILE_PATH, 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now()} - {message}\n")
    
    def process_new_tracks(self, tracks):
        """Մշակում է նոր երգերը"""
        for track in tracks:
            if self.is_already_logged(track['song_id'], track['time']):
                continue
            current_count = self.get_monthly_play_count(track['song_id'])
            print(f"🎵 {track['time'].strftime('%H:%M:%S')} - {track['artist']} - {track['title']}")
            print(f"   📊 Այս ամիս: {current_count} անգամ")
            if current_count >= MAX_PLAYS_PER_MONTH:
                self.send_warning(track, current_count)
            self.log_play(track)
            print(f"   ✅ Գրանցված է\n")
            if self.last_processed_time is None or track['time'] > self.last_processed_time:
                self.last_processed_time = track['time']
    
    def check_for_new_plays(self):
        """Ստուգում է նոր նվագարկումներ"""
        csv_file = self.get_latest_csv_file()
        if not csv_file:
            print("⚠️  CSV ֆայլ չի գտնվել")
            return
        new_tracks = self.parse_csv_file(csv_file)
        if new_tracks:
            print(f"\n📝 Գտնվել է {len(new_tracks)} նոր երգ")
            self.process_new_tracks(new_tracks)
    
    def get_daily_report_data(self, date=None):
        """Վերադարձնում է օրվա վիճակագրությունը"""
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT played_at, artist, title, song_id FROM play_history WHERE date_only = ? ORDER BY played_at', (date,))
        rows = cursor.fetchall()
        conn.close()
        return [{'time': r[0], 'artist': r[1], 'title': r[2], 'song_id': r[3]} for r in rows]
    
    def get_monthly_report_data(self, year_month=None):
        """Վերադարձնում է ամսական վիճակագրությունը"""
        if year_month is None:
            year_month = datetime.now().strftime("%Y-%m")
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute('''SELECT song_id, artist, title, COUNT(*) as play_count FROM play_history
                         WHERE year_month = ? GROUP BY song_id, artist, title
                         ORDER BY play_count DESC, artist, title''', (year_month,))
        rows = cursor.fetchall()
        conn.close()
        return [{'song_id': r[0], 'artist': r[1], 'title': r[2], 'play_count': r[3]} for r in rows]
    
    def get_three_month_report_data(self):
        """Վերադարձնում է 3 ամսվա վիճակագրությունը"""
        now = datetime.now()
        months = [(now - timedelta(days=30 * i)).strftime("%Y-%m") for i in range(3)]
        conn = sqlite3.connect(DATABASE_PATH)
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
    
    def generate_word_report(self):
        """Ստեղծում է Word հաշվետվություն"""
        print("\n📄 Սկսում եմ ստեղծել Word հաշվետվությունը...")
        today = datetime.now()
        report_filename = f"Radio_Report_{today.strftime('%Y-%m-%d')}.docx"
        os.makedirs(WORD_REPORT_PATH, exist_ok=True)
        
        daily_data = self.get_daily_report_data()
        monthly_data = self.get_monthly_report_data()
        three_month_data, months = self.get_three_month_report_data()
        
        js_code = self._generate_docx_js(daily_data, monthly_data, three_month_data, months, today, report_filename)
        js_file = os.path.join(WORD_REPORT_PATH, 'temp_gen.js')
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write(js_code)
        
        try:
            result = subprocess.run(['node', js_file], cwd=WORD_REPORT_PATH, 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print(f"✅ Word հաշվետվությունը ստեղծվել է: {os.path.join(WORD_REPORT_PATH, report_filename)}")
                os.remove(js_file)
            else:
                print(f"❌ Սխալ: {result.stderr}")
        except FileNotFoundError:
            print("❌ Node.js-ը չի գտնվել")
        except Exception as e:
            print(f"❌ Սխալ: {e}")
    
    def _generate_docx_js(self, daily, monthly, three_month, months, today, filename):
        """Generate simplified Word report with basic formatting"""
        daily_json = json.dumps(daily, ensure_ascii=False)
        monthly_json = json.dumps(monthly, ensure_ascii=False)
        
        js = 'const {Document, Packer, Paragraph, TextRun} = require("docx");\n'
        js += 'const fs = require("fs");\n'
        js += 'const daily = ' + daily_json + ';\n'
        js += 'const monthly = ' + monthly_json + ';\n'
        js += 'const sections = [new Paragraph({text:"ՕՐԱԿԱՆ ՀԱՇՎԵՏՎՈՒԹՅՈՒՆ"}),\n'
        js += f'new Paragraph({{text:"Ամսաթիվ՝ {today.strftime(r"%d.%m.%Y")}"}}),\n'
        js += f'new Paragraph({{text:"Ժամեր՝ {START_TIME} - {END_TIME}"}}),\n'
        js += 'new Paragraph({text:""}),\n'
        js += '...daily.map(i => new Paragraph({text: i.time + " - " + i.artist + " - " + i.title})),\n'
        js += 'new Paragraph({text:""}), new Paragraph({text:""}),\n'
        js += 'new Paragraph({text:"ԱՄՍԱԿԱՆ ՎԻՃԱԿԱԳՐՈՒԹՅՈՒՆ"}),\n'
        js += 'new Paragraph({text:""}),\n'
        js += '...monthly.map(i => new Paragraph({text: i.artist + " - " + i.title + " (" + i.play_count + ")"}))\n'
        js += '];\n'
        js += 'const doc = new Document({sections:[{children:sections}]});\n'
        js += f'Packer.toBuffer(doc).then(b => fs.writeFileSync("{filename}", b))\n'
        js += '.catch(e => console.error("Error:", e));\n'
        
        return js


def main():
    """Հիմնական ֆունկցիա"""
    print("=" * 70)
    print("🎙️  ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ ՀԱՄԱԿԱՐԳ - Digispot II")
    print("=" * 70)
    print(f"📁 Ֆայլերի պանակ: {CSV_FOLDER_PATH}")
    print(f"💾 Database: {DATABASE_PATH}")
    print(f"📄 Word հաշվետվություններ: {WORD_REPORT_PATH}")
    print(f"⏰ Մոնիտորինգի ժամեր: {START_TIME} - {END_TIME}")
    print(f"📊 Մաքսիմում նվագարկումներ ամսվա ընթացքում: {MAX_PLAYS_PER_MONTH}")
    print(f"📄 Word հաշվետվություն՝ ամեն օր ժամը {WORD_REPORT_TIME}")
    print(f"🔄 Ստուգում՝ ամեն {CHECK_INTERVAL_MINUTES} րոպեն մեկ")
    print("=" * 70)
    
    if not os.path.exists(CSV_FOLDER_PATH):
        print(f"\n❌ ՍԽԱԼ: Ֆայլերի պանակը չի գտնվել!")
        print(f"   Ուղի: {CSV_FOLDER_PATH}")
        return
    
    monitor = RadioMonitor()
    schedule.every(CHECK_INTERVAL_MINUTES).minutes.do(monitor.check_for_new_plays)
    schedule.every().day.at(WORD_REPORT_TIME).do(monitor.generate_word_report)
    
    print("\n✅ Մոնիտորինգը սկսված է!")
    print(f"🔄 Ստուգում եմ CSV/TXT ֆայլերը ամեն {CHECK_INTERVAL_MINUTES} րոպեն մեկ...")
    print("📄 Word հաշվետվությունը կստեղծվի ամեն օր ժամը", WORD_REPORT_TIME)
    print("⌨️  Սեղմիր Ctrl+C դադարեցնելու համար\n")
    
    monitor.check_for_new_plays()
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n⏹️  Մոնիտորինգը դադարեցված է")
        print("👋 Ցտեսություն!")


if __name__ == "__main__":
    main()
