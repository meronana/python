#Write a text file

import os

#simplfy mode usage
def toFile(filename,mode,data): 
    f = open(filename,mode)
    for i in range(5):
        f.write(str(i)+ ':' + data + '\r')
    #f.flush() #automatically called when file is closed
    f.close()

#Write will overwrite the entire file
def writeFile(filename):
    toFile(filename,'w','Hello World')

#Append will add to the file
def appendFile(filename):
    toFile(filename,'a','Hello again') 

#Read the file
def readFile(filename):
    if not os.path.exists(filename):
        print('File not found')
        return
    f = open(filename,'r')
    #for line in f.readlines():
    #    print(line)
    print(f.read())
    f.close()

    
#See it in action
myfile = 'hello.txt'
writeFile(myfile)
appendFile(myfile)
readFile(myfile)