from database import create_table, add_note, get_notes, get_notes_by_id

create_table()

notes = get_notes()

if len(notes) == 0:
    add_note("Pizza note", "That pizza from yesterday had too much cheese on it", "15-07-2026")
    notes = get_notes()

for note in notes:
    print(f"{note[0]} - {note[1]} - {note[2]}")

note_id = int(input("Choose note ID: "))
note = get_notes_by_id(note_id)

if note is None:
    print("Note not found")
else:
    print(f"ID: {note[0]}")
    print(f"Title: {note[1]}")
    print(f"Content: {note[2]}")
    print(f"Created at: {note[3]}")   
