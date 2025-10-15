import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "database", "data_source.db")

def ensure_db_dir():
    d = os.path.dirname(DB_PATH)
    if not os.path.exists(d):
        os.makedirs(d)

def get_conn():
    ensure_db_dir()
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        email TEXT UNIQUE,
        password_hash TEXT,
        chosen_bg TEXT,
        chosen_alarm TEXT,
        chosen_bgm TEXT
    )''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS settings_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        chosen_bg TEXT,
        chosen_alarm TEXT,
        chosen_bgm TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''
    CREATE TABLE IF NOT EXISTS timers_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        mode TEXT,
        duration INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def find_user_by_email(email):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email.lower().strip(),))
    row = cur.fetchone()
    conn.close()
    return row

def create_user(first_name, email, password_hash, chosen_bg="#edf2f4", chosen_alarm="alarm_duck.mp3", chosen_bgm="bg_cafe.mp3"):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (first_name, email, password_hash, chosen_bg, chosen_alarm, chosen_bgm) VALUES (?, ?, ?, ?, ?, ?)",
                (first_name, email.lower().strip(), password_hash, chosen_bg, chosen_alarm, chosen_bgm))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id

def update_user_settings(user_id, chosen_bg=None, chosen_alarm=None, chosen_bgm=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT chosen_bg, chosen_alarm, chosen_bgm FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    if not row:
        conn.close()
        return False
    nb = chosen_bg if chosen_bg is not None else row["chosen_bg"]
    na = chosen_alarm if chosen_alarm is not None else row["chosen_alarm"]
    nbm = chosen_bgm if chosen_bgm is not None else row["chosen_bgm"]
    cur.execute("UPDATE users SET chosen_bg = ?, chosen_alarm = ?, chosen_bgm = ? WHERE id = ?", (nb, na, nbm, user_id))
    cur.execute("INSERT INTO settings_history (user_id, chosen_bg, chosen_alarm, chosen_bgm) VALUES (?, ?, ?, ?)", (user_id, nb, na, nbm))
    conn.commit()
    conn.close()
    return True

def record_timer(user_id, mode, duration):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO timers_history (user_id, mode, duration) VALUES (?, ?, ?)", (user_id, mode, duration))
    conn.commit()
    conn.close()
