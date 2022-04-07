import sys
import random
import string

password = []
characters_left = -1

def update_characters_left(number_of_characaters):
    global characters_left
    if number_of_characaters < 0 or number_of_characaters > characters_left:
        print("liczba znaków z poza przedziału 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characaters
        print("Pozostało znaków:", characters_left)

password_lenght = int(input("Jak długie ma być hasło? "))

if password_lenght < 5:
    print("Hasło powinno mieć min. 5 znaków. Soróbuj jeszcze raz!")
    sys.exit(0)
else:
    characters_left = password_lenght

lowercase_letters = int(input("Ile małych liter ma mieć hasło?"))
update_characters_left(lowercase_letters)

upercase_letters = int(input("Ile dużych liter ma mieć hasło? "))
update_characters_left(upercase_letters)

special_characters = int(input("Ile znaków specjalnych ma mieć hasło? "))
update_characters_left(special_characters)

digits = int(input("Ile cyfr ma mieć hasło? "))
update_characters_left(digits)

if characters_left > 0:
    print("Nie wszystkie znaki zostały wypełnione. Hasło zostanie uzupełnione małymi literami")
    lowercase_letters += characters_left

print("\nDługość hasła:", password_lenght)
print("Małe litery:", lowercase_letters)
print("Duże litery:", upercase_letters)
print("Znaki specjalne:", special_characters)
print("Cyfry:", digits)

for _ in range(password_lenght):
    if lowercase_letters > 0 :
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if upercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        upercase_letters -= 1
    if special_characters > 0:
        password.append((random.choice(string.punctuation)))
        special_characters -= 1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1
random.shuffle(password)
print("Wygenerowane hasło:", ''.join(password))