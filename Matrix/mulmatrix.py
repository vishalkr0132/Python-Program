col = int(input("Enter the number of columns:"))
row = int(input("Enter the number of rows:"))

print("Enter the elements of the matrix 1 :")
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix 1:")
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=" ")
    print()

print("Enter the elements of the matrix 2 :")
matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print("matrix 2:")
for i in range(row):
    for j in range(col):
        print(matrix2[i][j], end = " ")
    print()

result = [[0 for i in range(col)] for j in range(row)]

#code for multiplication two matrices
for i in range(row):
    for j in range(col):
        for k in range(col):
            result[i][j] += matrix1[i][k] * matrix2[k][j]
            
print("Result of multiplication of two matrix :")
for i in range(row):
    for j in range(col):
        print(result[i][j], end = " ")
    print()
    
    
    
    col = int(input('Enter the number of columns: '))
row = int(input('Enter the number of rows: '))

# Input elements of matrix 1
print('Enter the elements of the matrix 1:')
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]

# Print matrix 1
print('Matrix 1:')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=' ')
    print()

# Code to sum elements of the specified column in matrix1
col_no = int(input('Enter the column number to be used for sum (0-indexed): '))

if 0 <= col_no < col:  # Ensure the input column is within the valid range
    total_sum = 0
    for i in range(row):
        total_sum += matrix1[i][col_no]  # Add elements from the specified column

    print(f'Sum of elements in column {col_no}: {total_sum}')
else:
    print('Invalid column number')
