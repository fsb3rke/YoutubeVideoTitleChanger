import json
with open('pref.json') as f:
    data = json.load(f)
username = data["bilgiler"]["user"]
password = data["bilgiler"]["pass"]
video = data["bilgiler"]["video"]