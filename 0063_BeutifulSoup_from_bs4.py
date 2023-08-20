import requests
from bs4 import BeautifulSoup

print("Linki na stronie onet.pl")
# Stąd mamy wszystkie linki wziąć
url = "https://onet.pl"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

for search in soup.find_all('a'):
    print(search.get('href'))


# Stąd mamy pliki javascript ogarnąć
print("Pliki javascript na stronie tryhackmme.com")
url = "https://tryhackme.com"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

for search in soup.find_all('script'):
    try:
         source = search.get('src')
         source = source.split('?')[0]
         if source.endswith(".js"):
            print(source)
    except:
        pass