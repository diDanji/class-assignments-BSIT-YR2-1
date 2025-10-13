class Car:
    #the __int__method is automatically called when you create a new object
    def __init__(self, speed, color):   
     print(speed)
     print(color)
    
    #store the values inside the object (encapsulation)
     self.__color = color
     self.__speed = speed
        
    #show that the constructor is called
    print("the __int__is called")

ford = Car(100, "red")
mustang = Car(200, "blue")

ford.speed = 300

print(ford.color)
print(ford.speed)