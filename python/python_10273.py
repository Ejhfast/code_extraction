# nginx and uWSGI obtain authentication data in Python
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
