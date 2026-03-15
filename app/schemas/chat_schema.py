from typing import Dict, List, Optional
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    persona: str
    history: Optional[List[Dict]] = []