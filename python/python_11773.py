# How do I fetch htmlcode from a url with a colon ":" in the url?
f = urllib2.urlopen("http://gulasidorna.eniro.se/hitta:svenska+kyrkan/")
htmlcode = f.read()
print htmlcode
