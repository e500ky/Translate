# Language Translator Application

This is a simple language translator application built using `customtkinter`, `tkinter`, `googletrans`, and `gTTS` libraries. It allows users to input text, select a language, and translate the text into the selected language. The application also supports voice output for the translated text.

## Features

- **Text Translation**: Allows users to input text and translate it into various languages.
- **Voice Output**: Plays the translated text as speech using `gTTS` and `pygame`.
- **Language Selection**: Users can choose from a variety of languages, including English, German, Spanish, French, Italian, Turkish, Korean, Japanese, Swedish, Greek, and Irish.
- **Clear Input**: Resets the input fields and selects the default language (English).
- **Hotkey Support**: Press `F2` to activate the speech functionality.

## Requirements

To run this application, you will need the following libraries:

- `customtkinter`
- `tkinter`
- `googletrans`
- `gTTS`
- `pygame`

You can install the required libraries by running:

```bash
pip install customtkinter googletrans gTTS pygame
```

## How to Use
Text Input: Type any text you want to translate into the text input field.
Select Language: Use the dropdown menu to select your desired language.
Translate: Click the "Translate" button or press Enter to translate the text.
Voice Output: Click the speaker icon or press F2 to listen to the translated text.
Clear: Press the "Reset" button to clear the input and output fields.
How to Run the Application
Ensure that all dependencies are installed.
Save the Python script to a file, for example, main.py.
Run the script using Python:
```bash
python main.py
```
The application window should appear, and you can begin using the translator.

File Structure
```bash
- main.py     # Python code for the application
- icon.ico    # Application icon (optional)
```
License
This project is licensed under the MIT License - see the LICENSE file for details.
