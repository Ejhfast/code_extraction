# How to pass URL with parameters in GET request in Flask?
_url = request.url.replace(request.url_root,'')
url = urllib.unquote(_url)
