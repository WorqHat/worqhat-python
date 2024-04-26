import requests 
def list_datasets(api_key=None):

    url = "https://api.worqhat.com/api/list-datasets"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.request(url, headers=headers)

    return response.text
    
    
def delete_dataset( api_key=None,dataset_id="123456789"):

    url = f"https://api.worqhat.com/api/delete-datasets/{dataset_id}"
    headers = {"Authorization": "Bearer " + api_key}

    response = requests.request(url, headers=headers)

    return response.text

    
def train_dataset(api_key=None,dataset_id="123456789", dataset_name="Sample Dataset", dataset_type="self", json_data="{'data':'This is sample Data'}", training_file=None, ):
   
    url = "https://api.worqhat.com/api/ai/datasets/train-datasets"
    headers = {"Authorization": "Bearer " + api_key}

        # Construct payload with multipart form-data
    payload = {
            "datasetId": dataset_id,
            "dataset_name": dataset_name,
            "dataset_type": dataset_type,
            "json_data": (None, json_data),
            "training_file": (training_file, open(training_file, 'rb'))
    }

    response = requests.request(url, files=payload, headers=headers)

    return response.text

    