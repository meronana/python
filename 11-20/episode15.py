#Intro to Function
#bloc of code which only runs when it is called
#Can pass data, known as a parameters(or argument) into a function

#Function parameter
#Function argument

#return data as result

#Define function
def test():
    print('This is a function')

#Defina a function with parameters and return a value
def sqft(w,h):
    v = w * h
    return v

#Call a function
test()

#Call a funtion multiple times
for x in range(4):
    test()

#Call a function with parameters
x = sqft(12,8)
print(f'The sqft is {x}')


