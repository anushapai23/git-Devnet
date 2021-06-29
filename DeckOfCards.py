import requests
import json
from pprint import pprint

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

response_json=response.json()
print(response_json)
deck_id=response_json['deck_id']
print(deck_id)
