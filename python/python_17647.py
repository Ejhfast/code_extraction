# HTTP requests.post fails
data = {'hash': hash, 'confirm': 'Continue as Free User'}
r = requests.post(url, data)
html = r.text
