# # class Me:
# #     def greet(self):
# #         return "Hello from me"
# # class Emma(Me):
# #     def greet(self):
# #         return "Hello from Emma"
    
# # class Ann(Me):
# #     def greet(self):
# #         return "Hello from Ann"
    
# # class John(Emma, Ann):
# #     pass

# # people = [John()] 

# # for people in people:
# #     print(people.greet())





# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def intro(self):
#         print (f"Hello, my name is {self.name}.")
        
# class Student(Person):
#     def Regno(self):
#         print (f"Hello, this is my regno.")
        
# stu = Student("Tonny")
# stu.intro()
# stu.Regno()


# class Vehicle:
#     def __init__(self, brand):
#        self.brand = brand
    
#     def move(self):
#         print (f'{self.brand} is raving')
        
        
# class Car(Vehicle):
#     def honk(self):
#         print(f'{self.brand} is beep beep')

# v = Car('Toyota')

# v.move()
# v.honk()



# class Account():
#     def __init__(self, balance):
#         self.balance = balance 
        
#     def deposit(self, amount):
#         self.deposit = self.balance + amount
        
# class SavingsAccount(Account):
#     def interest(self, rate):
#         self.balance = self.balance * (1 + rate)

# acc = SavingsAccount(2000)
# acc.deposit(200)
# acc.interest(0.01)


# print('this is your balance:', acc.balance)
        
        

# class Shape:
#     def area(self):
#         print ('Area is 0')
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width 
#         self.height = height
        
#     def area(self):
#         print('Area of a rectangle:', self.height * self.width)
        
# rect = Rectangle(67, 4)
# rect.area()





# class Animal:
#    def speak(self):
#          print("Animal speaks")
         
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
        
# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")  
        

# for loop in [Cat(), Dog()]:
#     loop.speak()




class Shape:
    def area(self):
        print ('Area is 0')
        
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        print('Area of a rectangle:', self.length * self.width)
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        print('Area of a circle:', 3.14 * self.radius * self.radius)


items = [Rectangle(5,6), Circle(5)]

for y in items:
    y.area()
