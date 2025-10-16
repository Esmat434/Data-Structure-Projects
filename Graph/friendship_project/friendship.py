from collections import deque

class FriendShip:
    def __init__(self,edges):
        self.edges=edges
        self.dict={}
    
    def adj_dict(self):
        for start,dist in self.edges:
            if start in self.dict:
                self.dict[start].append(dist)
            else:
                self.dict[start]=[dist]
            
            if dist in self.dict:
                self.dict[dist].append(start)
            else:
                self.dict[dist]=[start]
    
    def check_friend_ship(self,start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in self.dict.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visited