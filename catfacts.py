import requests
import json

params = {
    "limit": 5
}

r = requests.get('https://catfact.ninja/facts', params)

try:
   content = r.json()
except json.decoder.JSONDecodeError:
   print("Niepoprawny format")
else:
   for cat in content.get("data", []):
      print(cat["fact"])
      print(cat["length"])

print(content.get("current_page", []))