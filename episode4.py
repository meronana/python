#number - int float complex
#int
iVal = 34
print(f'iVal = {iVal}')

#float
fVal = 3.14 
print(f'fVal = {fVal}')
import sys  #make it able to use other peoples code
print(sys.float_info)

#complex - complex([real[,imag]]) -> other complex types
cVal = 3 +6j
print(f'cVal = {cVal}')
cVal = complex(5,3)
print(f'real = {cVal.real},imag = {cVal.imag}')  

#basic numerical operations

x = 3
print(f'x = {x}')

y = x + 3 #add
print(f'add = {y}')


y = x - 1 #subtract
print(f'subtract = {y}')


y = x * 6.946 #multiply  #multipy by float -> but python does it on its own
print(f'multiply = {y}')


y = x / 0.5 #divide  -> not always but for now
print(f'divide = {y}')


y = x ** 2 #power
print(f'pow = {y}')


y = x % 2.5 #remain
print(f'add = {y}')