#Ustawoiono by zakładami zarządzała AI (petla) ustawiona na obstawianie wyniku orzeł z
#określoną wielkością portfela.

import random

portfel = 100000
licznikgier = 0
licznikzwyciestw = 0

def rzutmoneta():
    moneta = ["orzel", "reszka", "kant"]
    wynik = random.choices(moneta, weights=[50, 50, 1])
    return wynik[0]

def obsluz_gracza(obstawione, stawka):
    global portfel, licznikgier, licznikzwyciestw
    licznikgier += 1
    wynikrzutu = rzutmoneta()
    if wynikrzutu == obstawione:
        print("Trafione")
        portfel += stawka
        licznikzwyciestw += 1
    else:
        # print(f"Niestety. Na monecie widnieje {wynikrzutu}")
        portfel -= stawka

def main():
    global portfel, licznikgier, licznikzwyciestw
    # portfel = int(input("Ile masz pieniędzy?: "))
    while True:
        if portfel <= 0:
            print("Spłukałeś się. Wyrzucają Cię za drzwi")
            print(f"Zagrałeś {licznikgier} razy i wszystko przebombałeś")
            print(f"Mimo to wygrałeś {licznikzwyciestw} razy")
            break
        else:
            print(f"{portfel}")
        # decyzja = input("Co obstawiasz? [o / r / k / q] (orzel, reszka, kant, quit): ")
        decyzja = "o"
        if decyzja == "o":
            obstawione = "orzel"
        elif decyzja == "r":
            obstawione = "reszka"
        elif decyzja == "k":
            obstawione = "kant"
        else:
            print(f"Dość? No to OK, to dość. Zostało Ci {portfel}. Zagrałeś {licznikgier} razy, trafiając {licznikzwyciestw} rzutów.")
            break
        # stawka = int(input("Ile stawiasz?: "))
        stawka = 1
        obsluz_gracza(obstawione,stawka)


if __name__ == "__main__":
    main()