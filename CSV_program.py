
def menue():
    print("Wynierz opcje")
    print("1.Dodaj pozycje")
    print("2.Usun pozycje")
    print("3.Zakoncz")

def show_data(position, title, grade, year):
    for i in range(0, len(position)):
        print("|",position[i],"|",title[i],"|",grade[i],"|",year[i])

def delete_movie(i):
    del title[i]
    del grade[i]
    del year[i]
    position.pop()

def add_movie():
    position.append(str(len(position)))
    title.append(str(input("Podaj tytuł filmu: ")))
    grade.append(str(input("Podaj ocene filmu: ")))
    year.append(str(input("Podaj rok filmu  ")))

position=[]
title=[]
grade=[]
year=[]

with open("movie_base.csv", "r") as file:
    lines = file.readlines()
    for i in lines:
        position.append(i.split(",")[0])
        title.append(i.split(",")[1])
        grade.append(i.split(",")[2])
        year.append(i.split(",")[3].strip("\n"))
file.close()

show_data(position,title,grade,year)

menue()
answear=int(input("Podaj odpowiedz"))

if answear==1:
     add_movie()
elif answear==2:
    pos=int(input("Podaj pozycje "))
    delete_movie(pos)
elif answear==3:
    print("Zakonczono program")
else:
    print("Nie ma takiej opcji")

new_data_row = []
for i in range(0, len(position)):
    new_data_row.append(position[i] + "," + title[i] + "," + grade[i] + "," + year[i])

new_data = "\n".join(new_data_row)

with open("movie_base.csv", "w") as file:
    file.write(new_data)
file.close()