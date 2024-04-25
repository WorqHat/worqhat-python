import requests 

def generate_image_v2(prompt, image_style="realistic", output_type="url", orientation="square", api_key=None):

    url = "https://api.worqhat.com/api/ai/images/generate/v2"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "image_style": image_style,
        "output_type": output_type,
        "orientation": orientation
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

    
def generate_image_v3(prompt, image_style="realistic", output_type="url", orientation="square", api_key=None):
    
    url = "https://api.worqhat.com/api/ai/images/generate/v3"
    headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "application/json"
    }

    payload = {
            "prompt": prompt,
            "image_style": image_style,
            "output_type": output_type,
            "orientation": orientation
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text


def modify_image_v2(file_path, modification, output_type="url", similarity=50, api_key=None):
   
    url = "https://api.worqhat.com/api/ai/images/modify/v2"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

        # Construct payload with multipart form-data
    payload = {
            "output_type": (None, output_type),
            "modification": (None, modification),
            "similarity": (None, str(similarity)),
            "existing_image": (file_path.split("/")[-1], open(file_path, 'rb'))
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text
 
    
def modify_image_v3(image_file, modification, output_type="url", similarity=50, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3"
    headers = {
            "Authorization": "Bearer " + api_key,
            "Content-Type": "multipart/form-data"
    }

        # Construct payload with multipart form-data
    payload = {
            "output_type": (None, output_type),
            "modification": (None, modification),
            "similarity": (None, str(similarity)),
            "existing_image": (image_file.name, image_file)
        }

    response = requests.post(url, files=payload, headers=headers)

    return response.text
    
def modify_image_v3(image_file, modification, output_type="url", similarity=50, api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "modification": modification,
        "similarity": str(similarity),
        "existing_image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def remove_text_from_image(image_file, output_type="url", api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3/remove-text"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "existing_image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def remove_background_from_image(image_file, output_type="url", api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3/remove-background"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "existing_image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def replace_background(image_file, modification="Create Variation of the Image", output_type="url", api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3/replace-background"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "modification": modification,
        "existing_image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def search_replace_image(image_file, modification="Create Variation of the Image", output_type="url", api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3/search-replace-image"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "modification": modification,
        "existing_image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def extend_image(image_file, left_extend=10, right_extend=10, top_extend=5, bottom_extend=5, description=None, output_type="url", api_key=None):
    url = "https://api.worqhat.com/api/ai/images/modify/v3/extend-image"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "leftExtend": left_extend,
        "rightExtend": right_extend,
        "topExtend": top_extend,
        "bottomExtend": bottom_extend,
        "existing_image": (image_file.name, image_file)
    }

    if description:
        payload["description"] = description

    response = requests.post(url, files=payload, headers=headers)

    return response.text

def upscale_image(image_file, scale=2, output_type="url", api_key=None):
    url = "https://api.worqhat.com/api/ai/images/upscale/v3"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "multipart/form-data"
    }

    payload = {
        "output_type": output_type,
        "scale": scale,
        "existing_image": (image_file.name, image_file)
    }

    response = requests.post(url, files=payload, headers=headers)

    return response.text

