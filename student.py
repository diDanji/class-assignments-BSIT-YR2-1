#encapsulation in python
# use of private, protected and public attributes
# public attributes can be accessed from outside the class  
# protected attributes can be accessed from within the class and its subclasses
# private attributes can only be accessed from within the class

class Student:
    def _init_(self, name):
        self.name = name        # public
        self._gpa = 3.5         # protected
        self._password = "1234" # private
        
student1 = Student("Tonny")
print(student1.name)