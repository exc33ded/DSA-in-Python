# With this method we can insert a node/elment any where is the linked list.

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
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node
        
new_LL = LinkedList()
new_LL.append(10)
new_LL.append(20)
new_LL.append(30)
new_LL.append(40)

print(new_LL.head.value)
print(new_LL.tail.value)
print(new_LL.length)
print(new_LL)