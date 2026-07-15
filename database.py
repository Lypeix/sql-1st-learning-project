import sqlite3

def connect():
    return sqlite3.connect("notes.db")

def create_table():
    connection = connect() # opens db
    cursor = connection.cursor() # creates object that sends commands to sql

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT NOT NULL
        )
    """) # cursor.execute makes that so the text is read by SQLite which then parses the valid vocabualry 

    connection.commit() # saves changes
    connection.close()

def add_note(title, content, created_at): # adds these 3 values from create_table to notes.db
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
    notes = cursor.fetchall # grabs selected rows and returns them as python objects

    connection.close

    return notes

def get_notes_by_id(note_id):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, content, created_at
        FROM notes
        WHERE id = ?
    """, (note_id,))

    note = cursor.fetchone()

    connection.close()

    return note
