# Python RESTful client like Guzzle from PHP
base_url = "http://example.com/"
def requests_get(url, *args, **kwargs):
    return requests.get(base_url + url,*args,**kwargs)
