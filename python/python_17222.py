# python: 500 error using json.load() in cherrypy
data = urlopen(url).read()
js = json.loads(data.decode('utf-8'))
