import random

a=random.randint(1,10)
cols,rows=(a,a)
c=[[random.randint(1,10) for i in range(rows)] for i in range(cols)]


print(c)

def zerowanie(c):
    n = len(c)
    for i in range(0, n):
        maxEl = abs(c[i][i])

        maxRow = i
        for k in range(i + 1, n):
            if abs(c[k][i]) > maxEl:
                maxEl = abs(c[k][i])
                maxRow = k

        for k in range(i,n):
            tmp = c[maxRow][k]
            c[maxRow][k] = c[i][k]
            c[i][k] = tmp

        for k in range(i + 1,n):
            d = -c[k][i] / c[i][i]
            for j in range(i, n ):
                if i == j:
                    c[k][j] = 0
                else:
                    c[k][j] += d * c[i][j]

zerowanie(c)

print(c)
det=1

for i in range(0,len(c)):
    det*=c[i][i]


print("Wyznacznik ",det)