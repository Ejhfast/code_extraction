# PUT request from tornado.httpclient.AsyncHTTPClient
from tornado.httpclient import HTTPRequest
request = HTTPRequest(opt.site_url + '/api/user/', method="PUT", body=urlencode(pdata))
response = yield gen.Task(http_client.fetch, request)
