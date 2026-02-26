class BasePersonality:
    name: str = "BasePersonality"
    def system_prompt(self) -> str:
        return "You are a helpful assistant."
    def format_prompt(self, user_message:str, context: str) -> str:
        return f"""
System:
{self.system_prompt()}

Context:
{context}

User:
{user_message}

Answer:
"""