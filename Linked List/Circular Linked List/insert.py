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
    
    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range.")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
csLL = CSLinkedList()
csLL.insert(0,10)
# csLL.insert(5, 20)
csLL.insert(1,30)
csLL.insert(0, 40)
csLL.insert(2, 50)
print(csLL.__str__())