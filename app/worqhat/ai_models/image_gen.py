import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def generate_image_v2(prompt="", image_style="realistic", output_type="url", orientation="square", api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

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

def generate_image_v3(prompt="", image_style="realistic", output_type="url", orientation="square", api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

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

def modify_image_v2(images=None,modification=None, output_type="URL", similarity="30",  api_key=None):
    # If modification or existing_images is not provided, return an error message
    if not modification:
        return "Modification description is missing"
    if not images or len(images) == 0:
        return "Existing images are missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v2"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    results = []

    for image in images:
        # Prepare payload
        payload = {
            "modification": modification,
            "output_type": output_type,
            "similarity": similarity
        }

        # Prepare files data in the required format
        if image.startswith('http://') or image.startswith('https://'):
            # If image is a URL, download the image content
            response = requests.get(image)
            files = [('existing_image', ('file', response.content, 'application/octet-stream'))]
        else:
            # If image is a local file path, read the file content
            with open(image, 'rb') as f:
                files = [('existing_image', ('file', f, 'application/octet-stream'))]

        # Make the API call
        response = requests.post(url, headers=headers, data=payload, files=files)
        results.append(response.text)

    return results


def modify_image_v3(images=None,modification=None, output_type="URL", similarity="30",  api_key=None):
    # If modification or existing_images is not provided, return an error message
    if not modification:
        return "Modification description is missing"
    if not images or len(images) == 0:
        return "Existing images are missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v3"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    results = []

    for image in images:
        # Prepare payload
        payload = {
            "modification": modification,
            "output_type": output_type,
            "similarity": similarity
        }

        # Prepare files data in the required format
        if image.startswith('http://') or image.startswith('https://'):
            # If image is a URL, download the image content
            response = requests.get(image)
            files = [('existing_image', ('file', response.content, 'application/octet-stream'))]
        else:
            # If image is a local file path, read the file content
            with open(image, 'rb') as f:
                files = [('existing_image', ('file', f, 'application/octet-stream'))]

        # Make the API call
        response = requests.post(url, headers=headers, data=payload, files=files)
        results.append(response.text)

    return results

def remove_text_from_image(image=None,output_type="URL",  api_key=None):
    # If existing_image is not provided, return an error message
    if not image:
        return "Existing image is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v3/remove-text"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare payload
    payload = {'output_type': output_type}

    # Prepare files data in the required format
    if image.startswith('http://') or image.startswith('https://'):
        # If image is a URL, download the image content
        response = requests.get(image)
        files = [('existing_image', ('file', response.content, 'image/png'))]
    else:
        # If image is a local file path, read the file content
        with open(image, 'rb') as f:
            files = [('existing_image', ('file', f, 'image/png'))]

    # Make the API call
    response = requests.post(url, headers=headers, data=payload, files=files)

    return response.text

def remove_background_from_image(output_type="URL", existing_image=None, api_key=None):
    # If existing_image is not provided, return an error message
    if not existing_image:
        return "Existing image is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v3/remove-background"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare payload
    payload = {'output_type': output_type}

    # Prepare files data in the required format
    if existing_image.startswith('http://') or existing_image.startswith('https://'):
        # If image is a URL, download the image content
        response = requests.get(existing_image)
        files = [('existing_image', ('file', response.content, 'image/png'))]
    else:
        # If image is a local file path, read the file content
        with open(existing_image, 'rb') as f:
            files = [('existing_image', ('file', f, 'image/png'))]

    # Make the API call
    response = requests.post(url, headers=headers, data=payload, files=files)

    return response.text

def replace_background(image=None,modification=None, output_type="URL",  api_key=None):
    # If modification or existing_image is not provided, return an error message
    if not modification:
        return "Modification description is missing"
    if not image:
        return "Existing image is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v3/replace-background"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare payload
    payload = {
        "modification": modification,
        "output_type": output_type
    }

    # Prepare files data in the required format
    if image.startswith('http://') or image.startswith('https://'):
        # If image is a URL, download the image content
        response = requests.get(image)
        files = [('existing_image', ('file', response.content, 'image/png'))]
    else:
        # If image is a local file path, read the file content
        with open(image, 'rb') as f:
            files = [('existing_image', ('file', f, 'image/png'))]

    # Make the API call
    response = requests.post(url, headers=headers, data=payload, files=files)

    return response.text

def search_replace_image(image=None,modification=None, output_type="URL", search_object=None,  api_key=None):
    # If modification, search_object, or existing_image is not provided, return an error message
    if not modification:
        return "Modification description is missing"
    if not search_object:
        return "Search object description is missing"
    if not image:
        return "Existing image is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v3/search-replace-image"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare payload
    payload = {
        "modification": modification,
        "output_type": output_type,
        "search_object": search_object
    }

    # Prepare files data in the required format
    if image.startswith('http://') or image.startswith('https://'):
        # If image is a URL, download the image content
        response = requests.get(image)
        files = [('existing_image', ('file', response.content, 'image/png'))]
    else:
        # If image is a local file path, read the file content
        with open(image, 'rb') as f:
            files = [('existing_image', ('file', f, 'image/png'))]

    # Make the API call
    response = requests.post(url, headers=headers, data=payload, files=files)

    return response.text


def extend_image(image=None,output_type="URL", left_extend="100", right_extend="100", top_extend="50", bottom_extend="50", description="",  api_key=None):
    # If existing_image is not provided, return an error message
    if not image:
        return "Existing image is missing"

    # If api_key is not provided, retrieve from environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not available, return an error message
    if not api_key:
        return "Please provide an appropriate API key"

    url = "https://api.worqhat.com/api/ai/images/modify/v3/extend-image"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare payload
    payload = {
        "output_type": output_type,
        "leftExtend": left_extend,
        "rightExtend": right_extend,
        "topExtend": top_extend,
        "bottomExtend": bottom_extend,
        "description": description
    }

    # Prepare files data in the required format
    if image.startswith('http://') or image.startswith('https://'):
        # If image is a URL, download the image content
        response = requests.get(image)
        files = [('existing_image', ('file', response.content, 'image/png'))]
    else:
        # If image is a local file path, read the file content
        with open(image, 'rb') as f:
            files = [('existing_image', ('file', f, 'image/png'))]

    # Make the API call
    response = requests.post(url, headers=headers, data=payload, files=files)

    return response.text

def upscale_image(image_file="", scale=2, output_type="url", api_key=None):
    # If api_key is not provided, get it from the environment variable
    if not api_key:
        api_key = os.getenv("API_KEY")

    # If api_key is still not provided, return an error message
    if not api_key:
        return "Please enter an appropriate API Key"

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
