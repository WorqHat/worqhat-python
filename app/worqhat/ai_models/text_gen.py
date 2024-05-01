import requests 
import json
def get_ai_response_v2(api_key=None,
                      question="", 
                      preserve_history=False, 
                      randomness=0.5, 
                      stream_data=False, 
                      conversation_history=[], 
                      training_data="", 
                      response_type="text"):
    
    url = "https://api.worqhat.com/api/ai/content/v2"

    payload = {
        "question": question,
        "preserve_history": preserve_history,
        "randomness": randomness,
        "stream_data": stream_data,
        "conversation_history": conversation_history,
        "training_data": training_data,
        "response_type": response_type
    }

    headers = {"Content-Type": "application/json"}

    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    response = requests.post(url, json=payload, headers=headers, stream=stream_data)

    if stream_data:
        for line in response.iter_lines():
            if line:
                # Check if the line contains JSON content
                if line.startswith(b'data:'):
                    json_content = line[len(b'data:'):].decode('utf-8').strip()
                    print(json_content)
    else:
        json_response = response.text
        try:
            json_data = json.loads(json_response)
            print(json.dumps(json_data, indent=4))
        except json.JSONDecodeError:
            print(json_response)

    
def get_ai_response_v3(api_key=None,
                      question="", 
                      preserve_history=False, 
                      randomness=0.5, 
                      stream_data=False, 
                      conversation_history=[], 
                      training_data="", 
                      response_type="text"):
    
    url = "https://api.worqhat.com/api/ai/content/v3"

    payload = {
        "question": question,
        "preserve_history": preserve_history,
        "randomness": randomness,
        "stream_data": stream_data,
        "conversation_history": conversation_history,
        "training_data": training_data,
        "response_type": response_type
    }

    headers = {"Content-Type": "application/json"}

    if api_key:
        headers["Authorization"] = "Bearer " + api_key

    response = requests.post(url, json=payload, headers=headers, stream=stream_data)

    if stream_data:
        for line in response.iter_lines():
            if line:
                # Check if the line contains JSON content
                if line.startswith(b'data:'):
                    json_content = line[len(b'data:'):].decode('utf-8').strip()
                    print(json_content)
    else:
        json_response = response.text
        try:
            json_data = json.loads(json_response)
            print(json.dumps(json_data, indent=4))
        except json.JSONDecodeError:
            print(json_response)
def get_alpha_ai_response(api_key=None,question="", 
                          preserve_history=False, 
                          randomness=0.5, 
                          stream_data=False, 
                          conversation_history=[], 
                          training_data="", 
                          response_type="text",
                          ):
        url = "https://api.worqhat.com/api/ai/content/v3/alpha"

        payload = {
            "question": question,
            "preserve_history": preserve_history,
            "randomness": randomness,
            "stream_data": stream_data,
            "conversation_history": conversation_history,
            "training_data": training_data,
            "response_type": response_type
        }

        headers = {"Content-Type": "application/json"}

        if api_key:
            headers["Authorization"] = "Bearer " + api_key

        response = requests.request("POST",url, json=payload, headers=headers)
        if stream_data:
            for line in response.iter_lines():
                if line:
                # Check if the line contains JSON content
                    if line.startswith(b'data:'):
                        json_content = line[len(b'data:'):].decode('utf-8').strip()
                        print(json_content)
        else:
            json_response = response.text
        try:
            json_data = json.loads(json_response)
            print(json.dumps(json_data, indent=4))
        except json.JSONDecodeError:
            print(json_response)
            
def get_large_ai_response_v2(api_key=None,question="", 
                          dataset_id="", 
                          preserve_history=True, 
                          randomness=0.5, 
                          stream_data=False, 
                          conversation_history=[], 
                          instructions=None, 
                          ):
        url = "https://api.worqhat.com/api/ai/content/v2-large/answering"

        payload = {
            "question": question,
            "datasetId": dataset_id,
            "preserve_history": preserve_history,
            "randomness": randomness,
            "stream_data": stream_data,
            "conversation_history": conversation_history,
            "instructions": instructions
        }

        headers = {"Content-Type": "application/json"}

        if api_key:
            headers["Authorization"] = "Bearer " + api_key

        response = requests.request("POST",url, json=payload, headers=headers)

        return response.text

#Stream data mediapipe

