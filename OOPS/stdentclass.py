class Student:
    pass

s1 = Student();
s1.name = "Harshit goyal"
print(s1.__dict__)
s2 = Student()
s2.name = "HArshit"
s2.roll = 12
print(s2.__dict__)


# hasattr
print(hasattr(s1, "name"))
print(hasattr(s1, "roll"))


# getattr
print(getattr(s1, 'name'))
print(getattr(s1, 'roll', 'roll no not found'))

delattr(s1, 'name')
print(s1.__dict__)


class Student1:
    passingPercentage = 33
    def getStdentDeatils(self):
        self.name = "Harshit"
        self.percentage = 97

    def ispassed(self):
        if self.percentage > Student1.passingPercentage:
            print(self.name , " you are passed with ", self.percentage)
    
    @staticmethod
    def welcomeNote():
        print("Welcome to school ")

c1 = Student1()
c1.getStdentDeatils()
c1.ispassed() 
c1.welcomeNote()