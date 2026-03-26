from app.core.danger_words import DANGER_WORDS

def detect_risk(message: str):
    text = message.lower()

    for category, words in DANGER_WORDS.items():
        for word in words:
            if word in text :
                return "berbahaya"
            
    return "aman"