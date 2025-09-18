import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

class OpenAIClient:
    def __init__(self, model='gpt-4o-mini'):
        self.model = model

    def complete(self, prompt: str, max_tokens=256):
        if not OPENAI_API_KEY:
            return "[LLM not configured: set OPENAI_API_KEY to enable OpenAI completions]"
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role":"user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.0
        )
        return resp.choices[0].message.content.strip()