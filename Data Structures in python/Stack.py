# STACK DATA STRUCTURE

class Stack():
    def __init__(self):
        self.items = [] # items is a class variable

    # push function requires the item that has to be inserted in the stack
    def push(self, item): # creating push method
        self.items.append(item) # operation that push method will be performing between new items and the stack

    # pop function does not require item to be mentioned, as by default the top element is popped
    def pop(self): # creating pop method
        return self.items.pop() # pop by default returns the last element inserted to the list

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty(): # if stack is not empty
            return self.items[-1] # then return the last added element (top element)

    def get_stack(self): # this method will return the items list
        return self.items

myStack = Stack() # creating an object of class Stack
myStack.push("A") # pushing A in the stack
myStack.push("B") # pushing B in the stack
print(myStack.get_stack()) # printing all the elements of the stack
myStack.push("C") # pushing C in the stack
print(myStack.get_stack()) # printing all the elements of the stack
myStack.pop() # popping the top element of the stack i.e.,C
print(myStack.get_stack()) # printing all the elements present in the stack
print(myStack.is_empty()) # checks whether stack is empty or not, and returns Bool
print(myStack.peek()) # as stack is not empty so returns the top element i.e., B




