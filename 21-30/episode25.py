#Working with binary files
#binary -> 
#download hex editor

#imports
import random #module that make random numbers
import operator #compare two list

#Create random bytes
def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0,255)) #0 to 255 chose random num
    return bytes

def displayBytes(bytes):
    print("-"*20) #take this 20times
    for index, item in enumerate(bytes,start=1):
        print(f'{index} = {item} ({hex(item)})')
    print("-"*20)

b = randomBytes(10)
displayBytes(b)

#Write bytes
def writebytes(filename, bytes):
    with open(filename,'wb') as file: #with some func as file - wb = w bites?
        for i in bytes:
            file.write(i.to_bytes(1,byteorder = 'big'))
        # file.close() - not need because with is destroying it 
    
#Read bytes
def readBytes(filename):
    bytes = []
    with open(filename,'rb') as file : #read bytes
        while True:
            b = file.read(1) #reading 1 byte
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big')) #byte to int
    return bytes

#See it in action

#create the random bytes
outbytes = randomBytes(10)
displayBytes(outbytes)

#Write bytes
filename = 'test.txt'
writebytes(filename,outbytes)

#Read bytes
inbytes = readBytes(filename)
displayBytes(inbytes)
print(f'match: {operator.eq(outbytes,inbytes)}')

