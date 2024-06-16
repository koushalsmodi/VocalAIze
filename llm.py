from openai import OpenAI

class LLM:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a helpful speech assistant on a phone call. You are being provided the entire history of the conversation. Adapt your conversation accordingly. You will be helping a human to book a table by calling up a restaurant. Ensure to get a reservation. Check if you have made a call at the right place."},
                    {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

