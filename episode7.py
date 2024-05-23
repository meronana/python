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






