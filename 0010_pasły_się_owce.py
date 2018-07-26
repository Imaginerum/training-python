''' Napisz program, który wczyta liczby całkowite B, W, Z a następnie poprawnie napisze tekst:

Na łące [pasła / pasły / pasło] się B [owca / owce / owiec]. Wieczorem [przyszedł / przyszły / przyszło] W
[wilk / wilki / wilków] i [zjadł / zjadły] Z [owcę / owce / owiec]. Rano na łące [nie było / była / były /
było już tylko B-Z] [owca / owce / owiec]

kontrola danych: B >=1, W >=1, Z>=0, B>=Z

'''

def owce() :

    print("Podaj liczbę owiec: ")
    B = int(input())
    print("Podaj liczbę wilków: ")
    W = int(input())
    print("Podaj liczbę zjedzonych owiec: ")
    Z = int(input())

    # kombinacja slowa 2-warunkowe :
    zja = [' zjadł ', ' zjadły ']

    # kombinacja słowa 3-warunkowa :
    pasł = [' pasła ', ' pasły ', ' pasło ']
    owc = [' owca', ' owce', ' owiec']
    przyszł = [' przyszedł ', ' przyszły ',' przyszło ']
    wil = [' wilk ',' wilki ',' wilków ']

    #kombinacja slowa 4-warunkowa :
    był = [' była juz tylko jedna', ' były już tylko {0}'.format(B-Z), ' było już tylko {0}'.format(B-Z), ' nie było już']


    def war(slowo, ile) : # 3 opcje warunkowe
        if (len(str(ile)) == 1):
            # 3 opcje warunkowe!!!
            if ile == 1:
                return (slowo[0])
            elif ((str(ile)[0] == str(2)) or (str(ile)[0] == str(3)) or (str(ile)[0] == str(4))):
                return (slowo[1])

            # 4 opcje warunkowe!!!
            elif (str(ile) == str(0) and len(slowo)>3):
                return slowo[3]

            # 2 opcje warunkowe!!!
            elif (str(ile) == str(1) and len(slowo) < 3):
                return slowo[0]
            elif (str(ile) != str(1) and len(slowo) < 3):
                return slowo[1]

            # 3 i 4 opcje warunkowe!!!
            else:
                return slowo[2]

        else:
            # 3 i 4 opcje warunkowe!!!
            if ((str(ile)[-2:] == str(12)) or (str(ile)[-2:] == str(13)) or (str(ile)[-2:] == str(14))):
                return (slowo[2])
            elif ((str(ile)[-1] == str(2)) or (str(ile)[-1] == str(3)) or (str(ile)[-1] == str(4))):
                return (slowo[1])

            # 2 opcje warunkowe!!!
            elif (str(ile) != str(1) and len(slowo) < 3):
                return slowo[1]

            else: # 3 i 4 opcje warunkowe!!!
                return (slowo[2])


    if (B >=1) & (W >=1) & (Z>=0) & (B>=Z) : #kontrola danych
        print('Na łące' + war(pasł, B) + 'się {0}'.format(B) + war(owc, B) +
        '. Wieczorem' + war(przyszł, W) + str(W) + war(wil, W) + 'i' + war(zja, W) + str(Z) +
        war(owc, Z) + '. Rano na łace' + war(był, B-Z) + war(owc, B-Z))

    else :
        print("Błędne dane.\nOwiec i wilków powinno być więcej, niż 1 i owiec powinno być więcej, niż wilków")

owce()