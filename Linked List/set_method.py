# Works togerther with "get method"

class Node:
    def __init__(self,  value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
    
    def perpend(self, value):