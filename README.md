# Text to Speech and Speech to Text Conversion Tool

This Python script uses the OpenAI API to convert text into spoken language and spoken language from an audio file into written text. It's designed to be easy to use and integrate into any project that requires text-to-speech or speech transcription.

## Requirements

To run this script, you will need:

- Python 3.6 or higher
- `openai` Python package
- An API key from OpenAI

## Setup

Follow these steps to set up the script:

1. **Install the required package**:
   Install the OpenAI Python package

2. **API Key**:
   - Obtain an API key
   - Set the API key in your environment variables for secure access

## Usage

### Text to Speech

To use the text-to-speech functionality, follow these instructions:

- Create a text file named `text.txt` in the same directory as the script, containing the text you want to convert to speech.
- Run the script using Python: python3 tts.py
- The script will generate an audio file (e.g., `output.mp3`) with the spoken version of the text.

### Speech to Text

To use the speech-to-text functionality, follow these instructions:

- Place an audio file named `speech.mp3` in the same directory as the script. If your file is named differently or located elsewhere, modify the file path in the script accordingly.
- Run the script using Python: python3 stt.py

- The script will automatically transcribe the audio and print the transcription to the console.

## How It Works

### Text to Speech

The script operates by performing the following steps:

1. **Initialization**:
   - A `TextToSpeech` object is created using your OpenAI API key. This object handles the interaction with the OpenAI API.

2. **Reading the Text File**:
   - The script reads the specified text file (`text.txt` by default). If the file is not found, the script will raise an error.

3. **Sending Text Data to OpenAI**:
   - The text data is sent to OpenAI's text-to-speech service. The script uses the `openai` Python package to make this request.

4. **Receiving the Audio Data**:
   - The OpenAI API processes the text and returns the audio data. The script captures this response and checks for any errors or issues in the conversion process.

5. **Saving the Audio File**:
   - The audio data is saved to an output file (e.g., `output.mp3`). The script can be modified to change the output file format or perform additional processing as needed.

6. **Error Handling**:
   - The script includes basic error handling to manage issues such as network errors, invalid API keys, and unsupported text formats. Any errors encountered during the process are logged to the console.

7. **Logging**:
   - The script logs key events and errors to the console to help with debugging and monitoring the conversion process.

### Speech to Text

The script operates by performing the following steps:

1. **Initialization**:
   - A `SpeechToText` object is created using your OpenAI API key. This object handles the interaction with the OpenAI API.

2. **Reading the Audio File**:
   - The script reads the specified audio file (`speech.mp3` by default). If the file is not found or is in an unsupported format, the script will raise an error.

3. **Sending Audio Data to OpenAI**:
   - The audio data is sent to OpenAI's speech-to-text service. The script uses the `openai` Python package to make this request.

4. **Receiving the Transcription**:
   - The OpenAI API processes the audio and returns the transcription. The script captures this response and checks for any errors or issues in the transcription process.

5. **Outputting the Transcription**:
   - The transcription is printed to the console. The script can be modified to save the transcription to a file or perform additional processing as needed.

6. **Error Handling**:
   - The script includes basic error handling to manage issues such as network errors, invalid API keys, and unsupported audio formats. Any errors encountered during the process are logged to the console.

7. **Logging**:
   - The script logs key events and errors to the console to help with debugging and monitoring the transcription process.

## Notes

- The default model used for transcription is `medium.en`. You can change this setting in the `speech_to_text` method within the `stt.py` file to any other model supported by OpenAI.
- The script currently supports MP3 audio format for both input and output. If your audio file is in a different format, you will need to convert it to MP3 or modify the script to handle other formats.
