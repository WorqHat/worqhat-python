import requests 
def pdf_extract( api_key=None, pdf_file=None):
    url = "https://api.worqhat.com/api/ai/v2/pdf-extract"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "file": (pdf_file.name, pdf_file)
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text

def web_extract(api_key=None, url_search="www.worqhat.com", headline=True, inline_code=True, code_blocks=True, references=True, tables=True):
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

    response = requests.request(url, json=payload, headers=headers)

    return response.text

def image_text_detection(api_key=None,image_file=None, output_type="json" ):
    url = "https://api.worqhat.com/api/ai/images/v2/image-text-detection"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "image": (image_file.name, image_file)
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text

def speech_to_text(api_key=None,audio_file=None ):
    url = "https://api.worqhat.com/api/ai/speech-text"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "audio": (audio_file.name, audio_file)
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text
