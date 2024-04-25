import requests

def Authenticate(api_key):
    url = "https://api.worqhat.com/authentication"
    headers = {"Authorization": "Bearer " + api_key}
    response = requests.post(url, headers=headers)
    return response.json()