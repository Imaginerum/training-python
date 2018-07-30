#Prgram, który na podstawie nr dnia poda jego nazwę:

def main():

    print('Podaj nr dnia tygodnia...')
    nr_dnia = int(input())

    #dane pod dict, key = dni, value = num:
    dni = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela']
    num = [num for num in range(1,8)]

    def switch_dzien_tyg(nr_dnia):
        switcher = dict(zip(num, dni)) #tworzy dict
        print(switcher.get(nr_dnia, "Niepoprawny dzień"))

    switch_dzien_tyg(nr_dnia)

    return 0

main()