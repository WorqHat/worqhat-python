import requests

def create_collection(collection, collection_schema, collection_sort_by, api_key=None):
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

    response = requests.post(url, json=payload, headers=headers)

    return response.text