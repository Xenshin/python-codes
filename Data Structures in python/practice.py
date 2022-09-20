class stack():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items
    
    def peek(self):
        return self.items[-1]

mystack = stack()
mystack.push("A")
mystack.push("B")
print(mystack.get_stack())
mystack.push("C")
print(mystack.get_stack())
print(mystack.peek())
mystack.pop()
print(mystack.get_stack())
mystack.pop()
mystack.pop()
print(mystack.is_empty())
