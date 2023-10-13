# Using Append Method

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

new_LL = LinkedList()
new_LL.append(10)
new_LL.append(20)

print(new_LL.head.value)
print(new_LL.tail.value)
print(new_LL.length)