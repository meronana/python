#Class Inheritance

#Feline class
class Feline:
    def __init__(self,name):
        self.name = name #not define name
        print('Creating a feline')

    def meow(self):  #defining what it can do
        print(f'{self.name} meow')
    
    def setName(self,name):
        print(f'{self} setting name: {name}')
        self.name = name

#Lion class
class Lion(Feline):
    def roar(self):
        print( f'{self.name} roar')
#Tiger class
class Tiger(Feline):
    #override the constructor is a bad example
    def __init__(self): #constructor -> never to override the constructor 
        #Super alow os to access the parent 
        #if we forget this we will have a bad time later
        super().__init__('No Name') #make sure of controll
        print('Creating a tiger')
    def stalk(self):
        #have to make sure name is in the parent
        #this is considered LBYL(look before you leap)
        #here we are dynamically adding the attribute

        #If we did not init the super we will have to be careful
        #If not hasattr(self,'name'): super().setName('No Name')
        print(f'{self.name} : stalking')
    
    def rename(self,name):
        super().setName(name)
        

c = Feline('kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow()
l.roar()

t = Tiger()
print(t)
t.stalk
t.rename('Tony')
t.meow()
