class Student:
    __name = None
    __rollNumber = None

    def setName(self, newName):
        self.__name = newName
        
    def getName(self):
        return self.__name

    def setRollNumber(self, newRollNumber):
        self.__rollNumber = newRollNumber

    def getRollNumber(self):
        return self.__rollNumber
    