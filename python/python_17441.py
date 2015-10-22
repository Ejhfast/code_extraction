# Unwanted string formatting
payload = json.dumps({"host": "tst123:3306"})
headers = {'content-type': 'application/json'}
r = requests.put(url, data=payload, headers=headers)
