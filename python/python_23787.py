# post multipart image to api
files = {'photo': ('image.png', open('image.png', 'rb'), 'image/png')}
r = requests.post(photoURL, header={'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5', 'Authorization': authKey} files=files)
print r.text
