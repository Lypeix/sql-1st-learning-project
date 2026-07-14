import sqlite3

def connect():
    return sqlite3.connect("notes.db")

def create_table():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,                  
                   content TEXT NOT NULL,
                   created_at TEXT NOT NULL
        )
    """
    )

    connection.commit()
    connection.close()

def add_note(title, content, created_at):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notes (title, content, created_at)
        VALUES (?, ?, ?)
    """, (title, content, created_at))

    connection.commit()
    connection.close()

def get_notes():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT id, title, created_at FROM notes")
    notes = cursor.fetchall()

    connection.close()

    return notes
