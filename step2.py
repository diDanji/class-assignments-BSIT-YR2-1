class Person:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        return f"Hello, my name is {self.name}"   

#explain the super() function
#super() function is used to call a method from a parent class
#it is used to access the parent class methods and properties
class Student(Person):
    def __init__(self, name, program, year):
        super().__init__(name)
        self.program = program
        self.year = year
    
class Lecturer(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
    
p = Person("Malice")
t = Lecturer("Dr. Sam", "Computer Science")
s = Student("Tonny", "BSIT", 2)

print(p.introduce())
print(t.introduce())
print(s.introduce())

