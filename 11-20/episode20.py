#Global

#Gloval keyword which allows code to modify a variable
#outside of the current scope.
x = 1
def test():
    x = 6
    print(x)

test()
print(x)

#Global variable
counter = 0

#Scope issues
def count(max):
    #without global, python is confused
    global counter #define to use global variable
    counter += 1 #refferenced before assighnment
    if counter >= max: return False
    return True

limit = 5
for x in range(limit):
    b = count(limit)
    print(counter)

print('Done')

count(1)


