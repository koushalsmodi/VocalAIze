# Speech to Text Conversion Tool

This Python script leverages the OpenAI API to convert spoken language from an audio file into written text. It's designed to be easy to use and integrate into any project that requires speech transcription.

## Requirements

To run this script, you will need:

- Python 3.6 or higher
- `openai` Python package
- An API key from OpenAI: You will need to obtain a key to authenticate your requests.

## Setup

Follow these steps to set up the script:

1. **Install the required package**:
   Run the following command to install the OpenAI Python package:

## Setup

1. **Install the required package**:

2. **API Key**:
   - Obtain an API key
   - Set the API key in your environment variables for secure access
     
## Usage

To use the script, simply run it with Python. Ensure you have an audio file named `speech.mp3` in the same directory as the script, or modify the path in the script to point to your audio file.

- The script will automatically transcribe the audio and print the transcription to the console.

## How It Works

The script operates by performing the following steps:

- Initializes a `SpeechToText` object using your OpenAI API key.
- Reads the specified audio file (`speech.mp3` by default).
- Sends the audio data to OpenAI's speech-to-text service.
- Receives the transcription and outputs it to the console.

## Notes

- The default model used for transcription is `medium.en`. You can change this setting in the `speech_to_text` method within the `stt.py` file to any other model supported by OpenAI.
- The script currently supports MP3 audio format. If your audio file is in a different format, you will need to convert it to MP3 or modify the script to handle other formats.

## Notes

- Currently, the script is set to use the `medium.en` model for transcription. This can be changed in the `speech_to_text` method in `stt.py`.
- The script expects the audio file to be in MP3 format. Ensure your file is compatible or modify the script accordingly.
