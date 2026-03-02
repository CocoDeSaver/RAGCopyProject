import requests
import numpy as np
from app.core.config import settings
def embed_text(text: str) -> np.ndarray:
    response = requests.post(
        f"{settings.OLLAMA_BASE_URL}/api/embeddings",
        json = {
            'model': settings.EMBED_MODEL,
            "prompt": text
        }
    )
    embedding = response.json()["embedding"]
    return np.array(embedding).astype("float32")