import os
import requests
from dotenv import load_dotenv
from worqhat.ai_models import detect_image_text


load_dotenv()
images=["https://firebasestorage.googleapis.com/v0/b/worqhat-prod.appspot.com/o/AiCOn%20Alpha.png?alt=media&token=87b5d86b-ee01-450b-aeb4-93ce5778ba18"]
r=detect_image_text(images)
print(r)
    