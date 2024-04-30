import requests
def image_analysis(api_key=None, images=None, question=None, training_data=None, output_type="text", stream_data=False):
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
    for i, image_file in enumerate(images or []):
        payload[f"image_{i}"] = (image_file.name, image_file)

    if training_data:
        payload["training_data"] = training_data

    response = requests.request(url, files=payload, headers=headers)

    return response.text

def face_detection(api_key=None, image_file=None):
    url = "https://api.worqhat.com/api/ai/images/v2/face-detection"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "image": (image_file.name, image_file)
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text

def facial_comparison(api_key=None, source_image_file=None, target_image_file=None):
    url = "https://api.worqhat.com/api/ai/images/v2/facial-comparison"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "source_image": (source_image_file.name, source_image_file),
        "target_image": (target_image_file.name, target_image_file)
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text
