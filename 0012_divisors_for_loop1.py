''''
1.Przećwiczenie petli for:

Napisz program wypisujący wszystkie dzielniki zadanej liczby naturalnej, liczbę tych dzielników oraz ich sumę. Program
powinien podawać komunikat, jeżeli podana liczba jest liczbą pierwszą.
'''


liczba = int(input("\nPodaj liczbę naturalną, której dzielniki chciałbyś poznać: "))

dzielniki = [i for i in range(1, liczba+1) if liczba % i == 0]
suma = 0
for i in dzielniki :
    suma += i

print("Dzielników liczby {0} jest {1}, to: ".format(liczba, len(dzielniki)) +
      str(dzielniki) + '\nA ich suma, to: {0}'.format(suma))
