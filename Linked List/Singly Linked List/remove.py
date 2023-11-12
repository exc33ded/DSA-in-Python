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
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
            
    def get(self, index):
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.length == 0:
            return None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):  
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
    
    def remove(self, index):
        if index >= self.length or index < -1:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1 or index == -1:
            return self.pop()
        else:
            prev_node = self.get(index - 1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node
        
new_ll = LinkedList()
new_ll.append(10)
new_ll.append(20)
new_ll.append(30)
new_ll.append(40)
new_ll.append(50)
new_ll.show()
print(new_ll.remove(-1))
print(new_ll.remove(2))
print(new_ll.remove(10))
new_ll.show()

# Another approch, not functions used        
    # def remove(self, index):
    #     if index < 0 or index >= self.length:
    #         return None
            
    #     elif index == 0:
    #         popped_node = self.head
    #         if self.length == 1:
    #             self.head = None
    #             self.length = None
    #         else:
    #             self.head = self.head.next
    #         popped_node.next = None
    #         self.length -= 1
    #         return popped_node
            
    #     else:
    #         temp = self.head
    #         for _ in range(index - 1):
    #             temp = temp.next
    #         popped_node = temp.next
            
        
    #     if popped_node.next is None:
    #         self.tail = temp
    #     temp.next = temp.next.next
    #     popped_node.next = None
    #     self.length -= 1
    #     return popped_node
    
