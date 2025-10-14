class Person:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        return f"Hello, my name is {self.name}"   

class Student(Person):
    pass
    
class Lecturer(Person):
    pass
    
p1 = Person("Malice")
t = Lecturer("Dr. Sam")
s = Student("Tonny")

print(p1.introduce())
print(t.introduce())
print(s.introduce())

