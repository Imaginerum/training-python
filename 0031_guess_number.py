#Guess number betwen 1 to 100 in 6 atemps

import random

def guess_number():
    secret_number = random.randint(1,100)
    print("Mam na myśli pewną liczbę z zakresu 1 do 100. Masz 6 prób. Zgadnij liczbę!")

    for guesses_taken in range(1,7):
        guess = int(input())
        if guess < secret_number:
            print("Podana liczba jest większa")
        elif guess > secret_number:
            print("Podana liczba jest mniejsza")
        else:
            break
    if guess == secret_number:
        print("Doskonale! Odgadłeś liczbę w ciągu od 1 do 100. Liczba to "+ str(secret_number))
    else:
        print("\nNie udało Ci się. GAME OVER!")

guess_number()