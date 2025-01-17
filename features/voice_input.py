import pyaudio
from vosk import Model, KaldiRecognizer

class VoiceInput:
    def __init__(self, model_path):
        # Load the Vosk model
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.audio = pyaudio.PyAudio()
        self.stream = None

    def listen_and_recognize(self):
        """Captures audio from the microphone and returns recognized text."""
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8192
        )
        self.stream.start_stream()

        print("Listening for voice input...")
        recognized_text = ""

        try:
            while True:
                data = self.stream.read(4096)
                if self.recognizer.AcceptWaveform(data):
                    result = self.recognizer.Result()
                    recognized_text = eval(result)["text"]
                    break  # Exit after capturing one phrase
        except Exception as e:
            print(f"Voice input error: {e}")
        finally:
            self.stop()
        return recognized_text

    def stop(self):
        """Stops the audio stream."""
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()

    def close(self):
        """Releases all resources."""
        self.audio.terminate()
