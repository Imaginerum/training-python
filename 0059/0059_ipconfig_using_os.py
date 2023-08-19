import os

os.system("ipconfig > ipconfig.txt")
with open("ipconfig.txt", "r") as pliczek:
    for linia in pliczek:
        if "IPv4" in linia:
            pokrojonalinia = linia.split(":")
            wyjscie = pokrojonalinia[1].replace("\n","")
            print(f'Dostępny adres IP to : {wyjscie}')