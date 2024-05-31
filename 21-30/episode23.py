#Reading a Text file

#Get a filename
import os, sys

print(f'file : {__file__}')
print(f'Args : {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Reading: {sfile}') 

#Exists - how to determine if it exists
#sfile = 'nope.txt'
if not os.path.exists(sfile):
    print('File not found')
    exit(1)

#open the file
#FileNotFoundError : wrong file path
f = open(sfile,'r') #reading

#Read a line
line = f.readline()
print(line)

#Read number of letters
char = f.read(10)
print(f'Chars : *{char}*')

#Position - where we are in the file
print(f'Position: {f.tell()} of {os.stat(sfile).st_size}')  #where we are at the size of file

#Seek - move to a position in the file 
#Zero based
f.seek(0) #right pack to [0]

#Read all lines
print('------------------------------------')
for l in f.readlines():
    print(l.strip()) #remove extra space 

#Close the file
#Allows other applications to work with it
f.close()

