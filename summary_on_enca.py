# class Student:
#     def __init__(self, name, gpa):
#         self.name = name        # public
#         self.__gpa = gpa        # protected
#         self._age = 20           # private
        
# s1 = Student("Tonny", 3.5)

# print(s1.name)      # public
# print(s1.__gpa)     # private
# print(s1._age)      # protect



# class Student:
#     def __int__(self, name, gpa):
#         self.__name = name
#         self.__gpa = gpa
    
#     def get_gpa(self):
#         return self.__gpa
    
#     def set_gpa(self, value):
#         if 0.0 <= value <= 5.0:
#             self.__gpa = value
#         else:
#             print("Invalid GPA value")
            
# s = Student("tonny", 3.5)

# print(s.get_gpa())
# s.set_gpa(9.0)



class Student:
    def __init__(self, name, gpa):
        self._gpa = gpa

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 5.0:
            self._gpa = value
        else:
            print("invalid GPA!")
     
S = Student(3.5, "tonny")
print(S.gpa)

S.gpa = 4.8 
S.gpa = 10





