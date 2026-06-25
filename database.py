import sqlite3

def init_db():
    conn = sqlite3.connect("naval.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS routes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start TEXT,
        end TEXT,
        distance REAL
    )
    """)

    conn.commit()
    conn.close()

def save_route(start, end, distance):
    conn = sqlite3.connect("naval.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO routes VALUES (NULL, ?, ?, ?)",
                (start, end, distance))

    conn.commit()
    conn.close()