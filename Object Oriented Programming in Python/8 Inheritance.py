''' Inheritance provides a way to create a new class from an existing class.
0) The new class is a specialised version of the existing class such that it inherits all the public attributes of the parent class'''

# SYNTAX
class vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    def printDetails(self):
        print("manufacturer:", self.make)
        print("color:", self.color)
        print("model:", self.model)
        
class car(vehicle):
    def __init__(self, make, color, model, doors):
        vehicle.__init__(self, make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("doors:", self.doors)

obj1 = car("suzuki", "grey", "2015", 4)
obj1.printCarDetails()

# Super() function:
# accessing parent class properties

class vehicle:
    fuelcap = 90
class car(vehicle):
    fuelcap = 50

    def display(self):
        # accessing fuel cap from the vehicle class using super()
        print("Fuel cap from the vehicle class:", super().fuelcap)
        # accessing fuel cap from the car class using self
        print("fuel cap from the car class:", self.fuelcap)

obj1 = car() # creating an object from class car
obj1.display()

# calling the parent class methods
class vehicle:
    def display(self):
        print("I am from the class vehicle")

class car(vehicle):
    def display(self):
        super().display()
        print("I am from the car class")

obj1 = car() # creating the car object
obj1.display() # calling the car class method display()
