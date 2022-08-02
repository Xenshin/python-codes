' A method is a group of statements that performs some operations and may or may not return a result'

# the self argument
''' the major difference between functions and methods in python is the first argument in the method definition.
conventionally, this is named 'self'. The user can use different name too'''

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