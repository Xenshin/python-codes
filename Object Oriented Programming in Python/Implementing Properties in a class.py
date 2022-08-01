# this code will compile
class employee:
    # defining the properties and assigning them none
    Id = None
    salary = None
    department = None # initializing the value of properties inside the class is necessary

# Accessing the properties and assigning valeu
'Syntax- '# object.property

''' There are two ways to assign values to properties of a class
1.) Assign values when defining the class
2.) Assign values in the main code'''


# Creating an object of the Employee class
steve = employee()

# assign"ing values to properties of steve - an object of the employee class
steve.Id = 3789
steve.salary = 2500
steve.department = "Human Resources"

# printing properties of steve - an object of the employee class
print("Id =", steve.Id)
print("Salary =", steve.salary)
print("Department =", steve.department)



    