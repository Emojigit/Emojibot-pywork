import requests

S = requests.Session()

URL = "https://zh.wikipedia.org/w/api.php"

# Retrieve login token first
PARAMS_lgtoken = {
    'action':"query",
    'meta':"tokens",
    'type':"login",
    'format':"json"
}

R = S.get(url=URL, params=PARAMS_0)
DATA = R.json()

LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

print("Login token: " + LOGIN_TOKEN)
print("Data: " + DATA)


PARAMS_login = {
    'action':"login",
    'lgname':"Emojibot-pywork@Emojibot-pywork-xtool-ec",
    'lgpassword':"nkd16fueruspgpnsrgqdnr6b9rf7k29m",
    'lgtoken':LOGIN_TOKEN,
    'format':"json"
}

R = S.post(URL, data=PARAMS_1)
DATA = R.json()

print(DATA)
inputs = input("do you want to contiyue?(y/n) ")
if inputs != "y":
    exit(1)


PARAMS_edit_token = {
    "action": "query",
    "meta": "tokens",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS_2)
DATA = R.json()

CSRF_TOKEN = DATA['query']['tokens']['csrftoken']

# Step 4: POST request to edit a page
pagedata = R.get(url="https://xtools.wmflabs.org/ec/zh.wikipedia.org/Emojiwiki"params={"format": "wikitext"})

PARAMS_edit = {
    "action": "edit",
    "title": "User:Emojiwiki/editstatistics",
    "token": CSRF_TOKEN,
    "format": "json",
    "appendtext": "Hello"
}

R = S.post(URL, data=PARAMS_3)
DATA = R.json()

print(DATA)
