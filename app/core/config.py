import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
EMBED_MODEL = "nomic-embed-text"

FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "vectorstore/faiss.index")
CHUNK_PATH = "vectorstore/chunks.pkl"
TOP_K = int(os.getenv("TOP_K", 5))