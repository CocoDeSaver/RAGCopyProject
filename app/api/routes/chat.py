from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.rag_service import generate_answer

router = APIRouter()

@router.post("/chat")
async def chat(data: ChatRequest):
    try: 
        response = generate_answer(
            user_message = data.message,
            persona_name = data.persona
        )
        return {
            "status" : "success",
            "persona" : data.persona,
            "response" : response
            }
    except Exception as e:
        return {
            "status" : "error",
            "message" : str(e)
        }