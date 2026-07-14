from database import get_notes_by_id

note_id = int(input("Choose note ID: "))
note = get_notes_by_id(note_id)

if note is None:
    print("Note not found")
else:
    print(f"ID: {note[0]}")
    print(f"Title: {note[1]}")
    print(f"Content: {note[2]}")
    print(f"Created at: {note[3]}")   
