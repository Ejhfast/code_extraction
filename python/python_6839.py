# How can I parse an external XML file with django/python
import urllib2
doc = urllib2.urlopen(your_url)
parsed = minidom.parse(doc)
