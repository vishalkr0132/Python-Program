col = int(input('Enter the number of columns: '))
row = int(input('Enter the number of rows: '))

print('Enter the elements of the matrix 1:')
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print('Matrix 1:')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=' ')
    print()
    
print('Enter the elements of the matrix 2:')
matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print('Matrix 2:')
for i in range(row):
    for j in range(col):
        print(matrix2[i][j], end = " ")
    print()
    
result = [[0 for i in range(col)] for j in range(row)]

#code for adding two matrices
for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        
print('Result of addition of two matrix :')
for i in range(col):
    for j in range(row):
        print(result[i][j], end = " ")
    print()