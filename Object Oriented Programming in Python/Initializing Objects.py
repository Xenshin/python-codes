''' The initializer is a special method because it does not have a return type. 
The first parameter of __init__ is self, which is a way to refer to the object being initialized.'''

# Defining initializers
'intializers are called when an object is created'
class Employee:
    # defining the properties and assigning them None
    def __init__(self, Id, salary, department):
        self.Id = Id
        self.salary = salary
        self.department = department

# creating an object of the employee class with default parameters
steve = Employee(3789, 2500, "Human Resources")

# printing properties of steve
print("Id =", steve.Id)
print("salary =", steve.salary)
print("department =", steve.department)

# the initializer is automatically called when an object is created.
''' It is important to define the initializer with complete parameters to avoid any errors.
Similar to methods, initializers also have the provision for optional parameters'''

# INITIALIZER WITH OPTIONAL PARAMETERS
class employee:
    # defining the properties and assigning None to them
    def __init__(self, Id = None, salary = 0, department = None): # it's necessary to assign initial values to class properties when defining the class
        self.Id = Id
        self.salary = salary
        self.department = department

# creating an object of the employee class with default parameters
steve = employee()
mark = employee("3789", 2500, "Human Resources")

# printing properties of steve and mark
print("steve")
print("Id:", steve.Id)
print("salary:", steve.salary)
print("department:", steve.department)
print("mark")
print("Id:", mark.Id)
print("salary:", mark.salary)
print("department:", mark.department)
