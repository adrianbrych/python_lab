import random


row,cols=(128,128)


matrix_one=[[random.randint(1,100) for i in range(cols)] for i in range(row)]
matrix_two=[[random.randint(1,100) for i in range(cols)] for i in range(row)]
matrix_end=[[0 for i in range(cols)] for i in range(row)]




for i in range(0,len(matrix_one)):
    for j in range(0, len(matrix_one)):
        matrix_end[i][j]=matrix_one[i][j]+matrix_two[i][j]


print(matrix_one)
print(matrix_two)
print(matrix_end)
