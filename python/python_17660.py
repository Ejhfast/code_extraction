# ValueError : Unkown url type in Django
endpoint = 'https://api-ssl.bitly.com/v3/shorten?access_token={0}&amp;longUrl={1}&amp;format=txt'
req = endpoint.format(settings.ACCESS_KEY, urllib.quote(long_url))
return urlopen(req).read()
