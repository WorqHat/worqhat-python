import requests 

def get_ai_responsev2(question, 
                    preserve_history=True, 
                    randomness=0.5, 
                    stream_data=False, 
                    conversation_history=None, 
                    training_data=None, 
                    response_type="text",
                    api_key=None):

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

        response = requests.post(url, json=payload, headers=headers)

        return response.text

    
def get_ai_responsev3(question, 
                    preserve_history=True, 
                    randomness=0.5, 
                    stream_data=False, 
                    conversation_history=None, 
                    training_data=None, 
                    response_type="text",
                    api_key=None):

   
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

        response = requests.post(url, json=payload, headers=headers)

        return response.text

def get_large_ai_response_v2(question, 
                          dataset_id, 
                          preserve_history=True, 
                          randomness=0.5, 
                          stream_data=False, 
                          conversation_history=None, 
                          instructions=None, 
                          api_key=None):
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

        response = requests.post(url, json=payload, headers=headers)

        return response.text


def get_alpha_ai_response(question, 
                          preserve_history=True, 
                          randomness=0.5, 
                          stream_data=False, 
                          conversation_history=None, 
                          training_data=None, 
                          response_type="text",
                          api_key=None):
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

        response = requests.post(url, json=payload, headers=headers)

        return response.text
