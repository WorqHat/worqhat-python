import requests

def fetch_all_collections(api_key=None):
    url = "https://api.worqhat.com/api/collections/fetch-all"
    headers = {
        "Authorization": "Bearer " + api_key
    }

    response = requests.post(url, headers=headers)

    return response.text

def fetch_all_docs_from_collection(collection, api_key=None, output_type="json"):
    url = "https://api.worqhat.com/api/collections/data/fetch/all"
    payload = {
        "collection": collection,
        "outputType": output_type
    }
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

def fetch_doc_from_collection(collection, doc_id, api_key=None):
    url = "https://api.worqhat.com/api/collections/data/fetch/document"
    payload = {
        "collection": collection,
        "documentId": doc_id
    }
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

def fetch_doc_count_by_field(collection, field, api_key=None):
    url = "https://api.worqhat.com/api/collections/data/fetch/count"
    payload = {
        "collection": collection,
        "key": field
    }
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

def fetch_unique_keys_ordered(collection, field, order_by, order_type, api_key=None):
    url = "https://api.worqhat.com/api/collections/data/fetch/unique"
    payload = {
        "collection": collection,
        "key": field,
        "orderBy": order_by,
        "orderType": order_type
    }
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

def fetch_docs_by_query(collection, queries, compounding="and", order_by=None, order_type="asc", limit=None, start_after=None, output_type="json", api_key=None):
    url = "https://api.worqhat.com/api/collections/data/fetch/query"
    payload = {
        "collection": collection,
        "queries": queries,
        "compounding": compounding,
        "orderBy": order_by,
        "orderType": order_type,
        "limit": limit,
        "startAfter": start_after,
        "outputType": output_type
    }
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

def fetch_docs_by_natural_query(collection, query, output_type="json", api_key=None):
    url = "https://api.worqhat.com/api/collections/data/fetch/natural-query"
    payload = {
        "collection": collection,
        "query": query,
        "outputType": output_type
    }
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.text

