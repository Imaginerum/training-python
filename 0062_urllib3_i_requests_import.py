import urllib3

http = urllib3.PoolManager()
r = http.request("GET", 'https://github.com/imaginerum/python-training')
print(f"Oto status strony {r.status}")
print(f"Zawartość formatu\n{r.data.decode('utf-8')}")

import requests

req = requests.get("https://github.com/imaginerum/python-training")
print(f"Strona jest {req.status_code}")
print(f"zawartość {req.text}")
