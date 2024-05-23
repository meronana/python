#Basic String Operations
str = "Hello World , this is a string!"

print(len(str)) #get the length
print(str * 3) #repeat 3 times
print(str.replace('Hello','Hola')) #replace  -> puthon have function to string
print(str.split(',')) #split  -> divide into two string
print(str.startswith('H')) #start with -> true or false
print(str.endswith('!')) #Ends with
print(str.upper()) #대문자로 upper
print(str.lower()) #소문자로 lower
print(str.capitalize()) 


#Slicing - or getting a sub string -> 특정부분만 도려냄
print(str[0:5]) # [0:5] - starting position : end position
print(str[6:]) # from 6 till the end
print(str[-7:]) # get from the backward 뒤에서부터 읽음

#index - the position
l = ','
c = str.find(l) # index of l, -1 if not found
print(f'Find returned {c}')

i = str.index(l)
print(f'Find returned {i}') 

x = str[:i]
print(x)