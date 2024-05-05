import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

def search_ai_v2(question="", training_data="", api_key=None):
    if question == "":
        return "Question is incomplete"

    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    if not api_key:
        return "Please enter an appropriate API key"

    url = "https://api.worqhat.com/api/ai/search/v2"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "question": question,
        "training_data": training_data
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text

def search_ai_v3(question="", training_data="", search_count=10, api_key=None):
    if question == "":
        return "Question is incomplete"

    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    if not api_key:
        return "Please enter an appropriate API key"

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

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text
