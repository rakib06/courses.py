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
    def size(self):
        return self.size 
    
    # O(1)
    def insertLast(self, data):
        self.size += 1
        newNode = Node(data)
        
        selectedNode = self.head
        
        while selectedNode is not None:
            selectedNode = selectedNode.newNode
            
        selectedNode.nextNode = newNode
    
    def traverseList(self):
        actualNode = self.head
        
        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode
    
    def remove(self, data):
        if self.head is not None: #if  the node is empty 
            return 
        
        currentNode = self.head
        previousNode = None
        
        while currentNode != data:
            previousNode = currentNode 
            currentNode = currentNode.nextNode
            
        if previousNode is None:
            self.head = currentNode.newNode # if the element is the first node 
        else:
            previousNode.nextNode = currentNode.nextNode
    
    