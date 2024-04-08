class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
        
    def __str__(self) -> str:
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
    
    def push(self, val):
        if self.isFull():
            return None
        else:
            self.list.append(val)
            return 'inserted'
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.list.pop()
        
    def peak(self):
        if self.isEmpty():
            return None
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
        

cusStack = Stack()
print(cusStack.isEmpty)
cusStack.push(10)
cusStack.push(10)
cusStack.push(10)
cusStack.push(10)
cusStack.push(10)
        