class Binary_Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.length=0
    
    def add_child(self,data):
        if type(data)!=Binary_Tree:
            data = Binary_Tree(data)
        if not self.left:
            self.left=data
            self.length+=1
        elif not self.right:
            self.right=data
            self.length+=1
        else:
            self.left.add_child(data)
    
    def delete(self, key):
        if not self:
            return None
        
        queue = [self]
        node_to_delete = None
        last_node = None
        parent_of_last = None

        while queue:
            current = queue.pop(0)
            if current.data == key:
                node_to_delete = current
            if current.left:
                queue.append(current.left)
                parent_of_last = current
                last_node = current.left
            if current.right:
                queue.append(current.right)
                parent_of_last = current
                last_node = current.right
        
        if node_to_delete:
            node_to_delete.data = last_node.data

            if parent_of_last.right == last_node:
                parent_of_last.right = None
            else:
                parent_of_last.left = None

    def search(self,target):
        if self.data == target:
            return True
        if self.left:
            status = self.left.search(target)
            if status:
                return True
        if self.right:
            status = self.right.search(target)
            if status:
                return True
        return False
        

tree = Binary_Tree(56)
tree.add_child(12)
tree.add_child(14)
tree.add_child(15)
tree.add_child(23)
tree.add_child(56)