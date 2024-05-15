import requests
import _json

url = f'https://eodhd.com/api/exchanges-list/?api_token=65aed5c0576eb6.64147179&fmt=json'
data = requests.get(url).json()

print(data)
