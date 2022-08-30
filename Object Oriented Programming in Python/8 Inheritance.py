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