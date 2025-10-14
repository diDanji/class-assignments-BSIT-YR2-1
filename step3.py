class Person:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        return f"Hello, my name is {self.name}"   

#using polymorphism to override the introduce method in the child classes
class Student(Person):
    def __init__(self, name, program, year):
        super().__init__(name)
        self.program = program
        self.year = year
    
    def introduce(self):
        return super().introduce() + f", I am studying {self.program} in year {self.year}."
    
class Lecturer(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department
        
    def introduce(self):
        return super().introduce() + f", I am a lecturer in the {self.department} department."
    
p = Person("Malice")
t = Lecturer("Dr. Sam", "Computer Science")
s = Student("Tonny", "BSIT", 2)

print(p.introduce())
print(t.introduce())
print(s.introduce())

