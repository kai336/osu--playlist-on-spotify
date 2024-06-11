# this program retrives OAuth access token
import requests
import os

# get token
def get_accses_token():
    osu_client_id = os.environ['OSU_CLIENT_ID']
    osu_client_secret = os.environ['OSU_CLIENT_SECRET']
    token_url = 'https://osu.ppy.sh/oauth/token'
    payload = {
        'client_id': osu_client_id,
        'client_secret': osu_client_secret,
        'grant_type': 'client_credentials',
        'scope': 'public'
    }
    response = requests.post(token_url, data=payload)
    token_info = response.json()
    access_token = token_info['access_token']

    os.environ['OSU_ACCESS_TOKEN'] = access_token
    print(f"access token: {os.environ['OSU_ACCESS_TOKEN']}") #success!