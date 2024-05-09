import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_pdf_text(pdf_file=None, api_key=None):
    # If pdf_file is not provided, return an error message
    if not pdf_file:
        return "PDF file is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")
        print(api_key)
    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/v2/pdf-extract"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare files data in the required format
    files = [('file', (os.path.basename(pdf_file), open(pdf_file, 'rb'), 'application/pdf'))]

    # Make the API call
    response = requests.post(url, files=files, headers=headers)

    return response.text

def web_extract(url_search="www.worqhat.com", headline=True, inline_code=True, code_blocks=True, references=True, tables=True, api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    url = "https://api.worqhat.com/api/ai/v2/web-extract"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "url_path": url_search,
        "headline": headline,
        "inline_code": inline_code,
        "code_blocks": code_blocks,
        "references": references,
        "tables": tables
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text


def detect_image_text(images=None, output_type="text", api_key=None):
    # If images is not provided or empty, return an error message
    if not images or len(images) == 0:
        return "Images are missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/v2/image-text-detection"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    results = []

    for image in images:
        # Prepare payload
        payload = {'output_type': output_type}

        # Prepare files data in the required format
        if image.startswith('http://') or image.startswith('https://'):
            # If image is a URL, download the image content
            response = requests.get(image)
            files = [('image', (os.path.basename(image), response.content, 'image/jpeg'))]
        else:
            # If image is a local file path, read the file content
            with open(image, 'rb') as f:
                files = [('image', (os.path.basename(image), f, 'image/jpeg'))]

        # Make the API call
        response = requests.post(url, headers=headers, data=payload, files=files)
        results.append(response.text)

    return results


def convert_speech_to_text(audio_file=None, api_key=None):
    # If audio_file is not provided, return an error message
    if not audio_file:
        return "Audio file is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/speech-text"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare files data in the required format
    files = [('audio', (os.path.basename(audio_file), open(audio_file, 'rb'), 'application/octet-stream'))]

    # Make the API call
    response = requests.post(url, files=files, headers=headers)

    return response.text