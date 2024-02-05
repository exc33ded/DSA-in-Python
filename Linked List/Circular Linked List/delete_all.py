class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self) -> str:
        return str(self.value)

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
            
    def delete_all(self):
        if self.length == 0:
            return None
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

        
csLL = CSLinkedList()
csLL.append(10)    
csLL.append(20)    
csLL.append(30)    
csLL.append(40)    
csLL.append(50) 
csLL.traversal()
csLL.delete_all()
csLL.traversal()