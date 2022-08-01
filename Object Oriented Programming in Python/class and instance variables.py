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

# WRONG USE OF CLASS VARIABLES
''' It is imperative to use class variable properly since they are shared by all the class objects and can be modified using any one of them'''
class Player:
    formerTeam = []
    teamName = 'liverpool'
    def __init__(self, name):
        self.name = name

p1 = Player("mark")
p1.formerTeam.append('Barcelona') # will make formerTeam = ['Barcelona']
p2 = Player("steve")
p1.formerTeam.append('Chelsea') # will make formerTeam = ['Barcelona', 'Chelsea']

print("name:", p1.name)
print("team name:", p1.teamName)
print(p1.formerTeam) # till here formerTeam value is formerTeam = ['Barcelona', 'Chelsea']
print("name:", p2.name)
print("team name:",p2.teamName)
print(p2.formerTeam) # till here formerTeam value is formerTeam = ['Barcelona', 'Chelsea']
