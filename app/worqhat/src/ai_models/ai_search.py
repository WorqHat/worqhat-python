import requests 
from ..utils import Authenticate

def search_ai_v2(question, training_data, api_key=None):
    auth_status = Authenticate(api_key).get("status")
    if auth_status == "success":
        url = "https://api.worqhat.com/api/ai/search/v2"
        headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "question": question,
            "training_data": training_data
        }

        response = requests.post(url, json=payload, headers=headers)

        return response.text
    else:
        return auth_status
    
def search_ai_v3(api_key=None, question="", training_data="", search_count=10):
   
    url = "https://api.worqhat.com/api/ai/search/v3"
    headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
    }

    payload = {
            "question": question,
            "training_data": training_data,
            "search_count": search_count
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

    return auth_status