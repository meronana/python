#Import madness

#__init__
#what is it, why do we need it

#make a sub folder
#add the files/codee

#Imports
from sub import * #import everything from sub
from sub import test as code 

#Call the code
def main():
    print('This is the main function')
    doTest()
    code.doTest()

if __name__ == "__main__":
    main()