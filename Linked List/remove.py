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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
            
    def get(self, index):
        if index == -1:
            return -1
        elif index < -1 or index >= self.length:
            return None
        else:
            for _ in range(index):
                current = current.next
            return current
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):  
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
        self.length -= 1
        return popped_node