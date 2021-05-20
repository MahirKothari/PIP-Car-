class Car(object):
    def __init__(self,model,colour,company,speed):
        self.model = model
        self.colour = colour
        self.company = company
        self.speed = speed 
    def start(self):
        print('started')
    def stop(self):
        print('stopped')
    def accelerate(self):
        print('accelerated')
    def changeGear(self):
        print('changedGear')
tesla = Car("HybridTruck",'grey','tesla',280)
print(tesla.colour)
print(tesla.start())