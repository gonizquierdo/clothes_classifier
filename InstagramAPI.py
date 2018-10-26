import requests
import json

class InstagramAPI:

    def __init__(self, client_id, client_secret, token):
        self._client_id = client_id
        self._client_secret = client_secret
        self._token = token

    def get_token(self):
        return self._token

    def get_user(self):
        res = requests.get('https://api.instagram.com/v1/users/self/', {'access_token': self._token})
        json_response = json.loads(res.text)
        return json_response['data']

    def get_recent_media(self):
        res = requests.get('https://api.instagram.com/v1/users/self/media/recent/', {'access_token': self._token})
        json_response = json.loads(res.text)
        return json_response['data']
