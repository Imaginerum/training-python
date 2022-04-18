#ZAD Built a programm that handle with collatz problem

def collatz():
    try:
        number = int(input("Podaj liczbę:\n"))
        while True:
            if number == 1:
                break
            elif number % 2 == 0:
                number = number // 2
                print(number)
            elif number % 2 == 1:
                number = number * 3 + 1
                print(number)
    except ValueError:
        print("Nie podałeś liczby!!!")


collatz()