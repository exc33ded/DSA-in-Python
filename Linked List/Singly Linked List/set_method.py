# Works togerther with "get method"

class Node:
    def __init__(self,  value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
    
    def perpend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
new_ll = LinkedList()
new_ll.perpend(10)
new_ll.perpend(20)
new_ll.perpend(30)
new_ll.perpend(40)
new_ll.perpend(50)

new_ll.show()

print(new_ll.set_value(3, 100))
new_ll.show()
