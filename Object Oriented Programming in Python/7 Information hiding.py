''' Information hiding refers to the concept of hiding the inner workings of a class and simply provide an interface through which the outside world
can interact with the class without knowing what's going on inside.

Components of Data Hiding:
1.) Encapsulation
2.) Abstraction
'''

# ENCAPSULATION:
''' It refers to binding data and the methods to manipulate that data together in a single unit, that is, class'''

''' When encapsulating classes, a good convention is to declare all variables of a class PRIVATE. This will restrict direct access by the code outside
the class.

To use these methods and variables outside the class, one has to implement PUBLIC methods.

These methods are called getters and setters'''

# ADVANTAGES OF ENCAPSULATION:
'''
1.) Classes make the code easy to change and maintain.
2.) Properties to be hidden can be specified easily.
3.) We decide which outside classes or functions can access the class properties
'''

# Getters and Setters
'''
1.) A getter method allows reading a property's value.
2.) A setter method allows modifying a property's value
'''

class user:
    def __init__(self, username=None):
        self.__username = username
    def setUsername(self,x):
        self.__username = x
    def getUsername(self):
        return (self.__username)

steve = user('steve1')
print('Before setting:', steve.getUsername())
steve.setUsername('steve2')
print('After setting:', steve.getUsername())

#UNDERSTANDING ENCAPSULTAION USING EXAMPLES:
'A bad example'
class User:
    def __init__(self, userName=None, password=None):
        self.userName = userName
        self.password = password

    def login(self, userName, password):
        if ((self.userName.lower() == userName.lower()) and (self.password == password)):
            print('Access granted')
        else:
            print('Invalid Credentials')

steve = User("Steve", "12345")
steve.login("steve", "12345")
steve.login("steve", "6789")
steve.password = "6789"
steve.login("steve", "6789")