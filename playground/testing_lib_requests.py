import requests

url = "https://dummy-json.mock.beeceptor.com/continents"
headers = {
    "Accept": "application/json",
}

response = requests.get(url, headers=headers, timeout=30.0)
if response.status_code == 200:
    data = response.json()
    continents = [(c['name'], c['code']) for c in data]
    print(continents)
else:
    print(f"Request failed with status code: {response.status_code}")