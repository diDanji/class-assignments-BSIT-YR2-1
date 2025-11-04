class Gadgets:
    def start(self,):
        print("Gadget started")

class Phone(Gadgets):
    def start(self,):
        print("hello Andriod")
        
class Laptop(Gadgets):
    def start(self):
        print("its a thinkpad...")
        
class Watch(Gadgets):
    def start(self):
        print("time is ticking...")

devices = [Phone(), Laptop(), Watch()]

for gadget in devices:
    gadget.start()
    
###############################################################################################
###############################################################################################
    
class Camera():
    def take(self):
        print("taking pictures...")

class Wifi():
    def connect(self):
        print("connecting to wifi...")
        
        
        
class Smartphone(Phone, Camera, Wifi):
    def start(self):
        print("Smartphone is starting...")
        
class SmartPrinter(Gadgets, Wifi):
    def start(self):
        print("SmartPrinter is starting...")
        
devices = [Smartphone(), SmartPrinter()]
for gadget in devices:
    devices.start()
    if isinstance(devices, Wifi):
        devices.connect()
    if isinstance(devices, Camera):
        devices.take()
        
        ###need to revise this###
