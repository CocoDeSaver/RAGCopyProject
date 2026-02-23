from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()
class ChatRequest(BaseModel):
    message: str

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
MODEL = os.getenv("OLLAMA_MODEL")

@app.post("/chat")
def chat(data: ChatRequest):
    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/generate",
        json = {
            "model" : MODEL,
            "prompt" : data.message,
            "stream" : False
        }
    )
    return {"answer": response.json()["response"]}