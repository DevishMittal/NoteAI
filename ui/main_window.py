from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTextEdit, QWidget, QPushButton
from features.voice_input import VoiceInput
from ui.toolbar import Toolbar


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

    def closeEvent(self, event):
        """Ensure voice input resources are released when the window is closed."""
        self.voice_input.close()
        super().closeEvent(event)
