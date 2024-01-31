class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp = self.head
        result = ""
        while True:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += "->"
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = new_node
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
    
csLL = CSLinkedList()
csLL.prepend(10)
csLL.prepend(20)
csLL.prepend(30)
csLL.prepend(40)
csLL.prepend(50)
print(csLL.__str__())