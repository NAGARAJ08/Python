class Student:

    def __init__(self, name, major, gpa, is_on_Probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_Probation = is_on_Probation

    def on_honor_roll(self):

        if self.gpa >= 8:
            return True
        else:
            return False



