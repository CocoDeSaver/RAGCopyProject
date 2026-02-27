import pickle
import numpy as np
from app.rag.embedder import embed_text
from app.rag.vector_store import load_index
from app.core.config import CHUNK_PATH, TOP_K

index = load_index()

with open(CHUNK_PATH, "rb") as f:
    chunks = pickle.load(f)

def retrieve(query: str):
    query_vector = embed_text(query)
    query_vector = np.expand_dims(query_vector, axis = 0)
    distances, indices = index.search(query_vector, TOP_K)
    results = []

    for i in indices[0]:
        results.append(chunks[i]["text"])
    return "\n\n".join(results)