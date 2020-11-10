import os

path="C:/Users/adria/PycharmProjects/pythonProject"

def listuj(katalog):
    print(katalog)
    lista_elementow = os.listdir(katalog)

    for element in lista_elementow:
        pelna_sciezka = os.path.join(katalog, element)

        if os.path.isdir(pelna_sciezka):
            listuj(pelna_sciezka)
        else:
            print(pelna_sciezka)


listuj(path)
