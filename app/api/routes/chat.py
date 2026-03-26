from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.rag_service import generate_answer

router = APIRouter()

@router.post("/chat")
async def chat(data: ChatRequest):
    try: 
        messages = data.history if data.history else []
        messages.append({
            'role' : 'user',
            'content' : data.message
        })
        result = generate_answer(
            messages = messages,
            persona_name = data.persona
        )

        return {
            "status" : "success",
            "persona" : data.persona,
            "reply" : result["reply"],
            "alert" : result["alert"]
            }

    except Exception as e:
        return {
            "status" : "error",
            "message" : str(e)
        }