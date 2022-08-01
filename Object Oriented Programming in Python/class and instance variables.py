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

# The correct implementation will be
class Player:
    teamName = 'Liverpool'  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables
        self.formerTeams = [] # formerly this player played with which club is individual attribute of the object


p1 = Player('Mark')
p1.formerTeams.append('Barcelona')
p2 = Player('Steve')
p2.formerTeams.append('Chelsea')

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams) # Now the property formerTeams is unique for each Player class object and can only be accessed by that unique object.


# USING CLASS VARIABLE SMARTLY
class player: # defining class
    teamName = 'liverpool'
    teamMembers = []
    def __init__(self, name):
        self.name = name
        self.formerTeams = []
        self.teamMembers.append(self.name)

# defining objects
p1 = player("mark") # this appends mark in teamMembers
p2 = player("steve") # this appends steve in teamMembers

print("name:", p1.name)
print("team members:", p1.teamMembers)
print("name:", p2.name)
print("team members:", p2.teamMembers)

