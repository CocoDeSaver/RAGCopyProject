import faiss
from app.core.config import settings

def load_index():
    return faiss.read_index(settings.FAISS_INDEX_PATH)

def save_index(index):
    faiss.write_index(index, settings.FAISS_INDEX_PATH)
