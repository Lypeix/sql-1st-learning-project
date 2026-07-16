# !DEVLOG!

## DAY 1 OF PROGRESS (13.07.2026):
### Session 1 (~45mins):
- Created multi-file structure
- Added create_table()
- Added add_note()
- Added get_notes()
- Studied theory regarding how does connection, parsing and cursor work

## DAY 2 OF PROGRESS (14.07.2026):
### Session 1 (~45mins):
- Added get_notes_by_id() to database.py
- Added usage to main.py
- Reconstructed connect(), create_table(), add_note() and get_notes() from memory after understanding how they work

## DAY 3 OF PROGRESS (15.07.2026):
### Session 1 (~60mins):
- Added delete_note() to database.py
- Added menu functions for main.py: show_notes(), view_note_details(), delete_note_by_input() and main()
- Added missing () to functions
- Fixed naming collision in delete_note() menu
- Added search_notes() to database.py
- Added search_notes input option to main.py

### Session 2 (~45mins):
- Added add_note() to main.py
- Added more space between functions for superior readability
- Added update_notes() to database.py
- Added update_notes_by_input() to main.py

## DAY 4 - PROJECT CONCLUDED (16.07.2026):
### Session 1 (~50mins): 
- Remade update_notes(), delete_notes(), search_notes() from memory
- Fixed the ordering of parameters in update_notes()
- Studied SQL elements in the code 
- Experimented by trying different ways to code, eg.
      def delete_note(note_id):
        connection = connect()
        cursor = connection.cursor()
    
        cursor.execute(f"""
        DELETE FROM notes
        WHERE id = {note_id}
        """) 
    
        connection.commit()
        connection.close()
  instead of placing note_id as tuple at the end of multi-line string
  result: everything seems to be working, however I've read that it inserts values directly into the SQL query string, which risks SQL injection that changes the query (sql command in the multi-line string) that might have  problematic side-effects depending on input like 5 OR 1=1
- Added comments explaining a few lines with my own wording

### Session 2 (~70mins):
- Added get_text() and get_int() helpers to utils.py
- Replaced input() and int(input()) in main.py with corresponding functions
- Added get_timestamp() to utils.py
- Replaced manual date input in add_note_by_input() with automatic timestamp generation
- Added dynamic UX note listing using display numbers instead of note IDs
- Added choose_note_id into main.py
- Updated the design of: view_note_details(), update_note_by_input() and delete_note_by_input to effectively feature choose_note_id
- Updated show_notes() so that it no longer creates a placeholder note whenever database is empty
- Fixed bugs caused by separating display numbers from raw IDs

Final note: Reconstruction of functions from Day 4 will be done on 17th of July, however the project is already finished
