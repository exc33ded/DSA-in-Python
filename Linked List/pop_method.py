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
            
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            return popped_node.value
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value
    
new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.append(50)

new_ll.show()
print()

print(new_ll.pop_first(), "\n")
new_ll.show()
        