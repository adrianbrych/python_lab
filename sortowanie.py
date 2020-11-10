import random

tablica=[]


for i in range(0,50,1):
    x=random.randint(1,100)
    tablica.append(x)
    print(tablica[i])

print("Ilosc elementow w tablicy wynosi",len(tablica))

tablica2=tablica.copy()

# Sprawdzenie

tablica.sort()
tablica.reverse()
for i in range(0,50,1):
    print(tablica[i])

# Swoj algorytm

n=len(tablica2)


for j in range(0,n-1):
    for i in range(n-1):
        if tablica2[i]<tablica2[i+1]:
            swap=tablica2[i+1]
            tablica2[i+1]=tablica2[i]
            tablica2[i]=swap



print("@@@@@@@@@@@@@@@@@@@@@")

for i in range(0,50,1):
    print(tablica2[i])
