from pathlib import Path
import os
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play
import sys
sys.path.append('/usr/bin/ffmpeg')

class TextToSpeech:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.speech_file_path = Path(__file__).parent / "speech.mp3"

    def text_to_speech(self, text: str):
        response = self.client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(self.speech_file_path)
        sound = AudioSegment.from_file(self.speech_file_path)
        play(sound)


if __name__ == "__main__":
    api_key = os.getenv('OPENAI_API_KEY')
    tts = TextToSpeech(api_key)
    tts.text_to_speech("Today is a wonderful day to build something people love! Yay!")
