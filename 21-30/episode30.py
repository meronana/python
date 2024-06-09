#introduction to classes

#OOP - object oriented programming
#Blue prints for creating objects
#Classes are a big topic
#We will cover this over multiple videos

#Create the class

#import the class
import cat
from cat import Cat #get Class Cat from file cat.py

#Use the class
def test(): #we don't have to put self if it is global
    b = Cat('KitKat',1,'brown') #Self -> not needed
    c = Cat('Ohtello',6,'black')
    print(b)
    print(c)
    b.description()
    c.description()

    c.meow()
    b.sleep()
    c.hungry()
    b.eat()

if __name__ == "__main__":
    x = Cat('test')
    print(x)
    test()

