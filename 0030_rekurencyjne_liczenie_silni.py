number = int(input("podaj liczbę: "))

def silnia(n):
    if n<2 :
        return 1
    else:
        return n * silnia(n-1)

print("silnia z " + str(number) + " to: " + str(silnia(number)))