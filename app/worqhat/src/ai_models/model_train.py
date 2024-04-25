import requests 
def list_datasets(api_key=None):
    auth_status = Authenticate(api_key).get("status")
    if auth_status == "success":
        url = "https://api.worqhat.com/api/list-datasets"
        headers = {"Authorization": "Bearer " + api_key}

        response = requests.get(url, headers=headers)

        return response.text
    else:
        return auth_status
    
    
def delete_dataset(dataset_id, api_key=None):
    auth_status = Authenticate(api_key).get("status")
    if auth_status == "success":
        url = f"https://api.worqhat.com/api/delete-datasets/{dataset_id}"
        headers = {"Authorization": "Bearer " + api_key}

        response = requests.delete(url, headers=headers)

        return response.text
    else:
        return auth_status
    
def train_dataset(dataset_id, dataset_name, dataset_type, json_data, training_file, api_key=None):
    auth_status = Authenticate(api_key).get("status")
    if auth_status == "success":
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

        response = requests.post(url, files=payload, headers=headers)

        return response.text
    else:
        return auth_status
    