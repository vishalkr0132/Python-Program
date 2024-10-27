col = int(input('Enter the number of columns: '))
row = int(input('Enter the number of rows: '))

print('Enter the elements of the matrix 1:')
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print('Matrix 1:')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=' ')
    print()
    
# Code for diagonal sum of matrix 1

print('Diagonal sum of Matrix 1:', sum(matrix1[i][i] for i in range(row)))