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
    
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
            
new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.append(50)

new_ll.traverse()