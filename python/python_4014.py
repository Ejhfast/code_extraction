# Is this the right way to write a POST function in Python?
def URLRequest(url, params, method="POST"):
    res, content = Http().request(url, method, urllib.urlencode(params))
    return {'res':res, 'content':content}
