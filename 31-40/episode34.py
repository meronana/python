#The underscore
#often ignored, multiple uses
#_Single
#__Double
#__Before
#After__
#__Both__


#_Single
#Skipping
for _ in range(5): #don't care what it is
    print('Hello')

#Test class
from person import *

#Before (Single)
#Internal use only called a week private
p = person()
p.setName('Bryan')
print(f'Weak private {p._name}')
p._name = 'NOOOO'
print(f'Weak private {p._name}') #internal is not for acessing outside the function

#Before(Double) ->Strong private - unable to access
#Internal use only, avoid confilct in subclass
#and tells python to rewrite the name (Mangling)
p = person()
p.work()
#p.__think()
#c = Child()
#c.testDouble()

#After (Any) 
class_ = person() #any type of class 명령어이므로 단독으로 이용 불가
print(class_)

#Before and after
#Considered special to Python, like the init and the amin fuction
p = person()
p.__call__() #변형 혹은 손상
