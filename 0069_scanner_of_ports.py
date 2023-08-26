#Prawdpopodobnie nie działa na Windowsie

from scapy.all import *
from scapy.layers.inet import TCP, IP



RED, BLUE, GREEN, ENDC= "\33[31m","\33[34m", "\33[35m", "\033[0m" # kodowanie: ANSI

target_ip = input("Podaj adres IP: ")

for port in range(21,81):

    created_packet = scapy.layers.inet.IP (dst=target_ip) / scapy.layers.inet.TCP (dport=port, flags="S", sport= RandShort())  # https://www.computerhope.com/jargon/p/packet.jpg
    ans,nonans = sr(created_packet, timeout=0.5, verbose=False) # ; TO JEST PIERWSZY KROK w TCP handshake https://www.techopedia.com/wp-content/uploads/2023/03/ad900dc1-ad94-4c7b-a3f8-154ad27c35f1.png
    # print("ANS: ", ans)
    # print("NONANS: ", nonans)  # pakiety które nie dotarły

    query_answer = str(ans[0]).split("seq=")[1].split()[0]
    seq = int(query_answer)     # chcemy miec liczbe, do operatora logicznego


    if seq > 0:
        print("Wartość seq dla portu {} jest równa:   {}  ".format(port, seq))
        service = str(ans[0]).split("sport=")[2].split()[0]
        print(f"[+] Port {BLUE}{port}{ENDC} jest {GREEN}otwarty{ENDC}, a dana usługa to: {RED}{service}{ENDC}.")
    else:
        continue

# 45.33.32.156

