import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget, QPushButton, QFileDialog
from features.voice_input import VoiceInput
from ui.toolbar import Toolbar
from features.file_handle import save_note, load_note  # Import the functions from file_handle.py


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Taking App")
        self.setGeometry(500, 300, 1920, 1080)

        # Initialize voice input with the Vosk model path
        self.voice_input = VoiceInput(r"D:\vosk-model-en-in-0.5\vosk-model-en-in-0.5")  # Update the model path as needed
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Text editor
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # Toolbar for text formatting features
        self.toolbar = Toolbar(self.text_edit, self)
        self.addToolBar(self.toolbar)

        # Voice input button
        self.voice_button = QPushButton("Start Voice Input")
        self.voice_button.clicked.connect(self.start_voice_input)
        layout.addWidget(self.voice_button)

        # Save button
        self.save_button = QPushButton("Save Note")
        self.save_button.clicked.connect(self.save_note)
        layout.addWidget(self.save_button)

        # Load button
        self.load_button = QPushButton("Load Note")
        self.load_button.clicked.connect(self.load_note)
        layout.addWidget(self.load_button)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_voice_input(self):
        """Handles voice-to-text input and appends the text to the editor."""
        self.voice_button.setText("Listening...")
        self.voice_button.setEnabled(False)

        try:
            recognized_text = self.voice_input.listen_and_recognize()
            if recognized_text:
                self.text_edit.append(recognized_text)
        except Exception as e:
            print(f"Error during voice input: {e}")
        finally:
            self.voice_button.setText("Start Voice Input")
            self.voice_button.setEnabled(True)

    def save_note(self):
        """Opens a file dialog to save the note."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Note", "", "Text Files (*.txt)")
        if file_path:
            content = self.text_edit.toPlainText()
            save_note(file_path, content)  # Save the note using the save_note function from file_handle.py

    def load_note(self):
        """Opens a file dialog to load a note."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Note", "", "Text Files (*.txt)")
        if file_path:
            content = load_note(file_path)  # Load the note using the load_note function from file_handle.py
            self.text_edit.setText(content)

    def closeEvent(self, event):
        """Ensure voice input resources are released when the window is closed."""
        self.voice_input.close()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
