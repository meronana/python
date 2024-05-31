
#Walrus operator and global
#Added in Python 3.8 looks like :=

#Assighn a variable from an exression
#Must have the right version

#Commin issues ( )
#y := len('hello') #invalid syntax
(y := len('hello')) #valid but not recommended
print(y) 

people = ['Bryan', 'Tammy','Rango']
if n := len(people) <= 3: print(n) #walrus -> without ()
if (n := len(people)) <= 3: print(n)

#Simple example
lines = []

def canAdd(max = 5):
    global lines #allow is ise the global line
    if allowed := (count := len(lines)) < max :#define the value # := usually define the value without defining it?
        print(f'You can enter {max - count} more')
    return allowed #조건문에 함수를 정의 하지 않은 상태로 넣을 수 있음??

while canAdd():
    lines.append(l := input('Enter a line:'))

print(f'You entered : {lines}')
