# How to use requests library without system-configured proxies
r = requests.get('http://google.com', proxies = { 'http': '', ... })
