# This program is for creating a linked list with one element, ie, one head and tail

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
# -------- OR -----------

class LinkedList_:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
new_linked_list = LinkedList(10)
print(new_linked_list) # <__main__.LinkedList object at 0x000001BC1F18BD50>
print(new_linked_list.head.value) # 10
print(new_linked_list.tail.value) # 10
print(new_linked_list.length) # 1