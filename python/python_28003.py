# How to grab/generate a cookie for a site
s = requests.Session()
url = "http://www.amazon.com"
r = s.get(url)
