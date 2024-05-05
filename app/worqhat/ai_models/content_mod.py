import requests 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def content_moderation(text_content="",api_key=None):
    if text_content == "":
        return "Text content is incomplete"
    if not api_key:
    # Retrieve API key from environment variable
        api_key = os.getenv("API_KEY")

    # If api_key is not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API key"

    url = "https://api.worqhat.com/api/ai/moderation"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text_content": text_content
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

def image_moderation(image_file=None,api_key=None):
    # If image_file is not provided, return an error message
    if not image_file:
        return "Image file is missing"
    if not api_key:
    # Retrieve API key from environment variable
        api_key = os.getenv("API_KEY")

    # If api_key is not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/v2/image-moderation"
    headers = {
        "Authorization": "Bearer " + api_key
    }

    payload = {
        "image": image_file
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text
