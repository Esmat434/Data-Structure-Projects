class PrinterSpooling:
    def __init__(self):
        self.queue = []
    
    def enqueue_document(self,docx):
        self.queue.append(docx)
        return f"{docx} in processing..."
    
    def dequeue_document(self):
        if not self.is_empty():
            value = self.queue.pop(0)
            return f"{value} printed successfully..." 
        raise ValueError("Nothing to print!")
    
    def get_all_docx(self):
        return self.queue
    
    def is_empty(self):
        return len(self.queue) == 0
    
