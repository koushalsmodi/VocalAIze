# Speech to Text Conversion Tool

This Python script utilizes the OpenAI API to convert speech from an audio file into text.

## Requirements

- Python 3.6 or higher
- `openai` Python package
- An API key from OpenAI

## Setup

1. **Install the required package**:

2. **API Key**:
   - Obtain an API key from OpenAI.
   - Set the API key in your environment variables.
     
## Usage

To use the script, simply run it with Python. Ensure you have an audio file named `speech.mp3` in the same directory as the script, or modify the path in the script to point to your audio file.

The script will print the transcription of the audio file to the console.

## How It Works

- The script initializes a `SpeechToText` object with your OpenAI API key.
- It reads an audio file and sends it to OpenAI's speech-to-text service.
- The transcription is received and printed out.

## Notes

- Currently, the script is set to use the `medium.en` model for transcription. This can be changed in the `speech_to_text` method in `stt.py`.
- The script expects the audio file to be in MP3 format. Ensure your file is compatible or modify the script accordingly.
