#Sets {}
#Set contains unordered, unique, immutable data
#which mean have no order and change it. only one no multible, 

#Creating a set
s = {1,2,2,2,3,4,5}
print(s)  #if there is multiple numbers of it it only print one of it

l = ['Bryand', 'Cairns',46]
s = set(l) # determines the position as it does
print(l) 

#Adding items
s.add('Hello')
s.update([1,2,3,'Hello'])
print(s)

#Removing items
s.discard('Hello') #will not throw error
s.remove(1) #will throw error
v = s.pop() #can't define which one to remove-> random
print(s)

#can not change items - remove and add
#s[0] = 'A'  #error -> no order
#print(s[0]) #indexing doesn't happen too
print(3 in s)
s.remove(3)
s.add(12)
print(s)

x = set('abcd')
y = set('cdefg')

s = x.union(y) #all element in either set
print(f'Union {s}')

s = x.intersection(y) #get all eliments are in all set 공통점
print(f'intersection {s}')

s = x.difference(y) #다른점
print(f'difference {s}')

s = x.symmetric_difference(y) #all the elelments that are in one of the sets
print(f'Symmetric {s}')



