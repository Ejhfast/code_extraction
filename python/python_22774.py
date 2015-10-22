# How to differentiate between GET and POST in plain CGI
import os
print os.environ['REQUEST_METHOD']
