"""
Write a program for keeping definition that helps user:
1) add new definition
2) looking for existing definition
3) delete chosen definition
"""
definitions = {}

while True:
    print("1. Dodaj definicję")
    print("2. Szukaj definicję")
    print("3. Usuń definicję")
    print("4. Pokarz definicję")
    print("5. Zakończ program", end="\n\n")
    choice = input("Co chcesz zrobić?\n")

    if choice == '1':
        key = input("Podaj klucz, czyli słowo do zdefiniowania: ")
        definition = input("Podaj definicję słowa-klucza\n")
        definitions[key] = definition
        print("Definicja dodana pomyślnie")

    elif choice == '2':
        search_definition = input("Podaj szukaną definicję: ")
        if search_definition in definitions:
            print("Szukana definicja to:\n", search_definition, ":", definitions[search_definition])
        else:
            print(search_definition, "nie istnieje w definicjach.")
    elif choice == '3':
        del_definition = input("Podaj definicję do usunięcia: ")
        if del_definition in definitions:
            del definitions[del_definition]
            print("Usunięto", del_definition, "z definicji")
        else:
            print("Nie ma takiej definicji w definicjach.")
    elif choice == '4':
        print(definitions, end='\n\n')
    elif choice == '5':
        break
    else:
        print("Coś poszło nie tak. Spróbuj jeszcze raz.\n")