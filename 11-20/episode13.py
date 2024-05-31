#for loop and range
 
#For loop in lists, tuples, sets
l = [1,2,3,4] #List
t = (1,2,3,4) #Tuple
s = {1,2,3,4} #Set

for i in l:
    print(f'i = {i}')

#For loop on dictionary
x = dict(Brayan = 46, Tammy = 48, Heather = 28, Chris = 30)
print(x)

for k in x.keys():
    print(f'Keys: {k} = {x[k]}')

for k,v in x.items():
    print(f'Keys: {k} = {v}') #k = keys v = value

#Range
x = range(5)
print(x)
for i in x:
    print(f'Range : {i}') 

#Range start, stop and step
x = range(5,21,3) #step - how many num between those steps

print(x)
for i in x:
    print(f'Stepped : {i}') #not include when stopped

