import requests
from app.core.config import OLLAMA_BASE_URL, OLLAMA_MODEL


def call_ollama(prompt: str):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]