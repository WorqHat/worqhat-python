import requests 
from ..utils import Authenticate

def image_analysis(images, question, training_data=None, output_type="text", stream_data=False, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/image-analysis"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "question": question,
        "stream_data": stream_data
    }

    # Add images to payload as files
    for i, image_file in enumerate(images):
        payload[f"image_{i}"] = (image_file.name, image_file)

    if training_data:
        payload["training_data"] = training_data

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def face_detection(image_file, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/face-detection"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def facial_comparison(source_image_file, target_image_file, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/facial-comparison"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "source_image": (source_image_file.name, source_image_file),
        "target_image": (target_image_file.name, target_image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text