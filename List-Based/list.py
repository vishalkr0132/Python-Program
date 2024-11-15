l = [2, 5, 3, 8, 4]

if len(l) < 2:
    print('List must be at least two elements')
    
largest = 0
second_largest = 0
for i in l:
    if i > largest:
        second_largest = largest
        largest = i
    # elif i > second_largest and i != largest:
    #     second_largest = i
        
print(second_largest)
    