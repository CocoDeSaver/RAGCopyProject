from app.personalities.registry import PERSONALITIES
from app.services.llm_service import call_ollama
from app.rag.retriever import retrieve

def generate_answer(user_message: str, persona_name: str):
    persona = PERSONALITIES.get(persona_name)

    if not persona:
        raise ValueError("Persona tidak ditemukan")
    
    context = retrieve(user_message)
    final_prompt = persona.format_prompt(user_message, context)
    return call_ollama(final_prompt)