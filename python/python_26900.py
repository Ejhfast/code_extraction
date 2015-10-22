# How to get http headers in flask?
from flask import request
request.headers.get('your-header-name')
