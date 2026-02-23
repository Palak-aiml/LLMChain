"""
llmchain/integrations/openai.py

Integration for OpenAI LLMs and embeddings.
"""
import openai

class OpenAIIntegration:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate(self, prompt, model="gpt-3.5-turbo"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    def embed(self, text, model="text-embedding-ada-002"):
        response = openai.Embedding.create(
            model=model,
            input=text
        )
        return response.data[0].embedding
