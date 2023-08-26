import paramiko
import getpass

target_ip = input("Podaj adres IP: ")
port = 22
username = input("Podaj nazwę użytkownika: ")
password = input("Wpisz hasło: ")
#ukrycie widoczności hasła: password = getpass.getpass()


ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.load_system_host_keys()
ssh_client.connect(hostname= target_ip, port= port, username = username, password = password)
stdin, stdout, stderr = ssh_client.exec_command("ls -l")
stdin.close()
files_and_dires = stdout.read().decode()
files_and_dires_without_decoding = stdout.read()
print("Na Twoim hoscie {} znajdują się następujące katalogi i pliki\r\n {}".format(target_ip, files_and_dires))
print("Na Twoim hoscie {} znajdują się następujące katalogi i pliki ZENKODOWANE\r\n {}".format(target_ip, files_and_dires_without_decoding))
