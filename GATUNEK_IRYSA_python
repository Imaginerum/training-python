import pandas as pd

url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv'
irysy = pd.read_csv(url, index_col='species').sort_index()
print('Witaj! Poprosze o dane.\n')

#pomocne:
blad1 = 'Blad! Jeszcze raz!\n'
blad2 = 'Nieprawidlowe dane'

#Dane:

proba = 2
sl = float(input('Podaj długość kielicha: '))
while proba > 0:
    if any(irysy['sepal_length'] == sl):
        logika = irysy.loc[(irysy['sepal_length']== sl)]
        print('Ok.')
        proba = 0
    elif proba == 1:
        print(irysy)
        print('\nWyzej mala podpowiedz :)\n')
        proba = 2
    else:
        print(blad1)
        sl = float(input('Podaj długość kielicha: '))
        proba -= 1


proba = 2
sw = float(input('Podaj szerokosc kielicha: '))
while proba > 0:
    if any(logika['sepal_width']== sw):
        logika = logika.loc[(logika['sepal_width']== sw)]
        print('Ok.')
        proba = 0
    elif proba == 1:
        print(logika)
        print('\nWyzej mala podpowiedz :)')
        proba = 2
    else:
        print(blad1)
        sw = float(input('Podaj szerokosc kielicha: '))
        proba -= 1

proba = 2
pl = float(input('Podaj długość płatka: '))
while proba > 0:
    if any(logika['petal_length']==pl):
        logika = logika.loc[(logika['petal_length']==pl)]
        print('Ok.')
        proba = 0
    elif proba == 1:
        print(logika)
        print('\nWyzej mala podpowiedz :)')
        proba = 2
    else:
        print(blad1)
        pl = float(input('Podaj długość płatka: '))
        proba -= 1

proba = 2
pw = float(input('Podaj szerokość płatka: '))
while proba > 0:
    if any(logika['petal_width']==pw):
        logika = logika.loc[(logika['petal_width']==pw)]
        print('Ok.')
        proba = 0
    elif proba == 1:
        print(logika)
        print('\nWyzej mala podpowiedz :)')
        proba = 2
    else:
        print(blad1)
        pw = float(input('Podaj szerokość płatka: '))
        proba -= 1

irys = [sl, sw, pl, pw]

gatunek = irysy - irys

#Rozwiazanie:

rozwiazanie = gatunek.loc[(gatunek['sepal_length']== 0.0) & (gatunek['sepal_width']==0.0) & (gatunek['petal_length']==0.0) & (gatunek['petal_width']==0.0)]
rozwiazanie = rozwiazanie.reset_index()['species'][0]

#odpowiedz

print(' \nGatunek irysa to: '+rozwiazanie+'\n')

