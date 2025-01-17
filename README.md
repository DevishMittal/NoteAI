# NoteAI

A feature-rich note-taking application built with PyQt5 that supports voice input, text formatting, and file management capabilities.

## Features

- Voice-to-text input using Vosk speech recognition
- Rich text formatting (font, color, alignment)
- Bullet points and numbered lists
- File save and load functionality
- User-friendly toolbar interface

- **Future Enhancements**:
  - AI-assisted autocomplete for faster note-taking.
  - Voice-to-text functionality using a local LLM.
  - Pen-paper style mode for a more realistic writing experience.

## Prerequisites

- Python 3.8 or higher
- PyQt5
- Vosk
- PyAudio

## Installation

1. Clone the repository:
```bash
git clone https://github.com/DevishMittal/NoteAI.git
cd NoteAI
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download the Vosk model:
- Visit [Vosk Models](https://alphacephei.com/vosk/models)
- Download the Indian English model (vosk-model-small-en-in-0.4) or any any other model according to the requirements.
- Extract the model to the `models` directory in your project folder

## Configuration

1. Update the Vosk model path in `main_window.py`:
```python
self.voice_input = VoiceInput(r"absolute path of your downloaded model")
```

## Running the Application

1. Ensure your virtual environment is activated
2. Run the application:
```bash
python main.py
```

## Usage

1. **Text Input**: Type directly into the text editor
2. **Voice Input**: 
   - Click "Start Voice Input"
   - Speak clearly into your microphone
   - The recognized text will appear in the editor

3. **Text Formatting**:
   - Use the toolbar to change font, color, and alignment
   - Add bullet points or numbered lists
   - Format selected text as needed

4. **File Operations**:
   - Click "Save Note" to save your current note
   - Click "Load Note" to open an existing note

## Requirements

Create a `requirements.txt` file with the following dependencies:
```
PyQt5
vosk
pyaudio
```

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## Acknowledgments

- Vosk Speech Recognition
- PyQt5 Framework