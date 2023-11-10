class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.tail.next = new_node
        self.length += 1
    
    def show(self):
        current = self.head
        while current:
            print(current.value, end = " ")
            current = current.next
        