from datetime import date
class Student:
    def __init__(self, name, age=15, percentage=80):
        self.name= name
        self.age = age;
        self.percentage = percentage

    @classmethod
    def getbirthdate(cls, name, year, percentage):
        return cls(name,date.today().year-year, percentage)


    def getStudentDetails(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("percentage : ", self.percentage)

    @staticmethod
    def welcomeNote():
        print("Welcome to this school ")


s1= Student("harshit")

s1 =Student.getbirthdate("Harshit", 1999, 81)
s1.getStudentDetails()