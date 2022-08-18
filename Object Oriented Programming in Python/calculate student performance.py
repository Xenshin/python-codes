class Student:
    def __init__(self,name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        marks_obtained = self.phy + self.chem + self.bio
        return marks_obtained

    def percentage(self):
        total_marks = 300
        percentage = (self.totalObtained()/total_marks)*100
        return percentage 
