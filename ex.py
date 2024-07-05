import os 
from openai import OpenAI
from tts import TextToSpeech
from stt import SpeechToText
from pathlib import Path

api_key="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"
client = OpenAI(api_key=api_key)

# List of phrases to watch out for
narrative_safeguards = [
    "sorry cannot help with this"
]

def get_assistant_response(messages: list[dict[str, str]]) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

def check_narrative_safeguards(text: str) -> bool:
    for phrase in narrative_safeguards:
        if phrase in text:
            return True
    return False

def check_intelligent_prompts(response: str) -> bool:
    # Example: Detect unreliable promises or excessive exaggerations
    if "guarantee" in response.lower() or "always" in response.lower():
        return True
    return False

if __name__ == '__main__':
    system_message = {"role": "system", 
                      "content": "You are a helpful assistant."}

    assistant_initial_text = "Hello, how can I help you today?"
    print(assistant_initial_text) 

    tts = TextToSpeech(api_key)
    tts.text_to_speech(assistant_initial_text)

    assistant_initial_message = {"role": "assistant",
                                 "content": assistant_initial_text}
    
    stt = SpeechToText(api_key)

    while True:
        audio_path = "my_speech.wav"
        stt.record_audio(audio_path, duration=10)

        user_input: str = stt.speech_to_text(audio_path)

        user_message = {"role": "user",
                        "content": user_input}

        messages = [
            system_message,
            assistant_initial_message,
            user_message
        ]

        response = get_assistant_response(messages)
        print(f"Assistant response: {response}")

        if check_narrative_safeguards(response):
            print("Reminder: Avoid using phrases like 'sorry cannot help with this'.")
        
        if check_intelligent_prompts(response):
            print("Reminder: Avoid making unreliable promises or excessive exaggerations.")

        messages.append({"role": "assistant", "content": response})
        tts.text_to_speech(response)
