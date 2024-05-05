
#("sk-02e44d2ccb164c738a6c4a65dbf75e89","Where can i see Taj mahal")
#Check image_analysis.py , image_moderation,image_gen.py,text_extract.py
import json
import requests
from dotenv import load_dotenv
from worqHat.ai_models import text_gen
import os
load_dotenv()

r= text_gen.get_ai_response_v2("How many cm in 1 m",api_key="sk-02e44d2ccb164c738a6c4a65dbf75e89")
print(r)
