import json

film = {
    "title" : "Ale ja nie będę tego robił",
    "release year" : 1969,
    "won oscar" : True,
    "actors" : ("Arkadiusz Włodarczyk", "Wioletta Włodarczyk"),
    "budget" : None,
    "credits" : {
        "director" : "Arkadiusz Włodarczyk",
        "writer" : "Alan Burger",
        "animator" : "Anime Animatrix"
    }
}

encodedFilm = json.dumps(film, ensure_ascii=False, indent=4, sort_keys=True)
print(encodedFilm)
with open("sample.json", 'w', encoding="UTF-8") as file:
    json.dump(film, file, ensure_ascii=False)

with open("sample.json", encoding="UTF-8") as file:
    wynik = json.load(file)
    print(wynik)
    import pprint
    pprint.pprint(wynik)

