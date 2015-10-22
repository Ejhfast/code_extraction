# How to make this Twisted Python Proxy faster?
req = urllib.urlopen("http://weblock.zbrowntechnology.info/ProgFiles/stats.php?%s" % params, proxies=proxies)
    resp = req.read()
    req.close()
