import os
import requests
from worqhat import analyze_images
from dotenv import load_dotenv
load_dotenv()
images=["orange.png"]
r=analyze_images(images,stream_data=True)
print(r)
    