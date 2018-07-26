#Prgram, który na podstawie nr dnia poda jego nazwę:

def main():

    print('Podaj nr dnia tygodnia...')
    nr_dnia = int(input())

    def switch_dzien_tyg(nr_dnia):
        switcher = {
            1 : "Poniedziałek",
            2 : "Wtorek",
            3 : "Środa",
            4 : "Czwartek",
            5 : "Piątek",
            6 : "Sobota",
            7 : "Niedziela"
        }
        print(switcher.get(nr_dnia, "Niepoprawny dzień"))
    switch_dzien_tyg(nr_dnia)
    return 0

main()