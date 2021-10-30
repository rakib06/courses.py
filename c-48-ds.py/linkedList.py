class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size= 0
    
    # O(1)
    def insertFirst(self, data):
        self.size = self.size +1
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
        
        else:
            newNode.nextNode = self.head # connecting with old head node
            self.head = newNode
    
    # O(1)
    def size(self)
        return self.size 