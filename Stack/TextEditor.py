class TextEditor:
    def __init__(self):
        self.stack = []
        self.undo_redo = []

    def push(self,text):
        self.stack.append(text)
        self.undo_redo.clear()
    
    def undo(self):
        if not self.is_empty():
            value = self.stack.pop()
            self.undo_redo.append(value)
            return self.stack[-1] if self.stack else ""
        raise ValueError("Nothing to undo!")
    
    def redo(self):
        if self.undo_redo:
            value = self.undo_redo.pop()
            self.stack.append(value)
            return value
        raise ValueError("Nothing to Redo!")
    
    def is_empty(self):
        return len(self.stack) == 0

    def get_text(self):
        return self.stack[-1] if self.stack else ""