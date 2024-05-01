import requests

def create_collection(api_key=None,collection='', collection_schema='', collection_sort_by='' ):
    url = "https://api.worqhat.com/api/collections/create"
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "collection": collection,
        "collectionSchema": collection_schema,
        "collectionSortBy": collection_sort_by
    }

    response = requests.post("POST",url, json=payload, headers=headers)

    return response.text