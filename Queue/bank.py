from collections import deque
import time
from random import randint as rnd

class Bank_Queue:
    def __init__(self):
        self.customer=deque()
    
    def enqueue(self,data):
        self.customer.append(data)
        return 
    
    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        wait_time = rnd(3,10)
        time.sleep(wait_time)
        name = self.customer.popleft()
        return f"Service done for {name}"

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty.")
        return self.customer[0]
    
    def is_empty(self):
        return len(self.customer) == 0
    
    def size(self):
        return len(self.customer)

azizi = Bank_Queue()
azizi.enqueue("ahmad")
azizi.enqueue("jan")
azizi.enqueue("khan")
azizi.enqueue("mohammad")
azizi.enqueue("ajmal")
print(azizi.dequeue())