class Student:
    stuCount = 0

    def __init__(self, name, stu_no,class_no,gender):
        self.name = name
        self.stu_no = stu_no
        self.class_no = class_no
        self.gender = gender
        Student.stuCount += 1

    def study(self):
        print "Student can study"

    def getStuCount(self):
        return Student.stuCount

class PrimaryStudent(Student):
    primaryStuCount = 0

    def canRecite(self):
        print "Primary Student can recite"

    def canOral(self):
        print "Primary Student can oral"


class MiddleStudent(Student):
    middelStucount = 0

    def __init__(self, name, stu_no,class_no,gender):
        self.name = name
        self.stu_no = stu_no
        self.class_no = class_no
        self.gender = gender
        Student.stuCount += 1
        
    def canChemistry(self):
        print "middle Student can Chemistry"

    def canPyhics(self):
        print "middle Student can Physics"
