import faiss
import pickle
import numpy as np
from app.rag.embedder import embed_text
from app.rag.file_loader import load_markdown_files
from app.rag.chunker import chunk_text
from app.core.config import FAISS_INDEX_PATH, CHUNK_PATH

def build_index():
    documents = load_markdown_files()
    all_chunks = []
    vectors = []
    
    for doc in documents:
        chunks = chunk_text(doc["content"])

        for chunk in chunks:
            vector = embed_text(chunk)
            vectors.append(vector)
            all_chunks.append({
                "text": chunk,
                "source": doc["source"]
            })
            print(f"Embedding chunk {len(vectors)+1}")

    vectors = np.vstack(vectors)
    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    faiss.write_index(index, FAISS_INDEX_PATH)
    with open(CHUNK_PATH, "wb") as f:
        pickle.dump(all_chunks, f)
    
    print("Faiss index berhasil dibuat")