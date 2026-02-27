import faiss
from app.core.config import FAISS_INDEX_PATH

def load_index():
    return faiss.read_index(FAISS_INDEX_PATH)

def save_index(index):
    faiss.write_index(index, FAISS_INDEX_PATH)
