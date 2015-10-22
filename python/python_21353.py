# How do I get the HTML of a web page if I have the url in python
response = urllib2.urlopen(url)
content = response.read()
