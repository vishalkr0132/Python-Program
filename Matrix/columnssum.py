col = int(input('Enter the number of columns: '))
row = int(input('Enter the number of rows: '))

print('Enter the elements of the matrix 1:')
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print('Matrix 1:')
for i in range(row):
    for j in range(col):
        print(matrix1[i][j], end=' ')
    print()
    
# Code for  sum based on used input columns of matrix 1
col_no = int(input('Enter the columns to be used for sum: '))
cnt = 0
for i in range(len(matrix1)):
    for j in range(col_no):
        cnt += matrix1[i][j]

print(f'Sum of column is {cnt}')