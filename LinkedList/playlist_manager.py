class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class PlayListManager:
    def __init__(self):
        self.head=None
        self.length=0
    
    def push_song(self,song):
        new_node = Node(song)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
        self.length+=1
    
    def play_song(self):
        if self.head:
            song = self.head.data
            self.head = self.head.next
            self.length-=1
            return f"{song} playing..."
        else:
            raise ValueError("Nothing to play!")
    
    def total_song(self):
        return self.length
    
    def __str__(self):
        if not self.head:
            return "No songs in playlist"
        
        temp = self.head
        _str = ''
        while temp:
            _str+= str(temp.data)
            if temp.next:
                _str+= " --> "
            temp = temp.next
        
        return _str

songs = PlayListManager()
songs.push_song("ahmad")
songs.push_song("mohammad")
songs.push_song("ajmal")
songs.push_song("khan")
print(songs)
print(songs.play_song())
print(songs)