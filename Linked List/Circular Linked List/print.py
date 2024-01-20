class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        
    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += "->"
        return result
            
csLL = CSLinkedList()
csLL.append(10)    
csLL.append(20)    
csLL.append(30)    
csLL.append(40)    
csLL.append(50)             
print(csLL.__str__())