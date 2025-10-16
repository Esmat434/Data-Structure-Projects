class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Students:
    def __init__(self):
        self.head=None
        self.length=0
    
    def push_student(self,data):
        new_node = Node(data)
        if self.head:
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=new_node
        self.length+=1

    def pop_students(self,name):
        index = self.finde_student_index_by_name(name)
        if index is None:
            raise ValueError("Student does not exists!")
        if index == 0:
            name = self.head.data
            self.head = self.head.next
            self.length-=1
            return f"{name} student successfully deleted."
        index-=1
        temp = self.head
        while index>=0:
            temp=temp.next
            index-=1
        name = temp.next.data
        temp=temp.next.next
        return f"{name} student successfully deleted."

    def finde_student_index_by_name(self,name):
        if not self.head:
            return None
        index=0
        temp=self.head
        while temp:
            if temp.data == name:
                return index
            index+=1
            temp=temp.next
        return None