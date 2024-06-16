import os
from llm import LLM
from tts import TextToSpeech


def main():
    # Fetch the API key from an environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")

    llm = LLM(api_key)
    tts = TextToSpeech(api_key)

    # Prompt for the API
    prompt = "Food order: Pizza from Dominos. You are on a call with dominos. Start the conversation pretending to be the user."

    # Generate text using the LLM class
    generated_text = llm.generate(prompt)
    print(f"Generated text: {generated_text}")

    # Generate speech from the generated text
    tts.text_to_speech(generated_text)

    # TODO: Speech to text.

    print("Speech has been generated, played, and saved.")

if __name__ == "__main__":
    main()
