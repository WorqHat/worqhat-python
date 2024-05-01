from worqHat.ai_models import *
#("sk-02e44d2ccb164c738a6c4a65dbf75e89","Where can i see Taj mahal")
#Check image_analysis.py , image_moderation,image_gen.py,text_extract.py
import json
import requests



# Example usage
api_key = "sk-02e44d2ccb164c738a6c4a65dbf75e89"
question = "What is the weather today?"
r=text_gen.get_alpha_ai_response(api_key=api_key, question=question, stream_data=True)
print(r)
