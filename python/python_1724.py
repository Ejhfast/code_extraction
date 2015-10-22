# WSGI/Django: pass username back to Apache for access log
from apache.httpd import request_rec
r = request_rec(environ['apache.request_rec'])
r.user = user
