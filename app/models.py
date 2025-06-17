import sqlite3
import os

def get_db():
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'instance', 'pc_assets.sqlite3')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    db = get_db()
    db.execute('''
    CREATE TABLE IF NOT EXISTS pc_assets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hostname TEXT UNIQUE,
        os TEXT,
        cpu TEXT,
        memory INTEGER,
        serial TEXT,
        mac TEXT,
        last_report TEXT
    )
    ''')
    db.commit()