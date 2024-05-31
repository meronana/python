#Function and scope

#Lexical scoping, Static scope
#range of functionality of carables
#Scope can be nested in other

#This is the global scope
name = 'Bryan Cairns'

#Functions can access the global scope
def test1():
    print(f'My name is {name}')

test1()

#Global scope can not access function scope 
x = 10
def test2():
    x = 50
    print(f'Function scope {x}')
test2()
print(f'Global scope {x}')

#Global > function > statement
x = 15
print(f'Global x: {x}')

def test3():
    x = 0
    print(f'Function x: {x}')
    for i in range(3):
        x+= 1
        y = x*i
        print(f'Statement x: {x}')
        print(f'Statement y: {y}')
    print(f'Funtional x: {x}')
    print(f'Funtional y: {y}') #This could be an issue!

test3()
print(f'Global x: {x}')
#print(f'Global y: {y}') #y is functional 

#Functions do not share scope with each other
def cats():
    z = 1 #Only exist in this function
    
def dogs():
    z = 3 #Only exist in this function

#Functions can return values
def number(steps):
    l = range(1,23, steps)
    for i in l:
        print(i)
    return l

def lotto():
    z = number(3)
    for x in z:
        print(f'Lucky number {x}')

lotto()
