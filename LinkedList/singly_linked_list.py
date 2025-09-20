class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.last=None
        self.length=0
    
    def push(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
        self.length+=1
    
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        temp=self.head
        while temp.next:
            temp=temp.next
        else:
            temp.next=new_node
            self.length+=1

    def insert(self,data,index):
        new_node=Node(data)
        if index>=self.length:
            self.append(data)
            return
        if index<=0:
            self.push(data)
            return 
        index-=1
        temp = self.head
        while index:    
            temp=temp.next
            index-=1
        else:
            new_node.next = temp.next
            temp.next=new_node
            self.length+=1
    
    def _delete_front(self):
        val = self.head.data
        self.head = self.head.next
        self.length-=1
        return val
    
    def _delete_end(self):
        if not self.head.next:
            val=self.head.data
            self.head=None
            self.length-=1
            return val
        
        temp = self.head
        while temp.next.next:
            temp=temp.next
        else:
            val = temp.next.data
            temp.next=None
            self.length-=1
            return val
    
    def delete(self,index):
        if not self.head:
            raise ValueError("Linked list is empty.")
        if index<=0:
            return self._delete_front()
        elif index>=self.length:
            return self._delete_end()
        index-=1
        temp = self.head
        while index:
            temp=temp.next
            index-=1
        else:
            val=temp.next.data
            temp.next=temp.next.next
            self.length-=1
            return val

    def __repr__(self):
        _str=''
        temp=self.head
        while temp.next:
            _str+=str(temp.data) + ' ---> '
            temp = temp.next
        else:
            _str+=str(temp.data)
        return _str

linked=LinkedList()
linked.push(2)
linked.push(3)
linked.push(4)
linked.append(5)
linked.append(6)
linked.insert(12,0)
linked.insert(23,24)
linked.insert(45,3)
linked.insert(55,-5)
