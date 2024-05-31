#while loop
#completing code over and over until its done

x = 0
while x <10:
    x += 1 #increament x
    print(f'x = {x}')
print('Test 1 is done')

#pass
#x = 0
#while x < 10:
#    pass #take no action
#print('Test 2 is done')

#Continue and break
x = 0
while True: #Loop forever
    x += 1
    if x < 5:
        print(f'x < 5 {x}')
        continue
    print(f'Do somethong {x}')

    if x == 10:
        print(f'Exiting x = {x}')
        break
    
print('Complete')