import math

a=float(input(print("Podaj wspolczynnik a funkcji kwadratowej ")))
b=float(input(print("Podaj wspolczynnik b funkcji kwadratowej ")))
c=float(input(print("POdaj wspolczynnik c funkcji kwadratowej ")))
x=a-b
print("Funkcja :",a,"*x^2 +",b,"*x+",c )

delta=b*b-4*a*c

if delta<0:
    print("Nie ma miejsc zerowych")
elif delta==0:
    x0=-b/(2*a)
    print("Funkcja posiada jedno miejsce zerowe:",x0)
else:
    x1=-b+math.sqrt(delta)/(2*a)
    x2=-b-math.sqrt(delta)/(2*a)
    print("Funkcja posiada 2 miejsca zerowe")
    print(x1)
    print(x2)
    









