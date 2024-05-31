#Dictionary indexed by keys 
#{k:v,k:v}
#which can be any immutable type -> cannot be changes

#Create a dictionary
d = {'Pet':'dog','Age':5,'Name':'spot'}
print(d)
d = dict(pet = 'dog', age = 5, name = 'spot')
print(d)

#Get keys and values
print(f'Items: {d.items()}')
print(f'Keys: {d.keys()}')
print(f'Values: {d.values()}')

#Getting a value from the key
print(f'Name: {d["name"]}') #don't have key named )
# only use ""in key.
#print(f'Test: {d["bla"]}') #if key is not found it will throw error

#Add an Item
d['trick'] = 'sit'
print(d)
d['trick'] = 'roll over' #if key exist it will change the value
print(d)

#Removing a item
del d['trick']
print(d)

#Treiview of what come

#Test for existing
if 'name' in d:
    #Code
    print(d['name'])
#Looping
for key in d.keys():
    print(f'{key} = {d[key]}')
