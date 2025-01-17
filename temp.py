import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget
from vosk import Model, KaldiRecognizer
import pyaudio


class NoteTakingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Taking App")
        self.setGeometry(500, 300, 1920, 1080)
        self.init_ui()

    def init_ui(self):
        # Main layout
        layout = QVBoxLayout()

        # Text editor
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # Voice-to-text button
        self.voice_button = QPushButton("Start Voice Input", self)
        self.voice_button.clicked.connect(self.start_voice_input)
        layout.addWidget(self.voice_button)

        # Central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_voice_input(self):
        self.voice_button.setText("Listening...")
        self.voice_button.setEnabled(False)
        

        # Load Vosk model
        model = Model(r"D:\vosk-model-small-hi-0.22\vosk-model-small-hi-0.22")  # Assumes you downloaded a Vosk model into the "model" folder
        recognizer = KaldiRecognizer(model, 16000)
        audio = pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()

        try:
            while True:
                data = stream.read(4096)
                if recognizer.AcceptWaveform(data):
                    result = recognizer.Result()
                    self.text_edit.append(eval(result)["text"])
                    break  # Exit after capturing one phrase
        except Exception as e:
            print(f"Error: {e}")
        finally:
            stream.stop_stream()
            stream.close()
            audio.terminate()
            self.voice_button.setText("Start Voice Input")
            self.voice_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = NoteTakingApp()
    main_window.show()
    sys.exit(app.exec_())
