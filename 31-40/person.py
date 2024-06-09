#Test class
#from typing import Any


class person:
    #weak Private - internal to the class
    _name = 'No name'
    def setName(self, name):
        self._name = name 
        print(f'Name set to {self._name}')
    
    #Strong private
    def __think(self):
        print('Thinking to my self')
    def work(self):
        self.__think()

    #Before and After
    def __init__(self): #internal to class also not to other inherited classes
        print('Constructor')
    
    def __call__(self):
        print('call someone')

class Child(person):
    def testDouble(self):
        self.__think(self)