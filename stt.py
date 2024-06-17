from pathlib import Path 
import os
from openai import OpenAI


class SpeechToText:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key = api_key)

    def speech_to_text(self, file_path: Path) -> str:
        audio_file = open(file_path, "rb")
        transcription = self.client.audio.transcriptions.create(
            model = "medium.en",
            file=audio_file, 
            response_format="text"
        )
        return transcription  # Directly return the transcription string
    
if __name__ == "__main__":
    stt = SpeechToText(os.getenv("OPENAI_API_KEY"))
    print(stt.speech_to_text(Path("./speech.mp3")))
