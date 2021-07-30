import json
with open('pref.json') as f:
    data = json.load(f)
username = ""
password = ""
video = ""
for name in data["bilgiler"]:
    username = name["user"]
for passw in data["bilgiler"]:
    password = passw["pass"]
for vidw in data["bilgiler"]:
    video = vidw["video"]