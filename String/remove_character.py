def remove_character(text):
    visited = ""
    for t in text:
        if t not in visited:
            visited+=t
    return visited