licznik = 0
zapiswtrakcie = False

with open("autopsy.jpg","rb") as obrazek:
    obrbajty = obrazek.read()

    for bajt in obrbajty:
        if hex(bajt) == "0xd8" and hex(poprzednibajt) == "0xff":
            print("mamy poczatek!")
            licznik += 1
            nazwapliku = str(licznik) + ".jpg"
            zapis = open(nazwapliku, "wb")
            zapis.write(poprzednibajt.to_bytes(1, 'little'))
            zapiswtrakcie = True
        if zapiswtrakcie:
            zapis.write(bajt.to_bytes(1, 'little'))
        if hex(bajt ) == "0xd9" and hex(poprzednibajt) == "0xff":
            print("mamy koniec!")
            zapis.close()
            zapiswtrakcie = False
        poprzednibajt = bajt

