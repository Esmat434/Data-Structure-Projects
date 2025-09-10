def polindrom(text):
    if not text:
        return ""
    
    text = text.strip().lower()
    p_text = text[::-1]
    
    if p_text == text:
        return "is polindrom"
    else:
        return "not polindrom"

print(polindrom("noon"))