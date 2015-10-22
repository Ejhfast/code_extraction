# Proper way to extract JSON data from the web given an API
import requests
r = requests.get('http://site.com/source.json', params={'s': 'somevalue/or other here'})
json_result = r.json()
