import json
from datetime import datetime
from utils import read_notes_file, save_notes_file

def add_note(title, msg):
    notes = read_notes_file()

    note = {
        'id': len(notes) + 1,
        'title': title,
        'msg': msg,
        'timestamp': datetime.now().isoformat()
    }

    notes.append(note)
    save_notes_file(notes)

    print('Заметка успешно сохранена.')

def read_notes(date_filter=None):
    notes = read_notes_file()

    if date_filter:
        filtered_notes = [note for note in notes if note['timestamp'].startswith(date_filter)]
        return filtered_notes
    else:
        return notes

def edit_note(note_id, new_title, new_msg):
    notes = read_notes_file()

    for note in notes:
        if note['id'] == note_id:
            note['title'] = new_title
            note['msg'] = new_msg
            note['timestamp'] = datetime.now().isoformat()
            break

    save_notes_file(notes)

    print('Заметка успешно отредактирована.')

def delete_note(note_id):
    notes = read_notes_file()

    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            break

    save_notes_file(notes)

    print('Заметка успешно удалена.')
