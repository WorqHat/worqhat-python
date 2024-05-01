import requests 

def content_moderation(api_key=None,text_content=""):
    if text_content=="":
        return("Question is incomplete")
    url = "https://api.worqhat.com/api/ai/moderation"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text_content": text_content
    }

    response = requests.request('POST',url, json=payload, headers=headers)

    return response.text

def image_moderation(api_key=None,image_file=None ):
    url = "https://api.worqhat.com/api/ai/images/v2/image-moderation"
    headers = {
        "Authorization": "Bearer " + api_key,
    }

    payload = {
        "image": image_file
    }

    response = requests.request('POST',url, files=payload, headers=headers)

    return response.text