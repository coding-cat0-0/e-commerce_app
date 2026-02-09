import requests

url = "http://127.0.0.1:9000/graphql/"
payload = {
    "query": "{ __typename }"
}
response = requests.post(url, json=payload)
print(f"Status: {response.status_code}")
print(f"Body: {response.text}")