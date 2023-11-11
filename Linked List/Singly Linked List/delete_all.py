class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1  
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end = " ")
            current = current.next
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
new_ll = LinkedList()
new_ll.prepend(10)
new_ll.prepend(20)
new_ll.prepend(30)
new_ll.prepend(40)
new_ll.prepend(50)
new_ll.show()

print(new_ll.delete_all())
new_ll.show()