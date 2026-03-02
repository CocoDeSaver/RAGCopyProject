import requests
from groq import Groq
from app.core.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)
print("API KEY:", settings.GROQ_API_KEY)

def generate_response(messages):
    response = client.chat.completions.create(
        model = settings.GROQ_MODEL,
        messages = messages,
        temperature = 0.7
    )
    return response.choices[0].message.content
