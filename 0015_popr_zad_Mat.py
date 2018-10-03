"""Sprawdza poprawność działań matematycznych wprowadzonych w postaci zmiennej typu string.

Args:
    rownianie = Równanie matematyczne w postaci zmiennej typu string

Returns:
    True or False; zgodnie z wynikiem równania.
    """

def popr_rownan(*args):

    #1. WPROWADZENIE danych.

    rownanie = input("Wprowadź równanie do sprawdzenia: ")

    #2. Wstępna obróbka równania:

    def obrobka1(dane, x=' '):
        '''Sprawia, że wyoliminowane zostaną 'spacje' w równaniu oraz staje się ono elementem listy'''

        dane = []
        [dane.append(i) for i in rownanie if i != x] #zgrywa w postaci listy + drop N/A
        return dane

    dane = obrobka1(rownanie)

    #3. Właściwa Obróbka równania:
    ''' Wyrzucenie 'spacji' oraz scalenie cyfr typu string oraz zmiana typu str-liczb listy na int-liczby. 
        Znaki w liście pozostają typu str'''


    rodzaj_znaku = ['+', '-', '/', '*', '=','^','%']        #lista uzywana wielokrotnie potem.

    def obrobka2(lista1):
        '''Obrabia dane w celu przygotowania do sprawdzenia poprawności równania
            Args:
                lista1 - dane
            Returns:
                lista2 - nowa lista z danymi dane'''

        #Concat cyfry typu string. Pozostawia: N/A .
        for idx in range(len(lista1)):
            if idx != 0 and lista1[idx] not in rodzaj_znaku and lista1[idx - 1] not in rodzaj_znaku:
                lista1[idx] = ''.join(lista1[idx - 1:idx + 1])
                lista1[idx - 1] = ''

        #Usuniecie: N/A + Dane str-liczbowe zmienione na int-liczbowe w nowej liście
        lista2 = []
        for element in lista1:
            if element != '' and element not in rodzaj_znaku:
                lista2.append(int(element))
            elif element != '' and element in rodzaj_znaku :
                lista2.append(element)

        return lista2

    dane = obrobka2(dane)

    #4. SPRAWDZENIE rownania:
    ''' Sprawdza, czy wprowadzone równanie matematyczne zostało rozwiązane poprawnie'''

    znak = {}
    for idx, val in enumerate(dane):
        '''Tworzy dict znaków; key to pozycja znaku w liście dane; value to wartość znaku.

        Args:
            znak = pusty dict().
            rodzaj znaku = określa kategorię znaku.
        Return:
            znak = dict, który zawiera pozycje znaku w liście i rodzaj znaku wg '''

        if val in rodzaj_znaku:
            znak[idx] = val


    def rozwiazanie(dane, znak, wynik=0):
        ''' Ma na celu wyrzucenie zgodnie z prawda wartości True or False zgodnie z rozwiązaniem równania '''

        if len(znak) == 2:
            if znak[1] in rodzaj_znaku:
                if znak[1] == '+' :
                    dane.append(dane[0]+dane[2]==dane[-1])
                elif znak[1] == '-':
                    dane.append(dane[0]-dane[2]==dane[-1])
                elif znak[1] == '/':
                    dane.append(dane[0]/dane[2]==dane[-1])
                elif znak[1] == '*':
                    dane.append(dane[0]*dane[2]==dane[-1])
                else:
                    dane.append('Wykracza poza mą pojetność')

    rozwiazanie(dane, znak)

    return dane[-1], dane[0:len(dane)-1]
print(popr_rownan())