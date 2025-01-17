import tkinter as tk
from tkinter import simpledialog, messagebox


class WinNotes:
    def __init__(self):
        self.notes = []

        # Create main application window
        self.root = tk.Tk()
        self.root.title("WinNotes")
        self.root.geometry("300x400")

        # Add a button to create a new note
        self.new_note_button = tk.Button(self.root, text="New Note", command=self.create_note)
        self.new_note_button.pack(pady=10)

        # Add a frame to display notes
        self.notes_frame = tk.Frame(self.root)
        self.notes_frame.pack(fill=tk.BOTH, expand=True)

        self.display_notes()

        self.root.mainloop()

    def create_note(self):
        # Prompt user for note content
        note_content = simpledialog.askstring("New Note", "Enter your note:")

        if note_content:
            self.notes.append(note_content)
            self.display_notes()

    def display_notes(self):
        # Clear the notes frame
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        # Display each note as a label
        for idx, note in enumerate(self.notes):
            note_label = tk.Label(self.notes_frame, text=note, bg="yellow", wraplength=250, anchor="w", justify="left")
            note_label.pack(fill=tk.X, padx=5, pady=5)

            # Add a delete button for each note
            delete_button = tk.Button(self.notes_frame, text="Delete", command=lambda idx=idx: self.delete_note(idx))
            delete_button.pack(pady=5)

    def delete_note(self, idx):
        # Remove the note from the list
        if 0 <= idx < len(self.notes):
            del self.notes[idx]
            self.display_notes()


if __name__ == "__main__":
    WinNotes()