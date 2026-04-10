import sqlite3

def connect():
    return sqlite3.connect("database.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY,
            title TEXT,
            body TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_post(post):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO posts (id, title, body)
        VALUES (?, ?, ?)
    """, (post["id"], post["title"], post["body"]))

    conn.commit()
    conn.close()

def list_posts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM posts")
    rows= cursor.fetchall()

    conn.close()
    return rows

def clear_posts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM posts")

    conn.commit()
    conn.close()