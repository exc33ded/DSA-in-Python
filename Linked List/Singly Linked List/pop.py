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
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def show(self):
        current = self.head
        while current:
            print(current.value, end = " ")
            current = current.next
    
    def pop(self):   # This will pop the last element
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
    
new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.append(50)

new_ll.show()

print("\n", new_ll.pop().value)
new_ll.show()
                