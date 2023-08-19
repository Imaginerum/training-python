#importy

import datetime

#zmienne globalne (zamiast tworzyc zmienne globalne możesz wpisać zmienną w menu(() i potem
#podać do poszczegolnych funckji, jako argument)

pamietniczek = []

#potem funkcje

def dopisz():
    global pamietniczek
    wpis = input("Co tam do pamietniczka idzie? ")
    now = datetime.datetime.now() #przywołujemy obiekt typu datetime funkcja datetime i metoda now()
    pamietniczek.append(f'{now.strftime("%d.%m.%Y %H:%M:%S")} = {wpis}')


def wylistuj():
    global pamietniczek
    for linia in pamietniczek:
        print(linia)


def menu():
    while True:
        print("Wybierz Funkcję\n1. Dopisz coś.\n2. Wylistuj\n3. Wyjdź\n")
        decyzja = input("To co robimy? ")
        if decyzja == "1":
            dopisz()
        elif decyzja == "2":
            wylistuj()
        else:
            print("Do zobaczenia")
            break

if __name__ == "__main__":
    menu()