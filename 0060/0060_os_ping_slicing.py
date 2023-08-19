import os

wynikpinga = os.system("ping 8.8.8.8 > ping.txt")

with open("ping.txt", "r") as plik:
    for line in plik:
        if "Reply" in line:
            newline = line.replace("\n",  "")
            pokrojonalinia = line.split("=")
            bajty = pokrojonalinia[1].split(" ")
            milisekundy = pokrojonalinia[2].split("ms")
            print(f'{bajty[0]} wrocily w {milisekundy[0]}')