# WSGI : If there aren't any cookies set yet.. *** cookie.load(environ['HTTP_COOKIE']) *** causes the whole script to break
def application(environ, start_response):
    if 'HTTP_COOKIE' in environ:
        cookie.load(environ['HTTP_COOKIE'])
