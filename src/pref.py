import json
with open('pref.json') as f:
    data = json.load(f)
username = ""
password = ""
for name in data["bilgiler"]:
    username = name["user"]
for passw in data["bilgiler"]:
    password = passw["pass"]