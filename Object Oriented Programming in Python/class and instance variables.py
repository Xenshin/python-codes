''' In python properties can be defined into two parts
1.) class variables
2.) Instance variables'''

# Class Variables
''' The class variables are shared by all instances or objects of the classes.
A change in the class variable will change the value of that property in all the objects of the class'''

# Instance Variables
''' The instance variables are unique to each instance or objects of the class. 
A change in the instance variable will change the value of the property in that specific object only'''

class player:
    teamName = 'Liverpool' # class variables

    def __init__(self, name):
        self.name = name # creating instance variables

p1 = player('Mark')
p2 = player('Steve')

print("name:", p1.name)
print("team name:", p1.teamName) 
print("name:", p2.name)
print("team name:", p2.teamName)

'''as we can see the variable name is different for different objects (p1, p2) of the class player and varible teamName has the same value'''

