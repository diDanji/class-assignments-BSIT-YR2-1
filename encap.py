class Car:
    #the __int__method is automatically called when you create a new object
    def __init__(self, speed, color):   
    
    #store the values inside the object (encapsulation)
     self.color = color
     self.speed = speed
        
    #show that the constructor is called
    print("the __int__is called")

# ford = Car(100, "red")
# mustang = Car(200, "blue")

# ford.speed = 300

