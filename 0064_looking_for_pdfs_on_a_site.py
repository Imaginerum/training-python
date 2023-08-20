import requests
from bs4 import BeautifulSoup

url = "http://mirror.hackthissite.org/hackthiszine"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

# szukamy tagów a, bo tag a zawiera w sobie linki
for search in soup.find_all('a'):
    # parametrem tagu a, który przechowuje faktyczny link jest href
    link = search.get('href')
    if link.endswith(".pdf"):
        print("http://mirror.hackthissite.org" + link)
        filename = link.split("/")[2]
        with open(filename, "wb") as file:
            temp_url = "http://mirror.hackthissite.org" + link
            req = requests.get(temp_url, stream=True)
            file.write(req.content)