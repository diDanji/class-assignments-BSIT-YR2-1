# # introdu
# fruits = ("apple", "banana", "cherry", "date")
# print(len(fruits))

# my_tuples = ("apple", "banana", "cherry", "date")
# print(len(my_tuples))

# music_genres = ("Love yours - J cole")
# print(len(music_genres))

# my_dict = {
#     "name": "Alice", 
#     "age": 30, 
#     "city": "New York"
#     }
# print(len(my_dict))


# class Car:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
    
#     def move(self):
#         print (f"{self.brand} {self.model} is moving!")
        
# class Boat:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
    
#     def move(self):
#         print(f"{self.model} {self.brand} is sailing badly!")
        
# class Plane:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
        
#     def move(self):
#         print(f"{self.model} {self.brand} is flying away!")
        
# car1 = Car("GLE_250", "Mercedes")
# boat1 = Boat("Speedster", "Yamaha")
# plane1 = Plane("Boeing 747", "Boeing") 

# for y in (car1, boat1, plane1):
#     y.move()


# class Vehicle:
#     def __init__(self, model, brand):
#         self.model = model
#         self.brand = brand
        
#     def move(self):
#         print (f"{self.brand} {self.model} is moving!")
        
# class Car(Vehicle):
#     pass

# class Boat(Vehicle):
#     def: move(self):
#         print(f"{self.model} {self.brand} is sailing badly!")
        
# class Plane(Vehicle):
#     def move(self):
#         print(f"{self.model} {self.brand} is flying away!")
        
# car1 = Car("GLE_250", "Mercedes")
# boat1 = Boat("Speedster", "Yamaha")
# plane1 = Plane("Boeing 747", "Boeing")

# for y in(car1, boat1, plane1):
#     print(y.model)
#     print(y.brand)
    
#     y.move()


# class NUP:
#     def __init__(self, candidate, slogan):
#         self.candidate = candidate
#         self.slogan = slogan 
        
#     def aspire(self):
#         print(f'{self.candidate} is our candidate for presidency come 2026 with the slogan "{self.slogan}"')
        
# class NRM:
#     def __init__(self, candidate, slogan):
#         self.candidate = candidate
#         self.slogan = slogan
    
#     def aspire(self):
#         print(f'{self.candidate} is our candidate for presidency come 2026 with the slogan "{self.slogan}"')
        
# class FDC:
#     def __init__(self, candidate, slogan):
#         self.candidate = candidate
#         self.slogan = slogan
    
#     def aspire(self):
#         print(f'{self.candidate} is our candidate for presidency come 2026 with the slogan "{self.slogan}"')
        
# p1 = NUP("Robert kyagulanyi . S.", "Building the Uganda we need")
# p2 = NRM("Yoweri .K. Museveni", "Protecting the gains")
# p3 = FDC("Nandala Mafabi", "fixing the economy and Money in our pockets")

# for politics in (p1,p2,p3):
#     politics.aspire()

    
    
    
# class BankAcccount:
#             def __init__(self, balance):
#                 self.balance = balance
                
#             def deposit(self, amount):
#                 self.balance += amount
                
#             def withdraw(self, amount):
#                 self.balance  -= amount
                
        
# account = BankAcccount(1000)
# account.deposit(500)
# account.withdraw(200)



class Employee:
    """
    Base class representing an employee.
    
    This program demonstrates *polymorphism* using the 'get_salary()' method.
    Each subclass of Employee overrides 'get_salary()' differently depending
    on the type of employee, but all share the same interface.
    When we call 'get_salary()' on each object in the list, Python determines
    which version to run based on the actual object type — this is polymorphism.
    """
    
    def __init__(self, name):
        self.name = name

    def get_salary(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def get_salary(self):
        return self.hourly_rate * self.hours_worked


class Intern(Employee):
    def __init__(self, name, allowance):
        super().__init__(name)
        self.allowance = allowance

    def get_salary(self):
        return self.allowance



employees = [
    FullTimeEmployee("Tonny", 1500000),
    PartTimeEmployee("Amos", 20000, 60),
    Intern("Trinity", 300000)
]

for emp in employees:
    print(f"{emp.name} ({emp.__class__.__name__}) earns: {emp.get_salary()} UGX")

