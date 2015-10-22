# Both using cookies and a proxy in Python with urllib2
cj = cookielib.CookieJar()
opener = build_opener(ProxyHandler({'http': 'ip:port'}), HTTPCookieProcessor(cj))
