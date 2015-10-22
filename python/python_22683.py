# Bottle Python Error 404: Not found: '/'
@bottle.get('/')
def home():
   return 'Hello!'
