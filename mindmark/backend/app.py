from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Path to the JSON file where notes will be stored
notes_file = 'notes.json'

# Load existing notes from the JSON file
def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, 'r') as f:
            return json.load(f)
    return []

# Save notes to the JSON file
def save_notes(notes):
    with open(notes_file, 'w') as f:
        json.dump(notes, f)

# Get all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = load_notes()
    return jsonify(notes)

# Create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    new_note = request.json
    notes = load_notes()
    notes.append(new_note)
    save_notes(notes)
    return jsonify(new_note), 201

# Update an existing note
@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    notes = load_notes()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note is None:
        return jsonify({'error': 'Note not found'}), 404

    updated_note = request.json
    note.update(updated_note)
    save_notes(notes)
    return jsonify(note)

# Delete a note
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    return jsonify({'message': 'Note deleted'})

if __name__ == '__main__':
    app.run(debug=True)