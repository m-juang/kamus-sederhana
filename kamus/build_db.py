"""
Membangun kamus.db dari schema.sql + seed.sql.
Cukup pakai modul bawaan Python (sqlite3), tidak perlu install apa pun.

Cara pakai:
    python3 build_db.py
"""
import sqlite3
import os

# ini komentar
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "kamus.db")

def run():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    with open(os.path.join(BASE_DIR, "schema.sql"), encoding="utf-8") as f:
        conn.executescript(f.read())
    with open(os.path.join(BASE_DIR, "seed.sql"), encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM words").fetchone()[0]
    print(f"kamus.db berhasil dibuat di: {DB_PATH}")
    print(f"Total kata tersimpan: {total}")
    conn.close()

if __name__ == "__main__":
    run()
