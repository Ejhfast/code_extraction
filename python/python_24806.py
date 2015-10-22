# urllib cannot read https
from urllib.request import urlopen
resp = urlopen('https://github.com')
print(resp.read())
