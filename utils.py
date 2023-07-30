import json

NOTES_FILE = "notes.json"

def read_notes_file():
    try:
        with open(NOTES_FILE, 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

    return notes

def save_notes_file(notes):
    with open(NOTES_FILE, 'w') as file:
        json.dump(notes, file, indent=4)
