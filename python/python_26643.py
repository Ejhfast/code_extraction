# urllib2.Request Keeps Downloading Cached File From Proxy
request = urllib2.Request(download_url)
    request.add_header('Cache-Control', 'max-age=0')
    response = urllib2.urlopen(request).read()
