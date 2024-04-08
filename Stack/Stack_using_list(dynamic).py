class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self, val):
        self.list.append(val)
        return 'insertion done!!'
    
    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            self.list.pop()
        
    def peak(self):
        if self.isEmpty():
            return 'Empty Stack'
        else:
            return self.list[len(self.list)-1]
        
    def delete(self):
        self.list = None
     
        
        
customStack = Stack()
print(customStack.isEmpty())
customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.push(40)
customStack.push(50)
print(customStack, "\n")
customStack.pop()
customStack.pop()
print(customStack, "\n")
print(customStack.peak())
print(customStack.delete())
print(customStack.isEmpty(), "\n")
