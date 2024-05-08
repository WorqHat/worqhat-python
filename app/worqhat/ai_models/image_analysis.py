import requests
import os
import base64
from urllib.parse import urlparse
from dotenv import load_dotenv
import json
# Load environment variables from .env file
load_dotenv()

def analyze_images(images, question="", training_data="", output_type="text", stream_data=False, api_key=None):
    # Load dotenv file to get the API key
    load_dotenv()

    # Get API key from environment variable or use the provided one
    api_key = api_key or os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API key is missing. Provide it as an argument or in the .env file.")

    # API endpoint
    url = "https://api.worqhat.com/api/ai/images/v2/image-analysis"

    # Prepare headers with authorization
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Prepare payload
    payload = {
        'output_type': output_type,
        'stream_data': str(stream_data).lower(),
        'question': question
    }

    # Prepare files data
    files = []
    for image in images:
        if image.startswith('http://') or image.startswith('https://'):
            # If URL, download the image
            response = requests.get(image)
            files.append(('images', (os.path.basename(image), response.content, 'image/jpeg')))
        else:
            # If file path, read file content and then append
            with open(image, 'rb') as f:
                file_content = f.read()
                files.append(('images', (os.path.basename(image), file_content, 'image/jpeg')))

    # Make the API call
    response = requests.post(url, headers=headers, data=payload, files=files)

    # Handle streaming data if enabled
    if stream_data:
        for line in response.iter_lines():
            if line:
                if line.startswith(b'data:'):
                    json_content = line[len(b'data:'):].decode('utf-8').strip()
                    print(json_content)
    else:
        # If not streaming, print the JSON response
        json_response = response.text
        try:
            json_data = json.loads(json_response)
            print(json.dumps(json_data, indent=4))
        except json.JSONDecodeError:
            print(json_response)
            
def detect_faces(images, api_key=None):
    # Load dotenv file to get the API key
    load_dotenv()

    # Get API key from environment variable or use the provided one
    api_key = api_key or os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API key is missing. Provide it as an argument or in the .env file.")

    # API endpoint
    url = "https://api.worqhat.com/api/ai/images/v2/face-detection"

    # Prepare headers with authorization
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Prepare files data
    files = []
    for image in images:
        if image.startswith('http://') or image.startswith('https://'):
            # If URL, download the image
            response = requests.get(image)
            files.append(('image', (os.path.basename(image), response.content, 'image/jpeg')))
        else:
            # If file path, read file content and then append
            with open(image, 'rb') as f:
                files.append(('image', (os.path.basename(image), f, 'image/jpeg')))

    # Make the API call
    response = requests.post(url, headers=headers, files=files)

    return response.text

def compare_faces(source_images, target_images, api_key=None):
    # Load dotenv file to get the API key
    load_dotenv()

    # Get API key from environment variable or use the provided one
    api_key = api_key or os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API key is missing. Provide it as an argument or in the .env file.")

    # API endpoint
    url = "https://api.worqhat.com/api/ai/images/v2/facial-comparison"

    # Prepare headers with authorization
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    # Prepare files data for source images
    source_files = []
    for source_image in source_images:
        if source_image.startswith('http://') or source_image.startswith('https://'):
            # If URL, download the image
            response = requests.get(source_image)
            source_files.append(('source_image', (os.path.basename(source_image), response.content, 'image/jpeg')))
        else:
            # If file path, read file content and then append
            with open(source_image, 'rb') as f:
                source_files.append(('source_image', (os.path.basename(source_image), f, 'image/jpeg')))

    # Prepare files data for target images
    target_files = []
    for target_image in target_images:
        if target_image.startswith('http://') or target_image.startswith('https://'):
            # If URL, download the image
            response = requests.get(target_image)
            target_files.append(('target_image', (os.path.basename(target_image), response.content, 'image/jpeg')))
        else:
            # If file path, read file content and then append
            with open(target_image, 'rb') as f:
                target_files.append(('target_image', (os.path.basename(target_image), f, 'image/jpeg')))

    # Combine source and target files
    files = source_files + target_files

    # Make the API call
    response = requests.post(url, headers=headers, files=files)

    return response.text
