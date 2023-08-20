import urllib3
import requests

http = urllib3.PoolManager()
r = http.request("GET", 'https://github.com/imaginerum/python-training')
print(f"Oto status strony {r.status}")
print(f"Zawartość formatu\n{r.data.decode('utf-8')}")


req = requests.get("https://github.com/imaginerum/python-training")
print(f"Strona jest {req.status_code}")
print(f"zawartość {req.text}")


payload = {"email":"dummy@mail.provider", "password":"password"}
r2 = requests.post("https://me.hack.me/login", data=payload)
if "logout" in r2.text:
    print("logged in!")
else:
    print("Acces Denied")