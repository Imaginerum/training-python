import math as m
import matplotlib.pyplot as plt


dane = {}

def main():

    for kat_stopnie in range(0,91):

        wynik = m.sin(kat_stopnie*m.pi/180)
        print("sin {0} = {1}".format(kat_stopnie, round(wynik, 10)))
        dane["sin {0}".format(kat_stopnie)] = wynik

    return 0

main()

plt.plot(dane.values(),dane.keys())
plt.title('Tablica Sinusow')
plt.xlabel('kat')
plt.ylabel('sinus')

plt.show()
