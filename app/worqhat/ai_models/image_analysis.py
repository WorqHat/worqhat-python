import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def image_analysis(images=None, question="", training_data="", output_type="text", stream_data=False, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/image-analysis"
    headers = {
        "Content-Type": "multipart/form-data"
    }

    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    headers["Authorization"] = "Bearer " + api_key

    payload = {
        "output_type": output_type,
        "question": question,
        "stream_data": stream_data
    }

    # Add images to payload as files
    for i, image_file in enumerate(images or []):
        payload[f"image_{i}"] = (image_file.name, image_file)

    if training_data:
        payload["training_data"] = training_data

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def face_detection(image_file=None, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/face-detection"
    headers = {
        "Content-Type": "multipart/form-data"
    }

    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    headers["Authorization"] = "Bearer " + api_key

    payload = {
        "image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def facial_comparison(source_image_file=None, target_image_file=None, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/facial-comparison"
    headers = {
        "Content-Type": "multipart/form-data"
    }

    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

    headers["Authorization"] = "Bearer " + api_key

    payload = {
        "source_image": (source_image_file.name, source_image_file),
        "target_image": (target_image_file.name, target_image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text
