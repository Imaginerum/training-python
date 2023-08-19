
licznik = 0
def zliczanieznakow():
    global licznik
    x = input("Podaj input: ")

    for znak in x:
        licznik += 1

while True:
    zliczanieznakow()
    print(f"Na razie nazbieralismy {licznik} znaków")