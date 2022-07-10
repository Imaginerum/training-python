import json
import pprint
import requests

params = {
    "api_key" : "ecefb4b7f9bf8de8c06bd0c65e69e12ddf7ee1c7",
    "country" : "pl",
    "year" : 2022
}

r = requests.get("https://calendarific.com/api/v2/holidays/", params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint.pprint(content)