# Receiving AJAX Data in Python on Dreamhost
def application(environ, start_response):
    start_response('200 OK')
    return 'Hi there!'
