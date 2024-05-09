import requests 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def content_moderation(text_content="",api_key=None):
    if text_content == "":
        return "Text content is incomplete. Please give some text and try again. "
    if not api_key:
    # Retrieve API key from environment variable
        api_key = os.getenv("API_KEY")

    # If api_key is not provided, return an error message
    if not api_key:
        raise ValueError("API key is missing. Provide it as an argument or in the .env file.")

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

def image_moderation(images=None, api_key=None):
    # If images is not provided or empty, return an error message
    if not images or len(images) == 0:
        return "No images found. Please try again "

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        raise ValueError("API key is missing. Provide it as an argument or in the .env file.")

    url = "https://api.worqhat.com/api/ai/images/v2/image-moderation"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    results = []

    for image in images:
        # Prepare files data in the required format
        if image.startswith('http://') or image.startswith('https://'):
            # If image is a URL, download the image content
            response = requests.get(image)
            files = [('image', ('file', response.content, 'application/octet-stream'))]
        else:
            # If image is a local file path, read the file content
            with open(image, 'rb') as f:
                files = [('image', ('file', f, 'application/octet-stream'))]

        # Make the API call
        response = requests.post(url, files=files, headers=headers)
        results.append(response.text)

    return results