import requests 

def content_moderation(text_content, api_key=None):
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

def image_moderation(image_file, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/v2/image-moderation"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text