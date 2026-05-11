import requests

url = "https://fortnite-api.com"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data['data']['items'][0]['name']) # Prints the name of a new cosmetic
