from scapy.all import *
from scapy.layers.inet import Ether
from scapy.layers.l2 import ARP
import scapy.layers.l2

for address in range(1, 255):
    ip = f"192.168.0.{address}"
    arp_out = scapy.layers.inet.Ether(dst="ff:ff:ff:ff:ff:ff    ") / scapy.layers.l2.ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    arp_in = srp1(arp_out, timeout=1, verbose=False)

    if arp_in:
        print(f"IP: {arp_in.psrc}, MAC: {arp_in.hwsrc}")