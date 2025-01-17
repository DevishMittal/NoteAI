import os

def save_note(file_path, content):
    """Save the current note content to a file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Note saved to {file_path}")
    except Exception as e:
        print(f"Error saving note: {e}")

def load_note(file_path):
    """Load the content of a saved note from a file."""
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            print(f"Note loaded from {file_path}")
            return content
        except Exception as e:
            print(f"Error loading note: {e}")
            return ""
    else:
        print(f"No note found at {file_path}")
        return ""
