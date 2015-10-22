# Unable to save image from web using urllib2
imgRequest = urllib2.Request(imgUrl, headers=headers)
imgData = urllib2.urlopen(imgRequest).read()
