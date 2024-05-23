#List [] -> ordered collection of data
# don't have to have sertan data type 

#create list
x = ['Bryan', 'Cairns', 46] # can mix data types
print(f'List: {x}') #Print the list
print(f'LenL {len(x)}') #Print the len

#Index and positioning - zero based
print(f'Zero: {x[0]}') #Firt item is zero
print(f'Slice: {x[1:2]}') #Slice the list

#Adding Items - append, insert
x.append('Pizza')
x.append('Beer') #just putting at the end
x.insert(1,'Cats') #put in sprcific position
print(f'List:{x}')

#Removing items - remove, pop, delete
x.remove('Cats') #Remove the item
print(f'List:{x}')

i = x.index('Pizza') #will raise error if not found
print(f'Food:{x.pop(i)}') #pop off-> 분리해냄-> list에는 없음
print(f'List:{x}')  #remove and return the item

i = x.index('Beer')
del x[i] #Delete without returning it
print(f'List:{x}')

#Extending - add elements from another list
y = ['Cats', 'Dogs', 'Birds']
x.extend(y) 
print(f'Extend:{x}')

#Sort - sort, reverse
x.remove(46)
x.sort()  #알파벳 순데로 나열 - if other type exist->Error!
print(f'Sort:{x}')
x.reverse()
print(f'Reverse:{x}') #반대로 나열

#making a copy
y = x.copy() #Copies the elements into a new list
y.reverse()
y.append('Apples')
print(f'Original:{x}')
print(f'New:{y}')

#Delete the whole thing
del y
#print(y) #y doesn't exist now

#Clearing elements
x.clear() #no elements in it
print(f'Cleared: {x}') 
print(f'Len: {len(x)}')

#Lists can contain other lists [[],[],[]]
x = []
y = [1,2,3]
z = ['Bryan', 'Cairns']
x.append(y)
x.insert(0,z)

print(f'List: {x}') 
print(f'Len: {len(x)}')
print(f'0:{x[0][0]}') 
print(f'1:{x[1][1]}') 

#changing items - positional
x = [1,2,3,4,5]
x[2] = 'TEST'
print(x)





