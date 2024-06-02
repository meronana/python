#Imports

#Lets make our code usble to other scripts
#This allows us to structure our code and simplify things
#We are really just scratching the surfaxe of the improt system

#Create the file
#in mycode.py

#Import as
import mycode as person #code which is outside the code
#if from oter file /.mycode
#turning entire file as argument

#Scope issues
#global name  ->if from module it's not defined thus it can't be called
#print(name)
print(person.name)

#Test the code
person.name = 'Bryan'
person.greet()
person.toFile('test.txt')

person.name = 'Tammy'
person.greet()

person.fromFile('test.txt')
person.greet()