import requests 

def content_moderation(api_key=None,text_content="Hello! My name is Alex" ):
    url = "https://api.worqhat.com/api/ai/moderation"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text_content": text_content
    }

    response = requests.request(url, json=payload, headers=headers)

    return response.text

def image_moderation(api_key=None,image_file=None ):
    url = "https://api.worqhat.com/api/ai/images/v2/image-moderation"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "image": (image_file.name, image_file)
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text