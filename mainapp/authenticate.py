import requests
import json
# code = "yw0n9v0vb7avxccynn8huko07c6tf5"


def get_access_token(code):
    clientid = "92h2m4t1t7vtoewujwz0z8xfq55qdm"
    clientsecret = "tofgqnlvv0k96r6sq8gzmeitu7tacz"
    resp = requests.post('https://id.twitch.tv/oauth2/token?client_id=92h2m4t1t7vtoewujwz0z8xfq55qdm&client_secret=u4lmk5v25eqvjr8wqpt6wdx5cb4w0p&code='+code+'&grant_type=authorization_code&redirect_uri=http://localhost:3000')
    access_token = resp.json()["access_token"]
    return access_token

def get_id_and_user(authorization):
    url = 'https://api.twitch.tv/helix/users'
    headers={'Authorization': 'Bearer ' + authorization, 'Client-Id': '92h2m4t1t7vtoewujwz0z8xfq55qdm'}
    r = requests.get(url, headers=headers)
    return authorization, r.json()['data'][0]['id']

# print(get_access_token(code))
# temp = get_id_and_user(get_access_token(code))
# print(temp[0],temp[1])