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


# ADVANTAGES OF METHOD OVERLOADING:
'''1.) Overloading saves us memory in the system
2.) Increases execution speed
3.) makes code cleaner and readable
4.) Allows the implementations of polymorphosism'''


# CLASS METHOD
'Class method work with class variables and are accessible using the class name rather than its object'
'Since all the class objects share the class variables, class methods are used to access and modify class variables'

class Player:
    teamName = 'Liverpool' # class variable

    def __init__(self, name):
        self.name = name # instance variable
    
    @classmethod
    def getTeamName(cls):
        return cls.teamName

print(Player.getTeamName()) # class method is accessed using class variable


# STATIC METHODS
'static methods are usually limited to class only and not their objects.'
'They have no direct relation to class variables or instance variables.'
'Static methods can be accessed using the class name or the object name'

class Player:
    teamName = 'Liverpool' # class variable

    def __init__(self, name):
        self.name = name # creating instance variables

    @staticmethod # constructor used to define static method
    def demo():
        print("I am a static method")

p1 = Player('lol') # defining an object for the class
p1.demo() # accessing the method through object
Player.demo() # accessign the method through class

'The purpose of a static method is to use its parameters and produce a useful result'

# through a class of bodyinfo, which contains the physical attribute of all the students
# now calculating the BMI

class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight/height**2

print(BodyInfo.bmi(64, 1.71))