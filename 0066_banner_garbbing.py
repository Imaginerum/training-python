#tworzenie prościutkiego banneru.

import socket

sock = socket.socket()
target_ip = input("Podaj adres IP: ")
port = int(input("Podaj nr portu: "))

sock.connect((target_ip, port))

sock.send("What the service? \r\n".encode())
socket.setdefaulttimeout(4)     #nie chcemy czekać dłużej, niż 4 sec na odpowiedź od servera.

resp = sock.recv(1024).decode()
print(resp)

sock.close()