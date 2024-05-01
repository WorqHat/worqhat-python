import requests 

def get_ai_responsev2(api_key=None,question="", 
                    preserve_history=True, 
                    randomness=0.5, 
                    stream_data=False, 
                    conversation_history=[], 
                    training_data="", 
                    response_type="text",
                    ):

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

        response = requests.request("POST",url, json=payload, headers=headers)

        return response.text

    
def get_ai_responsev3(api_key=None,question="", 
                    preserve_history=True, 
                    randomness=0.5, 
                    stream_data=False, 
                    conversation_history=[], 
                    training_data="", 
                    response_type="text",
                    ):

   
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

        response = requests.request("POST",url, json=payload, headers=headers)

        return response.text

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


def get_alpha_ai_response(api_key=None,question="", 
                          preserve_history=True, 
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

        return response.text
