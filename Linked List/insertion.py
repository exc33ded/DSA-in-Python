# Using Append Method

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __inint__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            