# open url with urllib2 that already have get parameter
tileurl = tile.replace(t1, "") ## Removing the parameters from the url
p = urlparse.parse_qs(t1) ## decoding the parameter
tileparam = urllib.urlencode(p) ## encoding the parameter...
