#Funtion in deph

#No arguments
def test():
    print('Normal function')

print('\r\n---------No arguments')
test()

#Postional and Keyword Arguments
def message(name,msg,age):
    print(f'Hello {name},{msg},you are {age} years old')
print('\r\n---------Positional and Keyword Arguments')
message('Bryan','good morning',22) #Positional
message('Bryan',22,'good morning') #Positional(wrong order)
message(msg='Good morning',age=22,name='Bryan') #Keywords
message('Bryan',msg='Good morning',age=22) #Keywords can be mixed

#Internal function - func inside func
def counter():
    def display(count = 0):
        print(f'Internal:{count}')
    for x in range(5): display(x)

print('\r\n---------Internal functions')
counter()
#display(15) is not defined

#*args = positional variable length arguments
def multiple(*args):
    z = 1
    for num in args:
        print(f'Num = {num}')
        z *= num
    print(f'Multiply: {z}')

print('\r\n---------*args')
multiple(1,2,3) #Can figure how many things are in it

# **kwargs is used to pass a keyworded variable length arguments
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys():print(f'{k} = {person[k]}')
    display('name')
    display('age')
    display('pet')
    display('kdjfa ')

print('\r\n---------**kwargs)')
profile(name = 'Bryan', age = 46) #coverting it into dictionary
profile(name = 'Bryan', age = 46,pet = 'Cat')
profile(name = 'Bryan', age = 46,pet = 'Cat',food = 'pizza')

#Lamda function(anaonymous function)
print('\r\n---------Lamda)')

#normal
def makesqft(width=0, height=0):
    return width*height
print(makesqft(width=10,height=8))
print(makesqft(15,8))

#Lamda
#z = lamda x: x*y
sqft = lambda width = 0,height = 0: width*height
print(makesqft(width=10,height=8))
print(makesqft(15,8))