import random

def przeczytajplik():
    try:
        with open("pliczek.txt", "r") as pliczek:
            print(pliczek.read())
    except FileNotFoundError:
        print("Nie ma takiego pliczku")

def dopiszdopliku():
    with open("pliczek.txt", "a") as pliczek:
        pliczek.write(str(random.randint(1,100)) + "\n")

przeczytajplik()
dopiszdopliku()
przeczytajplik()