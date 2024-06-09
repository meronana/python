#iterators 
#Making counting easy

t = (1,2,3,4)

for x in t:
    print(x)

#Iter Basics
#List, tuples, Dictionaries and sets are all iterable objects.
#They are iterable containers which you can get an iterator form.
people = ['Bryan', 'Tammy', 'Rango']
i = iter(people)
print(i) #which tells how python to go through it
print(next(i))
print(next(i))
print(next(i))
#print(next(i)) #StopIteration - tells when it is done

#Iterable class
import random
class Lotto:
    def __init__(self):
        self._max = 5

    def __iter__(self):
        #The yeild statement suspends function's execution
        #and send a value back to each caller, but retains enough
        #state to enable function to resume where it is left off
        for _ in range(self._max):
            yield random.randrange(0,100)

    def setMax(self,value):
        self._max = value

print('-'*20)
lotto = Lotto()
lotto.setMax(10)

for x in lotto:
    print(x)

print('-'*20)


