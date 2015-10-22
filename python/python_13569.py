# Is there an easy way to request a URL in python and NOT follow redirects?
import requests
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
