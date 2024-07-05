import os
from openai import OpenAI
from llm import LLM
from tts import TextToSpeech
from stt import SpeechToText
from pathlib import Path
client = OpenAI()

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

    # Analyze the generated text
    analysis = llm.analyze_text(generated_text)
    print(f"Analysis: {analysis}")

    # Generate speech from the generated text
    tts.text_to_speech(generated_text)

    # TODO: Speech to text.
    stt = SpeechToText(api_key)
    print(stt.speech_to_text(Path("./speech.mp3")))

    # Summarize and print ToDo items
    todos = llm.summarize_todos(generated_text)
    print(f"ToDo items: {todos}")

    # Query knowledge base for a specific scenario
    scenario = "finding_leads"
    guidance = llm.query_knowledge_base(scenario)
    print(f"Guidance for {scenario}: {guidance}")

    # Automate repetitive tasks
    follow_up = llm.schedule_follow_up("John Doe", "2023-10-15")
    print(follow_up)

    email_status = llm.send_email("johndoe@example.com", "Meeting Follow-Up", "Thank you for your time today.")
    print(email_status)

    crm_update = llm.update_crm("John Doe", "Discussed product features and next steps.")
    print(crm_update)

    print("Speech has been generated, played, and saved.")

if __name__ == "__main__":
    main()
