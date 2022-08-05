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

