import json
with open('pref.json') as f:
    data = json.load(f)
username = str(data["bilgiler"]["user"])
password = str(data["bilgiler"]["pass"])
video = str(data["bilgiler"]["video"])