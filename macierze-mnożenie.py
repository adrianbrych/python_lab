import random


cols,rows=(8,8)


matrix_one=[[random.randint(1,100) for i in range(rows)] for i in range(cols)]
matrix_two=[[random.randint(1,100) for i in range(rows)] for i in range(cols)]
matrix_end=[[0 for i in range(rows)] for i in range(cols)]


for i in range(0,len(matrix_one)):
    for j in range(0,len(matrix_one)):
        for k in range(0, len(matrix_one)):
             matrix_end[i][j]=matrix_end[i][j]+ matrix_one[i][k]*matrix_two[k][j]


print(matrix_one)
print(matrix_two)
print(matrix_end)