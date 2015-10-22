# Why can I import a library from the Django shell, but not inside my site?
from oauth2app import token
...
(r'^oauth2/token/?$', token.handler),
