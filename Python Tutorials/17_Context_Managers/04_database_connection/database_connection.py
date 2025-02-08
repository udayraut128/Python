import sqlite3
from contextlib import contextmanager

@contextmanager
def open_database(db_name):
    conn = sqlite3.connect(db_name)
    try:
        yield conn
    finally:
        conn.close()

with open_database('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO users (name) VALUES (?)', ('Alice',))
    conn.commit()


