#what are String? 
for x in 'hello': 
    print(f'{x} = {ord(x)}')
# turns string into aski

# How to make a string
first = "Bryan"
last = 'Cairns' #either way is possible
print(first + ' ' + last)
print(f'Hello my name is {first} {last}')

hers = "Heather's" #when like this if using single quote it might be confusing
print(hers)

#under the hood - Unicode(UTF8)
s1 = chr(72)
s2 = chr(105)
print(s1+s2)
print(chr(8710)) #way beyond aski -> math symbols

#escape characters - start with slash \
print(f'Hello{chr(13) + chr(10)} World')
print(f'Hello\r\nWorld')
strTest = "Hello\tWorld"
print(strTest)

hers = 'Heater\'s' # if putting \ befere it every thing is ok
print(hers)

quote = "Then he said \"hello\" to me"
print(quote)

#Must format strings to avoid errors
name = "Bryan"
age = 46
#print(name + ' ' + age) -> errror!!
print(f'My name is {name} I am {age} years old')
print("My name is %s, I am %i years old!" %(name, age))