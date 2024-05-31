#Navigation folders

#Special note - ther ar always mutiple ways to do something
#Use what works for you

#Import a module - group of code someone made 
import os
d = os.getcwd() #get current working directory
print(f'Current: {d}') #current directory

#Change folders
os.chdir('..') #change directory #.. ->up two levels
print(f'Current: {os.getcwd()}') #current directory
os.chdir(d)
print(f'Current: {os.getcwd()}') #current directory

#ListDir
for f in os.listdir(): 
    print(f)   #files in directory
    print(f'Path: {os.path.abspath(f)}')
    if os.path.isdir(f): print(f'Dir: {f}')
    if os.path.isfile(f): print(f'Flie: {f}')
    if os.path.islink(f): print(f'Link: {f}')

#ScantDir - python 3.5
for e in os.scandir():
    print(e)
    print(f'Name: {e.name}')
    print(f'Path: {e.path}')
    if e.is_dir: print(f'Dir: {e.name}')
    if e.is_file: print(f'Flie: {e.name}')
    if e.is_symlink: print(f'Link: {e.name}')

#Glob - multiple ways
#Recursive scan -> get into the folder in and in

import glob
os.chdir('..')
dir = os.getcwd()

for filename in glob.glob(pathname= dir + '**/**', recursive= True):
    print(f'glob: {filename}')

for currentpath, folders, files in os.walk('.'):
    for file in files:
        print(f'wlak: {os.path.join(currentpath,file)}')


