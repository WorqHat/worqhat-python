import os
import requests
from dotenv import load_dotenv

def analyze_images(images, question="", training_data="", output_type="text", stream_data=False, api_key=None):
    # Load dotenv file to get the API key
    load_dotenv()

    # Get API key from environment variable or use the provided one
    api_key = api_key or os.getenv("API_Key")

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

    return response.text

# Example usage
if __name__ == "__main__":
    images = ["https://firebasestorage.googleapis.com/v0/b/yoda-technologies-kb.appspot.com/o/email_attachments%2Fimage002.png?alt=media&token=ac1cbc02-a292-4226-a728-f097be6ab080","apple.jpg"]
    result = analyze_images(images, question="what is this")
    print(result)
