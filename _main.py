from database import create_table, add_note, get_notes, get_notes_by_id, delete_note, search_notes, update_notes
from utils import get_text, get_int

def show_notes():
    notes = get_notes()

    if len(notes) == 0:
        add_note("Pizza note", "That pizza from yesterday had too much cheese on it", "15-07-2026")
        notes = get_notes()

    for note in notes:
        print(f"{note[0]} - {note[1]} - {note[2]}")


def view_note_details():
    show_notes()
    try:
        note_id = get_int("Choose note ID: ")
    except ValueError:
        print("ID not found")
        return

    note = get_notes_by_id(note_id)

    if note is None:
        print("Note not found")
    else:
        print(f"ID: {note[0]}")
        print(f"Title: {note[1]}")
        print(f"Content: {note[2]}")
        print(f"Created at: {note[3]}")   

def add_note_by_input():
    title = get_text("Title: ").strip()

    if not title:
        print("Title cannot be empty")
        return
    
    content = get_text("Content: ").strip()

    if not content:
        print("Content cannot be empty")
        return
    
    created_at = get_text("Created at: ")

    if not created_at:
        print("Date cannot be empty")
        return
    
    add_note(title, content, created_at)
    print("Note has been added")


def update_note_by_input():
    show_notes()

    try:
        note_id = get_int("Choose Note ID to update\n> ")
    except ValueError:
        print("Invalid ID")
        return
    
    note = get_notes_by_id(note_id)

    if note is None:
        print("No matching note found")
        return

    new_title = get_text("New title\n> ")
    new_content = get_text("New content\n> ")

    if not new_title or not new_content:
        print("New title and content cannot be empty")
        return

    update_notes(note_id, new_title, new_content)
    print("Note updated!")

def delete_note_by_input():
    show_notes()

    try:
        note_id = get_int("Choose note ID: ")
    except ValueError:
        print("ID not found")
        return
    
    print(f"{note_id} has been successfuly deleted!")
    delete_note(note_id)


def search_notes_by_input():
    search_text = get_text("Search notes by title/content\n> ").strip()

    if not search_text:
        print("Search cannot be empty")
        return
    
    notes = search_notes(search_text)

    if len(notes) == 0:
        print("Note has not been found")
        return
    
    else:
        for note in notes:
            print(f"{note[0]} - {note[1]} - {note[2]}")


def main():
    create_table()

    while True:
        choice = get_text("What would you like to do? (Choose the number corresponding to your choice)"
                    "\n1. View notes"
                    "\n2. View note details"
                    "\n3. Add notes"
                    "\n4. Update notes"
                    "\n5. Delete notes"
                    "\n6. Search notes"
                    "\n7. Exit"
                    "\n> "
                    )
        
        if choice == "1":
            show_notes()

        elif choice == "2":
            view_note_details()

        elif choice == "3":
            add_note_by_input()

        elif choice == "4":
            update_note_by_input()

        elif choice == "5":
            delete_note_by_input()

        elif choice == "6":
            search_notes_by_input()

        elif choice == "7":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
