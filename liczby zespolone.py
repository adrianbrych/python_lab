import math

class liczby_zespolone:

    def __init__(self,czesc_urojona,czesc_rzeczywista):
        self.czesc_rzeczywista=czesc_rzeczywista
        self.czesc_urojona=czesc_urojona
    def wyswietl(self):
        print("Liczba zespolona:",self.czesc_rzeczywista,"+",self.czesc_urojona,"j")
    def get_real(self):
        print("Podaj czesc rzeczywista")
        self.czesc_rzeczywista=input()
    def get_imag(self):
        print("Podaj czesc urojona")
        self.czesc_urojona=input()
    def dodaj(self):
        re=input("Podaj czesc rzeczywista ktora chcesz dodac")
        im=input("Podaj czesc urojona ktora chcesz dodac")
        x_re=float(self.czesc_rzeczywista)+float(re)
        x_im=float(self.czesc_urojona)+float(im)
        print("Suma wynosi",x_re," + ",x_im,"j")
    def odejmij(self):
        re = input("Podaj czesc rzeczywista ktora chcesz odjac")
        im = input("Podaj czesc urojona ktora chcesz odjac")
        x_re = float(self.czesc_rzeczywista) - float(re)
        x_im = float(self.czesc_urojona) - float(im)
        print("Suma wynosi", x_re, " + ", x_im, "j")
    def mnozenie(self):
        re = input("Podaj czesc rzeczywista ktora chcesz pomnozyc")
        im = input("Podaj czesc urojona ktora chcesz pomnozyc")
        x_re=float(self.czesc_rzeczywista)*float(re)-float(self.czesc_urojona)*float(im)
        x_im=float(self.czesc_rzeczywista)*float(im)+float(self.czesc_urojona)*float(re)
        print("Wynik po przemnozeniu:",x_re,"+",x_im,"j")
    def sprzezenie(self):
        print("Liczba po sprzezeniu to ",self.czesc_rzeczywista,"+", -float(self.czesc_urojona),"j")
    def modul(self):
        mod=math.sqrt(float(self.czesc_rzeczywista)**2+float(self.czesc_urojona)**2)
        print("Modul wynosi",mod)
    def faza(self):
        mod = math.sqrt(float(self.czesc_rzeczywista)**2 + float(self.czesc_urojona)**2)
        cosinus=float(self.czesc_rzeczywista)/mod
        phase=math.acos(cosinus)
        print("Faza wynosi:",phase)

    def GUI(self):
        print("Prosty kalkulator")
        print("1.Dodadaj")
        print("2.Odejmij")
        print("3.Mnozenie")
        print("4.Sprzezenie")
        print("5.Modul")
        print("6.Faza")

        ans=input(print("Wybierz:"))
        if ans==1:
            obiekt=liczby_zespolone(0,0)
            obiekt.get_real()
            obiekt.get_imag()
            obiekt.dodaj()
        elif ans==2:
            obiekt = liczby_zespolone(0, 0)
            obiekt.get_real()
            obiekt.get_imag()
            obiekt.odejmij()
        elif ans==3:
            obiekt = liczby_zespolone(0, 0)
            obiekt.get_real()
            obiekt.get_imag()
            obiekt.mnozenie()
        elif ans==4:
            obiekt = liczby_zespolone(0, 0)
            obiekt.get_real()
            obiekt.get_imag()
            obiekt.sprzezenie()
        elif ans==5:
            obiekt = liczby_zespolone(0, 0)
            obiekt.get_real()
            obiekt.get_imag()
            obiekt.modul()
        elif ans==6:
            obiekt = liczby_zespolone(0, 0)
            obiekt.get_real()
            obiekt.get_imag()
            obiekt.faza()
        else:
            print("Nie ma takiej opcji")





calc=liczby_zespolone(0,0)
calc.GUI()


