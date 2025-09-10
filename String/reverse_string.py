def reverse_string1(text):
    if not text:
        return ""
    lst = text.split(' ')
    if len(lst) == 1:
        text = text[::-1]
        return text
    else:
        lst = lst[::-1]
        return " ".join(lst)

def reverse_string2(text, by_word=True):
    if not text:
        return ""
    
    if by_word:
        return " ".join(text.split()[::-1])
    else:
        return text[::-1]