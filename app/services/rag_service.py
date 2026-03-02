from app.personalities.registry import PERSONALITIES
from app.services.llm_service import generate_response
from app.rag.retriever import retrieve

def generate_answer(user_message: str, persona_name: str):
    persona = PERSONALITIES.get(persona_name)

    if not persona:
        raise ValueError("Persona tidak ditemukan")
    
    context = retrieve(user_message)
    system_prompt = persona.format_prompt(context)

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    return generate_response(messages)
