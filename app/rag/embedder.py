import requests
import numpy as np
from app.core.config import OLLAMA_BASE_URL, EMBED_MODEL

def embed_text(text: str) -> np.ndarray:
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embeddings",
        json = {
            'model': EMBED_MODEL,
            "prompt": text
        }
    )
    embedding = response.json()["embedding"]
    return np.array(embedding).astype("float32")