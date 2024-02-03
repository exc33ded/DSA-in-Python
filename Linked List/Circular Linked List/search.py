class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length  = 0
        
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
        
    def traversal(self):
        curr = self.head
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
            if curr == self.head:
                break
            
    def search(self, target):
        curr = self.head
        while curr:
            if curr.value == target:
                return True
            curr = curr.next
            
            if curr == self.head:
                break
        return False
        
csLL = CSLinkedList()
csLL.append(10)    
csLL.append(20)    
csLL.append(30)    
csLL.append(40)    
csLL.append(50) 
csLL.traversal()  
print(csLL.search(50))
print(csLL.search(100))