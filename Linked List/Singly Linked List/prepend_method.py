# This method append the node at the beginning, therefore prepend.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = " "
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
        
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

new_ll = LinkedList()
new_ll.prepend(10)
new_ll.prepend(20)
new_ll.prepend(30)
new_ll.prepend(40)
new_ll.prepend(50)

print(new_ll.head.value)
print(new_ll.tail.value)
print(new_ll.length)
print(new_ll)