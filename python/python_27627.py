# Python: urllib2 get nothing which does exist
r = requests.get('website', allow_redirects=True)
print r.text
