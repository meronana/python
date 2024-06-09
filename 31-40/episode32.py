#Multiple Inheritance

#Inherit from multiple classes at the same time

#Vehical class
class Vehical:
    speed = 0
    def drive(self,speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')

#Freezer class
class Freezer:
    temp = 0
    def freeze(self, temp):
        self.temp = temp
        print('Freezing')
    
    def display(self):
        print(f'Freezing at {self.temp}')


#FreezerTruck class
class FreezerTruck(Vehical,Freezer): #Method Resolution Order(MRO)
    def display(self):
        print(f'Is a Freezer: {issubclass(FreezerTruck,Freezer)}') #first chack, against check
        print(f'Is a Freezer: {issubclass(FreezerTruck,Vehical)}')

        #super(Vehical,self).display() #Works because of MRO
        #super(Freezer,self).display()

        Freezer.display(self)
        Vehical.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-30)
print('-'*20)
t.display()
