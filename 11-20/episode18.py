#Packing and Unpacking data

#Problem with *arg and **kwarg is we can not use lists and dictionaries
#instead we have to pack and unpack data

#Packing data
def pack(*nums):
    print(f'Packed : {nums}')
    for x in nums:
        print(f'packed: {x}')

pack(1,2,3)

#Unpacking data
def unpack(a,b,c):
    print('Unpack')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

num = [1,2,3]
unpack(*num)

#Dictionary issue
d = dict(name = 'Bryan', age = 36,pet = 'Cat')
print('Packing Dictionary')
pack(*d)
print('Unpacking Dictionary')
unpack(*d)

#Packing a dictionary
def packdict(**nums):
    print(f'nums = {nums}')
    for k in nums:
        print(f'Packed: {k} = {nums[k]}')
packdict(name = 'Bryan', age = 36,pet = 'Cat')

#Unpacking a dictionary
def unpackdict(name,age,pet):
    print('Unpacking a dictionary')
    print(f'Name = {name}')
    print(f'Age = {age}')
    print(f'Pet = {pet}')

d = dict(name = 'Bryan', age = 36,pet = 'Cat')
unpackdict(**d)