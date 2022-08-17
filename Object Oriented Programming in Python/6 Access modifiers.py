''' Access modifiers are tags we can associate with each member to define which parts of the program can access it directly.

    Two types of access modifiers:
    1.) Public attributes
    2.) Private attributes'''

# public attributes are those that can be accessed inside and outside the class
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.salary = salary
    def displayID(self):
        print("ID:",self.ID)

steve = Employee(3789, 2500)
steve.displayID()
print(steve.salary) # it is a public attribute as it can be accessed inside and outside the class

# private attributes cannot be accessed directly from outside the class but can be accessed inside the class

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary # private attribute

steve = Employee(3789, 2500)
print("ID:", steve.ID)
# print("salary:", steve.__salary) # will produce an error

"PRIVATE METHODS"

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary
    def displaySalary(self):
        print("salary:", self.__salary) # __salary which is a private attribute can be accessed inside the class
    def __displayID(self):
        print("ID:", self.ID)

steve = Employee(3789, 2500)
steve.displaySalary()
#steve.__displayID() # will produce error for being private method

" ACCESSING PRIVATE ATTRIBUTES IN THE MAIN CODE"

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary

steve = Employee(3789, 2500)
print(steve._Employee__salary) # to access private attributes outside the class we can use '_<className>' prefix
