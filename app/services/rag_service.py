from app.personalities.registry import PERSONALITIES
from app.services.safety_service import detect_risk
from app.services.llm_service import generate_response
from app.rag.retriever import retrieve
from typing import List, Dict 

def generate_answer(messages: List[Dict], persona_name: str):
    persona = PERSONALITIES.get(persona_name)

    if not persona:
        raise ValueError("Persona tidak ditemukan")
    
    query = messages[-1]["content"]
    alert = detect_risk(query)
    context = retrieve(query)
    system_prompt = persona.format_prompt(context)

    final_messages = [
        {"role": "system", "content": system_prompt} 
    ] + messages

    reply = generate_response(final_messages)

    return {
        "personality" : persona_name,
        "reply" : reply,
        "alert" : alert
    }