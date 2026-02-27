from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.rag_service import generate_answer

router = APIRouter()

@router.post("/chat")
def chat(data: ChatRequest):
    response = generate_answer(
        user_message = data.message,
        persona_name = data.persona
    )
    return {"response" : response}