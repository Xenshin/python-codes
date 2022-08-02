' A method is a group of statements that performs some operations and may or may not return a result'

# the self argument
''' the major difference between functions and methods in python is the first argument in the method definition.
conventionally, this is named 'self'. The user can use different name too'''

from re import S


class employee:
    # defining the initializer
    def __init__(self, Id=None, salary=None, department=None):
        self.Id = Id
        self.salary = salary
        self.department = department
    
    #defining methods
    def tax(self):
        return (self.salary*0.2)

    def salaryPerDay(self):
        return (self.salary/30)
    
# Intializing an object of the employee class:
steve = employee(3789, 2500, "human resources")

# printing properties of steve
print("Id:",steve.Id)
print("salary:", steve.salary)
print("department:", steve.department)
print("tax paid by steve:", steve.tax())
print("salary per day of steve:", steve.salaryPerDay())    

# METHOD OVERLOADING
'When a method is written in such a way that it can perform more than one task'

class Myclass:
    def __init__(self, Id=None, salary=None, department=None):
        self.Id = Id
        self.salary = salary
        self.department = department

    # method overloading
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
            return s

obj = Myclass()
print(obj.sum(10, 20, 30)) # this will run perfectly
# but when less arguments are passed than expected it shows error
'so we need to write our method in a way to increase its functionality'

class Myclass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            return "pass atleast two arguments for addition"
        return s

obj = Myclass()
print(obj.sum(10, 20, 30))
print(obj.sum(10, 20))
print(obj.sum(10))
# now our method can perform three different tasks based on the number of arguments passed

