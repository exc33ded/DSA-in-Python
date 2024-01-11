class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLL:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
csLL = CSLL(10)
print(csLL.head.value)